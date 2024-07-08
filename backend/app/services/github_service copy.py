# service layer for github api 

# TODO: 
# 
# use asyncio for async operations
# this service should be a class? 

import httpx
from app.core.config import settings
from app.models.repo import Repo
from app.db.database import db

async def fetch_repo_data(repo_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.github_api_url}{repo_name}")
        if response.status_code == 200:
            repo_data = response.json()
            return Repo(
                name=repo_data["name"],
                stars=repo_data["stargazers_count"],
                owner=repo_data["owner"]["login"],
                description=repo_data["description"],
                forks=repo_data["forks_count"],
                languages=[],  # Fetch languages if needed
                topics=repo_data.get("topics", [])
            )
        return None

async def save_repo_data(repo: Repo):
    await db.repos.insert_one(repo.dict(by_alias=True))

async def get_all_repos():
    repos = await db.repos.find().to_list(100)
    return [Repo(**repo) for repo in repos]

async def get_repo_by_id(repo_id: str):
    repo = await db.repos.find_one({"_id": repo_id})
    if repo:
        return Repo(**repo)
    return None
