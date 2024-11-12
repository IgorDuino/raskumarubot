import logging

from aiogram import Bot, Dispatcher
from core import db
from fastapi import FastAPI

logger = logging.getLogger(__name__)


def register_main_bot(dp: Dispatcher, app: FastAPI, bot: Bot, **kwargs):

    @app.on_event("startup")
    async def start_bot():
        logger.info("Initializing database")
        await db.init()

    @app.on_event("shutdown")
    async def stop_bot():
        await db.close()
        await dp.stop_polling()
