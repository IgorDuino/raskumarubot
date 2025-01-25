"""
Core service layer for user-related operations.

Provides functions for managing user data and preferences:
- Language preferences caching and retrieval
- User data validation and processing
- Integration with Redis cache and database
"""

import logging
import os
from typing import List
from PIL import Image, ImageSequence
import openai

from tortoise.exceptions import DoesNotExist

from app.core.db.models import User, GIF
from app.core.redis import RedisClient, get_redis_client

logger = logging.getLogger(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


async def get_user_language(user_id: int) -> str | None:
    """Get cached user language or re-cache new one from database"""
    redis_client: RedisClient = get_redis_client()
    result = await redis_client.get_user_language_by_id(user_id)
    if result is None:
        logger.debug(f"Re-caching user language, id={user_id}")
        try:
            result = (await User.get(id=user_id).only("language_code")).language_code
        except DoesNotExist:
            logger.warning(f"User with id={user_id} not found when caching language_code")
            return None
        logger.debug(f"Caching user_id={user_id} language={result}")
        await redis_client.set_user_language_by_id(user_id, result)
    return result


async def await_something(something):
    return await something


def extract_middle_frame(gif_path: str) -> Image:
    """Extract the middle frame from a GIF."""
    with Image.open(gif_path) as img:
        frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
        middle_frame = frames[len(frames) // 2]
        return middle_frame


async def process_frame_with_openai(frame: Image) -> List[str]:
    """Process the extracted frame using OpenAI Batch API GPT-4 vision."""
    frame_path = "/tmp/middle_frame.png"
    frame.save(frame_path)

    with open(frame_path, "rb") as image_file:
        response = openai.Image.create(
            file=image_file,
            model="gpt-4-vision",
            prompt="Extract text, key moments, and humor-related tags from this image. Focus on identifying elements that contribute to humor, such as facial expressions, actions, and context. Exclude tags like 'кот' or 'комару'.",
            size="500x500"
        )

    tags = response["data"]["tags"]
    return tags


async def save_gif_tags(gif_path: str, tags: List[str]):
    """Save the extracted tags to the database."""
    gif, created = await GIF.get_or_create(file_path=gif_path)
    gif.tags = tags
    await gif.save()
