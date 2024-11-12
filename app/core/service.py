import logging

from core.db.models import User
from core.redis import get_user_language_by_id, set_user_language_by_id
from tortoise.exceptions import DoesNotExist

logger = logging.getLogger(__name__)


async def get_user_language(user_id: int) -> str | None:
    """Get cached user language or re-cache new one from database"""
    result = await get_user_language_by_id(user_id)
    if result is None:
        logger.debug(f"Re-caching user language, id={user_id}")
        try:
            result = (await User.get(id=user_id).only("language_code")).language_code
        except DoesNotExist:
            logger.warning(f"User with id={user_id} not found when caching language_code")
            return None
        logger.debug(f"Caching user_id={user_id} language={result}")
        await set_user_language_by_id(user_id, result)
    return result


async def await_something(something):
    return await something
