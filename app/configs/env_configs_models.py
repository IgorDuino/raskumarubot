from pydantic import BaseModel, SecretStr


class BaseConfigsModel(BaseModel):
    IS_DEBUG: bool = False


class TelegramConfigsModel(BaseModel):
    TELEGRAM_BOT_TOKEN: str


class RedisConfigsModel(BaseModel):
    REDIS_URL: str


class DataBaseConfigsModel(BaseModel):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str


class SubgramConfigsModel(BaseModel):
    SUBGRAM_API_TOKEN: SecretStr
    SUBGRAM_PRODUCT_ID: str


class BuisnessConfigsModel(BaseModel):
    DAILY_FREE_GENERATIONS: int
    GENERATIONS_PER_USER_INVITE: int


class EnvConfigsModel(
    BaseConfigsModel,
    TelegramConfigsModel,
    RedisConfigsModel,
    DataBaseConfigsModel,
    SubgramConfigsModel,
    BuisnessConfigsModel,
):
    pass
