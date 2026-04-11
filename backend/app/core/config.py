from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    ENV: str
    DEBUG: bool
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()