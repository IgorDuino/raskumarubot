import logging

from aiogram import Dispatcher
from aiogram.utils.i18n import I18n

from app.bot.middlewares.i18n_middleware import CustomFSMI18nMiddleware
from app.bot.middlewares.user_block_check import UserBlockCheckMiddleware
from app.bot.middlewares.wlui.context import WLUIContextVar
from app.bot.middlewares.wlui.middleware import WnLoggingUserIdMiddleware

logger = logging.getLogger(__name__)


def setup_middleware(dp: Dispatcher) -> None:
    """Setup middleware for the bot.

    Args:
        dp (Dispatcher): The dispatcher to setup middleware for.
    """
    logger.info("Setting up middleware")
    i18n_middleware = CustomFSMI18nMiddleware(I18n(path="app/locales", default_locale="en", domain="messages"))
    wnl_middleware = WnLoggingUserIdMiddleware(WLUIContextVar())
    user_blockcheck_middleware = UserBlockCheckMiddleware()

    i18n_middleware.setup(dp)
    dp.update.middleware.register(wnl_middleware)
    dp.update.middleware.register(user_blockcheck_middleware)
