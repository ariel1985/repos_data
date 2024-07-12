""" 
Summary: script to define the API endpoints for the repositories data.

Description: This script defines the API endpoints for the repositories data. 
It includes the following endpoints:

- GET /: Returns a list of all repositories.
- GET /{id}: Returns details for a specific repository.


1. Create a data retrieval module which uses github api. This module should get a
name of github repository and returns the following data : ID, Stars, Owner,
Description, Forks, Languages, number of forks, topics.
*NOTE: If the search result is several repositories, take the first one.
You should find how to use Github API
(https://docs.github.com/en/rest?apiVersion=2022-11-28)

2. Data should be kept in a database.

3. The module should have a specific API, which can be used in order to trigger the
collection of a specific repository’s data.

"""

from fastapi import FastAPI
from .services.github_service import GitHubService
# from fastapi.middleware.cors import CORSMiddleware
from .services.mongodb_service import DBService
from .schemas.repo import Repository


app = FastAPI()

GHservice = GitHubService()
DBService = DBService()

# Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )




@app.get("/")
def get_all_repos():
    # TODO : Add pagination limit
    return GHservice.fetch_all_repos()

@app.get("/{repo_name}")
def retrieve_repo_by_name(repo_name: str):
    """Retrieve a repository by name.

    Args:
        repo_name (str): name or id of the repository

    Returns:
        _type_: Repository: Repository data
    """
    
    # Fetch repo from the database
    repo = GHservice.fetch_repo_data(repo_name)
    if "error" in repo:
        return {"error": "Repository not found"}
    
    # set the repository data
    repo = Repository(
        ID=repo["ID"],
        Name=repo["Name"],
        Owner=repo["Owner"],
        Stars=repo["Stars"],
        Description=repo["Description"],
        Forks=repo["Forks"],
        Languages=repo["Languages"],
    )
    
    # Save repo to the database
    
    # insert the repository into the database
    inserted_id = DBService.insert_repo("repos", repo)
    
    if inserted_id:
        print(f"Inserted repository with ID: {inserted_id}")
    else:
        print("Failed to insert repository")
        # TODO: log the error - use logger
    
    return repo


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run the FastAPI application using the following command:

# uvicorn app.main:app --reload

# To view the API documentation, navigate to /docs
