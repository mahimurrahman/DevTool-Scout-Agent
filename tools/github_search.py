import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def search_repositories(query):

    url = "https://api.github.com/search/repositories"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    params = {
    "q": query,
}

    response = requests.get(url, headers=headers, params=params)

    repos = response.json()["items"][:5]

    results = []

    for repo in repos:
        results.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "description": repo["description"]
        })

    return results