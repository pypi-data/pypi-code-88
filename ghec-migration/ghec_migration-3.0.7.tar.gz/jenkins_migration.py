import requests
from requests.auth import HTTPBasicAuth

import jenkins
import json
from PyInquirer import style_from_dict, Token, prompt
import re
import os
import logging
import xmltodict

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")

logging.basicConfig(
    level=LOGLEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("jenkins.log"),
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


def get_jobs(jenkins_answers):
    jenkins_url = jenkins_answers.get("jenkins_url")
    username = jenkins_answers.get("jenkins_username")
    token = jenkins_answers.get("jenkins_token")
    server = jenkins.Jenkins(jenkins_url, username=username, password=token)

    if "jenkins_url" in jenkins_answers and not jenkins_answers.get("path_to_data"):
        jobs = server.get_jobs(folder_depth=5)
        is_prompt_user = True

        for job in jobs:
            job_name = job.get("name")
            if job.get("_class") in ("org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject",
                                     "org.jenkinsci.plugins.workflow.job.WorkflowJob"):
                config = server.get_job_config(job.get("name"))
                replace_config(job_name, config, server, jenkins_answers)

            if is_prompt_user:
                is_okay_to_proceed = [
                    {
                        'type': 'list',
                        'name': 'is_ok',
                        'message': f"Check the job {job_name} in jenkins. Is it ok to proceed?",
                        'choices': [
                            'yes',
                            'no',
                            "don't ask me again!"
                        ]
                    }
                ]
                answers = prompt(is_okay_to_proceed, style=style)
                if answers.get("is_ok") == "no":
                    break
                else:
                    if answers.get("is_ok") == "don't ask me again!":
                        is_prompt_user = False

    elif "path_to_data" in jenkins_answers and jenkins_answers.get("path_to_data"):
        is_prompt_user = True
        with open(jenkins_answers.get("path_to_data"), "r") as jenkinsFile:
            for line in jenkinsFile.readlines():
                logging.info(f"Reconfiguring {line}")
                line = line.replace("\n", "")
                if line.endswith("/"):
                    append_api = "api/json?pretty=true"
                    json_api = f"{line}{append_api}"
                else:
                    append_api = "api/json?pretty=true"
                    json_api = f"{line}/{append_api}"

                response = requests.request("GET", json_api, auth=HTTPBasicAuth(username, token))

                if response.status_code == 200:
                    job_name = json.loads(response.content.decode())["fullName"]

                    config = server.get_job_config(job_name)

                    if "BitbucketSCMSource" in config:
                        reconfig_bitbucket(jenkins_answers, job_name, config, server)
                    else:
                        replace_config(job_name, config, server, jenkins_answers)

                    if is_prompt_user:
                        is_okay_to_proceed = [
                            {
                                'type': 'list',
                                'name': 'is_ok',
                                'message': f"Check the job {job_name} in jenkins. Is it ok to proceed?",
                                'choices': [
                                    'yes',
                                    'no',
                                    "don't ask me again!"
                                ]
                            }
                        ]
                    answers = prompt(is_okay_to_proceed, style=style)
                    if answers.get("is_ok") == "no":
                        break
                    else:
                        if answers.get("is_ok") == "don't ask me again!":
                            is_prompt_user = False


def replace_config(job_name, config, server, jenkins_answers):
    credentials_id = jenkins_answers.get("new_credentials_id")

    team_prefix = jenkins_answers.get("team_prefix")
    old_org = jenkins_answers.get("old_org")
    new_org = jenkins_answers.get("new_org")

    if "BitbucketSCMSource" in config:
        logging.info(" Got a bitbucket job to reconfig")
        reconfig_bitbucket(jenkins_answers=jenkins_answers, job_name=job_name, config=config, server=server)
    else:
        api_uri = "<apiUri>https://github.nike.com/api/v3<apiUri>"
        config = config.replace(old_org + "/", f"{new_org}/{team_prefix}.").replace(api_uri,
                                                                                    "<apiUri>https://api.github.com<apiUri>")

        config = config.replace("github.nike.com", "github.com")
        for org in old_org.split(","):
            config = config.replace(org, new_org)
            config = config.replace(org + "/", f"{new_org}/{team_prefix}.")
        if credentials_id.strip() != "":
            config = re.sub("<credentialsId>.*</credentialsId>", f"<credentialsId>{credentials_id}</credentialsId>",
                            config)

        server.reconfig_job(job_name, config_xml=config)
        logging.info(f"completed configuring {job_name}")


def reconfig_bitbucket(jenkins_answers, job_name, config, server):
    credentials_id = jenkins_answers.get("new_credentials_id")
    team_prefix = jenkins_answers.get("team_prefix")

    config = server.get_job_config(job_name)

    config_dict = xmltodict.parse(config)
    if "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject" in config_dict:
        repo_name = config_dict["org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject"]["sources"]["data"][
            "jenkins.branch.BranchSource"]["source"]["repository"]
        id_class = config_dict["org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject"]["sources"]["data"][
            "jenkins.branch.BranchSource"]["source"]["id"]
    elif "org.jenkinsci.plugins.workflow.job.WorkflowJob" in config_dict:
        repo_name = config_dict["org.jenkinsci.plugins.workflow.job.WorkflowJob"]["sources"]["data"][
            "jenkins.branch.BranchSource"]["source"]["repository"]
        id_class = config_dict["org.jenkinsci.plugins.workflow.job.WorkflowJob"]["sources"]["data"][
            "jenkins.branch.BranchSource"]["source"]["id"]

    source = {
        "@plugin": "github-branch-source@2.8.2",
        "@class": "org.jenkinsci.plugins.github_branch_source.GitHubSCMSource",
        "id": id_class,
        "apiUri": "https://github.nike.com/api/v3",
        "credentialsId": f"{credentials_id}",
        "repoOwner": "nike-internal",
        "repository": f"{repo_name}",
        "repositoryUrl": f"https://github.com/nike-internal/{team_prefix}.{repo_name}.git",
        "traits": {
            "org.jenkinsci.plugins.github__branch__source.BranchDiscoveryTrait": {
                "strategyId": "1"
            },
            "org.jenkinsci.plugins.github__branch__source.OriginPullRequestDiscoveryTrait": {
                "strategyId": "1"
            },
            "org.jenkinsci.plugins.github__branch__source.ForkPullRequestDiscoveryTrait": {
                "strategyId": "1",
                "trust": {
                    "@class": "com.cloudbees.jenkins.plugins.bitbucket.ForkPullRequestDiscoveryTrait$TrustTeamForks"
                }
            }
        }
    }

    config_dict["org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject"]["sources"]["data"][
        "jenkins.branch.BranchSource"]["source"] = source

    reconfig_xml = (xmltodict.unparse(config_dict, pretty=True))
    reconfig_xml.replace(">master<", ">main<")
    resp = server.reconfig_job(job_name, reconfig_xml)
