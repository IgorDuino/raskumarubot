from aiogram.utils.web_app import (
    WebAppInitData,
    check_webapp_signature,
    parse_webapp_init_data,
)
from configs.settings import env_parameters
from fastapi import Header, HTTPException, status


async def init_data_headers_middleware(
    x_init_data: str | None = Header(alias="X-TG-INIT-DATA"),
) -> WebAppInitData:
    if not x_init_data or not check_webapp_signature(
        env_parameters.TELEGRAM_BOT_TOKEN, x_init_data
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User unauthorized"
        )

    return parse_webapp_init_data(x_init_data)
