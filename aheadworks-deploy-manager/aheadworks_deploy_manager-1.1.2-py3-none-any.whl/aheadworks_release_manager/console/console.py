import os
from aheadworks_release_manager.api.release_manager import ReleaseManager
from aheadworks_core.model.data.jira import JiraConfig


class Console:
    """
    this application needed next env variables
    JIRA_USER_EMAIL
    JIRA_TOKEN
    """

    def __init__(self):
        jira_config = JiraConfig(os.getenv('JIRA_USER_EMAIL'), os.getenv('JIRA_TOKEN'))
        self.release_manager = ReleaseManager(jira_config)

    # Release manager
    def send_pack_to_manual_release(self, jira_project_key, module_version, discord_bot_url, path_to_files, assign_to):
        try:
            self.release_manager.send_pack_to_manual_release(
                jira_project_key,
                module_version,
                discord_bot_url,
                path_to_files,
                assign_to
            )
            exit_code = 0
        except Exception as error:
            print('Error: ' + repr(error))
            exit_code = 1

        exit(exit_code)
