import logging

from aiogram import Router, types

from app.core.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="Erorr handling router")


@router.errors()
async def error_handler(error_event: types.ErrorEvent):
    logger.critical(msg="Error event", exc_info=error_event.exception)

    if error_event.update.message is not None:
        chat_id = error_event.update.message.chat.id
    elif error_event.update.callback_query is not None:
        chat_id = error_event.update.callback_query.message.chat.id
    else:
        logger.error("No chat_id found in error event. Not telling anyone about the error")
        return

    await error_event.bot.send_message(
        chat_id=chat_id,
        text=_("SOMETHING_WENT_WRONG")(),
    )
