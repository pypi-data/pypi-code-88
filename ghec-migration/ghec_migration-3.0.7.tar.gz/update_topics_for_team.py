import requests
import sys

import json

"""[{
                'type': 'input',
                'name': 'source_org',
                'message': 'Organization Name',
                'default': "nike-platform-logistics"
            },
                {
                    'type': 'input',
                    'name': 'team_slug',
                    'message': 'Team Slug',
                    'default': "logistics-squad-airmax"
                },
                {
                    'type': 'list',
                    'name': 'team_slug',
                    'message': 'Select the permission level',
                    'choices': [
                        'push',
                        'pull',
                        'admin',
                        'maintain'
                    ]
                },
                {
                    'type': 'input',
                    'name': 'additional_topics',
                    'message': 'Additional topics, comma separated',
                    'default': "logistics,airmax"
                },
                {
                    'type': 'password',
                    'name': 'github_token',
                    'message': 'github personal access token'
                }]"""


def update_topics(answers: dict):
    source_org = answers.get("source_org")
    team_slug = answers.get("team_slug")
    permission_level = answers.get("permission_level")
    token = answers.get("github_token")
    topics_csv_string = answers.get("additional_topics")

    if permission_level not in ["push", "pull", "maintain", "admin", "triage"]:
        print("Permission level provided is invalid. "
              "It should be one of [\"push\", \"pull\", \"maintain\", \"admin\", \"triage\"]")
        exit(1)

    url = f"https://api.github.com/orgs/{source_org}/teams/{team_slug}/repos?page=1&per_page=100"
    results = []
    payload = {}
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }

    repo_response = requests.request("GET", url, headers=headers, data=payload)
    repos_contents = repo_response.content.decode("utf-8")

    if repo_response.status_code == 200:
        content = json.loads(repos_contents)
        results.extend(content)

        while "next" in repo_response.links:
            url = repo_response.links["next"]["url"]
            repo_response = requests.get(url, headers=headers)
            data = repo_response.json()
            results.extend(data)

    print("Total of " + str(len(results)) + " found")
    repo_results = []
    print("Filtering the repos...")
    for repo in results:
        rep_name = repo.get("name")
        get_team_level_url = f"https://api.github.com/orgs/{source_org}/teams/{team_slug}/repos/{source_org}/{rep_name}"
        headers["Accept"] = "application/vnd.github.v3.repository+json"
        team_response = requests.request("GET", get_team_level_url, headers=headers, data=payload)
        if team_response.status_code == 200:
            if team_response.json().get("permissions").get(permission_level):
                repo_results.append(rep_name)
        else:
            print(team_response.status_code)

    print(f"Found {str(len(repo_results))} repos where {team_slug} has {permission_level} access")
    for repo in repo_results:

        topic_url = f"https://api.github.com/repos/{source_org}/{repo}/topics"
        headers["Accept"] = "application/vnd.github.mercy-preview+json"
        topics = [team_slug]
        topics.extend(topics_csv_string.split(","))
        payload = {"names": topics}
        topics_response = requests.request("PUT", topic_url, headers=headers, data=json.dumps(payload))
        if topics_response.status_code == 200:
            print(f"topics updated for {repo}")
        else:
            print(topics_response.content.decode())
