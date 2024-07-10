from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Repo Insights"
    mongodb_uri: str
    github_api_repos: str = "https://api.github.com/repos/"
    github_api_repo: str = "https://api.github.com/repos/"

    class Config:
        env_file = ".env"

settings = Settings()

