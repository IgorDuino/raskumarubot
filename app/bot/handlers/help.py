"""
Help command handler for the Telegram bot.
Provides user assistance and command documentation.
"""

import logging

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji

from app.core.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="Help router")


@router.message(Command(commands=["help"]), F.chat.type == "private")
async def help_handler(message: types.Message):
    help_text = _("HELP_COMMAND_TEXT")()

    await message.answer(text=help_text)
    await message.react([ReactionTypeEmoji(emoji="ℹ️")])
