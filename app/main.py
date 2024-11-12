import logging
from typing import Any, Dict

from aiogram import Bot, Dispatcher
from aiogram.types import Update
from api.routes import app
from bot.handlers import (
    error,
    start,
)
from configs.settings import env_parameters
from bot.middlewares.i18n_middleware import i18n_middleware
from core.setup import local_register
from core.wlui.context import WLUIContextVar
from core.wlui.middleware import WnLoggingUserIdMiddleware
from fastapi import status

bot = Bot(env_parameters.TELEGRAM_BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher()
i18n_middleware.setup(dp)
dp.update.middleware.register(wnl_middleware)

dp.include_routers(
    error.router,
    start.router,
)

logger = logging.getLogger(__name__)


@app.post(
    f"/webhook/telegram/{env_parameters.TELEGRAM_BOT_TOKEN}",
    status_code=status.HTTP_200_OK,
    include_in_schema=False,
)
async def handle_telegram_update(payload: Dict[Any, Any]):
    try:
        update = Update(**payload)
    except Exception:
        logger.warning(f"Bad tg update. Payload: {payload}")
        return {"status": "error"}

    return await dp.feed_update(bot, update)


local_register.register_main_bot(
    dp, app, bot, allowed_updates=dp.resolve_used_update_types()
)
