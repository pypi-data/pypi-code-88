from curvenote.models import (
    ArticleVersionPost,
    BlockChild,
    BlockFormat,
    BlockKind,
    BlockPost,
    ContentVersionPost,
)
import logging
import os
import sys
import subprocess
import typer

from .version import __version__
from .client import Session
from .latex.project import LatexProject

app = typer.Typer()

logger = logging.getLogger()


def version_callback(value: bool):
    if value:
        typer.echo(
            r"""
   ______                                  __
  / ____/_  ________   _____  ____  ____  / /____
 / /   / / / / ___/ | / / _ \/ __ \/ __ \/ __/ _ \
/ /___/ /_/ / /   | |/ /  __/ / / / /_/ / /_/  __/
\____/\__,_/_/    |___/\___/_/ /_/\____/\__/\___/
        """
        )
        typer.echo(f"Curvenote CLI Version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    )
):
    return


@app.command()
def get_me(
    token: str = typer.Argument(
        ..., envvar="CURVENOTE_TOKEN", help="API token generated from curvenote.com"
    )
):
    session = Session(token)
    typer.echo(session.user().json(indent=4))


@app.command()
def get_my_projects(
    token: str = typer.Argument(
        ..., envvar="CURVENOTE_TOKEN", help="API token generated from curvenote.com"
    )
):
    session = Session(token)
    for project in session.my_projects():
        typer.echo(project.json(indent=4))


@app.command()
def push(
    path: str = typer.Argument(..., help="Local file or folder to push to curvenote."),
    project: str = typer.Argument(
        ...,
        help=(
            "Identifier of target Project. PROJECT may match title, name, or id "
            "of an existing Project. If no existing Project is found, a new "
            "Project will be created with title PROJECT."
        ),
    ),
    article: str = typer.Option(
        None,
        help=(
            "Identifier of target Article. ARTICLE may match title, name, or id "
            "of an existing Article. If no existing Article is found, a new "
            "Article will be created with title ARTICLE. ARTICLE is ignored if "
            "PATH is a folder. If PATH is a folder or ARTICLE is not provided, "
            "filename will be used for Article."
        ),
    ),
    team: str = typer.Option(
        None,
        help=(
            "Team to use when creating a new Project. TEAM is ignored if PROJECT "
            "already exists. If PROJECT does not exist and TEAM is not provided, "
            "the new Project will be created under the current user."
        ),
    ),
    token: str = typer.Argument(
        ..., envvar="CURVENOTE_TOKEN", help="API token generated from curvenote.com"
    ),
):
    """Push contents of local file or folder to curvenote Project"""
    if not os.path.exists(path):
        raise ValueError(f"path not found: {path}")
    session = Session(token)

    typer.echo("Checking for project access")
    project_obj = session.get_or_create_project(
        title=project,
        team=team,
    )
    if os.path.isdir(path):
        typer.echo("pushing from folder")
        session.documents_from_folder(folder=path, project=project_obj)
    elif os.path.isfile(path):
        _, file_extension = os.path.splitext(path)
        if file_extension == ".ipynb":
            typer.echo("pushing notebook file...")
            session.notebook_from_file(
                filename=path, project=project_obj, title=article
            )
        elif file_extension == ".md":
            typer.echo("pushing markdown file...")
            session.article_from_file(filename=path, project=project_obj, title=article)
        else:
            raise ValueError(f"unsupported file type: {file_extension}")
    else:
        raise ValueError(f"unable to resolve path: {path}")


@app.command()
def pull_as_latex(
    target: str = typer.Argument(
        ...,
        help=(
            "Local folder in which to construct the Latex assets. If TARGET exists it"
            "and all files will be removed and a new empty folder structure created"
        ),
    ),
    project: str = typer.Argument(
        ...,
        help=(
            "Identifier of existing Project containing ARTICLE. PROJECT may match title,"
            " name, or id of an existing Project. If no existing Project is found, an "
            "error will be raised"
        ),
    ),
    article: str = typer.Argument(
        ...,
        help=(
            "Identifier of existing Article. ARTICLE may match title, name, or id "
            "of an existing Article. If no existing Article is found, an error will"
            "be raised."
        ),
    ),
    token: str = typer.Argument(
        ..., envvar="CURVENOTE_TOKEN", help="API token generated from curvenote.com"
    ),
    version: int = typer.Option(
        None,
        help=(
            "Version of the article to pull, if not specified will pull the latest version."
        ),
    ),
):
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    session = Session(token)

    try:
        project_obj = session.get_project(project)
    except ValueError as err:
        typer.echo(f"Could not find project: {project} or you do not have access")
        raise typer.Exit(code=1) from err

    typer.echo(f"Found project: {project_obj.name}")

    try:
        LatexProject.build_single_article(
            session, target, project_obj, article, version
        )
    except ValueError as err:
        typer.echo(err)
        raise typer.Exit(code=1)


@app.command()
def build_pdf(
    target: str = typer.Argument(
        ...,
        help=(
            "Local folder containing the local LaTeX project."
            "Must contain an index.tex file."
        ),
    ),
):
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    typer.echo("Build PDF from LaTeX")
    typer.echo(f"Target folder: {target}")
    typer.echo("Invoking xelatex...")
    try:
        XELATEX_CMD=f'cd {target}; latexmk -f -xelatex -synctex=1 -interaction=nonstopmode -file-line-error -latexoption="-shell-escape" index.tex'
        ret_val = subprocess.run(XELATEX_CMD, shell=True)
        if ret_val.returncode != 0:
            typer.echo(f"mklatex returned with a non zero error code, but thePDF was still created")
            typer.Exit(code=1)
    except ValueError as err:
        typer.echo(f"Fatal error while running mklatex")
        typer.Exit(code=1)

    typer.echo(f"mklatex reports success!")
    typer.Exit(code=0)


@app.command()
def clone_content(
    project: str = typer.Argument(
        ...,
        help=(
            "Identifier of existing Project containing ARTICLE. PROJECT may match title,"
            " name, or id of an existing Project. If no existing Project is found, an "
            "error will be raised"
        ),
    ),
    article: str = typer.Argument(
        ...,
        help=(
            "Identifier of existing Article. ARTICLE may match title, name, or id "
            "of an existing Article. If no existing Article is found, an error will"
            "be raised."
        ),
    ),
    new_article_name: str = typer.Argument(
        ...,
        help=(
            "Title of the new article to be created with cloned content."
            "If an article with the same name is found, an error will be raised."
        ),
    ),
    token: str = typer.Argument(
        ..., envvar="CURVENOTE_TOKEN", help="API token generated from curvenote.com"
    ),
    version: int = typer.Option(
        None,
        help=(
            "Version of the article to pull, if not specified will pull the latest version."
        ),
    ),
):
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    session = Session(token)

    typer.echo("Checking for project access")
    try:
        project_obj = session.get_project(project)
    except ValueError as err:
        typer.echo(f"Unable to access project {project}")
        typer.Exit(code=1)

    typer.echo("Fetching existing article block")
    try:
        block = session.get_block(project_obj, article, BlockKind.article)
    except ValueError as err:
        typer.echo(f"Unable to access article {article}")
        typer.Exit(code=1)

    version = int(version) if version is not None else block.latest_version
    typer.echo("Fetching existing article version")
    try:
        version = session.get_version(block, version)
    except ValueError as err:
        typer.echo(f"Unable to get article version {version}")
        typer.echo(str(err))
        typer.Exit(code=1)

    new_order = []
    new_children = {}

    for o in version.order:
        child = version.children[o]
        try:
            child_block = session.get_block(project_obj, child.src.block)
        except ValueError as err:
            typer.echo(f"Unable to access child, skipping {child.src}")
            continue

        if child_block.kind != BlockKind.content:
            typer.echo(f"Found {child_block.kind} block, referencing")
            new_order.append(child.id)
            new_children[child.id] = child
        else:
            typer.echo("Found content block, cloning")
            child_version = session.get_version(child_block, child.src.version)
            new_child_block = session.upload_block(
                BlockPost(kind=child_block.kind), project=project_obj
            )
            new_child_version = session.upload_version(
                version=ContentVersionPost(content=child_version.content),
                block=new_child_block,
            )
            new_order.append(child.id)
            new_children[child.id] = BlockChild(id=child.id, src=new_child_version.id)

    typer.echo(f"Existing article had {len(version.order)} children")
    typer.echo(f"Cloned article will have {len(new_order)} children")

    typer.echo(f"Creating new article")
    try:
        new_article_block = session.upload_block(
            BlockPost(name=new_article_name, kind=BlockKind.article),
            project=project_obj,
        )
    except ValueError as err:
        typer.echo("Could not create new article block")
        typer.echo(str(err))
        typer.Exit(code=1)

    try:
        session.upload_version(
            version=ArticleVersionPost(
                order=new_order,
                children=new_children,
                title=new_article_name,
            ),
            block=new_article_block,
        )
    except ValueError as err:
        typer.echo("Could not create new article version")
        typer.echo(str(err))
        typer.Exit(code=1)

    typer.echo(f"New article created: {new_article_name}")
