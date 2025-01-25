import logging
from aiogram import Router, types
from aiogram.filters import Command
from app.core.service import search_gifs_by_tags
from app.bot.keyboards.inline import create_gif_search_results_keyboard
from app.bot.utils.texts import _

logger = logging.getLogger(__name__)
router = Router(name="GIF Search router")


@router.message(Command(commands=["gif_search"]))
async def gif_search_handler(message: types.Message):
    tags = message.get_args().split()
    if not tags:
        await message.answer(_("NO_TAGS_PROVIDED")())
        return

    gifs = await search_gifs_by_tags(tags)
    if not gifs:
        await message.answer(_("NO_GIFS_FOUND")())
        return

    keyboard = create_gif_search_results_keyboard(gifs)
    await message.answer(_("GIF_SEARCH_RESULTS")(), reply_markup=keyboard)
