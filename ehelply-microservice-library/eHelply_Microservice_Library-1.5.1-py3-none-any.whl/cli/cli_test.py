from typing import List
import typer
import pytest
from pytest import ExitCode
import os
from pathlib import Path
import coverage

cli = typer.Typer()


# https://docs.pytest.org/en/documentation-restructure/how-to/writing_plugins.html#well-specified-hooks
class eHelplyPytest:
    pass
    # def pytest_sessionfinish(self):
    #     print("", "*** starting coverage report ***")


COVERAGE_THRESHOLD: int = 70


@cli.command()
def units(

):
    # Run DB migrations or unit tests for features relying on DB migrations will fail
    #   Thus, failing prod build/deploys
    typer.echo("Running Migrations..")
    from alembic.config import Config
    import alembic.command

    config = Config('alembic.ini')
    config.attributes['configure_logger'] = False

    alembic.command.upgrade(config, 'head')

    # Run unit tests

    root_path = Path(os.getcwd())

    docs_location = Path(root_path).resolve().joinpath('test-results')
    docs_location.mkdir(exist_ok=True)

    result: ExitCode = pytest.main(
        [
            "-s",
            "-v",
            # "--cov-report", "term-missing",
            "--cov-report", f"html:{str(docs_location)}",
            "--cov=src",
            "tests/"
        ]
    )

    if result != ExitCode.OK:
        raise typer.Exit(code=result)

    cov = coverage.Coverage()
    cov.load()

    omit: List[str] = [
        "src/example/*",
        "src/db/alembic/*",
        "src/db/*schema*.py",
        "src/db/*model*.py",
        "src/*seeders*",
        "src/service_meta.py",
        "src/service_template/*",
        "src/db/__init__.py",
        "src/service.py"
    ]

    # coverage_amount: float = cov.json_report(
    #     omit=omit
    # )

    coverage_amount: float = cov.report(
        show_missing=True,
        omit=omit
    )

    if coverage_amount < COVERAGE_THRESHOLD:
        raise Exception(
            f"Test coverage is {int(coverage_amount)}% which is below {COVERAGE_THRESHOLD}%. Thus, build has failed.")
