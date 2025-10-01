©# Cohere AI Integration Setup Guide

Your Python website now uses **Cohere AI** for powerful article analysis! This guide will help you set up and configure Cohere for optimal performance.

## 🚀 Why Cohere?

- **Cost-Effective**: More affordable than many AI alternatives
- **High Quality**: Excellent for text generation and analysis
- **Fast Response**: Quick API responses
- **Reliable**: Stable and well-maintained service
- **Command Model**: Cohere's flagship model for best results

## 🔑 Getting Your Cohere API Key

### Step 1: Create Account
1. Visit [Cohere Dashboard](https://dashboard.cohere.ai/)
2. Sign up for a free account
3. Verify your email address

### Step 2: Generate API Key
1. Go to [API Keys](https://dashboard.cohere.ai/api-keys)
2. Click "Create API Key"
3. Give it a descriptive name (e.g., "Python Website")
4. Copy the generated key (starts with `co-`)

### Step 3: Set Environment Variable
```bash
# Set the API key
export COHERE_API_KEY="co-your-api-key-here"

# Or add to your .env file
echo "COHERE_API_KEY=co-your-api-key-here" >> .env
```

## 🛠️ Testing the Integration

### 1. Start the Server
```bash
source venv/bin/activate
python app.py
```

### 2. Check AI Status
```bash
curl http://localhost:5000/api/health
```

You should see:
```json
{
  "ai_available": true,
  "message": "Server is running",
  "status": "healthy"
}
```

### 3. Test AI Features
1. Visit http://localhost:5000/articles
2. Fetch some articles from a RSS feed
3. Click "AI Summary" or "Sentiment" buttons
4. Watch the AI analysis appear in modal dialogs!

## 📊 Cohere Model Details

### Command Model
- **Purpose**: General-purpose text generation
- **Strengths**: Summaries, analysis, reasoning
- **Context Window**: 4,096 tokens
- **Best For**: Article summarization and analysis

### Parameters Used
```python
{
    'model': 'command',
    'temperature': 0.3,      # Balanced creativity
    'max_tokens': 300,       # Appropriate length
    'p': 0.75,              # Nucleus sampling
    'k': 0,                 # No top-k filtering
    'frequency_penalty': 0,  # No repetition penalty
    'presence_penalty': 0    # No topic penalty
}
```

## 💰 Cost Information

### Pricing (as of 2024)
- **Free Tier**: 1,000 tokens/month
- **Pay-as-you-go**: $0.0015 per 1,000 tokens
- **Typical Article Analysis**: ~200-400 tokens
- **Cost per Article**: ~$0.0003-0.0006

### Usage Monitoring
1. Visit your [Cohere Dashboard](https://dashboard.cohere.ai/)
2. Check "Usage" tab for current consumption
3. Set up billing alerts if needed

## 🔧 Configuration Options

### Environment Variables
```env
# Required for AI features
COHERE_API_KEY=your-api-key-here

# Optional: Customize AI behavior
COHERE_MODEL=command
COHERE_TEMPERATURE=0.3
COHERE_MAX_TOKENS=300
```

### Customizing AI Prompts
Edit `services/ai_service.py` to modify AI behavior:

```python
# Custom summary prompt
prompt = f"""
You are an expert article summarizer. Create a {max_length}-word summary of this article:

Title: {article_title}
Content: {article_content[:3000]}

Focus on the most important information and key takeaways.

Summary:"""
```

## 🎯 AI Features Available

### 1. Article Summaries
- **Input**: Article title and content
- **Output**: Concise 150-word summary
- **Use Case**: Quick article understanding

### 2. Key Points Extraction
- **Input**: Article content
- **Output**: 5 main bullet points
- **Use Case**: Identifying core topics

### 3. Sentiment Analysis
- **Input**: Article content
- **Output**: Sentiment (positive/negative/neutral) with confidence
- **Use Case**: Understanding article tone

## 🚨 Troubleshooting

### Common Issues

#### "Cohere API key not found"
```bash
# Check if environment variable is set
echo $COHERE_API_KEY

# If empty, set it:
export COHERE_API_KEY="your-key-here"
```

#### "Failed to initialize Cohere client"
- Verify API key format (should start with `co-`)
- Check internet connection
- Ensure account has credits

#### "Rate limit exceeded"
- Wait a few minutes before retrying
- Consider upgrading your Cohere plan
- Implement request throttling

#### Poor AI Quality
- Increase `max_tokens` for longer responses
- Adjust `temperature` (0.1-0.5 for more focused)
- Improve prompt clarity

### Debug Mode
Enable detailed logging:
```python
# In services/ai_service.py
logging.basicConfig(level=logging.DEBUG)
```

## 🔒 Security Best Practices

### API Key Management
```bash
# Never commit API keys to git
echo "COHERE_API_KEY" >> .gitignore

# Use environment variables in production
export COHERE_API_KEY="production-key"

# Rotate keys regularly
```

### Production Deployment
```bash
# Docker environment
docker run -e COHERE_API_KEY="your-key" python-website

# Docker Compose
environment:
  - COHERE_API_KEY=your-production-key
```

## 📈 Performance Optimization

### Caching
```python
# Implement response caching
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_summary(title, content):
    return generate_summary(title, content)
```

### Batch Processing
```python
# Process multiple articles at once
articles = [article1, article2, article3]
summaries = [generate_summary(a.title, a.content) for a in articles]
```

### Error Handling
```python
try:
    response = self.client.generate(...)
except cohere.CohereError as e:
    logger.error(f"Cohere API error: {e}")
    return fallback_response()
```

## 🔄 Migration from OpenAI

If you were previously using OpenAI:

### Changes Made
- ✅ Replaced `openai` with `cohere` library
- ✅ Updated API calls to use Cohere format
- ✅ Changed environment variable from `OPENAI_API_KEY` to `COHERE_API_KEY`
- ✅ Updated prompts for Cohere's model

### Benefits of Cohere
- Lower cost per token
- Faster response times
- Better for text analysis tasks
- More predictable pricing

## 📚 Additional Resources

### Cohere Documentation
- [Official Cohere Docs](https://docs.cohere.com/)
- [API Reference](https://docs.cohere.com/reference)
- [Model Comparison](https://docs.cohere.com/docs/models)

### Community
- [Cohere Discord](https://discord.gg/cohere)
- [GitHub Examples](https://github.com/cohere-ai)
- [Blog & Tutorials](https://txt.cohere.com/)

## 🎉 Success!

Your Python website now has powerful AI capabilities powered by Cohere! 

**Next Steps:**
1. Get your Cohere API key
2. Set the environment variable
3. Restart the server
4. Enjoy AI-powered article analysis!

Visit http://localhost:5000/articles to see it in action! 🚀
