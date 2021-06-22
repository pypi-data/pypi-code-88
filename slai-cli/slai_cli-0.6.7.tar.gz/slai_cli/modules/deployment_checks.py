from slai_cli import log
from slai_cli import constants


def _install_requirement_interactively(*, model_name, docker_client, requirement):
    exit_code = docker_client.install_requirement(
        model_name=model_name, requirement=requirement
    )
    if exit_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.warn(f"Failed to install: {requirement}")


def _check_handler_imports(*, model_name, model_version, docker_client):
    exit_code = docker_client.check_handler_imports(
        model_name=model_name, model_version=model_version
    )
    if exit_code == constants.REQUIREMENTS_RETURN_CODE_MISSING_DEP:
        if log.action_confirm(
            "Looks like a dependency is missing, would you like to add it interactively?"
        ):
            requirement = log.action_prompt(
                "Add python dependency (e.g. numpy==1.20.1): ",
                type=str,
            )

            return _install_requirement_interactively(
                model_name=model_name,
                docker_client=docker_client,
                requirement=requirement,
            )
        else:
            return constants.REQUIREMENTS_RETURN_CODE_EXIT

    elif exit_code == constants.REQUIREMENTS_RETURN_CODE_IMPORT_ERROR:
        log.warn("Trainer script failed due to import error.")
        return constants.REQUIREMENTS_RETURN_CODE_IMPORT_ERROR

    return constants.REQUIREMENTS_RETURN_CODE_SUCCESS


def check_handler_imports(*, model_name, model_version, docker_client):
    log.action("Checking if model handler imports are valid...")

    import_return_code = _check_handler_imports(
        model_name=model_name, model_version=model_version, docker_client=docker_client
    )
    while (
        import_return_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS
        and import_return_code != constants.REQUIREMENTS_RETURN_CODE_EXIT
    ):
        import_return_code = _check_handler_imports(
            model_name=model_name,
            model_version=model_version,
            docker_client=docker_client,
        )

    return import_return_code
