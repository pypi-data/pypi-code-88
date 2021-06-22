import json
import logging
import os
import time

import requests
from PyInquirer import style_from_dict, Token, prompt
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")

logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

accept_header = "application/vnd.github.mercy-preview+json"

errors = []

s = requests.Session()
retries = Retry(total=5, backoff_factor=2, status_forcelist=[404, 422])
s.mount('https://', HTTPAdapter(max_retries=retries))


def prompt_questions(repo, proceed_with_prompt):
    if proceed_with_prompt:
        proceed = [
            {
                'type': 'list',
                'name': 'is_ok',
                'message': f"Check the  {repo} in target repo. Is it ok to proceed To next repo?",
                'choices': [
                    'yes',
                    'no',
                    "don't ask me again!"
                ]
            }
        ]

        proceed_answers_ok = prompt(questions=proceed, style=style)

        return proceed_answers_ok
    else:
        proceed_answers_ok = {}
        proceed_answers_ok["is_ok"] = "don't ask me again!"
        return proceed_answers_ok


def get_team(answers_github):
    try:
        target_team_name = answers_github.get("target_team_name")
        target_org = answers_github.get("target_github_org")
        team_url = f"https://api.github.com/orgs/{target_org}/teams/{target_team_name}"
        password = answers_github.get("github_password")
        team_resp = s.get(team_url,
                          headers={"Authorization": "token " + password,
                                   "Accept": accept_header})
        team_ids = []
        if team_resp.status_code == 200:
            team_id = json.loads(team_resp.content.decode()).get("id")
            team_ids.append(team_id)
            if "parent" in json.loads(team_resp.content.decode()) \
                    and json.loads(team_resp.content.decode())["parent"] is not None:
                parent_id = json.loads(team_resp.content.decode())["parent"]["id"]
                team_ids.append(parent_id)
        else:
            logging.error(f"Team not found response is {team_resp.content.decode()}")
            exit(1)

        return team_ids
    except Exception as ex:
        logging.error("Unable to fetch team id", exc_info=True)


def search_by_topic(topic, source_org, password, answers_github, user_found):
    results = []

    logging.info("Searching by topic...")

    topics = topic.split(",")
    list_of_topics = [f"topic:{single_topic}" for single_topic in topics]

    separator = "+"
    search_string = separator.join(list_of_topics)

    url = f"https://api.github.com/search/repositories?q=org:{source_org} {search_string}"

    team_ids = get_team(answers_github)

    headers = {"Authorization": "token " + password,
               "Accept": "application/vnd.github.mercy-preview+json"}

    repo_response = s.get(
        url,
        headers=headers)

    repos_contents = repo_response.content.decode("utf-8")

    if repo_response.status_code == 200:
        content = json.loads(repos_contents)
        count = json.loads(repos_contents).get("total_count")

        results.extend(content.get("items"))

        while "next" in repo_response.links:
            url = repo_response.links["next"]["url"]
            repo_response = s.get(url, headers=headers)
            data = repo_response.json()
            results.extend(data.get("items"))

        logging.info("\n Found " + str(len(results)) + " repos with topic " + topic + " in the org " + source_org)
        questions = [
            {
                'type': 'confirm',
                'name': 'listRepos',
                'message': 'List repos found?',
                'default': False
            }, ]
        answers = prompt(questions, style=style)

        if answers.get('listRepos'):
            for item in results:
                logging.info(item.get("full_name"))

                questions = [
                    {
                        'type': 'confirm',
                        'name': 'proceedToTransfer',
                        'message': 'If the list of repos are correct, can we proceed to transfer the repos? ',
                        'default': False
                    }, ]
            proceed_answers = prompt(questions, style=style)
        else:
            proceed_answers = {"proceedToTransfer": True}

        if proceed_answers.get("proceedToTransfer"):
            proceed_with_prompt = True
            for item in content.get("items"):
                try:
                    repo = item.get("name")
                    transfer_repo(item.get("name"), answers_github, user_found)
                    logging.info(f"Completed transfer for " + item.get("name"))
                    proceed_answers_ok = prompt_questions(repo, proceed_with_prompt)

                    if proceed_answers_ok.get("is_ok") == "yes":
                        continue
                    elif proceed_answers_ok.get("is_ok") == "no":
                        break
                    elif proceed_answers_ok.get("is_ok") == "don't ask me again!":
                        proceed_with_prompt = False

                except Exception as ex:
                    logging.info("Failed to transfer due to " + str(ex))

                    logging.exception(ex, exc_info=True)

                    proceed_answers_ok = prompt_questions(repo, proceed_with_prompt)

                    if proceed_answers_ok.get("is_ok") == "yes":
                        continue
                    elif proceed_answers_ok.get("is_ok") == "no":
                        break
                    elif proceed_answers_ok.get("is_ok") == "don't ask me again!":
                        proceed_with_prompt = False
        else:
            logging.info("Re-run the tool with correct search criteria!!")
            exit(1)
    else:
        logging.info("No Repos found! Try running the tool again with correct topic ")


def rename_repo(repo, org, answers, headers):
    try:
        time.sleep(1)
        team_prefix = answers.get("prefix")
        logging.info(f"Renaming {repo} to {team_prefix}.{repo} in {org}")
        url = f"https://api.github.com/repos/{org}/{repo}"

        data = {"name": team_prefix + "." + repo}
        headers["Accept"] = "application/vnd.github.v3+json"
        logging.info(url)
        rename_response = s.request("PATCH", url=url, data=json.dumps(data), headers=headers)

        if rename_response.status_code == 200:
            logging.info("Renamed successfully")
            return True

        else:
            logging.error(
                f"Renaming {repo} failed due to error {str(rename_response.status_code)} and response content is {rename_response.content.decode()}")
            errors.append(repo + "| Renaming failed")
            return False
    except Exception as ex:
        logging.error(f"Renaming {repo} failed due to error", exc_info=True)
        logging.info(ex)


def rename_master_to_main(repo, org, answers, headers):
    try:
        logging.info("Renaming master to main")
        team_prefix = answers.get("prefix")

        branch_url = f"https://api.github.com/repos/{org}/{repo}/branches/master/rename"
        data = {"new_name": "main"}

        rename_response = s.post(url=branch_url, headers=headers,
                                 data=json.dumps(data))
        if rename_response.status_code == 201:
            logging.info("Renamed master to main")
            return True
        else:
            logging.info(
                f"Renaming to master failed for repo {repo} due to {str(rename_response.status_code)} and response content is {rename_response.content.decode()}")
            errors.append(repo + "| Renaming master failed")
            return False
    except Exception as ex:
        logging.exception(f"Renaming to master failed for repo {repo}")
        logging.info(ex)


def make_repo_internal(repo, answers, headers):
    try:
        team_prefix = answers.get("prefix")
        target_org = answers.get("target_github_org")
        url = f"https://api.github.com/repos/{target_org}/{team_prefix}.{repo}"

        private_payload = json.dumps({
            "private": True,
            "visibility": "internal"
        })

        headers["Accept"] = "application/vnd.github.nebula-preview+json"

        response = s.request("PATCH", url, headers=headers, data=private_payload)

        if response.status_code == 200:
            logging.info(f"Made {repo} internal after transfer")
        else:
            logging.info(
                f"Unable to change privacy of repo {repo} to internal due to error {str(response.status_code)} and response is {response.content.decode()}")
    except Exception as ex:
        logging.exception(f"Unable to change privacy of repo {repo} to internal")
        logging.error(ex)


def update_webhooks(repo, org, answers, headers):
    # logging.info("Updating Web Hooks .... ")
    #
    # team_prefix = answers.get("prefix")
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    # headers["User-Agent"] = "python"
    # conn = http.client.HTTPSConnection("api.github.com", context=ctx)
    #
    # url = f"/repos/{org}/{team_prefix}.{repo}/hooks"
    #
    # payload = ''
    # conn.request("GET", url, payload, headers)
    #
    # hooks_response = conn.getresponse()
    # data = hooks_response.read()
    #
    # # logging.info(data.decode("utf-8"))
    #
    # if hooks_response.status == 200:
    #     response_json = json.loads(data.decode("utf-8"))
    #
    #     for config in response_json:
    #         hook_url = config.get("config").get("url")
    #         hook_id = config.get("id")
    #         if "bmx" in hook_url:
    #             new_hook_url = f"https://github-webhooks.baat-tools-prod.nikecloud.com/v1/{hook_url}"
    #             url = f"https://api.github.com/repos/{org}/{team_prefix}.{repo}/hooks/{hook_id}"
    #             data = {"config": {"url": new_hook_url}}
    #             response = s.patch(url, data=json.dumps(data),
    #                                headers=headers)
    #             if response.status_code == 200:
    #                 logging.info("Updated Web Hooks ")
    #
    #         else:
    #             logging.info(f"not a bmx repo wehbook {hook_url}")
    #     return True
    # else:
    #     logging.info("no webhooks found")
    return True


def transfer_repo_to_targetorg(repo, answers, headers):
    try:
        source_org = answers.get("source_github_org")
        target_org = answers.get("target_github_org")
        team_prefix = answers.get("prefix")
        team_ids = get_team(answers)

        logging.info(f"Transferring repo {repo} to {target_org}")
        url = f"https://api.github.com/repos/{source_org}/{repo}/transfer"

        data = {"new_owner": target_org, "team_ids": team_ids}
        time.sleep(0.2)
        response = s.post(url=url, headers=headers,
                          data=json.dumps(data))
        if response.status_code == 202:
            return True
        else:
            errors.append(repo + "| Failed to transfer")
            logging.info("Transfer failed due to error " + str(
                response.status_code) + f"response is {response.content.decode()}")
            logging.info(response.content.decode())
            return False
    except Exception as ex:
        logging.exception("Transfered failed with exception")
        logging.error(ex)


def make_team_admin_writers(repo, answers, headers):
    try:
        logging.info("changing team level access")
        team_slug = answers.get("target_team_name")
        team_admin_slug = answers.get("target_team_admin")
        team_prefix = answers.get("prefix")

        target_org = answers.get("target_github_org")

        team_url = f"https://api.github.com/orgs/{target_org}/teams/{team_slug}"

        team_resp = s.get(team_url,
                          headers=headers)
        parent_slug = team_prefix
        if team_resp.status_code == 200 and "parent" in json.loads(team_resp.content.decode()) and \
                json.loads(team_resp.content.decode())["parent"] is not None:
            parent_slug = json.loads(team_resp.content.decode())["parent"]["slug"]

        access_levels = {
            parent_slug: "push",
            team_slug: "maintain",
            team_admin_slug: "admin",
            f"{team_prefix}-external-contributors": "push"

        }

        for slug, access_level in access_levels.items():

            team_access_url = f"https://api.github.com/orgs/{target_org}/teams/{slug}/repos/{target_org}/{team_prefix}.{repo}"

            payload = json.dumps({
                "permission": access_level
            })

            response = s.put(team_access_url, headers=headers, data=payload)

            if response.status_code == 204:
                logging.info(f"Changed {slug} to be a {access_level}")
            else:
                logging.info(response.content.decode())
                logging.info(
                    f"Team access failed with error code " + str(response.status_code) + " url is " + team_access_url)
            time.sleep(0.5)
    except Exception as ex:
        logging.exception("Updating team access failed due to error")
        logging.info(ex)


def add_user_as_admin(repo, answers, headers, user):
    try:
        logging.info(f"Adding user {user} as adming to repo {repo}")
        source_org = answers.get("source_github_org")
        permissions_url = f"https://api.github.com/repos/{source_org}/{repo}/collaborators/{user}"

        response = s.put(url=permissions_url, headers=headers, data=json.dumps({"permission": "admin"}))

        if response.status_code == 201 or response.status_code == 204:
            logging.info(f"User {user} added as admin to the repo {repo}")
        else:
            logging.info(f"unable to add {user} as admin to the repo {repo} due to error {response.content.decode()}")
    except Exception as ex:
        logging.exception(f"unable to add {user} as admin to the repo {repo} due to error ")
        logging.error(ex)


def remove_user_as_admin(repo, answers, headers, user):
    try:
        logging.info(f"Removing user {user} as adming to repo {repo}")
        source_org = answers.get("source_github_org")
        permissions_url = f"https://api.github.com/repos/{source_org}/{repo}/collaborators/{user}"

        response = s.delete(url=permissions_url, headers=headers)

        if response.status_code == 201 or response.status_code == 204:
            logging.info(f"User {user} removed as admin to the repo {repo}")
        else:
            logging.info(
                f"unable to remove {user} as admin to the repo {repo} due to error {response.content.decode()}")
    except Exception as ex:
        logging.exception(f"unable to remove {user} as admin to the repo {repo} due to error {type(ex)} ")
        logging.error(ex)


def add_branch_protection_main(repo, answers, headers):
    try:

        target_org = answers.get("target_github_org")
        team_slug = answers.get("target_team_name")
        team_prefix = answers.get("prefix")

        url = f"https://api.github.com/repos/{target_org}/{team_prefix}.{repo}/branches/main/protection"

        payload = json.dumps({
            "required_status_checks": {
                "strict": True,
                "contexts": [
                    "continuous-integration/jenkins/pr-merge",
                    "continuous-integration/jenkins/branch"
                ]
            },
            "enforce_admins": False,
            "required_pull_request_reviews": {
                "dismissal_restrictions": {
                    "teams": [
                        team_slug
                    ]
                },
                "dismiss_stale_reviews": True,
                "require_code_owner_reviews": True,
                "required_approving_review_count": 2
            },
            "restrictions": None
        })
        headers['Accept'] = 'application/vnd.github.luke-cage-preview+json'

        response = s.put(url, headers=headers, data=payload)

        if response.status_code == 200:
            logging.info("Updated branch protection rules")
        else:
            logging.info(f"Failed to Update branch protection rules due to error {response.content.decode()}")

    except Exception as ex:
        logging.exception("Updating Branch protection rules Failed ")


def transfer_repo(repo, answers, user_found):
    try:
        logging.info("\nTransferring " + repo + " to target organization")
        source_org = answers.get("source_github_org")
        target_org = answers.get("target_github_org")

        headers = {"Authorization": "token " + answers.get('github_password'),
                   "Accept": "application/vnd.github.mercy-preview+json"}

        # add as admin

        add_user_as_admin(repo, answers, headers, user_found)

        # Rename Repo
        is_rename_success = True

        if is_rename_success:
            is_branch_rename_success = rename_master_to_main(repo, source_org, answers, headers)
            if is_branch_rename_success:
                is_update_webhook_success = update_webhooks(repo, source_org, answers, headers)
                if is_update_webhook_success:
                    is_rename_success = rename_repo(repo, source_org, answers, headers)
                    if is_rename_success:
                        is_transfer_success = transfer_repo_to_targetorg(repo, answers, headers)
                        if is_transfer_success:
                            logging.info(f"Transfer completed for repo {repo}")

                            # add branch protection rules
                            add_branch_protection_main(repo, answers, headers)
                            make_team_admin_writers(repo, answers, headers)
                            make_repo_internal(repo, answers, headers)
                            remove_user_as_admin(repo, answers, headers, user_found)
                        else:
                            logging.info(f"Transfer failed for repo {repo}")
                    else:
                        logging.info(f"Renaming failed for repo {repo}")
                else:
                    logging.info(f"updating webhooks failed for repo {repo}")
            else:
                logging.info(f"Renaming master failed for repo {repo}")
        else:
            logging.info(f"Renaming failed for {repo} proceeding to other")
    except Exception as ex:
        logging.exception(ex)


def migrate_github(answers, topic_answers):
    headers = {"Authorization": "token " + answers.get('github_password'),
               "Accept": "application/vnd.github.mercy-preview+json"}

    get_user_url = "https://api.github.com/user"

    get_user_response = s.get(url=get_user_url, headers=headers)

    user_found = get_user_response.json().get("login")

    logging.info(f"Logged in as user {user_found}")

    if "topic_name" in topic_answers:
        topic = topic_answers.get("topic_name")
        logging.info("searching for repos with topic name " + topic)
        search_by_topic(
            topic, answers.get('source_github_org'), answers.get('github_password'),
            answers, user_found
        )
    else:
        filepath = topic_answers.get("filepath")
        proceed_with_prompt = True
        logging.info("Reading repos from " + filepath)
        team_ids = get_team(answers)
        with open(filepath, 'r') as inputFile:
            for line in inputFile.readlines():
                repo_name = line.replace("\n", "")
                transfer_repo(repo_name, answers, user_found)

                if proceed_with_prompt:
                    proceed = [
                        {
                            'type': 'list',
                            'name': 'is_ok',
                            'message': f"Check the  {repo_name} in target repo. Is it ok to proceed To next repo?",
                            'choices': [
                                'yes',
                                'no',
                                "don't ask me again!"
                            ]
                        }
                    ]

                    proceed_answers_ok = prompt(questions=proceed, style=style)

                    if proceed_answers_ok.get("is_ok") == "yes":
                        continue
                    elif proceed_answers_ok.get("is_ok") == "no":
                        break
                    elif proceed_answers_ok.get("is_ok") == "don't ask me again!":
                        proceed_with_prompt = False
