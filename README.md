# KAGUYA - AI Personality Engine

<div align="center">

![KAGUYA](https://kaguya-engine.vercel.app/logo.svg)

**A sophisticated AI personality engine with emotion, relationships, and evolution**

[Live Demo](https://kaguya-engine.vercel.app) • [PyPI Package](https://pypi.org/project/kaguya/) • [GitHub](https://github.com/galinaplinoel-stack/KAGUYA)

</div>

---

## About

KAGUYA is an AI Personality Engine that brings characters to life with:

- 🎭 **Personality System** - Define complex personality traits and behaviors
- 💜 **Emotion Engine** - Dynamic emotional states that evolve over time
- 💫 **Relationship System** - Track and develop relationships with users
- 🧬 **Evolution** - Personality grows and adapts through interactions
- 🧠 **Memory System** - Persistent memory across conversations
- 💬 **Conversation Memory** - Context-aware responses

## Live Website

Visit the live demo at **[kaguya-engine.vercel.app](https://kaguya-engine.vercel.app)**

Features:
- Animated space background with stars, planets, and nebula
- Interactive dashboard preview
- API documentation
- Responsive design (desktop & mobile)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/personality` | GET/POST | Manage personality traits |
| `/api/emotion` | GET/POST | Emotion state management |
| `/api/chat` | POST | Chat with AI personality |
| `/api/relationships` | GET | View relationships |
| `/api/memory` | GET | Memory system status |

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **API:** Node.js Serverless Functions
- **Hosting:** Vercel
- **Theme:** Dark cyberpunk with glassmorphism

## Installation (PyPI)

```bash
pip install kaguya
```

## Development

```bash
# Clone the repo
git clone https://github.com/galinaplinoel-stack/kaguya-vercel.git
cd kaguya-vercel

# Install dependencies
npm install

# Run locally
vercel dev
```

## Deployment

```bash
# Deploy to Vercel
vercel --prod --yes --token YOUR_TOKEN
```

## Project Structure

```
kaguya-vercel/
├── api/
│   ├── health.js
│   ├── personality.js
│   ├── emotion.js
│   ├── chat.js
│   ├── relationships.js
│   └── memory.js
├── public/
│   └── index.html
├── vercel.json
└── README.md
```

## Related Projects

- [KAGUYA Python Package](https://pypi.org/project/kaguya/) - Full Python implementation
- [KAGUYA GitHub](https://github.com/galinaplinoel-stack/KAGUYA) - Source code

## License

MIT License

---

<div align="center">

Made with 💙 by [galinaplinoel-stack](https://github.com/galinaplinoel-stack)

</div>
