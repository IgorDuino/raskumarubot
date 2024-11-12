import logging
from datetime import datetime

from tortoise import fields
from tortoise.models import Model

logger = logging.getLogger(__name__)


class User(Model):
    class Meta:
        table = "users"
        ordering = ["created_at"]

    id = fields.BigIntField(pk=True, unique=True, index=True)
    first_name = fields.CharField(max_length=64)
    last_name = fields.CharField(max_length=64, null=True)
    username = fields.CharField(max_length=32, index=True, null=True)
    language_code = fields.CharField(max_length=2, null=True)
    is_premium = fields.BooleanField(null=True)

    deeplink = fields.CharField(max_length=128, null=True)
    has_blocked_bot = fields.BooleanField(default=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    @classmethod
    async def update_data(
        cls,
        user_id: int,
        first_name: str,
        last_name: str,
        username: str,
        language_code: str,
        is_premium: bool,
        deeplink: str | None,
    ) -> bool:
        """Returns True if user was created, False if user was updated."""
        user = await cls.filter(id=user_id).first()
        if user is None:
            await cls.create(
                id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                language_code=language_code,
                is_premium=is_premium,
                deeplink=deeplink,
            )
            return True
        await cls.filter(id=user_id).update(
            first_name=first_name,
            last_name=last_name,
            username=username,
            language_code=language_code,
            is_premium=is_premium,
            updated_at=datetime.now(),
        )
        return False
