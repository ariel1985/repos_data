""" 
Summary: script to define the API endpoints for the repositories data.

Description: This script defines the API endpoints for the repositories data. 
It includes the following endpoints:
- A welcome endpoint that returns a welcome message.
- An endpoint to retrieve a repository data by name from GitHub API and save it to the database.

1. Create a data retrieval module which uses github api. This module should get a
name of github repository and returns the following data : ID, Stars, Owner,
Description, Forks, Languages, number of forks, topics.
*NOTE: If the search result is several repositories, take the first one.

2. Data should be kept in a database.

3. The module should have a specific API, which can be used in order to trigger the
collection of a specific repository’s data.

"""

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import ValidationError
# from fastapi.middleware.cors import CORSMiddleware
from .service_github import GitHubService
from .service_mongodb import DBService
from .models import RepoModel 

app = FastAPI()

github = GitHubService()
db = DBService()


# TODO: CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def welcome():
    return {
        "message": "Welcome to the Repositories API",
        "docs_url": "http://localhost:8000/docs",
    }

# Retrieve a repository data by name from GitHub API and save it to the database.
@app.get("/{repo_name}", response_model=RepoModel)
def retrieve_repo_by_name(repo_name: str) -> RepoModel:
    
    print ('repo_name:', repo_name)
    # Fetch repository data from GitHub API
    data = github.fetch_repo_data(repo_name)
    
    # Raise an error if the repository is not found
    if data.get("error"):
        raise HTTPException(status_code=404, detail=f"Repository {repo_name} not found")
    
    try:
        # Convert and validate data
        repo_data = {
            "repo_id": str(data.get("id")),  # Ensure id is a string
            "name": data.get("name") or "",  # Ensure name is a string
            "stars": int(data.get("stargazers_count", 0)),  # Ensure stars is an integer
            "owner": data.get("owner", {}).get("login", "unknown"),  # Assuming owner is a nested dict
            "description": data.get("description") or "",  # Ensure description is a string
            "forks": int(data.get("forks_count", 0)),  # Ensure forks is an integer
            "languages": [data.get("language")] if data.get("language") else [],  # Ensure languages is a list
            "topics": data.get("topics", []),  # Assuming topics is already a list
        }
        print ('repo_data:', repo_data)
        
        r = RepoModel(**repo_data)
    except ValidationError as e:
        # Handle validation errors, e.g., log them or return a detailed response
        raise HTTPException(status_code=422, detail=f"Data validation error: {e.errors()}") from e
    
    # Save repo to the database
    
    
    # insert the repository into the database
    inserted_id = db.insert_repo("repos", repo_data)
    
    if inserted_id:
        print(f"Inserted repository with ID: {inserted_id}")
    else:
        print("Failed to insert repository")
        # TODO: log the error - use logger
    
    return r


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run the FastAPI application using the following command:

# uvicorn app.main:app --reload

# To view the API documentation, navigate to /docs
