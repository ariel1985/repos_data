import requests

def get_repository_details(username, repo_name):
    """
    Fetches details for a specific GitHub repository.
    
    :param username: GitHub username or organization name
    :param repo_name: Repository name
    :return: Dictionary with repository details or error message
    """
    base_url = "https://api.github.com/repos"
    url = f"{base_url}/{username}/{repo_name}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        data = response.json()
        
        # Extracting some details for demonstration
        repo_details = {
            "ID": data["id"],
            "Name": data["name"],
            "Owner": data["owner"]["login"],
            "Stars": data["stargazers_count"],
            "Description": data["description"],
            "Forks": data["forks_count"],
            "Languages": data["language"],
            "Topics": data["topics"]
        }
        
        return repo_details
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    username = 'ariel1985' #"octocat"
    repo_name = 'poc' #"Hello-World"
    details = get_repository_details(username, repo_name)
    print(details)