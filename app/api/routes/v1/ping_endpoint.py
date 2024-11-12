import logging
from typing import Literal

from fastapi import APIRouter, status

logger = logging.getLogger(__name__)
router = APIRouter(tags=["configs"])


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
async def ping() -> dict[Literal["ping"], Literal["pong"]]:
    """Ping us!"""
    return {"ping": "pong!"}
