import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    DEBUG: bool = False
    DATABASE_URL: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../../../.env")


settings = Settings()