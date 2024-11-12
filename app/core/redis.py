import logging
import uuid
from datetime import timedelta
from typing import Optional

import orjson
import redis.asyncio as aioredis
from configs.settings import env_parameters
from core.schemas.text_to_image_prompt import UserTextToImageSettings
from pydantic import BaseModel

pool = aioredis.ConnectionPool.from_url(
    str(env_parameters.REDIS_URL), max_connections=10, decode_responses=True
)
redis_client = aioredis.Redis(connection_pool=pool)
logger = logging.getLogger(__name__)


class RedisData(BaseModel):
    key: bytes | str
    value: bytes | str
    ttl: Optional[int | timedelta] = None


async def __set_redis_key(
    redis_data: RedisData, *, is_transaction: bool = False
) -> None:
    async with redis_client.pipeline(transaction=is_transaction) as pipe:
        await pipe.set(redis_data.key, redis_data.value)
        if redis_data.ttl:
            await pipe.expire(redis_data.key, redis_data.ttl)

        await pipe.execute()


async def set_by_key(key: str, value: str, ttl: int | timedelta | None = None) -> None:
    return await __set_redis_key(RedisData(key=key, value=value, ttl=ttl))


async def get_by_key(key: str) -> str | None:
    return await redis_client.get(key)


async def get_generation_url_by_id(generation_id: str) -> str | None:
    logger.debug(f"Getting generation url by id: {generation_id}")
    return await redis_client.get(f"generation_url:{generation_id}")


async def set_generation_settings_by_uuid(
    uuid: uuid.UUID, settings: UserTextToImageSettings
) -> None:
    await set_by_key(
        f"outfit_generation_settings:{uuid}",
        value=orjson.dumps(settings.model_dump()),
        ttl=timedelta(minutes=59),
    )


async def set_generation_url_by_id(generation_id: str, url: str) -> None:
    logger.debug(f"Setting generation url by id: {generation_id}, url={url}")
    await set_by_key(f"generation_url:{generation_id}", url, timedelta(minutes=59))


async def get_generation_settings_by_uuid(
    uuid: uuid.UUID,
) -> UserTextToImageSettings | None:
    data = await get_by_key(f"outfit_generation_settings:{uuid}")
    return UserTextToImageSettings(**data) if data else None


async def get_telegram_file_id_by_id(id: str):
    return await get_by_key(f"generation_tg_file_id:{id}")


async def set_telegram_file_id_by_id(id: str, file_id: str):
    return await set_by_key(f"generation_tg_file_id:{id}", file_id)


async def set_user_language_by_id(id: int, lang: str) -> None:
    await set_by_key(f"user:language:{id}", lang)


async def get_user_language_by_id(id: int) -> str | None:
    return await get_by_key(f"user:language:{id}")


async def set_user_premium_by_id(user_id: int, is_premium: bool) -> None:
    # for 15 minutes is_premium is cached to not hit the other service via API
    await set_by_key(get_user_premium_key(user_id), str(is_premium), ttl=60 * 15)


async def get_user_premium_by_id(user_id: int) -> bool | None:
    bool_str = await get_by_key(get_user_premium_key(user_id))
    return True if bool_str == "True" else False if bool_str == "False" else None


async def delete_by_key(key: str) -> None:
    return await redis_client.delete(key)


async def get_user_text_to_image_settings_by_key(key: str) -> dict | None:
    generation_settings = await redis_client.get(key)
    return orjson.loads(generation_settings) if generation_settings else None


async def set_user_text_to_image_settings_by_key(
    key: str, generation_settings: dict
) -> None:
    await set_by_key(key, orjson.dumps(generation_settings))
