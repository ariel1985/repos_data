from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Repo Insights"
    mongodb_uri: str
    github_api_url: str = "https://api.github.com/repos/"

    class Config:
        env_file = ".env"

settings = Settings()

