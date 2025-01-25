from aiogram import Router

from app.bot.handlers import error, help, start, gif_search

core_bot_router = Router()
core_bot_router.include_routers(
    error.router,
    start.router,
    help.router,
    gif_search.router,
)
