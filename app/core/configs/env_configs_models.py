from pydantic import BaseModel, SecretStr


class BaseConfigsModel(BaseModel):
    IS_DEBUG: bool = False
    EXTERNAL_URL: str | None = None


class TelegramConfigsModel(BaseModel):
    TELEGRAM_BOT_TOKEN: SecretStr
    WEBHOOK_SECRET_TOKEN: SecretStr | None = None


class RedisConfigsModel(BaseModel):
    REDIS_URL: str


class DataBaseConfigsModel(BaseModel):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str


class SettingsModel(
    BaseConfigsModel,
    TelegramConfigsModel,
    RedisConfigsModel,
    DataBaseConfigsModel,
):
    pass
