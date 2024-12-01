"""
Main application entry point that initializes both FastAPI and Telegram bot.
Configures middleware, routes, and webhook handling for Telegram updates.
Sets up internationalization and logging for the application.
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.handlers import core_bot_router
from app.bot.middlewares import setup_middleware
from app.core.configs.config import settings

logger = logging.getLogger(__name__)
bot = Bot(settings.TELEGRAM_BOT_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def setup_bot(dp: Dispatcher) -> asyncio.Task | None:
    setup_middleware(dp)
    dp.include_routers(core_bot_router)
    polling_task = None
    if os.environ.get("TGBOT_IS_POLLING") == "1":
        # Start bot polling in a separate task
        logger.info("Starting bot polling")
        polling_task = asyncio.create_task(dp.start_polling(bot))
    else:
        logger.info("Setting up webhook")
        if not settings.EXTERNAL_URL:
            raise ValueError("EXTERNAL_URL is not set! Please set it in .env file.")
        webhook_url = f"{settings.EXTERNAL_URL}/webhook/telegram/{settings.TELEGRAM_BOT_TOKEN}"
        await bot.set_webhook(
            url=webhook_url,
            secret_token=settings.WEBHOOK_SECRET_TOKEN.get_secret_value() if settings.WEBHOOK_SECRET_TOKEN else None,
        )
    return polling_task


async def stop_bot(polling_task: asyncio.Task | None):
    if polling_task:
        logger.info("Stopping bot polling")
        polling_task.cancel()
        try:
            await polling_task
        except asyncio.CancelledError:
            pass
