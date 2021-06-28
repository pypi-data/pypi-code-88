import yaml
from os import path, remove
from pathlib import Path
from .message_log import Log
import prompt
from jinja2 import Template


config_path = path.expanduser('~/.grepsr')


def load_config(file_name, file_path=None):
    """Loads yml config file for user configuration

    Args:
        file_name (str): the name of file in the path gcli/config
    """

    if file_path is None:
        file_path = config_path
    try:
        file = f'{file_path}/{file_name}'
        with open(file, 'r') as f:
            file_content = f.read()
            return yaml.full_load(file_content)
    except:
        Log.error("{}  not found in Path {}".format(file_name, file_path))


def save_config(update=False):

    if update == False:
        setup_config = {}
    else:
        setup_config = load_config('config.yml')

    platforms = ['php', 'node', 'python', 'php_next']
    crawler_paths = []

    for plat in platforms:
        if _yes_no_prompt(f"\nProcess configuration for {Log.OKCYAN + plat + Log.ENDC} platform?"):
            if update == False:
                setup_config[plat] = {}
                setup_config[plat]['paths'] = []

                if(plat == 'php'):
                    setup_config[plat]['sdk_image'] = '486559570021.dkr.ecr.eu-central-1.amazonaws.com/vortex/sdk:stable'
                elif(plat == 'php_next'):
                    setup_config[plat]['sdk_image'] = '486559570021.dkr.ecr.eu-central-1.amazonaws.com/vortex/backend-next:latest'
                else:
                    setup_config[plat]['sdk_image'] = ''

            setup_config[plat]['env'] = {}
            Log.heading("\nStep 1: Path Configuration")

            if(update == True):
                if(_yes_no_prompt("Do you want to update crawler paths?") == True):
                    setup_config[plat]['paths'] = []
                    while True:
                        base_path = prompt.string(
                            prompt="Enter path for your plugin directory: ")
                        base_path = path.expanduser(base_path.rstrip('/'))
                        setup_config[plat]['paths'].append(base_path)
                        crawler_paths.append(base_path)
                        if(_yes_no_prompt("Do you want to another path?") == False):
                            break
            elif(update == False):
                while True:
                    base_path = prompt.string(
                        prompt="Enter path for your plugin directory: ")
                    base_path = path.expanduser(base_path.rstrip('/'))
                    setup_config[plat]['paths'].append(base_path)
                    crawler_paths.append(base_path)
                    if(_yes_no_prompt("Do you want to another path?") == False):
                        break
            else:
                pass

            Log.heading("\nStep 2: SDK Configuration")
            if(update == True):
                if(_yes_no_prompt("Do you want to update SDK image ?") == True):
                    if(plat == 'php'):
                        setup_config[plat]['sdk_image'] = '486559570021.dkr.ecr.eu-central-1.amazonaws.com/vortex/sdk:stable'
                    elif(plat == 'php_next'):
                        setup_config[plat]['sdk_image'] = '486559570021.dkr.ecr.eu-central-1.amazonaws.com/vortex/backend-next:latest'
                    else:
                        setup_config[plat]['sdk_image'] = ''

                    sdk_image = prompt.string(
                        prompt=f"Enter SDK image for {Log.OKCYAN + plat + Log.ENDC} (defaults to stable sdk if empty): ", empty=True)
                    if(sdk_image is not None):
                        setup_config[plat]['sdk_image'] = sdk_image
            elif(update == False):
                sdk_image = prompt.string(
                    prompt=f"Enter SDK image for {Log.OKCYAN + plat + Log.ENDC} (defaults to stable sdk if empty): ", empty=True)
                if(sdk_image is not None):
                    setup_config[plat]['sdk_image'] = sdk_image
            else:
                pass

            Log.heading("\nStep 3: Environment variable Coniguration")
            if(_yes_no_prompt("Do you want to add environment variables?") == True):
                while True:
                    env_key_val = prompt.string(
                        f"Enter env variable for {Log.OKCYAN + plat + Log.ENDC} (Eg:- CFG_PARAMS_SELENIUM_HOST: 192.168.90.64) \n")
                    try:
                        env_key_val = env_key_val.split(':')
                        setup_config[plat]['env'][env_key_val[0].strip()
                                                  ] = env_key_val[1].strip()
                    except:
                        Log.error("Please follow the correct format")
                    if(_yes_no_prompt("Do you want to another env variable?") == False):
                        break

    if(update == True):
        if(_yes_no_prompt("Do you want to update your aws keys?") == True):
            setup_config['aws_access_key_id'] = prompt.string(
                f"Enter aws id \n")
            setup_config['aws_secret_access_key'] = prompt.string(
                f"Enter aws secret key \n")
    else:
        setup_config['aws_access_key_id'] = prompt.string(
            f"Enter aws id \n")
        setup_config['aws_secret_access_key'] = prompt.string(
            f"Enter aws secret key \n")

    setup_config['app_env'] = 'tst'

    with open(config_path + '/config_test.yml', 'w') as w:
        w.write(yaml.dump(setup_config))

    if(update == False):
        _generate_autocomplete_script(crawler_paths)


def _yes_no_prompt(ques):
    answer = prompt.character(prompt=ques + ' (y/n) ', empty=True)
    if(answer == 'y' or answer is None):
        return True
    else:
        return False


def _generate_autocomplete_script(crawler_paths):
    Log.info("Generating Autocomplete Script")
    data = {}
    data['paths'] = []
    for p in range(len(crawler_paths)):
        d = {}
        d['ind'] = p
        d['dest_path'] = crawler_paths[p]
        data['paths'].append(d)

    if path.exists(config_path + '/autocomplete.sh'):
        remove(config_path +
               '/autocomplete.sh')

    template_dir = Path(__file__).parent.parent.absolute()
    template_file = '{}/templates/{}'.format(
        template_dir, 'autocomplete.jinja2')

    with open(template_file) as file:
        template = Template(file.read())

    with open(config_path + '/autocomplete.sh', 'w') as dest_file:
        dest_file.write(template.render(data))
