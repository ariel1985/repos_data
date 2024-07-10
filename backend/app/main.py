""" 
Summary: script to define the API endpoints for the repositories data.

Description: This script defines the API endpoints for the repositories data. 
It includes the following endpoints:

- GET /: Returns a list of all repositories.
- GET /{id}: Returns details for a specific repository.


Main APIs -
1. Get all repositories (limited field set).
2. Get a specific repository, according to name or ID
3. In the case of getting a name that was not found in the database, you should go and search for it using the data collection layer.
4. In the case of an ID that was not found - return an error.

"""

from fastapi import FastAPI
from .services.github_service import GitHubService
# from fastapi.middleware.cors import CORSMiddleware
# import db service
from .services.mongodb_service import DBService

app = FastAPI()

GHservice = GitHubService()
DBService = DBService()

@app.get("/")
def get_all_repos():
    # TODO : Add pagination limit
    return GHservice.fetch_all_repos()

@app.get("/{repo_name}")
def get_repo_by_name(repo_name: str):
    # check if the repo exists in the database
    DBrepo = DBService.get_repo("repos", {"Name": repo_name})
    if DBrepo:
        return DBrepo
    
    # if not, fetch it from the GitHub API
    repo = GHservice.fetch_repo_data(repo_name)
    if "error" in repo:
        return {"error": "Repository not found"}
    return repo


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
# Run the FastAPI application using the following command:
# uvicorn app.main:app --reload

# To view the API documentation, navigate to /docs
