import logging

from aiogram import Bot, Router, types
from configs.settings import env_parameters
from core.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="Erorr handling router")
bot = Bot(env_parameters.TELEGRAM_BOT_TOKEN, parse_mode="HTML")


@router.errors()
async def error_handler(error_event: types.ErrorEvent):
    logger.critical(msg="Error event", exc_info=error_event.exception)

    if error_event.update.message is not None:
        chat_id = error_event.update.message.chat.id
    elif error_event.update.callback_query is not None:
        chat_id = error_event.update.callback_query.message.chat.id
    else:
        logger.error(
            "No chat_id found in error event. Not telling anyone about the error"
        )
        return

    await bot.send_message(
        chat_id,
        text=_("SOMETHING_WENT_WRONG")(),
    )
