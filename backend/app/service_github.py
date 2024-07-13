import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_URL = os.getenv("GITHUB_API_URL")

print('GITHUB_USERNAME:', GITHUB_USERNAME)
print('GITHUB_URL:', GITHUB_URL)

class GitHubService:
	
	def __init__(self):
		self.username = GITHUB_USERNAME
		self.base_url =  GITHUB_URL

	def fetch_repo_data(self, repo_name: str) -> dict:
		url = f"{self.base_url}/{self.username}/{repo_name}"
		print('00000000000000000000000000000url:', url)
		try:
			response = requests.get(url, timeout=10)
			response.raise_for_status()
			return response.json()
   
			# Note: to make it compatible with SOLID principles - move the logic to the main.py
			# return {
			# 	"ID": data["id"],
			# 	"Name": data["name"],
			# 	"Owner": data["owner"]["login"],
			# 	"Stars": data["stargazers_count"],
			# 	"Description": data["description"],
			# 	"Forks": data["forks_count"],
			# 	"Languages": data["language"],
			# }
		except requests.RequestException as e:
			return {"error": str(e)}

if __name__ == "__main__":
	repo_name = 'poc' #"Hello-World"
	service = GitHubService()
	repo = service.fetch_repo_data(repo_name)
	print('repo:', repo)