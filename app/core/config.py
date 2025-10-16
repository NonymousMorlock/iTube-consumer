from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    REGION_NAME: str
    AWS_SQS_VIDEO_PROCESSING_QUEUE: str


settings = Settings()
