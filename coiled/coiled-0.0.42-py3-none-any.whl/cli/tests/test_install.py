import shutil

import coiled
import pytest
from click.testing import CliRunner
from coiled.cli.install import DEFAULT_PIP_PACKAGES, install, remote_name_to_local_name
from coiled.cli.utils import conda_command, parse_conda_command

if shutil.which("conda") is None:
    pytest.skip(
        "Conda is needed to create local software environments", allow_module_level=True
    )


def test_install_bad_name_raises(sample_user):
    bad_name = "not-a-software-environment"
    runner = CliRunner()
    result = runner.invoke(install, [bad_name])

    assert result.exit_code != 0
    err_msg = str(result.exception).lower()
    assert "could not find" in err_msg
    assert bad_name in err_msg


@pytest.mark.timeout(400)
@pytest.mark.test_group("bad-solve")
def test_install_bad_solve_raises_informative_message(
    sample_user, monkeypatch, docker_prune
):
    name = "my-env"
    coiled.create_software_environment(
        name=name,
        conda={"channels": ["conda-forge"], "dependencies": ["xgboost=1.1.1"]},
    )

    def mock_get_platform():
        return "windows"

    monkeypatch.setattr(coiled.cli.install, "get_platform", mock_get_platform)
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code != 0
    keywords = ["solved conda environment", name, "windows", "conda-forge", "xgboost"]
    assert all(i in str(result.exception) for i in keywords)


@pytest.mark.test_group("install-conda")
def test_install_conda(sample_user, docker_prune):
    name = "my-env"
    coiled.create_software_environment(name=name, conda=["toolz"])
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code == 0
    output = result.output.lower()
    assert "conda activate" in output
    assert name in output


@pytest.mark.test_group("test-install-pip")
def test_install_pip(sample_user, docker_prune):
    name = "my-env"
    coiled.create_software_environment(name=name, pip=["toolz"])
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code == 0

    local_name = remote_name_to_local_name(account=sample_user.user.username, name=name)
    cmd = [conda_command(), "run", "-n", local_name, "pip", "list", "--format=json"]
    output = parse_conda_command(cmd)
    assert any(i["name"] == "toolz" for i in output)


@pytest.mark.test_group("test_install_post_build")
def test_install_post_build(sample_user, docker_prune):
    name = "my-env"
    coiled.create_software_environment(
        name=name, conda=["toolz"], post_build=["export FOO=BARBAZ", "echo $FOO"]
    )
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code == 0
    assert "BARBAZ" in result.output


@pytest.mark.test_group("slow")
def test_install_defaults(sample_user, docker_prune):
    # Ensure default packages (e.g. ipython, coiled) are installed
    name = "my-env"
    coiled.create_software_environment(name=name, pip=["toolz"])
    runner = CliRunner()
    result = runner.invoke(install, [name])

    if result.exit_code != 0:
        if result.exc_info:
            raise result.exc_info[1].with_traceback(result.exc_info[2])
        else:
            raise ValueError("test_install_defaults failed, not sure why")

    local_name = remote_name_to_local_name(account=sample_user.user.username, name=name)
    cmd = [conda_command(), "run", "-n", local_name, "pip", "list", "--format=json"]
    output = parse_conda_command(cmd)
    for package in DEFAULT_PIP_PACKAGES:
        assert any(i["name"] == package for i in output)


@pytest.mark.test_group("veryslow")
def test_install_multiple(sample_user, docker_prune):
    name = "my-env"
    coiled.create_software_environment(
        name=name,
        conda=["toolz"],
        pip=["ipython"],
        post_build=["export FOO=BARBAZ", "echo $FOO"],
    )
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code == 0
    assert "BARBAZ" in result.output


@pytest.mark.test_group("veryslow")
def test_create_software_env_uppercase_name(sample_user, docker_prune):
    name = "my-ENV"
    coiled.create_software_environment(name=name, conda=["toolz"])
    runner = CliRunner()
    result = runner.invoke(install, [name])

    assert result.exit_code == 0
    assert "my-env" in result.output
