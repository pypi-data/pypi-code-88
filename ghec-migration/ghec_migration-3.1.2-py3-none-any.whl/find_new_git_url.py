import sys

import requests


def find_urls(answers):
    source_org = answers.get("source_org")
    path_to_data = answers.get("path_to_data")
    token = answers.get("github_token")

    with open("new_references.csv", "w") as writeFile:
        writeFile.write("Old URL, New URL\n")
        with open(path_to_data, "r") as listOfFiles:
            for repo in listOfFiles:
                repo = repo.replace("\n", "")
                repo_name = repo.replace(".git", "").replace(f"https://github.com/{source_org}/", "").replace("\n", "")
                print(f"Getting new url for {repo_name}")
                url = f"https://api.github.com/repos/{source_org}/{repo_name}"

                headers = {
                    'Authorization': f'token {token}',
                    'Accept': 'application/vnd.github.nebula-preview+json',

                }
                response = requests.request("GET", url, headers=headers)
                html_url = response.json().get("html_url")

                writeFile.write(f"{repo},{html_url}.git\n")

        print("Completed process. The new git Urls can be found at new_references.csv")
