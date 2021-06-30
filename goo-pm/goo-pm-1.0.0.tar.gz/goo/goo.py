#!/usr/bin/env python3
import os
import shutil
import click
import json
import validators
import requests
import tempfile
from configparser import ConfigParser
from zipfile import ZipFile
from git import Repo
from bs4 import BeautifulSoup

DEFAULT_GODOT_VERSION = "3.*.*"
OK = "✔ "
ERR = "✘ "
INFO = "→ "
WARN = "⚠ "

@click.group()
def cli():
    pass


def goo_root():
    current_dir = os.getcwd()
    while current_dir != os.path.abspath(os.sep):
        if os.path.isfile(os.path.join(current_dir, "goo.json")):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return ""


@cli.command("init", help = "Initialize Goo in the current project directory.")
@click.option(
    "-v", "--gd-version", default = DEFAULT_GODOT_VERSION, show_default = True,
    help = "Specifies the version of Godot you're working with."
)
def goo_init(gd_version):
    if goo_root() != "":
        click.echo(INFO + " Goo is already initialized.")
        exit(1)
    if not os.path.isdir("./addons"):
        try:
            os.mkdir("./addons")
        except:
            click.echo(ERR + " Couldn't create the addons/ directory.")

    try:
        with open("./goo.json", "w") as f:
            f.write(json.dumps(
                {"godot-version": gd_version, "dependencies": {}},
                indent = 2
            ))
    except:
        click.echo(ERR + " Couldn't create goo.json, initialization failed...")
        exit(1)

    with open("./.gitignore", "a") as f:
        f.writelines("addons/\n")
    click.echo(OK + " Goo initialized in the current directory.")


@cli.command(
    "install",
    help = """Install all the missing dependencies or install a plugin and
        save it as a dependency. You can install plugins either from 
        the Godot Asset Library by specifying <author/plugin name>
        (e.g.: goo install \"CoolJane/My Plugin\"), or from a Git
        repository, by specifying the URL of the remote repository.
        If no argument is provided, Goo will only install the missing
        dependencies, if any."""
)
@click.argument("plugin", required = False)
@click.option(
    "-v", "--version", default = "*", show_default = True,
    help = "Specifies the required version of a plugin"
)
@click.option("-b", "--branch", default = "main|master", show_default = True,
    help = """Specifies the branch from which you want to pull changes
        (only works with plugins installed from Git repos)"""
)
def install(plugin, version, branch):
    root = goo_root()
    if root == "":
        click.echo(ERR + "Goo is not initialized yet.")
        exit(1)

    if plugin is None:
        if not install_missing_dependencies():
            exit(1)
    else:
        installed_from_git = False
        if validators.url(plugin):
            if version != "*":
                click.echo(WARN + "The --version option is ignored for " +
                    "plugins that are installed from Git repos.")
            installed_from_git = True
            if not install_from_git_repo(plugin, branch):
                exit(1)
        else:
            if branch != "main|master":
                click.echo(WARN + "The --branch option is ignored for " +
                    "plugins that are installed from the Godot Asset Library")
            if not install_from_assetlib(plugin, version):
                exit(1)
        click.echo(INFO + "Saving dependency...")
        if not add_dependency(plugin, installed_from_git, version, branch):
            exit(1)
        click.echo(OK + "Done.")


@cli.command(
    "update",
    help = "Update all the installed plugins for this project."
)
def update():
    root = goo_root()
    if root == "":
        click.echo(ERR + "Goo is not initialized yet.")
        exit(1)
    
    outdated_plugins = 0
    successful_updates = 0
    not_installed = 0
    dependencies = get_goo_cfg()["dependencies"]
    for plugin_name, plugin_info in dependencies.items():
        if len(plugin_info.split(";b=")) == 2:
            click.echo(INFO + "Updating \"%s\" (Git)..." % (plugin_name))

            repo_dir = os.path.join(
                goo_root(),
                "addons",
                ".%s-repo" % (plugin_name)
            )
            if not os.path.isdir(repo_dir):
                click.echo(ERR + "The plugin is not installed yet.")
                not_installed += 1
                continue

            repo = Repo(repo_dir)
            o = repo.remotes.origin
            result = o.pull()
            # https://gitpython.readthedocs.io/en/stable/reference.html
            # ?highlight=pull#git.remote.FetchInfo
            if result[0].flags == 4:
                click.echo(OK + "It's up-to-date.")
            elif result[0].flags == 128 or result[0].flags == 16:
                click.echo(ERR + "Couldn't update.")
                outdated_plugins += 1
            else:
                click.echo(OK + "Successfully updated.")
                outdated_plugins += 1
                successful_updates += 1
        else:
            target_version = plugin_info
            if target_version != "*":
                continue
            
            click.echo(INFO + "Updating \"%s\"..." % (plugin_name))
            current_version = get_installed_version(plugin_name)
            if current_version == "":
                click.echo(ERR + "The plugin is not installed yet.")
                not_installed += 1
                continue
            if len(current_version.split(".")) != 3:
                current_version += ".0"

            last_update_info = search_plugin(
                plugin_name,
                get_latest_version_str = True
            ).split(";v=")
            if len(last_update_info) <= 1:
                click.echo(
                    ERR + "Couldn't look for new versions " +
                    "(perhaps the plugin isn't available on the Godot " +
                    "Asset Library anymore)"
                )
                print(last_update_info)
                outdated_plugins += 1
                continue

            latest_version = last_update_info[1]
            if latest_version == current_version:
                click.echo(OK + "It's up-to-date.")
                continue

            click.echo(
                INFO + "New version found (%s), installing it..." %
                (latest_version)
            )
            outdated_plugins += 1
            plugin_dir = os.path.join(
                goo_root(), "addons", plugin_name.replace("/", "_", 1)
            )
            tmp_plugin_dir = os.path.join(
                goo_root(), "addons", "." + plugin_name.replace("/", "_", 1)
            )
            shutil.move(plugin_dir, tmp_plugin_dir)
            if not install_from_assetlib(plugin_name, latest_version):
                click.echo(ERR + "Couldn't update.")
                shutil.move(tmp_plugin_dir, plugin_dir)
            else:
                shutil.rmtree(tmp_plugin_dir)
                click.echo(OK + "Successfully updated.")
                successful_updates += 1
    click.echo("---")
    if not outdated_plugins:
        click.echo(OK + "Everything is up-to-date.")
    else:
        if outdated_plugins == successful_updates:
            click.echo(OK + "Outdated dependencies successfully updated.")
        else:
            click.echo(
                ERR + "Some dependencies couldn't be updated. " +
                "Successful updates: %d/%d" % (
                    successful_updates, outdated_plugins
                )
            )
            exit(1)
    if not_installed:
        click.echo(WARN + "Some dependencies are not installed yet.")
        click.echo(
            INFO + "Tip: Run 'goo install' to install all the missing" +
            "dependencies."
        )


@cli.command(
    "uninstall",
    help = "Uninstall a plugin and remove the dependency on it."
)
@click.argument("plugin_name")
@click.option(
    "--force-dependency-removal/--dont-force-dependency-removal",
    "-f/",
    default = False,
    help = "Remove the dependency even if it's not installed."
)
def uninstall(plugin_name, force_dependency_removal):
    root = goo_root()
    if root == "":
        click.echo(ERR + "Goo is not initialized yet.")
        exit(1)
    
    plugin_dir = os.path.join(
        goo_root(),
        "addons",
        plugin_name.replace("/", "_", 1)
    )
    repo_dir = os.path.join(
        goo_root(),
        "addons",
        ".%s-repo" % (plugin_name.replace("/", "_", 1))
    )
    if os.path.isdir(plugin_dir):
        click.echo(INFO + "Uninstalling \"%s\"..." % (plugin_name)) 
        shutil.rmtree(plugin_dir)
        if os.path.isdir(repo_dir):
            shutil.rmtree(repo_dir)
    else:
        if not force_dependency_removal:
            click.echo(
                ERR + "The plugin \"%s\" is not installed." % (plugin_name)
            )
            exit(1)

    click.echo(INFO + "Removing dependency...")
    if not remove_dependency(plugin_name):
        exit(1)
    click.echo(OK + "Done.")

def install_from_git_repo(plugin_repo, branch):
    if plugin_repo[-1] == "/":
        plugin_repo = plugin_repo[:-1]
    repo_url_parts = plugin_repo.split("/")
    plugin_name = repo_url_parts[len(repo_url_parts) - 1].replace(".git", "")
    plugin_repo_dir = ".%s-repo" % (plugin_name)
    plugin_path = os.path.join(goo_root(), "addons", plugin_name)
    plugin_repo_path = os.path.join(goo_root(), "addons", plugin_repo_dir)

    click.echo(INFO + "Installing \"%s\" using Git..." % (plugin_name))
    if os.path.isdir(plugin_repo_path):
        click.echo(ERR + "The plugin is already installed.")
        return False

    try:
        if branch == "main|master":
            Repo.clone_from(plugin_repo, plugin_repo_path)
        else:
            Repo.clone_from(plugin_repo, plugin_repo_path, branch = branch)
    except:
        click.echo(
            ERR + "Couldn't install %s from the specified Git repo." % 
            (plugin_name)
        )
        return False
    
    click.echo(INFO + "Validating...")
    plugin_cfg_search = find_all_files("plugin.cfg", plugin_repo_path)
    if not len(plugin_cfg_search):
        click.echo(
            ERR + "The specified Git repo doesn't seem to be a Godot plugin."
        )
        shutil.rmtree(plugin_repo_path)
        return False
    elif len(plugin_cfg_search) > 1:
        click.echo(
            ERR + "The specified Git repo contains more than one plugin."
        )
        shutil.rmtree(plugin_repo_path)
        return False
    plugin_cfg_dir = os.path.dirname(
        plugin_cfg_search[0][plugin_cfg_search[0].find(
            plugin_repo_dir + "/"
        ) + (len(plugin_repo_dir) + 1):]
    )
    
    click.echo(INFO + "Copying files...")
    shutil.copytree(
        plugin_repo_path,
        plugin_path
    )
    
    click.echo(INFO + "Organizing plugin file tree...")
    organize_plugin_directory(plugin_path, plugin_cfg_dir)
    return True


def install_from_assetlib(plugin, version):
    click.echo(INFO + "Fetching plugin data...")
    plugin_download_url = search_plugin(plugin, plugin_version = version)
    cfg = get_goo_cfg()
    error_messages = {
        "not found": "Plugin \"%s\" not found." % (plugin),

        "not available": ("The plugin \"%s\" is not available for Godot %s\n" +
            INFO + "Tip: Use '*' to match any version number. Example: 3.*.*") %
            (plugin, cfg["godot-version"]),
        
        "version not available": ("The specified version of \"%s\" is not " +
            "available for Godot %s") % (plugin, cfg["godot-version"]),
        
        "version not found": "Version %s not found for the plugin \"%s\"" % (
            version, plugin),

        "too many plugins": "The downloaded zip file contains more than one " +
            "plugin.",
        
        "canceled by user": "Operation canceled by the user.",
            
        "extraction error": "Couldn't extract the plugin files " +
            "(perhaps the plugin is already installed)",

        "": "Unknown error.",
    }

    if not validators.url(plugin_download_url):
        error = plugin_download_url
        click.echo(ERR + error_messages[error])
        return False
    else:
        url_parts = plugin_download_url.split("/")
        fname = url_parts[len(url_parts) - 1]
        
        click.echo(INFO + "Downloading \"%s\"..." % (plugin))
        if not download_plugin_zip_file(plugin_download_url, fname):
            click.echo(ERR + "Couldn't get the plugin zip file.")
            return False
        
        plugin_path = os.path.join(
            goo_root(), "addons", plugin.replace("/", "_")
        )
        zip_file = os.path.join(tempfile.gettempdir(), fname)
        plugin_cfg_dir = ""
        
        click.echo(INFO + "Extracting files...")
        extraction_result = extract_plugin_zip_file(zip_file, plugin_path)
        if extraction_result.split(" ")[0] != "ok":
            click.echo(ERR + error_messages[extraction_result])
            return False
        plugin_cfg_dir = extraction_result[3:]

        click.echo(INFO + "Organizing plugin file tree...")
        organize_plugin_directory(plugin_path, plugin_cfg_dir)
    return True
    

def install_missing_dependencies():
    dependencies = get_goo_cfg()["dependencies"]
    missing_dependencies = 0
    failed_installations = 0
    
    for plugin_name, plugin_info in dependencies.items():
        click.echo(INFO + "Checking %s..." % (plugin_name))
        if os.path.isdir(os.path.join(
            goo_root(),
            "addons",
            plugin_name.replace("/", "_", 1)
        )):
            click.echo(OK + "Already installed.")
            continue
        
        click.echo(ERR + "Not installed yet, installing...")
        missing_dependencies += 1
        if len(plugin_info.split(";b=")) == 2:
            plugin_info_parts = plugin_info.split(";b=")
            plugin_repo_url = plugin_info_parts[0]
            branch = plugin_info_parts[1]
            if not install_from_git_repo(plugin_repo_url, branch):
                failed_installations += 1
        else:
            version = plugin_info
            if not install_from_assetlib(plugin_name, version):
                failed_installations += 1
            
    click.echo("---")
    if not missing_dependencies:
        click.echo(OK + "No missing dependencies.")
    else:
        if not failed_installations:
            click.echo(
                OK + "All the missing dependencies were successfully installed."
            )
        else:
            click.echo(ERR + "Some dependencies couldn't be installed.")
            click.echo(INFO + "Successful installations: %d/%d" % (
                missing_dependencies - failed_installations,
                missing_dependencies
            ))
            return False
    return True
        

def get_request(url, stream = False):
    try:
        response = requests.get(url, stream = stream)
    except KeyboardInterrupt:
        click.echo(ERR + "Operation canceled by the user.")
        exit(1)
    except:
        click.echo(
            ERR +
            "Connection error (perhaps you're installing plugins too fast " +
            "or you have no internet connection)"
        )
        exit(1)
    return response


def download_plugin_zip_file(plugin_download_url, fname):
    with open(os.path.join(tempfile.gettempdir(), fname), "wb") as f:
        response = get_request(plugin_download_url, True)
        if response.status_code != 200:
            return False
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
    return True


def extract_plugin_zip_file(zip_file, plugin_path):
    plugin_cfg_dir = ""
    with ZipFile(zip_file, "r") as z:
        file_list = z.namelist()
        is_valid_plugin = False
        for f in file_list:
            if os.path.basename(f) == "plugin.cfg":
                if is_valid_plugin:
                    return "too many plugins"
                else:
                    is_valid_plugin = True
                    plugin_cfg_dir = os.path.dirname(f)
        if not is_valid_plugin:
            if not click.confirm(
                WARN + "The downloaded zip file doesn't seem to contain " +
                "a Godot plugin.\n" +
                INFO + "Do you wish to continue with the installation " +
                "anyway?",
                default = False
            ):
                os.remove(zip_file)
                click.echo(ERR + "Operation canceled by the user.")
                return "canceled by user"
        try:
            os.mkdir(plugin_path)
            z.extractall(path = plugin_path)
            os.remove(zip_file)
        except:
            return "extraction error"
    return "ok " + plugin_cfg_dir


def organize_plugin_directory(plugin_path, plugin_cfg_dir):
    file_list = get_dir_files(plugin_path)
    ok_files = []
    for f in file_list:
        fname = os.path.basename(f)
        if (
            os.path.dirname(f) == plugin_cfg_dir or
            "license" in fname.lower() or
            "licence" in fname.lower() or
            "copying" in fname.lower() or
            "readme" in fname.lower() or
            "contributing" in fname.lower() or
            "contributors" in fname.lower() or
            "credits" in fname.lower()
        ):
            os.rename(
                os.path.join(plugin_path, f),
                os.path.join(plugin_path, fname)
            )
            ok_files.append(fname)
    for f in os.listdir(plugin_path):
        fpath = os.path.join(plugin_path, f)
        if not f in ok_files:
            if os.path.isdir(fpath):
                shutil.rmtree(fpath)
            else:
                os.remove(fpath)


def get_installed_version(plugin_name):
    plugin_dir_name = plugin_name.replace("/", "_", 1)
    plugin_cfg_file = os.path.join(
        goo_root(), "addons", plugin_dir_name, "plugin.cfg"
    )
    if not os.path.isfile(plugin_cfg_file):
        return ""

    config = ConfigParser()
    config.read(plugin_cfg_file)
    return config.get("plugin", "version").replace("\"", "")


def get_dir_files(path, parent_directories = ""):
    files = []
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            files.extend(get_dir_files(
                entry_path,
                os.path.join(parent_directories, entry)
            ))    
        files.append(os.path.join(parent_directories, entry))
    return files


def find_all_files(fname, path):
    result = []
    for root, dirs, files in os.walk(path):
        if fname in files:
            result.append(os.path.join(root, fname))
    return result


def search_plugin(plugin, **kwargs):
    plugin_version = kwargs.get("plugin_version", "*")
    get_latest_version_str = kwargs.get("get_latest_version_str", False)
    
    base_url = "https://godotengine.org/asset-library/asset"
    search_url = base_url + "?filter=%s&user=%s"
    versions_url = base_url + "/edit?asset=%s&status=new+accepted"
    if len(plugin.split("/")) != 2:
        return "not found"
    plugin_author = plugin.split("/")[0]
    plugin_name = plugin.split("/")[1]
    # plugin_search_result should be a link to a .zip file or an error (str)
    plugin_search_result = ""

    page_response = get_request(search_url % (plugin_name, plugin_author))
    if page_response.status_code != 200:
        return "not found"
   
    page = BeautifulSoup(page_response.content, "lxml")
    results = page.select("h4 a:first-child", href = True)

    if len(results) == 0:
        return "not found"
    for r in results:
        """
        we make sure plugin_name actually matches only one plugin on the
        Godot Asset Lib
        """
        if r.text != plugin_name:
            return "not found"
    """
    we just want the id of any release of the plugin so we can access the
    page that contains the list of versions
    """
    plugin_id = results[0]["href"].split("/asset-library/asset/")[1]

    versions_response = get_request(versions_url % (plugin_id))
    if versions_response.status_code != 200:
        return "not found"
    versions_page = BeautifulSoup(versions_response.content, "lxml")
    version_links = versions_page.select("h4 a:first-child", href = True)
    for v in version_links:
        info_response = get_request("https://godotengine.org" + v["href"])
        if info_response.status_code != 200:
            continue
        
        info_page = BeautifulSoup(info_response.content, "lxml")
        plugin_info = {}
        for row in info_page.find_all("tr"):
            columns = row.find_all("td")
            if len(columns) < 2:
                continue
            elif len(columns) == 2:
                plugin_info[columns[0].text.strip()] = columns[1].text.strip()
            else:
                plugin_info[columns[0].text.strip()] = columns[2].text.strip()
        
        if plugin_version == "*":
            if gd_version_ok(
                plugin_info["Godot version"].replace("Godot ", "")
            ):
                if not get_latest_version_str:
                    return plugin_info["Download Url (Computed)"]
                else:
                    return "%s;v=%s" % (
                        plugin_info["Download Url (Computed)"],
                        plugin_info["Version String"]
                    )
            else:
                plugin_search_result = "not available"
        else:
            if plugin_version == plugin_info["Version String"]:
                if gd_version_ok(
                    plugin_info["Godot version"].replace("Godot ", "")
                ):
                    return plugin_info["Download Url (Computed)"]
                else:
                    return "version not available"
            plugin_search_result = "version not found"
    return plugin_search_result


def gd_version_ok(version):
    cfg = get_goo_cfg()
    target_gdversion_digits = cfg["godot-version"].lower().split(".")
    version_digits = version.split(".")
    if (
        len(target_gdversion_digits) != 3 and
        len(target_gdversion_digits) != 2
    ):
        return False
    if len(target_gdversion_digits) == 2:
        target_gdversion_digits.append("0")
    if len(version_digits) == 2:
        version_digits.append("0")
    return (target_gdversion_digits[0] == "*" or \
        target_gdversion_digits[0] == version_digits[0]) and \
        (target_gdversion_digits[1] == "*" or \
        target_gdversion_digits[1] == version_digits[1]) and \
        (target_gdversion_digits[2] == "*" or \
        target_gdversion_digits[2] == version_digits[2])


def get_goo_cfg():
    goo_cfg = {}
    try:
        with open(os.path.join(goo_root(), "goo.json"), "r") as f:
            goo_cfg = json.loads(f.read())
    except:
        click.echo(ERR + "Invalid goo.json file.")
        exit(1)
    return goo_cfg


def add_dependency(plugin_name_or_url, installed_from_git, version, branch):
    if not os.path.isfile(os.path.join(goo_root(), "goo.json")):
        click.echo(ERR + "goo.json doesn't exist (is goo initialized?)")
        return False
    
    cfg = get_goo_cfg()
    if not installed_from_git:
        plugin_identifier = plugin_name_or_url
    else:
        aux = plugin_name_or_url.split("/")
        plugin_identifier = aux[len(aux) - 1]
        if plugin_identifier[-4:] == ".git":
            plugin_identifier = plugin_identifier[:len(plugin_identifier) - 4]

    cfg["dependencies"][plugin_identifier] = \
        version if not installed_from_git else "%s;b=%s" % (
            plugin_name_or_url, branch
        )
    try:
        with open(os.path.join(goo_root(), "goo.json"), "w") as f:
            f.write(json.dumps(cfg, indent = 2))
    except:
        click.echo(
            ERR + "Couldn't add the dependency (can't open goo.json)"
        )
        return False
    return True


def remove_dependency(plugin_name):
    if not os.path.isfile(os.path.join(goo_root(), "goo.json")):
        click.echo(ERR + "goo.json doesn't exist (is goo initialized?)")
        return False
    
    cfg = get_goo_cfg()
    dependency_exists = False
    if plugin_name in cfg["dependencies"].keys():
        del cfg["dependencies"][plugin_name]
        dependency_exists = True
    if plugin_name.replace("_", "/", 1) in cfg["dependencies"].keys():
        del cfg["dependencies"][plugin_name.replace("_", "/", 1)]
        dependency_exists = True
    if not dependency_exists:
        click.echo(ERR + "\"%s\" is not a dependency." % (plugin_name))
        return False

    try:
        with open(os.path.join(goo_root(), "goo.json"), "w") as f:
            f.write(json.dumps(cfg, indent = 2))
    except:
        click.echo(
            ERR + "Couldn't remove the dependency (can't open goo.json)"
        )
        return False
    return True


if __name__ == "__main__":
    cli()


def __main__():
    cli()

