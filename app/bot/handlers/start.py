import logging

from aiogram import F, Router, types
from aiogram.filters import Command, CommandObject
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji
from configs.settings import env_parameters
from core.db.models import User
from core.keyboards.inline import choose_generate_action, choose_language
from core.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="Start router")


@router.message(Command(commands=["start"]), F.chat.type == "private")
async def start_handler(message: types.Message, command: CommandObject):
    # add basic info to db
    deeplink = command.args
    deeplink_split = deeplink.split("_", "") if deeplink is not None else None
    if deeplink is not None and len(deeplink_split) == 2:
        try:
            user_who_invited_id = int(deeplink_split[1])
        except ValueError:
            user_who_invited_id = None
    else:
        user_who_invited_id = None

    if user_who_invited_id is not None and not await User.exists(
        id=user_who_invited_id
    ):
        logger.warning(f"User with id={user_who_invited_id} not found")
        user_who_invited_id = None

    await message.react([ReactionTypeEmoji(emoji="❤")])
    user_language = "ru" if message.from_user.language_code == "ru" else "en"
    is_created = await User.update_data(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
        message.from_user.language_code,
        user_language,
        message.from_user.is_premium,
        deeplink,
    )
    if is_created:
        await message.answer(
            text=_("START_COMMAND_FIRST_TIME")(), reply_markup=choose_language()
        )
        if user_who_invited_id is not None:
            await User.filter(id=message.from_user.id).update(
                invited_by=user_who_invited_id,
                free_credit_count=env_parameters.GENERATIONS_PER_USER_INVITE,
            )
            user_who_invited = await User.get(id=user_who_invited_id)
            user_who_invited.free_credit_count += (
                env_parameters.GENERATIONS_PER_USER_INVITE
            )
            await user_who_invited.save()
            await message.bot.send_message(
                user_who_invited_id,
                _(
                    "USER_JOINED_BY_YOUR_URL",
                    name=f"@{message.from_user.username}" if message.from_user.username else message.from_user.full_name,
                    credit_count=str(env_parameters.GENERATIONS_PER_USER_INVITE),
                )(),
            )
    else:
        await message.answer(
            text=_("START_COMMAND_WELCOME_BACK")(),
            reply_markup=choose_generate_action(),
        )
