import os
import logging
from typing import Dict, Any, Optional
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
from app.schemas.repo import Repository

# Load environment variables from .env file
load_dotenv()

# Get the mongo url and name from the .env file
MONGO_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("MONGODB_DB_NAME")

print("checking out the mongo uri", MONGO_URI)
print("checking out the db name", DB_NAME)

class DBService:
    def __init__(self, mongo_uri: str = MONGO_URI, db_name: str = DB_NAME):
        # Dependency Injection for MongoDB URI and Database Name
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.logger = logging.getLogger(__name__)

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def insert_repo(self, collection_name: str, repo_data: Dict[str, Any]) -> Optional[str]:
        try:
            # Data Validation against Repository schema
            validated_data = Repository(**repo_data)
            insert_result = self.get_collection(collection_name).insert_one(validated_data.dict())
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
            validated_data = Repository(**update_data)
            result = self.get_collection(collection_name).update_one(query, {'$set': validated_data.dict()})
            return result
        except PyMongoError as e:
            self.logger.error("Error updating repository: %s", e)
            return None
        except ValueError as e:
            self.logger.error("Validation error for update data: %s", e)
            return None

    def delete_repo(self, collection_name: str, query: Dict[str, Any]):
        try:
            return self.get_collection(collection_name).delete_one(query)
        except PyMongoError as e:
            self.logger.error("Error deleting repository: %s", e)
            return None

if __name__ == "__main__":
    # Example usage of the DBService class
    service = DBService()
    
    # Insert a new repository detail
    repo_data = {
        "ID": 123,
        "Name": "example-repo",
        "Owner": "example-user",
        "Stars": 100,
        "Description": "An example repository",
        "Forks": 50,
        "Languages": "Python",
    }
    inserted_id = service.insert_repo("repos", repo_data)
    print(f"Inserted repository with ID: {inserted_id}")
    
    # Get all repository details
    all_repos = service.get_all_repos("repos")
    print("All repositories:")
    for repo in all_repos:
        print(repo)
    
    # Get a specific repository detail
    repo = service.get_repo("repos", {"Name": "example-repo"})
    print("Repository by name:")
    print(repo)
    
    # Update a repository detail
    update_data = {"Stars": 200}
    result = service.update_repo("repos", {"Name": "example-repo"}, update_data)
    print(f"Updated {result.modified_count} repository")
    
    # Delete a repository detail
    result = service.delete_repo("repos", {"Name": "example-repo"})
    print(f"Deleted {result.deleted_count} repository")
    