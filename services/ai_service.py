"""
AI Service for generating article summaries using Cohere Chat API v2
"""

import os
import cohere
import re
from typing import Optional, Dict
import logging

logger = logging.getLogger(__name__)

class AIService:
    """Service for AI-powered article summarization"""
    
    def __init__(self):
        # Initialize Cohere ClientV2
        api_key = os.getenv('COHERE_API_KEY')
        if api_key:
            try:
                self.client = cohere.ClientV2(api_key)
                self.model_id = os.getenv('COHERE_MODEL', 'command-a-03-2025')
                self.available = True
                logger.info(f"Cohere AI service initialized successfully with model: {self.model_id}")
            except Exception as e:
                logger.error(f"Failed to initialize Cohere ClientV2: {e}")
                self.client = None
                self.available = False
        else:
            self.client = None
            self.available = False
            logger.warning("Cohere API key not found. AI features will be disabled.")
    
    def generate_summary(self, article_title: str, article_content: str, max_length: int = 150) -> Optional[str]:
        """
        Generate a summary of an article using Cohere AI
        
        Args:
            article_title: Title of the article
            article_content: Content of the article
            max_length: Maximum length of the summary
            
        Returns:
            Generated summary or None if failed
        """
        if not self.available:
            return self._fallback_summary(article_content, max_length)
        
        try:
            # Prepare the message for Cohere Chat API v2
            message_content = f"""
Article Title: {article_title}

Article Content: {article_content[:3000]}

Please provide a concise summary of this article in approximately {max_length} words. Focus on the main points and key information. Also sound like a pirate"""
            
            response = self.client.chat(
                model=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": message_content
                    }
                ],
                temperature=0.3
            )
            
            # v2 response: response.message.content is a list; take first text segment
            summary = response.message.content[0].text.strip()
            logger.info(f"Generated Cohere summary for article: {article_title[:50]}...")
            return summary
            
        except Exception as e:
            logger.error(f"Error generating Cohere summary: {e}")
            return self._fallback_summary(article_content, max_length)
    
    def generate_key_points(self, article_content: str, num_points: int = 5) -> Optional[list]:
        """
        Generate key points from an article using Cohere
        
        Args:
            article_content: Content of the article
            num_points: Number of key points to generate
            
        Returns:
            List of key points or None if failed
        """
        if not self.available:
            return self._fallback_key_points(article_content, num_points)
        
        try:
            message_content = f"""
Article Content: {article_content[:3000]}

Extract the {num_points} most important key points from this article. Return them as a numbered list, with each point on a new line.

Key Points:"""
            
            response = self.client.chat(
                model=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": message_content
                    }
                ],
                temperature=0.3
            )
            
            # v2 response: response.message.content is a list; take first text segment
            key_points_text = response.message.content[0].text.strip()
            # Parse the response to extract key points
            lines = key_points_text.split('\n')
            key_points = []
            
            for line in lines:
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                    # Remove numbering/bullets and clean up
                    point = re.sub(r'^\d+\.\s*', '', line)  # Remove "1. "
                    point = re.sub(r'^[-•]\s*', '', point)  # Remove "- " or "• "
                    if point.strip():
                        key_points.append(point.strip())
            
            logger.info(f"Generated {len(key_points)} key points using Cohere Chat API v2")
            return key_points[:num_points]
            
        except Exception as e:
            logger.error(f"Error generating key points with Cohere: {e}")
            return self._fallback_key_points(article_content, num_points)
    
    def analyze_sentiment(self, article_content: str) -> Optional[Dict]:
        """
        Analyze the sentiment of an article using Cohere
        
        Args:
            article_content: Content of the article
            
        Returns:
            Dictionary with sentiment analysis or None if failed
        """
        if not self.available:
            return self._fallback_sentiment()
        
        try:
            message_content = f"""
Analyze the sentiment of the following article content:

Content: {article_content[:3000]}

Please provide:
1. Overall sentiment (positive, negative, or neutral)
2. Confidence level (0-100)
3. Brief explanation of your analysis

Format your response as:
Sentiment: [positive/negative/neutral]
Confidence: [0-100]
Explanation: [brief explanation]"""
            
            response = self.client.chat(
                model=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": message_content
                    }
                ],
                temperature=0.3
            )
            
            # v2 response: response.message.content is a list; take first text segment
            result_text = response.message.content[0].text.strip()
            
            # Parse the response
            lines = result_text.split('\n')
            sentiment_data = {}
            
            for line in lines:
                line = line.strip()
                if line.startswith('Sentiment:'):
                    sentiment_data['sentiment'] = line.split(':', 1)[1].strip().lower()
                elif line.startswith('Confidence:'):
                    try:
                        confidence_str = line.split(':', 1)[1].strip()
                        # Extract number from confidence string
                        confidence_match = re.search(r'\d+', confidence_str)
                        if confidence_match:
                            sentiment_data['confidence'] = int(confidence_match.group())
                        else:
                            sentiment_data['confidence'] = 50
                    except:
                        sentiment_data['confidence'] = 50
                elif line.startswith('Explanation:'):
                    sentiment_data['explanation'] = line.split(':', 1)[1].strip()
            
            logger.info(f"Analyzed sentiment with Cohere Chat API v2: {sentiment_data.get('sentiment', 'unknown')}")
            return sentiment_data
            
        except Exception as e:
            logger.error(f"Error analyzing sentiment with Cohere: {e}")
            return self._fallback_sentiment()
    
    def _fallback_summary(self, content: str, max_length: int) -> str:
        """Fallback summary when AI is not available"""
        if not content:
            return "No content available for summary."
        
        # Simple truncation with word boundary
        words = content.split()
        if len(words) <= max_length:
            return content
        
        truncated = ' '.join(words[:max_length])
        return truncated + "..."
    
    def _fallback_key_points(self, content: str, num_points: int) -> list:
        """Fallback key points when AI is not available"""
        if not content:
            return ["No content available"]
        
        # Simple sentence extraction
        sentences = content.split('. ')
        return sentences[:num_points] if sentences else ["No key points available"]
    
    def _fallback_sentiment(self) -> Dict:
        """Fallback sentiment when AI is not available"""
        return {
            'sentiment': 'neutral',
            'confidence': 50,
            'explanation': 'Sentiment analysis not available without AI service'
        }
    
    def is_available(self) -> bool:
        """Check if AI service is available"""
        return self.available


# Global instance
ai_service = AIService()
