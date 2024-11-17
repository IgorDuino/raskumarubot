import logging

from aiogram import F, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji

from app.bot.keyboards.inline import choose_language
from app.core.db.models import User
from app.core.redis import RedisClient
from app.core.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="Start router")


@router.message(Command(commands=["start"]), F.chat.type == "private")
async def start_handler(message: types.Message, command: CommandObject, redis: RedisClient):
    await message.answer(text=_("START_COMMAND_TEXT")(), reply_markup=choose_language())
    await message.react([ReactionTypeEmoji(emoji="❤")])

    user, is_created = await User.update_or_create(
        id=message.from_user.id,
        defaults={
            "first_name": message.from_user.first_name,
            "last_name": message.from_user.last_name,
            "username": message.from_user.username,
            "language_code": message.from_user.language_code,
            "is_premium": message.from_user.is_premium,
            "deeplink": command.args,
            "is_blocked_by_user": False,
            "is_blocked_by_bot": False,
        },
    )

    await redis.set_user_block_status(message.from_user.id, False)
