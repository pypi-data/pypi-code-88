import click
import os
import re
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

    dsf-cli g project my-new-project

    dsf-cli generate project my-new-project

    cd my-new-project

    create forcer

    dsf-cli g forcer my-new-forcer

    create predictable

    dsf-cli g predictable my-new-predictable

    run server

    dsf-cli run-server

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
    os.environ["PYTHONPATH"] = currentPipelineFolder
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

    create_main_folders('pipeline', 'main')
    create_main_folders('artifacts', 'pipeline')
    create_main_folders('models', 'artifacts')
    create_main_folders('vocabs', 'artifacts')
    # create_main_folders('other', 'artifacts')
    create_main_folders('preprocessor', 'pipeline')
    create_main_folders('predictables', 'pipeline')
    create_main_folders('predictors', 'pipeline')
    create_main_folders('forcers', 'pipeline')
    create_main_folders('postprocessor', 'pipeline')
    create_main_folders('schema', 'pipeline')
    create_main_folders('tester', 'main')
    create_main_folders('trainer', 'main')
    create_main_folders('server', 'main')

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
    # create_tester_file(projectName, directories['tester'], 'tester')
    # create_tester_file(projectName, directories['tester'], 'reporter')
    create_tester_file(projectName, directories['server'], 'server', False)
    create_tester_file(projectName, directories['server'], 'test_server_post', False)
    # create_tester_file(projectName, directories['trainer'], 'trainer')
    # create_pipeline_file(projectName, 'labelizer')
    # create_pipeline_file(projectName, 'pipeline')
    #
    create_project_config_json()
    create_server_config_json()
    #
    # create_tester_file(projectName, 'dataset')
    # create_tester_file(projectName, 'reporter')
    # create_tester_file(projectName, 'tester')
    # create_tester_file(projectName, 'tester_server')


def create_main_folders(targetDir, baseDir):
    global directories
    directories[targetDir] = directories[baseDir] + '/' + targetDir
    if not os.path.exists(directories[targetDir]):
        os.mkdir(directories[targetDir])

def create_pipeline_file(projectName, folder, pipelineType, createInitFile=True):
    data = read_template_file(pipelineType)
    replace_in_template_and_create_file(projectName, folder, pipelineType, data, createInitFile)


def create_tester_file(projectName, folder, pipelineType, createInitFile=True):
    data = read_template_file('tester/' + pipelineType)
    replace_in_template_and_create_file(projectName, folder, pipelineType, data, createInitFile)

def create_exist_pipeline_file(type, fileName):
    pipelineType = type + 's'
    folder = 'pipeline/' + pipelineType
    if os.path.exists(folder):
        data = read_template_file(type)
        fileNameNoUnderscore = to_capitalize_no_underscore(fileName)
        className = fileNameNoUnderscore + type.capitalize()
        currentPipelineFolder = os.path.basename(os.getcwd())
        currentDir = folder.replace('/', '.')

        data = data.replace('generatedClass', className)

        new_file = folder + "/" + fileName + ".py"
        current_init_file = folder + "/__init__.py"
        new_init_export = "from " + currentDir + '.' + fileName + " import " + className

        create_file(new_file, data)
        create_init_file(current_init_file, new_init_export)
        inject_to_pipeline(fileName, className, new_init_export)
    else:
        print('please create a project and go to project location first')
    pass


def read_template_file(pipelineType):
    with open(os.path.join(__location__, 'cli/' + pipelineType + '_template.py'), 'r') as file:
        data = file.read()
        return data

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        return data

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
        file.close()

def replace_in_template_and_create_file(projectName, folder, pipelineType, data, createInitFile):
    pipelineTypeNoUnderscore = to_capitalize_no_underscore(pipelineType)
    projectNameNoUnderscore = to_capitalize_no_underscore(projectName)
    className = projectNameNoUnderscore + pipelineTypeNoUnderscore
    classNameForBaseObject = projectNameNoUnderscore + pipelineTypeNoUnderscore
    currentDir = folder.replace('/', '.')
    currentDirNoMainDir = folder.replace(directories['main'] + '/', '').replace('/', '.')
    currentBaseDir = directories['main'].replace('/', '.')
    currentPipelineDir = directories['pipeline'].replace('/', '.')

    data = data.replace('generatedClassName', classNameForBaseObject)
    data = data.replace('generatedClass', className)
    data = data.replace('generatedProjectName', projectNameNoUnderscore)
    data = data.replace('generatedDirectory', currentDir)
    data = data.replace('generatedBaseDir', currentBaseDir)
    data = data.replace('generatedPipelineDir', currentPipelineDir)

    new_file = folder + "/" + pipelineType + ".py"
    create_file(new_file, data)

    if createInitFile:
        new_init_file = folder + "/__init__.py"
        new_init_export = "from " + currentDirNoMainDir + '.' + pipelineType + " import " + className
        create_init_file(new_init_file, new_init_export)

def create_predictable_file(fileName):
    pass

def create_file(new_file_path, data):
    if not os.path.exists(new_file_path):
        f = open(new_file_path, "w")
        f.write(data)
        f.close()
def create_init_file(init_path, init_export):
    if not os.path.exists(init_path):
        f = open(init_path, "w")
        f.write(init_export)
        f.close()
    else:
        f = open(init_path, 'r+')
        data = f.read()
        if init_export not in data:
            if len(data) and not data.endswith('\n'):
                f.write('\n')
            f.write(init_export)
            f.close()

def inject_to_pipeline(fileName, className, new_init_export):
    file_path = 'pipeline/pipeline.py'
    if os.path.exists(file_path):
        data = read_file(file_path)
        new_tab_line = '\n'
        data_changed = False
        last_index_of_import = -1
        first_index_of_add_component = -1
        index_of_class = re.search(r'class[^\n]*', data)

        # finding current indent config
        index_of_build_pipeline = re.search(r'def build_pipeline[^\n]*', data)
        index_of_build_preprocessor = re.search(r'self.preprocessor =[^\n]*', data)
        index_of_build_postprocessor = re.search(r'self.postprocessor =[^\n]*', data)
        index_of_build_pipeline_row = re.search(r'.*def build_pipeline[^\n]*', data)
        if index_of_build_pipeline:
            build_pipeline_indent = (index_of_build_pipeline.start() - index_of_build_pipeline_row.start()) * 2
            new_tab_line = new_tab_line.ljust(build_pipeline_indent + 1)

        new_component_line = 'self.' + fileName + ' = ' + className + '()'
        add_component_line = 'self.add_component(self.' + fileName + ')'

        # finding imports and add components indexes
        last_index_of_add_component = -1
        all_from_import = [i.end() for i in re.finditer(r'from[^\n]*', data)]
        all_add_components = [[i.start(), i.end()] for i in re.finditer(r'self.add_component[^\n]*', data)]
        if len(all_from_import):
            last_index_of_import = all_from_import[-1]
        if len(all_add_components):
            first_index_of_add_component = all_add_components[0][0]
            last_index_of_add_component = all_add_components[-1][-1]
        # finding imports and add components indexes


        index_to_add = 0

        # add import to end of imports or to top of file
        if last_index_of_import > -1 and new_init_export not in data:
            s = '\n' + new_init_export
            index_to_add += len(s)
            data = data[:last_index_of_import] + s + data[last_index_of_import:]
            data_changed = True
        elif index_of_class and new_init_export not in data:
            s = new_init_export + '\n\n'
            index_to_add += len(s)
            data = data[:index_of_class.start()] + s + data[index_of_class.start():]
            data_changed = True

        # check if build_pipeline exist but with no components yet
        if first_index_of_add_component == -1 and last_index_of_add_component == -1 and index_of_build_pipeline:
            s = new_tab_line
            current_end = index_of_build_pipeline.end()
            if index_of_build_preprocessor:
                current_end = index_of_build_preprocessor.end()
            if index_of_build_postprocessor:
                current_end = index_of_build_postprocessor.end()
            index = current_end + index_to_add
            index_to_add += len(s)
            data = data[:index] + s + data[index:]
            data_changed = True
            first_index_of_add_component = current_end
            last_index_of_add_component = current_end

        # adding new component line
        if first_index_of_add_component > -1 and new_component_line not in data:
            first_index_of_add_component += index_to_add
            if len(all_add_components):
                new_component_line = new_component_line + new_tab_line
            index_to_add += len(new_component_line)
            data = data[:first_index_of_add_component] + new_component_line + data[first_index_of_add_component:]
            data_changed = True

        #adding add_component line
        if last_index_of_add_component > -1 and add_component_line not in data:
            last_index_of_add_component += index_to_add
            add_component_line = new_tab_line + add_component_line
            index_to_add += len(add_component_line)
            data = data[:last_index_of_add_component] + add_component_line + data[last_index_of_add_component:]
            data_changed = True

        if data_changed:
            write_to_file(file_path, data)

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

def create_server_config_json():
    with open(os.path.join(__location__, 'cli/cors_allowed_origins.json'), 'r') as file:
        data = file.read()
        data = data.replace('generatedDirectory', directories['main'])
        new_file = directories['server'] + '/cors_allowed_origins.json'
        if not os.path.exists(new_file):
            f = open(new_file, "w")
            f.write(data)
            f.close()

def to_capitalize_no_underscore(text):
    return ''.join(elem.capitalize() for elem in text.split('_'))

if __name__ == '__main__':
    cli(prog_name='cli')
