# RSS Feed & AI Features Documentation

Your Python website now includes powerful RSS feed integration and AI-powered article analysis capabilities!

## 🚀 Features Overview

### 📰 RSS Feed Integration
- **Fetch RSS Feeds**: Get articles from popular RSS sources
- **Parse Articles**: Extract titles, summaries, content, and metadata
- **Custom Feeds**: Support for any RSS feed URL
- **Popular Feeds**: Pre-configured popular RSS sources

### 🤖 AI-Powered Analysis
- **Article Summaries**: Generate concise AI summaries
- **Key Points Extraction**: Identify main topics and points
- **Sentiment Analysis**: Analyze article tone and sentiment
- **Fallback Support**: Works without AI API key (basic summaries)

## 🛠️ Setup Instructions

### 1. Basic Setup (Without AI)
The RSS functionality works immediately without any additional configuration:

```bash
# Start the server
source venv/bin/activate
python app.py
```

Visit: http://localhost:5000/articles

### 2. AI Features Setup (Optional)
To enable AI-powered summaries and analysis:

1. **Get Cohere API Key**:
   - Visit: https://dashboard.cohere.ai/api-keys
   - Create a new API key
   - Copy the key

2. **Set Environment Variable**:
   ```bash
   export COHERE_API_KEY="your-api-key-here"
   ```
   
   Or create a `.env` file:
   ```env
   COHERE_API_KEY=your-api-key-here
   ```

3. **Restart the server**:
   ```bash
   python app.py
   ```

## 📱 How to Use

### Accessing the Articles Page
1. Navigate to http://localhost:5000/articles
2. Select a feed from the dropdown or enter a custom RSS URL
3. Click "Fetch Articles" to load articles

### Using AI Features
1. **AI Summary**: Click "AI Summary" button on any article
2. **Sentiment Analysis**: Click "Sentiment" button to analyze article tone
3. **View Results**: Results appear in modal dialogs

## 🔧 API Endpoints

### RSS Feeds
- `GET /api/feeds` - Get list of popular RSS feeds
- `GET /api/fetch-feed?url=<rss_url>` - Fetch articles from specific RSS feed

### AI Analysis
- `POST /api/generate-summary` - Generate AI summary for article
- `POST /api/generate-key-points` - Extract key points from article
- `POST /api/analyze-sentiment` - Analyze article sentiment

### Health Check
- `GET /api/health` - Check server status and AI availability

## 📊 Supported RSS Feeds

### Pre-configured Feeds
1. **BBC News** - Latest news from BBC
2. **TechCrunch** - Technology news and startup information
3. **Hacker News** - Top stories from Hacker News
4. **Reddit Programming** - Programming discussions
5. **Python.org News** - Python job listings and news

### Custom Feeds
You can use any RSS feed URL by entering it in the custom feed input field.

## 🤖 AI Service Details

### Cohere Integration
- **Model**: Command (Cohere's flagship model)
- **Features**: Summaries, key points, sentiment analysis
- **Fallback**: Works without API key using basic text processing

### AI Capabilities
1. **Summaries**: 150-word concise summaries
2. **Key Points**: 5 main points extracted
3. **Sentiment**: Positive/Negative/Neutral analysis with confidence

### Cost Considerations
- Cohere API charges per token used
- Typical cost: $0.001-0.002 per article analysis
- Set usage limits in your Cohere account
- More cost-effective than many alternatives

## 🔧 Configuration

### Environment Variables
```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# AI Configuration (Optional)
COHERE_API_KEY=your-cohere-api-key-here
```

### RSS Service Settings
```python
# In services/rss_service.py
timeout = 30  # Request timeout in seconds
max_articles = 20  # Maximum articles per feed
```

## 🎨 Customization

### Adding New RSS Feeds
Edit `services/rss_service.py` and add to `get_popular_feeds()`:

```python
{
    'name': 'Your Feed Name',
    'url': 'https://example.com/rss',
    'description': 'Description of the feed',
    'category': 'Category'
}
```

### Customizing AI Prompts
Edit `services/ai_service.py` to modify AI behavior:

```python
# Example: Custom summary prompt
prompt = f"""
Create a {max_length}-word summary of this article:
Title: {article_title}
Content: {article_content}
"""
```

### Styling the Articles Page
Edit `templates/articles.html` to customize the appearance:
- Article cards layout
- Color scheme
- Button styles
- Modal designs

## 🐛 Troubleshooting

### Common Issues

#### RSS Feed Not Loading
- **Check URL**: Ensure the RSS feed URL is valid
- **Network**: Check internet connection
- **CORS**: Some feeds may block cross-origin requests

#### AI Features Not Working
- **API Key**: Verify COHERE_API_KEY is set correctly
- **Credits**: Check Cohere account has sufficient credits
- **Rate Limits**: Cohere has rate limits on API calls

#### Server Errors
- **Dependencies**: Ensure all packages are installed
- **Python Version**: Requires Python 3.8+
- **Port Conflicts**: Make sure port 5000 is available

### Debug Mode
Enable debug logging:

```python
# In app.py
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Tips

### RSS Fetching
- Feeds are cached for 5 minutes
- Limit to 20 articles per feed
- Use timeout of 30 seconds

### AI Processing
- Summaries are cached to avoid duplicate API calls
- Batch multiple requests when possible
- Monitor Cohere usage and costs

## 🔒 Security Considerations

### API Key Security
- Never commit API keys to version control
- Use environment variables
- Rotate keys regularly

### RSS Feed Security
- Validate RSS URLs before fetching
- Sanitize HTML content
- Implement rate limiting for public use

## 🚀 Deployment

### Production Deployment
1. **Set Environment Variables**:
   ```bash
   export COHERE_API_KEY="your-production-key"
   export FLASK_ENV=production
   ```

2. **Use Gunicorn**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Docker Deployment**:
   ```bash
   docker-compose up
   ```

### Environment Variables for Production
```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secure-secret-key
COHERE_API_KEY=your-production-api-key
```

## 📚 Examples

### Fetching a Custom RSS Feed
```javascript
// JavaScript example
fetch('/api/fetch-feed?url=https://example.com/rss')
  .then(response => response.json())
  .then(data => {
    console.log('Articles:', data.data.articles);
  });
```

### Generating AI Summary
```javascript
// JavaScript example
fetch('/api/generate-summary', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    title: 'Article Title',
    content: 'Article content...',
    max_length: 150
  })
})
.then(response => response.json())
.then(data => {
  console.log('Summary:', data.summary);
});
```

## 🎯 Future Enhancements

### Planned Features
- **Article Caching**: Store articles in database
- **User Preferences**: Save favorite feeds
- **Advanced Analytics**: Reading patterns and trends
- **Multi-language Support**: Summaries in different languages
- **Export Options**: PDF/Word document generation

### Integration Ideas
- **Email Newsletters**: Send daily digest
- **Social Media**: Auto-post summaries
- **Slack/Discord**: Bot integration
- **Mobile App**: React Native companion

---

**Your RSS feed and AI-powered article analysis system is ready to use! 🎉**

Visit http://localhost:5000/articles to start exploring articles with AI insights.
