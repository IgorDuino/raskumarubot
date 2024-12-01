import logging
from typing import Any, Dict

from aiogram.types import Update
from fastapi import APIRouter, status

from app.bot import bot, dp
from app.core.configs.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(tags=["webhook"])


@router.post(
    f"/webhook/telegram/{settings.TELEGRAM_BOT_TOKEN.get_secret_value()}",
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
