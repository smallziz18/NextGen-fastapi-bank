from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

BASE_DIR = Path(__file__).parent.parent.parent.parent  # ajuste selon la profondeur
ENV_FILE = BASE_DIR / ".envs/.env"

class Settings(BaseSettings):
    ENVIRONMENT: Literal["dev", "test", "prod"] = "dev"
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore"
    )
    API_V1_STR: str = ""
    PROJECT_NAME: str = ""
    PROJECT_DESCRIPTION: str = ""
    SITE_NAME: str = ""


settings = Settings()
print("Loaded settings:", settings.model_dump())
