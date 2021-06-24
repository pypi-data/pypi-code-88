#                       Copyright (c) 2021 Zenqi.
#                 This project was created by discord_template
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
from InquirerPy.utils import color_print as cprint
from InquirerPy import prompt, inquirer, get_style
from InquirerPy.separator import Separator
from jinja2 import Environment, FileSystemLoader
import getpass
import requests
import shutil
import sys
import json
from discord_template import __version__
import time
import subprocess
from tabulate import tabulate

BASE_DIR = os.path.dirname(os.path. abspath(__file__))

def startup():
    
    try:
        with open(f"{BASE_DIR}\\startup", "r") as f:
            data = json.load(f)
            f.close()

    except FileNotFoundError:
        with open(f"{BASE_DIR}\\startup", "w") as f:
            json.dump({'auto_update': True}, f)
            f.close()

    if data['auto_update'] == True:

        cprint([('yellow', 'NOTE: '), ('cyan', 'Checking for update... ( You can disable using `discord update disable` )')])
        time.sleep(1)
        try:
            r = requests.get(url="https://raw.githubusercontent.com/znqi/discordtemplate/main/version.json").json()

        except Exception:
            cprint([('yellow', "WARNING: "), ('cyan', 'Failed to check for updates.')])

        NEW_VERSION     = r['version']
        RELEASE_NOTE    = r['note']


        if __import__("discord_template").__version__ != NEW_VERSION:
            cprint([('red', 'NEW UPDATE: '), ('cyan', f'Version {NEW_VERSION} is out now! Installing the update...\n'), ('yellow', 'RELEASE NOTE: '), ('cyan', f'{RELEASE_NOTE}')])
            time.sleep(2)
            subprocess.run("pip install --upgrade discordtemplate")
            sys.exit()



def config_startup_settings(data):
    try:
        with open(f"{BASE_DIR}\\startup", "r") as f:
            _data = json.load(f)
            f.close()
    except FileNotFoundError:
        with open(f"{BASE_DIR}\\startup", "w") as f:
            json.dump({'auto_update': True}, f)
            f.close()

    with open(f"{BASE_DIR}\\startup", "w") as fd:
        _data.update(data)
        json.dump(_data, fd)
        fd.close()
        
        

def name_auto_complete() -> dict:
    return {f"{getpass.getuser().lower()}'s bot": None, getpass.getuser(): None, "bot": None }

def render_template(name, *args, **kwargs):
    
    env = Environment(loader=FileSystemLoader(f"{BASE_DIR}\\env"))
    template = env.get_template(name)
    output = template.render(*args, **kwargs)

    return output

def clear():

    if sys.platform == "win32":
        os.system("cls")

    else:
        os.system('clear')
    

class DiscordTemplate:
    def __init__(self, folder_name=None):
        clear()
        if folder_name != None:
            self.dir = f"{os.getcwd()}\\{folder_name}"
        else:
            self.dir = os.getcwd()

        if folder_name != None:
            try:
                os.mkdir(self.dir)
                os.chdir(self.dir)

            except FileExistsError:
                cprint([('red', "ERROR: "), ('cyan', f"Cannot create @ {self.dir}. The folder already exists.")])
                sys.exit()

        cprint([("blue", """\n      .o8   o8o                                              .o8  \n     "888   `"'                                             "888  \n .oooo888  oooo   .oooo.o  .ooooo.   .ooooo.  oooo d8b  .oooo888  \nd88' `888  `888  d88(  "8 d88' `"Y8 d88' `88b `888""8P d88' `888  \n888   888   888  `"Y88b.  888       888   888  888     888   888  \n888   888   888  o.  )88b 888   .o8 888   888  888     888   888  \n`Y8bod88P" o888o 8""888P' `Y8bod8P' `Y8bod8P' d888b    `Y8bod88P"""), ("white", f"""\n\n          - 🔹 A discord bot template for discord.py v{__version__}.\n""")])
        questions = [
            {
                "type": "input",
                "message": "What would be the name of the bot:",
                "completer": name_auto_complete(),
                
            },
            {
                "type": "input",
                "message": "What would be the prefix of the bot:",
                "default": "!",
                "validate": lambda text: len(text) > 0,
                "invalid_message": "Please enter prefix.",
            },
            {
                "type": "input",
                "message": "Enter the bot's token:",
                "validate": lambda text: len(text) > 58,
                "invalid_message": "Invalid bot token format. Please get the token @ https://discord.com/developers/applications/"
            },
            {
                "type": "list",
                "message": "Enter Bot's Gateway Intents [Optional]:",
                "choices": [
                    {"name": "All Gateway Itents", "value": 'discord.Intents.all()'},
                    {"name": "Default Gateway Intents", "value": 'discord.Intents.default()'},
                    
                    Separator(),
                    {"name": "Messages Gateway Intents", "value": 'discord.Intents(messages=True)'},
                    {"name": "Guilds Gateway Intents", "value": 'discord.Intents(guilds=True)'},
                    {"name": "Members Gateway Intents", "value": 'discord.Intents(members=True)'},
                    {"name": "", "value": 'discord.Intents()'},
                    
                    Separator(),
                    {"name": "Do not use any Gateway Intents", "value": None},
                ],
                
            },
            
        ]

        result = prompt(questions=questions)
        is_heroku = inquirer.confirm("Would you like to add heroku integration?", default=True, style=get_style({"question": "#6a0dad"}, style_override=True)).execute()
        
        print("")
        cprint([('yellow', "CREATING: "), ('cyan', "Main file @ {}".format(self.dir))])
        self.write_main_file(self.dir, render_template("main", d_intents=result[2], username=getpass.getuser()))


        cprint([('yellow', "CREATING: "), ('cyan', "Config file @ {}".format(self.dir))])
        self.write_config(self.dir, render_template("config", _name=result[0], prefix=result[1], token=result[2], heroku=is_heroku))

        self.copy_cogs_ext(f"{self.dir}\\ext")


    def write_config(self, dir, content):
        with open(f"{dir}\\config.json", "w") as f:
            f.write(content)

    def write_main_file(self, dir, content):
        with open(f'{dir}\\main.py', 'w') as f:
            f.write(content)

    def copy_cogs_ext(self, dir):
        if os.path.isdir(dir): os.mkdir(dir)

        cprint([('purple', "COPYING: "), ('cyan', "Cog files to {}".format(dir))])
        shutil.copytree(f"{BASE_DIR}\\env\\ext", dir)


def help_command():
    clear()
    cprint([("blue", """\n      .o8   o8o                                              .o8  \n     "888   `"'                                             "888  \n .oooo888  oooo   .oooo.o  .ooooo.   .ooooo.  oooo d8b  .oooo888  \nd88' `888  `888  d88(  "8 d88' `"Y8 d88' `88b `888""8P d88' `888  \n888   888   888  `"Y88b.  888       888   888  888     888   888  \n888   888   888  o.  )88b 888   .o8 888   888  888     888   888  \n`Y8bod88P" o888o 8""888P' `Y8bod8P' `Y8bod8P' d888b    `Y8bod88P"""), ("white", f"""\n\n          - 🔹 A discord bot template for discord.py v{__version__}.\n""")])
    print("")
    cprint([('yellow', 'Version: '), ('cyan', '{}'.format(__version__))])
    cprint([('yellow', 'discord.py: '), ('cyan', '{}'.format(__import__('discord').__version__))])
    cprint([('yellow', 'Python: '), ('cyan', '{}.{}'.format(sys.version_info[0], sys.version_info[1]))])
    cprint([('blue', '─'*70)])
    cprint([('cyan', tabulate([['create', 'create discord bot template', 'discord create demo_bot'], ['run', 'Run the bot', 'discord run'], ['update', 'Either enable, disable or update', 'discord update']], ['Commands', 'Description', 'Example'], tablefmt="fancy_grid"))])
    print("")
    
def run():
    

    try:
        if sys.argv[1] == "update":

            try:

                if sys.argv[2] == "disable":
                    config_startup_settings({"auto_update": False})
                    cprint([('yellow', "SETTINGS: "), ('cyan', "Startup config successfully changed.")])
                    sys.exit()

                elif sys.argv[2] == "enable":
                    config_startup_settings({"auto_update": True})
                    cprint([('yellow', "SETTINGS: "), ('cyan', "Startup config successfully changed.")])
                    sys.exit()
            
            except IndexError:
                pass

            subprocess.run("pip install --upgrade discordtemplate")
        
        else:
            startup()
        
        if sys.argv[1] == "create":

            folder_name = None
            
            try:
                if sys.argv[2] == ".":
                    folder_name = None
                
                else:
                    folder_name = sys.argv[2]
            
            except IndexError:
                pass
            

            DiscordTemplate(folder_name)


        elif sys.argv[1] == "run":
            # soon
            pass

        elif sys.argv[1] == "heroku":
            # soon
            pass
            
           
    except IndexError:
        help_command()


if __name__ == "__main__":
    run()
