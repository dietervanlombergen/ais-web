"""
RSS Feed Service for fetching and parsing RSS feeds
"""

import requests
import xmltodict
from datetime import datetime
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
import logging
import re

logger = logging.getLogger(__name__)

class RSSService:
    """Service for handling RSS feed operations"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def fetch_rss_feed(self, feed_url: str) -> Optional[Dict]:
        """
        Fetch and parse an RSS feed
        
        Args:
            feed_url: URL of the RSS feed
            
        Returns:
            Dictionary containing feed metadata and articles, or None if failed
        """
        try:
            logger.info(f"Fetching RSS feed: {feed_url}")
            
            # Fetch the feed
            response = self.session.get(feed_url, timeout=self.timeout)
            response.raise_for_status()
            
            # Parse the XML content
            feed_data = xmltodict.parse(response.content)
            
            # Extract feed metadata
            if 'rss' in feed_data and 'channel' in feed_data['rss']:
                channel = feed_data['rss']['channel']
                feed_info = {
                    'title': channel.get('title', 'Unknown Feed'),
                    'description': channel.get('description', ''),
                    'link': channel.get('link', feed_url),
                    'updated': channel.get('lastBuildDate', channel.get('pubDate', '')),
                    'language': channel.get('language', 'en'),
                    'total_entries': len(channel.get('item', []))
                }
                
                # Extract articles
                articles = []
                items = channel.get('item', [])
                if not isinstance(items, list):
                    items = [items]  # Handle single item case
                
                for item in items[:20]:  # Limit to 20 most recent articles
                    article = self._parse_article_xml(item)
                    if article:
                        articles.append(article)
                
                return {
                    'feed_info': feed_info,
                    'articles': articles,
                    'fetch_time': datetime.now().isoformat(),
                    'success': True
                }
            else:
                logger.error(f"Invalid RSS format for {feed_url}")
                return None
            
        except requests.RequestException as e:
            logger.error(f"Failed to fetch RSS feed {feed_url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error parsing RSS feed {feed_url}: {e}")
            return None
    
    def _parse_article_xml(self, item: Dict) -> Optional[Dict]:
        """
        Parse individual RSS item from XML into article format
        
        Args:
            item: RSS item dictionary from XML parsing
            
        Returns:
            Dictionary containing article data, or None if parsing failed
        """
        try:
            # Extract basic article information
            article = {
                'title': item.get('title', 'Untitled'),
                'link': item.get('link', ''),
                'published': item.get('pubDate', ''),
                'updated': item.get('updated', item.get('pubDate', '')),
                'author': item.get('author', item.get('dc:creator', 'Unknown')),
                'summary': '',
                'content': '',
                'tags': [],
                'guid': item.get('guid', item.get('link', '')),
                'source': 'RSS Feed'
            }
            
            # Extract summary/description
            if 'description' in item:
                article['summary'] = self._clean_html(item['description'])
            elif 'summary' in item:
                article['summary'] = self._clean_html(item['summary'])
            
            # Extract full content if available
            if 'content:encoded' in item:
                article['content'] = self._clean_html(item['content:encoded'])
            elif 'content' in item:
                article['content'] = self._clean_html(item['content'])
            
            # Extract tags/categories
            categories = item.get('category', [])
            if not isinstance(categories, list):
                categories = [categories]
            article['tags'] = [cat for cat in categories if cat]
            
            # Parse publication date
            pub_date = item.get('pubDate', '')
            if pub_date:
                try:
                    # Try to parse common RSS date formats
                    article['published_date'] = self._parse_rss_date(pub_date)
                except:
                    article['published_date'] = pub_date
            
            return article
            
        except Exception as e:
            logger.error(f"Error parsing article: {e}")
            return None
    
    def _parse_rss_date(self, date_string: str) -> str:
        """
        Parse RSS date string into ISO format
        
        Args:
            date_string: RSS date string
            
        Returns:
            ISO formatted date string
        """
        try:
            # Common RSS date formats
            formats = [
                '%a, %d %b %Y %H:%M:%S %Z',
                '%a, %d %b %Y %H:%M:%S %z',
                '%a, %d %b %Y %H:%M:%S GMT',
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%dT%H:%M:%S%z',
                '%Y-%m-%dT%H:%M:%SZ'
            ]
            
            for fmt in formats:
                try:
                    dt = datetime.strptime(date_string, fmt)
                    return dt.isoformat()
                except ValueError:
                    continue
            
            # If no format matches, return original
            return date_string
            
        except Exception:
            return date_string
    
    def _clean_html(self, html_content: str) -> str:
        """
        Clean HTML content and extract text
        
        Args:
            html_content: Raw HTML content
            
        Returns:
            Cleaned text content
        """
        if not html_content:
            return ''
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text and clean up whitespace
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:1000]  # Limit to 1000 characters for summary
            
        except Exception as e:
            logger.error(f"Error cleaning HTML: {e}")
            return html_content[:500] if html_content else ''
    
    def get_popular_feeds(self) -> List[Dict]:
        """
        Get list of popular RSS feeds for demonstration
        
        Returns:
            List of popular RSS feed URLs and metadata
        """
        return [
            {
                'name': 'BBC News',
                'url': 'http://feeds.bbci.co.uk/news/rss.xml',
                'description': 'Latest news from BBC',
                'category': 'News'
            },
            {
                'name': 'TechCrunch',
                'url': 'https://techcrunch.com/feed/',
                'description': 'Latest technology news and startup information',
                'category': 'Technology'
            },
            {
                'name': 'Hacker News',
                'url': 'https://hnrss.org/frontpage',
                'description': 'Top stories from Hacker News',
                'category': 'Technology'
            },
            {
                'name': 'Python.org News',
                'url': 'https://www.python.org/jobs/feed/rss/',
                'description': 'Python job listings and news',
                'category': 'Programming'
            }
        ]


# Global instance
rss_service = RSSService()
