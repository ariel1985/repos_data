
# https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-public-repositories

import requests

class GitHubService:
	def __init__(self):
		self.base_url =  "https://api.github.com/repos"
	
	def fetch_repo_data(self, username, repo_name):
		url = f"{self.base_url}/{username}/{repo_name}"
		try:
			response = requests.get(url, timeout=10)
			response.raise_for_status()
			data = response.json()
			return {
				"ID": data["id"],
				"Name": data["name"],
				"Owner": data["owner"]["login"],
				"Stars": data["stargazers_count"],
				"Description": data["description"],
				"Forks": data["forks_count"],
				"Languages": data["language"],
				# Complete the dictionary based on your needs
			}
		except requests.RequestException as e:
			return {"error": str(e)}

if __name__ == "__main__":
    username = 'ariel1985' #"octocat"
    repo_name = 'poc' #"Hello-World"
    service = GitHubService()
    details = service.get_repository_details(username, repo_name)
    