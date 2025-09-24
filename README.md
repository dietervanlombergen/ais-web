# Python Website Development Environment

A complete Python web development setup using Flask, Bootstrap, and modern web technologies.

## 🚀 Features

- **Flask Web Framework** - Lightweight and flexible Python web framework
- **Bootstrap 5** - Modern, responsive CSS framework
- **Virtual Environment** - Isolated Python environment
- **Template Engine** - Jinja2 for dynamic HTML generation
- **Static Assets** - Organized CSS, JavaScript, and images
- **Contact Form** - Working contact form with AJAX
- **API Endpoints** - Health check and form handling APIs
- **Responsive Design** - Mobile-first approach
- **Modern UI** - Clean, professional design

## 📁 Project Structure

```
AIS/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── venv/                # Virtual environment (created after setup)
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   └── contact.html     # Contact page
└── static/              # Static assets
    ├── css/
    │   └── style.css    # Custom styles
    ├── js/
    │   └── main.js      # Custom JavaScript
    └── images/          # Image assets
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

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

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file (already included) with your configuration:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
```

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
- Feature cards highlighting key capabilities
- API status checker
- Responsive design

### About Page (`/about`)
- Project information and technology stack
- Getting started instructions
- Next steps recommendations

### Contact Page (`/contact`)
- Contact information display
- Working contact form with AJAX submission
- Form validation and feedback

### API Endpoints

- `GET /api/health` - Health check endpoint
- `POST /contact` - Contact form submission

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
python app.py
```

### Production Deployment

For production deployment, consider:

1. **Set production environment variables:**
   ```env
   FLASK_ENV=production
   FLASK_DEBUG=False
   SECRET_KEY=your-production-secret-key
   ```

2. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Popular deployment platforms:**
   - Heroku
   - DigitalOcean App Platform
   - AWS Elastic Beanstalk
   - Google Cloud Run

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

- **Database Integration**: SQLite, PostgreSQL, or MySQL
- **User Authentication**: Login/logout functionality
- **REST API**: Complete API with CRUD operations
- **Testing**: Unit tests with pytest
- **Docker**: Containerization for easy deployment
- **CI/CD**: Automated testing and deployment

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

1. Check the browser console for errors
2. Verify all dependencies are installed
3. Ensure the virtual environment is activated
4. Check that port 5000 is available

---

**Happy coding! 🐍**
