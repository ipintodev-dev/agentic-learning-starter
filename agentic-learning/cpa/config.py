from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int = 8000
    math_agent_http_url: str | None = None  # e.g., http://localhost:8081

settings = Settings()