# 🚀 Ultimate Telegram Bot Template

A supercharged, production-ready template for building scalable Telegram bots with all the bells and whistles!

## ✨ Features

- 🤖 **Aiogram 3** - Built with [aiogram](https://docs.aiogram.dev/) for elegant bot handlers
- ⚡ **FastAPI Integration** - Lightning-fast API endpoints with automatic OpenAPI docs
- 🔥 **Webhook Support** - Production-ready webhook handling for reliable bot updates
- 🗄️ **Database Ready** - Pre-configured database integration with Tortoise ORM
- 📡 **Redis Support** - Built-in Redis for caching and real-time data handling
- 🌍 **i18n Support** - Multi-language support using Babel
- 🔐 **Environment Management** - Secure configuration using Pydantic settings
- 📊 **Logging & Monitoring** - Comprehensive logging setup with rotating file handlers
- 🐳 **Docker Support** - Containerized for easy deployment and scaling
- 🧪 **Health Checks** - Built-in health check endpoints for monitoring

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Modern API framework
- [aiogram](https://docs.aiogram.dev/) - Powerful Telegram Bot framework
- [Tortoise ORM](https://tortoise.github.io/) - Easy async ORM for Python
- [Redis](https://redis.io/) - In-memory data store
- [Babel](https://babel.pocoo.org/) - Internationalization framework
- [Docker](https://www.docker.com/) - Containerization
- [Poetry](https://python-poetry.org/) - Dependency management

## 🚀 Quick Start

1. Clone the repository:

```bash
git clone https://github.com/verybigsad/telegram-bot-template.git
```

2. Install dependencies:

```bash
poetry install
```

3. Set up your environment variables:

```bash
cp app/.env.example app/.env
```

4. Run the bot in polling mode:

```bash
python start-polling.py
```

## 🔧 Configuration

soon to be here :eyes:

## 📝 Project Structure

```
app/
├── api/            # FastAPI routes and schemas
├── core/           # Core functionality
│   ├── db/         # Database models and config
│   ├── redis/      # Redis integration
├── locales/        # Locales for i18n
└── bot/            # Telegram bot handlers and logic
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

Built with ❤️ and ☕ by verybigsad.
- [github](https://github.com/verybigsad)
- [telegram](https://t.me/verybigsad)
- [linkedin](https://www.linkedin.com/in/m-khromov/)
