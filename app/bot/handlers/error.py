import logging

from aiogram import Bot, Router, types
from aiogram.client.default import DefaultBotProperties

from app.bot.utils.texts import _
from app.core.configs.config import settings

logger = logging.getLogger(__name__)
router = Router(name="Error handling router")
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode="HTML"))


@router.errors()
async def error_handler(error_event: types.ErrorEvent):
    logger.critical(msg="Error event", exc_info=error_event.exception)
    try:
        user_id = error_event.update.event.from_user.id
    except AttributeError:
        logger.debug(
            f"Update {error_event.update.event_type} does not contain user id, not telling anyone about the error."
        )
        return
    try:
        await bot.send_message(
            chat_id=user_id,
            text=_("SOMETHING_WENT_WRONG")(),
        )
    except Exception as e:
        logger.error(f"Error sending error message to user {user_id}: {e}")
