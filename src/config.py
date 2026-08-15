from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "diario_oficial"
    database_url: str = "sqlite:///./diario.db"
    llm_api_key: str = ""


settings = Settings()