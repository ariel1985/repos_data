import requests

class GitHubService:
	
	def __init__(self):
		# TODO: get these from settings or env file
		self.username = 'ariel1985' #"octocat" - 
		self.base_url =  "https://api.github.com/repos"
		

	def fetch_repo_data(self, repo_name):
		url = f"{self.base_url}/{self.username}/{repo_name}"
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
			}
		except requests.RequestException as e:
			return {"error": str(e)}

	def fetch_all_repos(self):
		url = f"https://api.github.com/users/{self.username}/repos"
		try:
			response = requests.get(url, timeout=10)
			response.raise_for_status()
			data = response.json()
			# TODO: return only the name of repos
			return data
		except requests.RequestException as e:
			return {"error": str(e)}

if __name__ == "__main__":
	repo_name = 'poc' #"Hello-World"
	service = GitHubService()
	# details = service.get_repository_details(repo_name)
	repos = service.fetch_all_repos()
	if len(repos) == 0:
		print('No repositories found')
		exit()
	print('Total amount of public repositories:', len(repos) )
	print('name', repos[0]['name'])
	print('full name', repos[0]['full_name'])
	# print(details)
