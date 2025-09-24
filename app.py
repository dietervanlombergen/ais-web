from flask import Flask, render_template, request, jsonify
import os
import logging
from services.rss_service import rss_service
from services.ai_service import ai_service

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically save to database or send email
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your message!'
        })
    
    return render_template('contact.html')

@app.route('/articles')
def articles():
    """Display articles from RSS feeds"""
    return render_template('articles.html')

@app.route('/api/feeds')
def get_feeds():
    """Get list of available RSS feeds"""
    try:
        feeds = rss_service.get_popular_feeds()
        return jsonify({
            'success': True,
            'feeds': feeds
        })
    except Exception as e:
        logger.error(f"Error getting feeds: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/fetch-feed')
def fetch_feed():
    """Fetch articles from a specific RSS feed"""
    feed_url = request.args.get('url')
    if not feed_url:
        return jsonify({
            'success': False,
            'error': 'Feed URL is required'
        }), 400
    
    try:
        feed_data = rss_service.fetch_rss_feed(feed_url)
        if not feed_data:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch or parse RSS feed'
            }), 500
        
        return jsonify({
            'success': True,
            'data': feed_data
        })
    except Exception as e:
        logger.error(f"Error fetching feed {feed_url}: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/generate-summary', methods=['POST'])
def generate_summary():
    """Generate AI summary for an article"""
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({
                'success': False,
                'error': 'Title and content are required'
            }), 400
        
        title = data['title']
        content = data['content']
        max_length = data.get('max_length', 150)
        
        summary = ai_service.generate_summary(title, content, max_length)
        
        return jsonify({
            'success': True,
            'summary': summary,
            'ai_available': ai_service.is_available()
        })
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/generate-key-points', methods=['POST'])
def generate_key_points():
    """Generate key points for an article"""
    try:
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({
                'success': False,
                'error': 'Content is required'
            }), 400
        
        content = data['content']
        num_points = data.get('num_points', 5)
        
        key_points = ai_service.generate_key_points(content, num_points)
        
        return jsonify({
            'success': True,
            'key_points': key_points,
            'ai_available': ai_service.is_available()
        })
    except Exception as e:
        logger.error(f"Error generating key points: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment of an article"""
    try:
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({
                'success': False,
                'error': 'Content is required'
            }), 400
        
        content = data['content']
        sentiment = ai_service.analyze_sentiment(content)
        
        return jsonify({
            'success': True,
            'sentiment': sentiment,
            'ai_available': ai_service.is_available()
        })
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy', 
        'message': 'Server is running',
        'ai_available': ai_service.is_available()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
