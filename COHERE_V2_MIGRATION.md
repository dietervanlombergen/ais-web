# Cohere Chat API v2 Migration

Deze update migreert je applicatie naar Cohere's nieuwe Chat API v2 na de deprecation van de Generate API op 15 september 2025.

## 🔄 Wat is er veranderd?

### API Migratie
- ✅ **Oude API**: `cohere.Client()` + `client.generate()`
- ✅ **Nieuwe API**: `cohere.ClientV2()` + `client.chat()`

### Belangrijkste Wijzigingen
1. **Client**: `Client()` → `ClientV2()`
2. **API Call**: `generate()` → `chat()`
3. **Parameters**: `prompt` → `messages` array
4. **Response**: `response.generations[0].text` → `response.message.content[0].text`
5. **Model**: `command` → `command-a-03-2025` (of andere snapshot)

## 🛠️ Technische Details

### Nieuwe Code Structuur
```python
# OLD (deprecated sinds 15-09-2025)
client = cohere.Client(api_key)
response = client.generate(model="command", prompt=text)
result = response.generations[0].text

# NEW (Chat API v2)
client = cohere.ClientV2(api_key)
response = client.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": text}]
)
result = response.message.content[0].text
```

### Environment Variables
```env
# Vereist
COHERE_API_KEY=co-your-api-key-here

# Optioneel (default: command-a-03-2025)
COHERE_MODEL=command-a-03-2025
```

## 📦 Dependencies Update

### Requirements.txt
```
cohere>=5.0.0  # Was: cohere==4.37
```

### Installatie
```bash
pip install --upgrade cohere
```

## 🚀 Deployment

### Docker Compose
```yaml
environment:
  - COHERE_API_KEY=${COHERE_API_KEY}
  - COHERE_MODEL=${COHERE_MODEL:-command-a-03-2025}
```

### Environment Setup
```bash
# Set je API key (zelfde als voorheen)
export COHERE_API_KEY="co-your-api-key-here"

# Optioneel: kies een ander model
export COHERE_MODEL="command-a-03-2025"
```

## 🔍 Beschikbare Models

### Command Snapshots
- `command-a-03-2025` - Nieuwste algemene model
- `command-r-08-2024` - Fallback optie
- `command-light` - Sneller, minder tokens

### Model Selection
```python
# In services/ai_service.py
self.model_id = os.getenv('COHERE_MODEL', 'command-a-03-2025')
```

## ✅ Wat Werkt Nu

### AI Features
1. **Article Summaries**: Concisie samenvattingen via Chat API v2
2. **Key Points**: Belangrijkste punten extractie
3. **Sentiment Analysis**: Positief/negatief/neutraal analyse
4. **Fallback Support**: Werkt zonder API key (basis samenvattingen)

### API Endpoints
- `POST /api/generate-summary` - AI samenvattingen
- `POST /api/generate-key-points` - Belangrijkste punten
- `POST /api/analyze-sentiment` - Sentiment analyse

## 🧪 Testing

### Health Check
```bash
curl http://localhost:8000/api/health
```

Verwacht:
```json
{
  "ai_available": true,
  "message": "Server is running",
  "status": "healthy"
}
```

### AI Features Test
1. Ga naar http://localhost:8000/articles
2. Fetch RSS artikelen
3. Klik "AI Summary" of "Sentiment" buttons
4. Verifieer AI analyse verschijnt

## 🔒 Security & Best Practices

### API Key Management
```bash
# Nooit committen naar git
echo "COHERE_API_KEY" >> .gitignore

# Environment variables gebruiken
export COHERE_API_KEY="co-your-key-here"

# Rotate keys regelmatig
```

### Production Deployment
```bash
# Docker met environment variables
docker run -e COHERE_API_KEY="your-key" python-website:latest

# Docker Compose
COHERE_API_KEY=your-production-key docker-compose up
```

## 🐛 Troubleshooting

### Common Issues

#### "Generate API was removed" Error
```bash
# Oplossing: Upgrade naar Chat API v2 (al gedaan)
pip install --upgrade cohere>=5.0.0
```

#### "ClientV2 not found" Error
```bash
# Oplossing: Upgrade Cohere library
pip install --upgrade cohere
```

#### Model Not Found
```bash
# Check beschikbare models
# Default: command-a-03-2025
# Fallback: command-r-08-2024
```

### Debug Logging
```python
# In services/ai_service.py
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Performance

### Kosten
- **Chat API v2**: Vergelijkbare prijzen als Generate API
- **Model Snapshots**: Verschillende kosten per model
- **Token Usage**: Ongeveer 200-400 tokens per artikel analyse

### Optimalisatie
```python
# Caching implementeren
@lru_cache(maxsize=100)
def cached_summary(title, content):
    return generate_summary(title, content)

# Batch processing
articles = [article1, article2, article3]
summaries = [generate_summary(a.title, a.content) for a in articles]
```

## 🎯 Voordelen van Chat API v2

1. **Future-Proof**: Nieuwste Cohere API
2. **Better Performance**: Geoptimaliseerd voor chat workflows
3. **More Flexible**: Betere conversation handling
4. **Active Support**: Cohere's focus ligt nu op Chat API

## 🚀 Next Steps

### Immediate
1. ✅ Migratie naar ClientV2 voltooid
2. ✅ Chat API v2 geïmplementeerd
3. ✅ Docker Compose geüpdatet
4. ✅ Requirements.txt geüpdatet

### Optional Enhancements
1. **Model Selection UI**: Dropdown voor model keuze
2. **Response Caching**: Cache AI responses
3. **Batch Processing**: Meerdere artikelen tegelijk
4. **Error Recovery**: Betere fallback handling

## 🎉 Success!

Je applicatie gebruikt nu Cohere's nieuwste Chat API v2! 

**Verificatie:**
1. Start je containers: `docker-compose up`
2. Check logs: `docker-compose logs web`
3. Test AI features: http://localhost:8000/articles
4. Geniet van AI-powered artikel analyse! 🚀

---

**Migration voltooid op:** $(date)  
**Cohere Library Version:** 5.18.0  
**API Version:** Chat API v2  
**Status:** ✅ Production Ready
