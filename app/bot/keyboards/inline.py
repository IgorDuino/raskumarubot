from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.bot.utils.texts import _


def choose_language() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text=_("ENGLISH_LANG_BUTTON")(), callback_data="en_lang_button")
    kb.button(text=_("RUSSIAN_LANG_BUTTON")(), callback_data="ru_lang_button")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def start_webapp(button_text: str, url: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text=button_text, web_app=WebAppInfo(url=url))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def create_gif_search_results_keyboard(gifs) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for gif in gifs:
        kb.button(text=gif.file_path, callback_data=f"gif_{gif.id}")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
