from aheadworks_core.api.jira_api_manager import JiraApiManager
from aheadworks_core.api.discord_api_manager import DiscordApiManager
from datetime import datetime
import os

class ReleaseManager:
    """api manager for release"""

    RELEASE_PACK_TASK_LABEL = 'RELEASE-PACK'
    PD_TASK_LABEL = 'PD'
    TEST_TASK_LABEL = 'TEST'

    def __init__(self, jira_api_config):
        self.jira_api_config = jira_api_config
        self.jira_api_manager = JiraApiManager(config=self.jira_api_config)
        self.discord_api_manager = DiscordApiManager()

    def send_pack_to_manual_release(self, jira_project_key, module_version, discord_bot_url, path_to_files, assign_to):
        jira_instance = self.jira_api_manager.get_jira_instance()

        files_to_upload = []
        file_names = os.listdir(path_to_files)
        for file_name in file_names:
            files_to_upload.append(('file', (file_name, open(path_to_files + '/' + file_name, 'rb'))))

        jql = 'labels%3D{}-{}'.format(jira_project_key, module_version)
        links = self.get_release_tasks(jql)
        msg = '\n'.join(list(map(lambda x: x['url'], links.values())))

        release_task_key = links[self.RELEASE_PACK_TASK_LABEL]['key']
        pd_task_key = links[self.PD_TASK_LABEL]['key']
        test_task_key = links[self.TEST_TASK_LABEL]['key']

        # add attachments
        self.add_attachments_to_task(release_task_key, files_to_upload)

        # assign release pack to user
        release_issue = jira_instance.issue(release_task_key)
        release_issue.update(assignee={'accountId': assign_to})

        # uncomment if needed check transitions for issue
        # transitions = jira_instance.transitions(release_issue)
        # set done to pd and test issue. transition=31 - Task Done
        pd_issue = jira_instance.issue(pd_task_key)
        jira_instance.transition_issue(pd_issue, transition=31)

        test_issue = jira_instance.issue(test_task_key)
        jira_instance.transition_issue(test_issue, transition=31)

        # release current version
        version = jira_instance.get_project_version_by_name(jira_project_key, module_version)
        release_date = datetime.today().strftime('%Y-%m-%d')
        version.update(released=True, releaseDate=release_date)

        self.discord_api_manager.send_msg(discord_bot_url, msg)

    def get_release_tasks(self, jql):
        links = dict()
        search_labels = [self.RELEASE_PACK_TASK_LABEL, self.PD_TASK_LABEL, self.TEST_TASK_LABEL]
        tasks = self.jira_api_manager.search_tasks_jql(jql)
        if 'issues' in tasks and len(tasks['issues']):
            for task in tasks['issues']:
                if 'labels' in task['fields'] and 'labels' in task['fields']:
                    task_labels = task['fields']['labels']
                    label_intersection = list(set(task_labels) & set(search_labels))
                    if len(label_intersection) == 1:
                        task_key = task['key']
                        task_url = self.jira_api_config.url + '/browse/' + task_key
                        links[label_intersection[0]] = dict({'url': task_url, 'key': task_key})
                    else:
                        raise Exception('Incorrect labels count found.')
                else:
                    raise Exception('Labels not found.')
        else:
            raise Exception('Release Tasks not found.')

        return links

    def add_attachments_to_task(self, task_key, files):
        tasks = self.jira_api_manager.add_attachments_to_task(task_key, files)
