from pydantic.v1 import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    The Settings class inherits from the parent BaseSettings class from the pydantic_settings module.
    Contains the necessary settings for working with the database, with the SMTP.server and application.
    """

    TG_TOKEN: str
    ADMIN_ID: int
    APP_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")