from aheadworks_core.api.jira_api_manager import JiraApiManager
from aheadworks_core.api.discord_api_manager import DiscordApiManager
from aheadworks_core.api.magento_manager import MagentoManager
from aheadworks_core.model.parser.json import Json as JsonParser
from aheadworks_core.model.cd import Cd as cd
from datetime import datetime
import os
import subprocess
import json
import shutil

class ReleaseManager:
    """api manager for release"""

    RELEASE_PACK_TASK_LABEL = 'RELEASE-PACK'
    PD_TASK_LABEL = 'PD'
    TEST_TASK_LABEL = 'TEST'

    LICENCE = """/**
 * Aheadworks Inc.
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the EULA
 * that is bundled with this package in the file LICENSE.txt.
 * It is also available through the world-wide-web at this URL:
 * https://ecommerce.aheadworks.com/end-user-license-agreement/
 *
 * @package    <PACKAGE_NAME>
 * @version    <VERSION>
 * @copyright  Copyright (c) 2020 Aheadworks Inc. (http://www.aheadworks.com)
 * @license    https://ecommerce.aheadworks.com/end-user-license-agreement/
 */"""

    def __init__(self, jira_api_config):
        self.jira_api_config = jira_api_config
        self.jira_api_manager = JiraApiManager(config=self.jira_api_config)
        self.discord_api_manager = DiscordApiManager()
        self.magento_manager = MagentoManager()
        self.json_parser = JsonParser()

    def jira_release(self, jira_project_key, composer_file, discord_bot_url, path_to_files, assign_to):
        module_version = self.json_parser.get_variable_from_file('version', composer_file)

        print('jira project key: ' + jira_project_key)
        print('module version: ' + module_version)
        print('discord bot url: ' + discord_bot_url)
        print('path to files: ' + path_to_files)
        print('assign to, account id: ' + assign_to)

        if not jira_project_key:
            print('jira_project_key is empty, skip jira release.')
            return False

        jira_instance = self.jira_api_manager.get_jira_instance()

        files_to_upload = []
        file_names = os.listdir(path_to_files)
        for file_name in file_names:
            files_to_upload.append(('file', (file_name, open(path_to_files + '/' + file_name, 'rb'))))

        jql = 'labels%3D{}-{}'.format(jira_project_key, module_version)
        links = self.get_release_tasks(jql)

        release_task_key = links[self.RELEASE_PACK_TASK_LABEL]['key']
        pd_task_key = links[self.PD_TASK_LABEL]['key']
        test_task_key = links[self.TEST_TASK_LABEL]['key']

        # add attachments
        self.add_attachments_to_task(release_task_key, files_to_upload)

        module_dependencies = self.magento_manager.get_module_dependencies_from_composer(composer_file)
        composer_package_name = ','.join(list(map(lambda x: x['full_module_name'], module_dependencies.values())))

        # assign release pack to user
        release_issue = jira_instance.issue(release_task_key)
        release_issue.update(assignee={'accountId': assign_to})
        jira_instance.add_comment(release_issue, 'Composer Package Name:\n' + composer_package_name)

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

        project = jira_instance.project(jira_project_key)

        msg = '{} {}\n'.format(project.name, module_version)
        msg += '\n'.join(list(map(lambda x: x['url'], links.values())))
        msg += '\n' + self.jira_api_manager.get_release_report_all_issues_url(jira_project_key, version.id)

        self.discord_api_manager.send_msg(discord_bot_url, msg)

        return True

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
                        task_url = self.jira_api_manager.get_issue_url(task_key)
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

    def build_ecommerce_pack(self, bitbucket_workspace, bitbucket_repo_slug):
        request = 'api.bitbucket.org/2.0/repositories/{}/{}/downloads'.format(
            bitbucket_workspace,
            bitbucket_repo_slug
        )
        with open('./composer.json') as f:
            composer = json.load(f)
        license_template = self.LICENCE
        # @todo use module_dependencies = self.magento_manager.get_module_dependencies_from_composer(composer_file)
        list_of_modules = list()
        versions = dict()
        core_module_name = composer['name']
        list_of_modules.append(core_module_name.split('/')[1])
        if composer.get('require') != None:
            for module in composer['require']:
                if module.find("aheadworks") != -1:
                    list_of_modules.append(module.split('/')[1])
        if composer.get('suggests') != None:
            for module in composer['suggests']:
                if module.find(core_module_name) != -1:
                    list_of_modules.append(module.split('/')[1])
                    version = composer['suggests'][module]
                    versions[module.split('/')[1]] = version.strip('><=')
        # end @todo
        os.system("mkdir -p app/code/Aheadworks")
        os.system("mkdir /build_archives")
        with cd('app/code/Aheadworks'):
            for module in list_of_modules:
                proc = subprocess.Popen(['git', 'clone', 'git@bitbucket.org:awm2ext/' + module + '.git'])
                proc.communicate()
                if proc.returncode != 0:
                    raise Exception("Failed download module " + module)
                with cd(module):
                    if module in versions.keys():
                        proc = subprocess.Popen(['git', 'checkout', versions[module]])
                        proc.communicate()
                path_to_composer = module + "/composer.json"
                path_to_registration = module + "/registration.php"
                ec1 = os.path.isfile(path_to_composer)
                ec2 = os.path.isfile(path_to_registration)
                if not (ec1) or not (ec2):
                    raise Exception(module + " haven't build")
                proc = subprocess.Popen(['rm', module + '/bitbucket-pipelines.yml'])
                proc.communicate()
                self.add_license_to_php_files(os.getcwd() + '/' + module, license_template)
                proc = subprocess.Popen(['rm', module + '/.gitignore'])
                os.system("rm -rf ./" + module + "/.git")
                os.system(
                    "echo See https://ecommerce.aheadworks.com/end-user-license-agreement/ >> " + module + "/license.txt")
                proc.communicate()
                with open(path_to_registration) as f2:
                    lines = f2.readlines()
                for line in lines:
                    if line.find("headworks_") != -1:
                        module_directory_name = line.strip('\"\'').split('_')[1][0:-3]
                is_core = core_module_name.split('/')[1] == module
                if is_core:
                    marketplace_name = core_module_name.split('/')[1]
                    core_module_directory_name = module_directory_name
                    result_name = module_directory_name + '-' + composer['version']
                os.system('mv ' + module + ' ' + module_directory_name)
                if not is_core:
                    with open('./' + module_directory_name + '/composer.json') as f5:
                        meta_composer = json.load(f5)
                        module_zip_name = meta_composer['name'].split('/')[1]
                    self.make_archive('./' + module_directory_name + '/.', module_zip_name + '.zip')
                    os.system(
                        'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + module_zip_name + '.zip"')
                    os.system('cp ' + module_zip_name + '.zip /build_archives')
                    os.system('rm ' + module_zip_name + '.zip')
        os.system('apk add zip')
        with cd('app/code/Aheadworks/' + core_module_directory_name):
            os.system('zip -r ' + marketplace_name + '.zip ' + './')
            os.system(
                'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + marketplace_name + '.zip"')
            os.system('cp ' + marketplace_name + '.zip /build_archives')
            os.system('rm ' + marketplace_name + '.zip')
        cd('../../..')
        os.system('pwd')
        os.system('echo $BB_AUTH_STRING')
        os.system('zip -r aw_m2_' + result_name + '.community_edition.zip app')
        ce = '"aw_m2_' + result_name + '.community_edition.zip"'
        os.system('zip -r aw_m2_' + result_name + '.enterprise_edition.zip app')
        ee = '"aw_m2_' + result_name + '.enterprise_edition.zip"'
        os.system("cp " + ce + " /build_archives")
        os.system("cp " + ee + " /build_archives")
        os.system(
            'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + ce + '"')
        os.system(
            'curl -X POST "https://IgorSednev:FAdCM9dzPXzMYsbypdXe@' + request.strip() + '" ' + '--form files=@"' + ee + '"')

    def add_license_to_php_files(self, path, license_template):
        with cd(path):
            with open(path + '/composer.json') as f:
                composer = json.load(f)
            with open(path + "/registration.php") as reg:
                l = reg.readlines()
                for line in l:
                    if line.find("Aheadworks_") != -1:
                        package_name = line.split("_")[1][:-2]
            license_result = list()
            for line in license_template:
                if line.find("package") != -1:
                    print(line)
                    print(package_name)
                    line = line.replace("<PACKAGE_NAME>", package_name[:-1])
                if line.find("version") != -1:
                    print(line)
                    print(composer["version"])
                    line = line.replace("<VERSION>", composer["version"])
                license_result.append(line)
            license_result[-1] += '\n'
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".php"):
                        with open(os.path.join(root, file)) as f:
                            original_lines = f.readlines()
                        result_lines = list()
                        if len(original_lines):
                            result_lines.append(original_lines[0])
                        else:
                            print('WARNING: file ' + os.path.join(root, file) + " is empty")
                        for line in license_result:
                            result_lines.append(line)
                        for line in original_lines[1:]:
                            result_lines.append(line)
                        result = open(os.path.join(root, file), 'w')
                        result.writelines([item for item in result_lines])
                        result.close()

    def make_archive(self, source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[-1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), destination)
