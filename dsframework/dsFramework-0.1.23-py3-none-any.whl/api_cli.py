import click
import os
import sys
import subprocess

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

directories = {
    'main': '',
    'pipeline': '',
    'artifacts': '',
    'models': '',
    'vocabs': '',
    'other': '',
    'preprocessor': '',
    'predictables': '',
    'predictors': '',
    'forcers': '',
    'postprocessor': '',
    'schema': '',
    'tester': '',
    'trainer': '',
    'server': '',
}
class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)

@click.group(cls=AliasedGroup)
def cli():
    """
    DS framework cli

    ** how to use **

    g = generate

    create project

    ds-framework-cli g project my-new-project

    ds-framework-cli generate project my-new-project

    cd my-new-project

    create forcer

    ds-framework-cli g forcer my-new-forcer

    create predictable

    ds-framework-cli g predictable my-new-predictable

    run server

    ds-framework-cli run-server

    """
# @click.option("--type", prompt="type", help="type of component")
# @click.option("--project_name", prompt="project_name", help="project_name")
# def apis(type, project_name):


@cli.command()
@click.argument('type')
@click.argument('project_name')
def generate(type, project_name):
    """List all cataloged APIs."""
    try:
        f = globals()["generate_%s" % type]
    except Exception as e:
        click.echo('type ' + type + ' not found')
        return
    f(project_name)

@cli.command()
def run_server():
    currentPipelineFolder = os.path.abspath(os.getcwd())
    currentParentFolder = os.path.join(currentPipelineFolder,"..")
    os.environ["PYTHONPATH"] = currentParentFolder
    folder = currentPipelineFolder + '/server/server.py'
    subprocess.call('python ' + folder, shell=True)

ALIASES = {
    "g": generate
}

def generate_project(projectName):
    projectName = clean_name(projectName)
    click.echo('project generated ' + projectName)
    create_project(projectName)

def generate_forcer(fileName):
    fileName = clean_name(fileName)
    create_exist_pipeline_file('forcer', fileName)

def generate_predictable(fileName):
    fileName = clean_name(fileName)
    create_exist_pipeline_file('predictable', fileName)

def clean_name(name):
    name = name.replace('-', '_')
    return name

def create_folders(projectName):
    global directories
    directories['main'] = projectName + '_project'
    if not os.path.exists(directories['main']):
        os.mkdir(directories['main'])

    create_main_folders(projectName, 'pipeline', 'main')
    create_main_folders(projectName, 'artifacts', 'pipeline')
    create_main_folders(projectName, 'models', 'artifacts')
    create_main_folders(projectName, 'vocabs', 'artifacts')
    # create_main_folders(projectName, 'other', 'artifacts')
    create_main_folders(projectName, 'preprocessor', 'pipeline')
    create_main_folders(projectName, 'predictables', 'pipeline')
    create_main_folders(projectName, 'predictors', 'pipeline')
    create_main_folders(projectName, 'forcers', 'pipeline')
    create_main_folders(projectName, 'postprocessor', 'pipeline')
    create_main_folders(projectName, 'schema', 'pipeline')
    create_main_folders(projectName, 'tester', 'main')
    create_main_folders(projectName, 'trainer', 'main')
    create_main_folders(projectName, 'server', 'main')

def create_project(projectName):
    create_folders(projectName)
    create_pipeline_file(projectName, directories['artifacts'], 'shared_artifacts')
    create_pipeline_file(projectName, directories['schema'], 'inputs')
    create_pipeline_file(projectName, directories['schema'], 'outputs')
    create_pipeline_file(projectName, directories['preprocessor'], 'preprocess')
    create_pipeline_file(projectName, directories['predictors'], 'predictor')
    create_pipeline_file(projectName, directories['forcers'], 'forcer')
    create_pipeline_file(projectName, directories['postprocessor'], 'postprocess')
    create_pipeline_file(projectName, directories['predictables'], 'predictable')
    create_pipeline_file(projectName, directories['pipeline'], 'pipeline')
    create_pipeline_file(projectName, directories['main'], 'test_pipeline', False)
    # create_testet_file(projectName, directories['tester'], 'tester')
    # create_testet_file(projectName, directories['tester'], 'reporter')
    create_testet_file(projectName, directories['server'], 'server', False)
    create_testet_file(projectName, directories['server'], 'test_server_post', False)
    # create_testet_file(projectName, directories['trainer'], 'trainer')
    # create_pipeline_file(projectName, 'labelizer')
    # create_pipeline_file(projectName, 'pipeline')
    #
    create_project_config_json()
    #
    # create_testet_file(projectName, 'dataset')
    # create_testet_file(projectName, 'reporter')
    # create_testet_file(projectName, 'tester')
    # create_testet_file(projectName, 'tester_server')


def create_main_folders(projectName, targetDir, baseDir):
    global directories
    directories[targetDir] = directories[baseDir] + '/' + targetDir
    if not os.path.exists(directories[targetDir]):
        os.mkdir(directories[targetDir])

def create_pipeline_file(projectName, folder, pipelineType, createInitFile=True):
    with open(os.path.join(__location__, 'cli/' + pipelineType + '_template.py'), 'r') as file:
        data = file.read()
        pipelineTypeNoUnderscore = ''.join(elem.capitalize() for elem in pipelineType.split('_'))
        projectNameNoUnderscore = ''.join(elem.capitalize() for elem in projectName.split('_'))
        className = projectNameNoUnderscore + pipelineTypeNoUnderscore
        classNameFotBaseObject = projectNameNoUnderscore + pipelineTypeNoUnderscore
        data = data.replace('generatedClassName', classNameFotBaseObject)
        data = data.replace('generatedClass',className)
        data = data.replace('generatedProjectName',projectNameNoUnderscore)
        currentDir = folder.replace('/', '.')
        currentBaseDir = directories['main'].replace('/', '.')
        currentPipelineDir = directories['pipeline'].replace('/', '.')
        data = data.replace('generatedDirectory', currentDir)
        data = data.replace('generatedBaseDir', currentBaseDir)
        data = data.replace('generatedPipelineDir', currentPipelineDir)
        new_file = folder + "/" + pipelineType + ".py"
        new_init_file = folder + "/__init__.py"
        new_init_export = "from " + currentDir + '.' + pipelineType + " import " + className
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()
        if createInitFile:
            create_pipeline_init_file(new_init_file, new_init_export)

def create_exist_pipeline_file(type, fileName):
    pipelineType = type + 's'
    folder = 'pipeline/' + pipelineType
    if os.path.exists(folder):
        fileNameNoUnderscore = ''.join(elem.capitalize() for elem in fileName.split('_'))
        className = fileNameNoUnderscore + type.capitalize()
        with open(os.path.join(__location__, 'cli/' + type + '_template.py'), 'r') as file:
            data = file.read()
            data = data.replace('generatedClass', className)
            new_file = folder + "/" + fileName + ".py"
            current_init_file = folder + "/__init__.py"
            currentPipelineFolder = os.path.basename(os.getcwd())
            currentDir = folder.replace('/', '.')
            new_init_export = "from " + currentPipelineFolder + '.' + currentDir + '.' + fileName + " import " + className
            if not os.path.exists(new_file):
                f = open(new_file, "w")
                f.write(data)
                f.close()
            if os.path.exists(current_init_file):
                f = open(current_init_file, 'r+')
                data = f.read()
                if new_init_export not in data:
                    if len(data):
                        f.write('\n')
                    f.write(new_init_export)
                    f.close()
    else:
        print('please create a project and go to project location first')
    pass

def create_predictable_file(fileName):
    pass

def create_testet_file(projectName, folder, pipelineType, createInitFile=True):
    with open(os.path.join(__location__, 'cli/tester/' + pipelineType + '_template.py'), 'r') as file:
        data = file.read()
        projectNameNoUnderscore = ''.join(elem.capitalize() for elem in projectName.split('_'))
        pipelineTypeNoUnderscore = ''.join(elem.capitalize() for elem in pipelineType.split('_'))
        className = projectNameNoUnderscore + pipelineTypeNoUnderscore
        classNameFotBaseObject = projectNameNoUnderscore + pipelineTypeNoUnderscore
        data = data.replace('generatedClassName', classNameFotBaseObject)
        data = data.replace('generatedClass',className)
        data = data.replace('generatedProjectName',projectNameNoUnderscore)
        currentDir = folder.replace('/', '.')
        currentBaseDir = directories['main'].replace('/', '.')
        currentPipelineDir = directories['pipeline'].replace('/', '.')
        data = data.replace('generatedDirectory', currentDir)
        data = data.replace('generatedBaseDir', currentBaseDir)
        data = data.replace('generatedPipelineDir', currentPipelineDir)
        new_file = folder + "/" + pipelineType + ".py"
        new_init_file = folder + "/__init__.py"
        new_init_export = "from " + currentDir + '.' + pipelineType + " import " + className
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()
        if createInitFile:
            create_tester_init_file(new_init_file, new_init_export)

def create_pipeline_init_file(init_path, init_export):
    if not os.path.exists(init_path):
        f = open(init_path, "w")
        f.write(init_export)
        f.close()

def create_tester_init_file(init_path, init_export):
    f = open(init_path, "a")
    f.write(init_export)
    f.write("\n")
    f.close()

def create_project_config_yaml():
    with open(os.path.join(__location__, 'cli/config.yaml'), 'r') as file:
        data = file.read()
        data = data.replace('generatedDirectory', directories['main'])
        new_file = directories['main'] + '/pipeline/config.yaml'
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()

def create_project_config_json():
    with open(os.path.join(__location__, 'cli/config.json'), 'r') as file:
        data = file.read()
        data = data.replace('generatedDirectory', directories['main'])
        new_file = directories['main'] + '/config.json'
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()
if __name__ == '__main__':
    cli(prog_name='cli')
