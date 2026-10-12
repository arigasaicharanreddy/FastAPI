
from pydantic_settings import BaseSettings, SettingsConfigDict

# helps to read .env file 
class Settings(BaseSettings):
    DB_CONNECTION: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
