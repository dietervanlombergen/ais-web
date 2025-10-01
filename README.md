# RSS AI News Aggregator

An intelligent RSS news aggregator powered by AI that fetches articles from popular RSS feeds and provides AI-generated summaries, key points, and sentiment analysis using Cohere's advanced language models.

## 🚀 Features

### Core Functionality
- **RSS Feed Integration** - Fetch and parse articles from popular RSS feeds (BBC News, TechCrunch, Hacker News, Reddit, Python.org)
- **AI-Powered Analysis** - Generate intelligent summaries, extract key points, and analyze sentiment using Cohere AI
- **Interactive Web Interface** - Modern, responsive design with real-time article browsing
- **Custom Feed Support** - Add and analyze any RSS feed URL
- **Real-time Processing** - Instant AI analysis with loading states and error handling

### Technical Features
- **Flask Web Framework** - Robust Python web application with RESTful API
- **Cohere AI Integration** - Advanced language model integration for content analysis
- **Bootstrap 5 UI** - Modern, responsive interface with interactive components
- **Docker Support** - Containerized deployment with Docker Compose
- **Health Monitoring** - Built-in health checks and service status monitoring
- **Error Handling** - Comprehensive error handling with fallback mechanisms

## 📁 Project Structure

```
AIS/
├── app.py                    # Main Flask application with RSS and AI endpoints
├── run.py                    # Development server runner
├── requirements.txt          # Python dependencies (Flask, Cohere, BeautifulSoup, etc.)
├── Dockerfile               # Docker container configuration
├── docker-compose.yml       # Multi-service Docker setup
├── nginx.conf               # Nginx reverse proxy configuration
├── README.md                # This documentation file
├── services/                # Core application services
│   ├── ai_service.py        # Cohere AI integration for summaries and analysis
│   └── rss_service.py       # RSS feed fetching and parsing
├── templates/               # HTML templates
│   ├── base.html            # Base template with Bootstrap
│   ├── index.html           # Home page with feature overview
│   ├── articles.html        # RSS articles page with AI analysis
│   ├── about.html           # About page
│   └── contact.html         # Contact page
└── static/                  # Static assets
    ├── css/
    │   └── style.css        # Custom styles and animations
    ├── js/
    │   └── main.js          # Utility functions and interactions
    └── images/              # Image assets
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Cohere API key (for AI features)
- Docker (optional, for containerized deployment)

### Quick Start

1. **Clone or navigate to the project directory:**
   ```bash
   cd /Users/4ntoon/AIS
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file with your Cohere API key:
   ```env
   COHERE_API_KEY=your_cohere_api_key_here
   COHERE_MODEL=command-a-03-2025
   SECRET_KEY=your-secret-key-here
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```

6. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with your configuration:

```env
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Cohere AI Configuration
COHERE_API_KEY=your_cohere_api_key_here
COHERE_MODEL=command-a-03-2025
```

### Getting a Cohere API Key

1. Visit [Cohere Console](https://dashboard.cohere.ai/)
2. Sign up for an account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

**Note:** Without a Cohere API key, the application will still work but will use fallback text processing instead of AI-powered analysis.

### Adding Dependencies

To add new Python packages:

1. Install the package:
   ```bash
   pip install package-name
   ```

2. Update requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```

## 📱 Pages and Features

### Home Page (`/`)
- Hero section with call-to-action buttons
- Feature cards highlighting RSS and AI capabilities
- API status checker with AI service availability
- Responsive design with modern UI

### Articles Page (`/articles`) - **Main Feature**
- **RSS Feed Selection** - Choose from popular feeds or add custom URLs
- **Article Browsing** - Display articles with metadata, tags, and summaries
- **AI Analysis Features**:
  - 🤖 **AI Summary** - Generate intelligent article summaries
  - 📊 **Sentiment Analysis** - Analyze article sentiment with confidence scores
  - 🔑 **Key Points** - Extract main points from articles
- **Interactive Interface** - Real-time loading states and error handling
- **Responsive Design** - Works on all devices

### About Page (`/about`)
- Project information and technology stack
- Getting started instructions
- Next steps recommendations

### Contact Page (`/contact`)
- Contact information display
- Working contact form with AJAX submission
- Form validation and feedback

### API Endpoints

#### Core Endpoints
- `GET /api/health` - Health check with AI service status
- `GET /api/feeds` - Get list of available RSS feeds
- `GET /api/fetch-feed` - Fetch articles from RSS feed

#### AI Analysis Endpoints
- `POST /api/generate-summary` - Generate AI summary of article
- `POST /api/generate-key-points` - Extract key points from article
- `POST /api/analyze-sentiment` - Analyze article sentiment

## 🎨 Customization

### Styling
- Edit `static/css/style.css` for custom styles
- Bootstrap classes are available for quick styling
- Font Awesome icons are included

### Templates
- All templates extend `base.html`
- Use Jinja2 syntax for dynamic content
- Responsive design with Bootstrap grid system

### JavaScript
- Custom JavaScript in `static/js/main.js`
- Utility functions for notifications and API requests
- Smooth scrolling and animations

## 🚀 Deployment

### Local Development
```bash
# Using the development runner (recommended)
python run.py

# Or directly with Flask
python app.py
```

### Docker Deployment

#### Quick Start with Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application
http://localhost:8000
```

#### Docker Services
- **Web Application** - Main Flask app with AI services
- **Nginx** - Reverse proxy (production profile)
- **PostgreSQL** - Database (optional, database profile)

### Production Deployment

#### Using Docker Compose (Recommended)
1. **Set production environment variables:**
   ```env
   FLASK_ENV=production
   FLASK_DEBUG=False
   SECRET_KEY=your-production-secret-key
   COHERE_API_KEY=your_cohere_api_key
   ```

2. **Deploy with production profile:**
   ```bash
   docker-compose --profile production up -d
   ```

#### Manual Production Setup
1. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 120 app:app
   ```

2. **Popular deployment platforms:**
   - **Docker Hub + Cloud Platforms** - Deploy using the built Docker image
   - **AWS Elastic Beanstalk** - Supports Docker deployment
   - **Google Cloud Run** - Serverless container deployment
   - **DigitalOcean App Platform** - Container-based deployment
   - **Heroku** - Container deployment with Docker support

## 🔍 Development Tips

### Virtual Environment
- Always activate the virtual environment before development
- Use `deactivate` to exit the virtual environment
- Never commit the `venv/` directory to version control

### Code Organization
- Keep templates in the `templates/` directory
- Place static assets in the `static/` directory
- Use environment variables for configuration

### Debugging
- Flask debug mode is enabled for development
- Check browser console for JavaScript errors
- Use Flask's built-in debugger for Python errors

## 📚 Next Steps

Consider adding these features:

### Enhanced AI Features
- **Custom AI Models** - Fine-tune models for specific domains
- **Batch Processing** - Process multiple articles simultaneously
- **AI Caching** - Cache AI responses for improved performance
- **Advanced Analytics** - Trending topics, keyword analysis

### User Experience
- **User Accounts** - Personal article collections and preferences
- **Bookmarking** - Save articles for later reading
- **Search Functionality** - Search through articles and summaries
- **Email Notifications** - Daily/weekly digest emails

### Technical Improvements
- **Database Integration** - Store articles and user data
- **API Rate Limiting** - Protect against abuse
- **Caching Layer** - Redis for improved performance
- **Testing Suite** - Comprehensive unit and integration tests
- **CI/CD Pipeline** - Automated testing and deployment
- **Monitoring** - Application performance monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

### Common Issues
1. **AI Service Not Available** - Check your Cohere API key in `.env`
2. **RSS Feed Errors** - Verify feed URLs are accessible and valid
3. **Port Conflicts** - Ensure ports 5000 (dev) or 8000 (prod) are available
4. **Dependencies Issues** - Ensure virtual environment is activated and dependencies installed

### Debugging Steps
1. Check the browser console for JavaScript errors
2. Verify all dependencies are installed: `pip install -r requirements.txt`
3. Ensure the virtual environment is activated: `source venv/bin/activate`
4. Check application logs for detailed error messages
5. Test API endpoints directly: `curl http://localhost:5000/api/health`

### Getting Help
- Check the application logs for detailed error messages
- Verify your Cohere API key is valid and has sufficient credits
- Ensure your internet connection allows access to RSS feeds
- Test with the built-in health check endpoint

---

**Happy coding! 🐍🤖📰**
