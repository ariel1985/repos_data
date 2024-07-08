""" 
Summary: script to define the API endpoints for the repositories data.

Description: This script defines the API endpoints for the repositories data. 
It includes the following endpoints:

- GET /: Returns a list of all repositories.
- GET /{id}: Returns details for a specific repository.


Main APIs -
a. Get all repositories (limited field set).
b. Get a specific repository, according to name or ID .
3. In the case of getting a name that was not found in the database, you should go and search for it using the data collection layer.
4. In the case of an ID that was not found - return an error.


"""
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.repo import Repo, RepoCreate
from app.services.github_service import fetch_repo_data, save_repo_data, get_repo_by_id, get_all_repos

router = APIRouter()

@router.get("/", response_model=list[Repo])
async def read_repos():
    repos = await get_all_repos()
    return repos

@router.get("/{id}", response_model=Repo)
async def read_repo(id: str):
    repo = await get_repo_by_id(id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
    return repo


if __name__ == "__main__":
    username = 'ariel1985' #"octocat"
    repo_name = 'poc' #"Hello-World"
    details = read_repos()
    
    print(details)
    