import requests
import json
import sys


def make_private(repo_name, answers):
    source_org = answers.get("source_org")
    token = answers.get("github_token")
    url = f"https://api.github.com/repos/{source_org}/{repo_name}"

    private_payload = json.dumps({
        "private": True,
        "visibility": "private"
    })
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.nebula-preview+json',
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=private_payload)

    if response.status_code == 200:
        print(f"Made {repo_name} private for transfer")


def make_private_flow(answers: dict):

    source_org = answers.get("source_org")
    token = answers.get("github_token")

    url = f"https://api.github.com/orgs/{source_org}/repos?per_page=100&page=1"
    results = []
    payload = {}
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.nebula-preview+json',
        'Cookie': 'logged_in=no'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    results.extend(response.json())

    while "next" in response.links:
        url = response.links["next"]["url"]

        response = requests.get(url, headers=headers)
        data = response.json()
        results.extend(data)


    for repo in results:
        if repo.get("visibility") == "internal":
            repo_name = repo.get("name")
            print(f"{repo_name} is internal, making it private")
            make_private(repo_name=repo.get("name"), answers=answers)
        else:
            repo_name = repo.get("name")
            print(f"{repo_name} is already private")
