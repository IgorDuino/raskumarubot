import pytest
from fastapi import Header, HTTPException, status
from aiogram.utils.web_app import WebAppInitData
from app.api.middlewares.telegram_auth import telegram_auth_dependency_function
from app.bot.middlewares.user_block_check import UserBlockCheckMiddleware
from app.bot.middlewares.wlui.middleware import WnLoggingUserIdMiddleware
from app.core.db.models import User
from app.core.redis import RedisClient, get_redis_client

@pytest.mark.asyncio
async def test_telegram_auth_dependency_function_success(mocker):
    mocker.patch("app.api.middlewares.telegram_auth.check_webapp_signature", return_value=True)
    mocker.patch("app.api.middlewares.telegram_auth.parse_webapp_init_data", return_value=WebAppInitData(user_id=1))
    x_init_data = "valid_init_data"
    result = await telegram_auth_dependency_function(x_init_data)
    assert result.user_id == 1

@pytest.mark.asyncio
async def test_telegram_auth_dependency_function_failure(mocker):
    mocker.patch("app.api.middlewares.telegram_auth.check_webapp_signature", return_value=False)
    x_init_data = "invalid_init_data"
    with pytest.raises(HTTPException) as exc_info:
        await telegram_auth_dependency_function(x_init_data)
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.asyncio
async def test_user_block_check_middleware(mocker):
    mocker.patch("app.core.redis.get_redis_client", return_value=mocker.Mock(spec=RedisClient))
    mock_redis = get_redis_client()
    mock_redis.is_user_blocked.return_value = False
    mock_redis.set_user_block_status.return_value = None
    mocker.patch("app.core.db.models.User.get_or_none", return_value=User(id=1, is_blocked_by_bot=False))
    middleware = UserBlockCheckMiddleware()
    handler = mocker.AsyncMock()
    update = mocker.Mock()
    update.event.from_user.id = 1
    await middleware(handler, update, {})
    handler.assert_called_once()

@pytest.mark.asyncio
async def test_wn_logging_user_id_middleware(mocker):
    wlui_context = mocker.Mock()
    middleware = WnLoggingUserIdMiddleware(wlui_context)
    handler = mocker.AsyncMock()
    event = mocker.Mock()
    data = {"bot": mocker.Mock(id=1)}
    wlui_context.use_message_id.return_value = mocker.Mock()
    wlui_context.use_bot_id.return_value = mocker.Mock()
    wlui_context.use_chat_id.return_value = mocker.Mock()
    wlui_context.use_chat_type.return_value = mocker.Mock()
    await middleware(handler, event, data)
    handler.assert_called_once()
