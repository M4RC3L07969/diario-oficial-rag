from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "official_gazettes"
    database_url: str = "sqlite:///./gazettes.db"
    llm_api_key: str = ""


settings = Settings()