from __future__ import print_function, unicode_literals

import sys
import traceback
import github_migration
import jenkins_migration
import make_private
import update_topics_for_team
import find_new_git_url

from PyInquirer import style_from_dict, Token, prompt


def _main():
    try:
        style = style_from_dict({
            Token.QuestionMark: '#E91E63 bold',
            Token.Selected: '#673AB7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#2196f3 bold',
            Token.Question: '',
        })

        print('Github Migration')
        chose_flow = [
            {
                'type': 'list',
                'name': 'selectFlow',
                'message': 'What do you want to do?',
                'choices': [
                    'Github Migration',
                    'Jenkins BMX Migration',
                    'Make repos private',
                    'Update topics',
                    'Find new git URL for CI/CD changes (SNOW)'
                ]
            }
        ]

        chose_flow_answers = prompt(chose_flow, style=style)

        if chose_flow_answers.get("selectFlow") == "Github Migration":

            questions = [
                {
                    'type': 'input',
                    'name': 'source_github_org',
                    'message': 'Source github org',
                    'default': 'nike-platform-fulfillment'
                },
                {
                    'type': 'input',
                    'name': 'target_github_org',
                    'message': 'Target github org',
                    'default': 'nike-internal'
                },
                {
                    'type': 'input',
                    'name': 'target_team_name',
                    'message': 'Target Team Slug',
                    'default': 'fulfillment-squad-artemis'
                },
                {
                    'type': 'input',
                    'name': 'target_team_admin',
                    'message': 'Target Team Admin Slug',
                    'default': 'fulfillment-admins'
                },
                {
                    'type': 'input',
                    'name': 'prefix',
                    'message': 'Team Prefix',
                    'default': 'fulfillment'
                },
                {
                    'type': 'password',
                    'name': 'github_password',
                    'message': 'Github access token',

                }
            ]
            answers = prompt(questions, style=style)

            chose_search = [
                {
                    'type': 'list',
                    'name': 'search_criteria',
                    'message': 'How do you want to get the repos?',
                    'choices': [
                        'Search by Topic',
                        'Provide list of Repos'
                    ]
                }
            ]

            chose_search_answers = prompt(chose_search, style=style)

            if chose_search_answers.get("search_criteria") == "Search by Topic":

                questions = [
                    {
                        'type': 'input',
                        'name': 'topic_name',
                        'message': 'Topic Name. Enter multiple separated by comma',
                        'default': 'artemis'
                    },
                ]
                topic_answers = prompt(questions, style=style)
            else:
                questions = [
                    {
                        'type': 'input',
                        'name': 'filepath',
                        'message': 'Provide the file with the repo names to be migrated',
                        'default': '/Users/vmari2/repos.txt'
                    },
                ]
                topic_answers = prompt(questions, style=style)

            github_migration.migrate_github(
                answers, topic_answers
            )
        elif chose_flow_answers.get("selectFlow") == "Make repos private":
            make_private_questions = [{
                'type': 'input',
                'name': 'source_org',
                'message': 'Organization Name',
                'default': "nike-platform-logistics"
            },
                {
                    'type': 'password',
                    'name': 'github_token',
                    'message': 'github personal access token'
                }]
            make_private_answers = prompt(questions=make_private_questions, style=style)
            make_private.make_private_flow(make_private_answers)

        elif chose_flow_answers.get("selectFlow") == "Update topics":

            update_topics_questions = [{
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
                    'name': 'permission_level',
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
                }]
            update_topics_answers = prompt(update_topics_questions, style=style)
            update_topics_for_team.update_topics(update_topics_answers)
        elif chose_flow_answers.get("selectFlow") == "Find new git URL for CI/CD changes (SNOW)":
            change_url_questions = [
                {
                    'type': 'input',
                    'name': 'source_org',
                    'message': 'Source github organization',
                    'default': "nike-platform-fulfillment"
                },
                {
                    'type': 'input',
                    'name': 'path_to_data',
                    'message': 'File path for the list of Old URLs',
                    'default': "/Users/XXXX/test.txt"
                },
                {
                    'type': 'password',
                    'name': 'github_token',
                    'message': 'Github Token'
                },
            ]

            find_new_git_url_answers = prompt(change_url_questions, style=style)
            find_new_git_url.find_urls(find_new_git_url_answers)

        else:

            questions = [

                {
                    'type': 'input',
                    'name': "jenkins_url",
                    'message': "Provide the jenkins url"
                },
                {
                    'type': 'input',
                    'name': "path_to_data",
                    'message': "Provide the file with the list of jobs. Leave blank if you want to reconfigure all jobs in the jenkins instance"
                },
                {
                    'type': 'password',
                    'name': 'jenkins_token',
                    'message': 'Jenkins Token'
                },
                {
                    'type': 'input',
                    'name': 'jenkins_username',
                    'message': 'Jenkins Username',
                    'default': 'change_it@nike.com'
                },
                {
                    'type': 'input',
                    'name': 'new_org',
                    'message': 'New Github Org',
                    'default': 'nike-internal'
                },
                {
                    'type': 'input',
                    'name': 'old_org',
                    'message': 'Old Github Org(s). Provide comma separated values ',
                    'default': 'mp-commerce-fulfillment'
                },
                {
                    'type': 'input',
                    'name': 'team_prefix',
                    'message': 'Team Prefix',
                    'default': 'fulfillment'
                },
                {
                    'type': 'input',
                    'name': 'new_credentials_id',
                    'message': 'Provide the new credentials to Change credentials id. Leave blank if not changing ',
                    'default': ''
                }
            ]
            jenkins_answers = prompt(questions, style=style)
            jenkins_migration.get_jobs(jenkins_answers)

    except Exception as ex:
        traceback.print_exc()
        print(ex)


def main():
    return _main()


if __name__ == "__main__":
    sys.exit(_main())
