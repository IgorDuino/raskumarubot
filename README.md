# 🤖 Raskumarubot

Raskumarubot is a Telegram bot designed to provide various functionalities, including GIF search, user management, and more. This bot is built using aiogram and FastAPI, and it leverages Redis for caching and Tortoise ORM for database interactions.

## ✨ Features

- **GIF Search**: Search for GIFs based on tags.
- **User Management**: Manage user data and preferences.
- **Health Checks**: Monitor the health of the bot and its dependencies.
- **i18n Support**: Multi-language support using Babel.
- **Webhook Support**: Production-ready webhook handling for reliable bot updates.
- **Polling Mode**: Run the bot in polling mode for development and testing.

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
git clone https://github.com/IgorDuino/raskumarubot.git
```

2. Install dependencies:

```bash
poetry install
```

3. Set up your environment variables:

```bash
cp .env.example .env
```

4. Run the bot in polling mode:

```bash
python run_polling.py
```

## 🔧 Configuration

To configure the bot, update the `.env` file with the necessary environment variables:

- `IS_DEBUG`: Set to `True` for debug mode, `False` for production.
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `REDIS_URL`: URL for your Redis instance.
- `DB_USERNAME`: Database username.
- `DB_PASSWORD`: Database password.
- `DB_HOST`: Database host.
- `DB_PORT`: Database port.
- `DB_NAME`: Database name.

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
