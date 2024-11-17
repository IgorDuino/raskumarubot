import logging

import aiohttp
from fastapi import APIRouter, status
from redis import Redis
from tortoise import connections

from app.core.configs.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(tags=["health"])


async def check_database_connection() -> bool:
    try:
        conn = connections.get("default")
        await conn.execute_query("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return False


async def check_redis_connection() -> bool:
    try:
        redis_client = Redis.from_url(settings.REDIS_URL)
        return redis_client.ping()
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        return False


async def check_telegram_api() -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/getMe") as response:
                return response.status == 200
    except Exception as e:
        logger.error(f"Telegram API health check failed: {str(e)}")
        return False


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_endpoint():
    database_connection: bool = await check_database_connection()
    redis_connection: bool = await check_redis_connection()
    api_connection: bool = await check_telegram_api()

    health = database_connection and redis_connection and api_connection
    return {
        "health": "ok" if health else "partial",
        "status": {
            "database": database_connection,
            "redis": redis_connection,
            "api": api_connection,
        },
    }
