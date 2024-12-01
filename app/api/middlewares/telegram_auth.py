from typing import Annotated

from aiogram.utils.web_app import WebAppInitData, check_webapp_signature, parse_webapp_init_data
from fastapi import Depends, Header, HTTPException, status

from app.core.configs.config import settings


async def telegram_auth_dependency_function(
    x_init_data: str = Header(alias="X-TG-INIT-DATA"),
) -> WebAppInitData:
    if not x_init_data or not check_webapp_signature(settings.TELEGRAM_BOT_TOKEN.get_secret_value(), x_init_data):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized")

    return parse_webapp_init_data(x_init_data)


TelegramAuthDep = Annotated[WebAppInitData, Depends(telegram_auth_dependency_function)]
