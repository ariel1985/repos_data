from pymongo import MongoClient

class DBService:
	def __init__(self):
		# Connect to the MongoDB server, assuming it's running on the default port 27017
		self.client = MongoClient('mongodb://localhost:27017/')
		# Select the 'repos' database
		self.db = self.client['repos']
	
	def get_collection(self, collection_name):
		# Return a collection object to perform operations on
		return self.db[collection_name]
	
	def insert_repo(self, collection_name, repo_data):
		# Insert a new repository detail into the specified collection
		return self.get_collection(collection_name).insert_one(repo_data).inserted_id
	
	def get_all_repos(self, collection_name):
		# Return all repository details from the specified collection
		return list(self.get_collection(collection_name).find())
	
	def get_repo(self, collection_name, query):
		# Return a single repository detail matching the query
		return self.get_collection(collection_name).find_one(query)
	
	def update_repo(self, collection_name, query, update_data):
		# Update a repository detail matching the query
		return self.get_collection(collection_name).update_one(query, {'$set': update_data})
	
	def delete_repo(self, collection_name, query):
		# Delete a repository detail matching the query
		return self.get_collection(collection_name).delete_one(query)

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
    
    