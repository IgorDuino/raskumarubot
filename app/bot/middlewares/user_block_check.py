import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from app.core.db.models import User
from app.core.redis import RedisClient, get_redis_client

logger = logging.getLogger(__name__)


class UserBlockCheckMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self._redis: RedisClient = get_redis_client()
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id

        # Get blocked status from Redis bitmap
        is_blocked = await self._redis.get_user_block_status(user_id)

        if not is_blocked:
            # If not in bitmap or not blocked, check DB
            user = await User.get_or_none(id=user_id)
            if user and user.is_blocked_by_bot:
                await self._redis.set_user_block_status(user_id, True)
                is_blocked = True

        # If user is blocked, don't process the message
        if is_blocked:
            logger.info(f"Blocked user {user_id} tried to interact with bot")
            return

        # Continue processing if user is not blocked
        return await handler(event, data)
