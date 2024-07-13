import os
import logging
from typing import Dict, Any, Optional
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
from .models import RepoModel

# Load environment variables from .env file
load_dotenv()

# Get the mongo url and name from the .env file
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")


class DBService:
    def __init__(self, mongo_uri: str = MONGO_URI, db_name: str = DB_NAME):
        # Dependency Injection for MongoDB URI and Database Name
        self.client = MongoClient(mongo_uri)
        
        # if db_name exists in mongodb, use it
        if db_name in self.client.list_database_names():
            self.db = self.client[db_name]
            print(f"Database {db_name} found.")
        # otherwise, create a new db with the name db_name
        else:
            self.db = self.client[db_name]
            print(f"Database {db_name} not found. Creating a new one.")            
        
        self.logger = logging.getLogger(__name__)

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def insert_repo(self, collection_name: str, repo_data: Dict[str, Any]) -> Optional[str]:
        try:
            # Data Validation against Repository schema
            validated_data = RepoModel(**repo_data)
            
            # if repo data exists, update it instead of inserting
            if self.get_repo(collection_name, {"name": repo_data["name"]}):
                return self.update_repo(collection_name, {"name": repo_data["name"]}, repo_data)
            
            # TODO: add a created_at timestamp to the repo data
            insert_result = self.get_collection(collection_name).insert_one(validated_data.model_dump())
            
            return insert_result.inserted_id
        
        except PyMongoError as e:
            self.logger.error("Error inserting repository data: %s", e)
            return None
        except ValueError as e:
            self.logger.error("Validation error for repository data: %s", e)
            return None

    def get_all_repos(self, collection_name: str):
        try:
            return list(self.get_collection(collection_name).find())
        except PyMongoError as e:
            self.logger.error("Error fetching all repositories: %s", e)
            return []

    def get_repo(self, collection_name: str, query: Dict[str, Any]):
        try:
            return self.get_collection(collection_name).find_one(query)
        except PyMongoError as e:
            self.logger.error("Error fetching repository: %s", e)
            return None
    
    def update_repo(self, collection_name: str, query: Dict[str, Any], update_data: Dict[str, Any]):
        try:
            return self.get_collection(collection_name).update_one(query, {"$set": update_data})
        except PyMongoError as e:
            self.logger.error("Error updating repository: %s", e)
            return None

    def delete_repo(self, collection_name: str, query: Dict[str, Any]):
        try:
            return self.get_collection(collection_name).delete_one(query)
        except PyMongoError as e:
            self.logger.error("Error deleting repository: %s", e)
            return None

if __name__ == "__main__":
    
    repo_name = "d-repo-name"
    print("checking out the mongo uri", MONGO_URI)
    print("checking out the db name", DB_NAME)
    print("checking out the repo name", repo_name)
    
    # Example usage of the DBService class
    service = DBService()
    
    print("Insert a new repository detail")
    repo_data = {
        "repo_id": "123",
        "name": repo_name,
        "stars": 100,
        "owner": "example-owner",
        "description": "example-description",
        "forks": 10,
        "languages": ["Python", "JavaScript"],
        "topics": ["example-topic1", "example-topic2"],
    }
    inserted_id = service.insert_repo("repos", repo_data)
    print(f"Inserted repository with ID: {inserted_id}")
    
    print("Get all repository details:")
    all_repos = service.get_all_repos("repos")
    print("All repositories:")
    for repo in all_repos:
        print(repo)
    
    print("Get a specific repository detail:")
    drepo = service.get_repo("repos", {"name": repo_name})
    print("Repository by name:", repo_name)
    print(drepo)
    
    print("Delete a repository detail:")
    result = service.delete_repo("repos", {"name": repo_name})
    print(f"Deleted {result.deleted_count} repository")
    