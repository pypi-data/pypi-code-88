class BadCredError(Exception):
    """
    Handles passing through bad credentials to Docker
    """

    def __init__(self, message="Credentials failed to authenticate."):
        super().__init__(message)


class DockerNotRunningError(Exception):
    """
    Handles trying to run RIO locally without Docker running
    """

    def __init__(self, message="Docker is not running!"):
        super().__init__(message)


class NoLocalFlagError(Exception):
    """
    Handles when local flag is not set

    ***SET TO BE DEPRECATED UPON RELEASING CLOUD SUPPORT THROUGH CLI***
    """

    def __init__(self, message="Please email contact@chainopt.com for remote deployment services."):
        super().__init__(message)


class LoggingError(Exception):
    """
    Handles when creation of logs has failed.
    """

    def __init__(self, message="Logs could not be generated. Please check your code and retry or contact support."):
        super().__init__(message)


class PackageDeletionError(Exception):
    """
    Handles when deleting a package has failed.
    """

    def __init__(self, message="Unable to delete package."):
        super().__init__(message)


class DuplicatePackageError(Exception):
    """
    Handles when a user attempts to deploy a package with a duplicate name
    and chooses not to overwrite the package with the new deployment.
    """

    def __init__(self, message="A package already exists with that name."):
        super().__init__(message)


class BadPortError(Exception):
    """
    Handles when a user inputs a port that cannot be used.
    """

    def __init__(self, message="Please try again and enter a port number between 1024 and 65535. You may also not "
                               "specify a port and it will be assigned automatically."):
        super().__init__(message)


class UploadAPIError(Exception):
    """
    Handles when the RIO upload API is non-responsive.
    """

    def __init__(self, message="Upload API unavailable!"):
        super().__init__(message)


class DeployAPIError(Exception):
    """
    Handles when the RIO deploy API is non-responsive.
    """

    def __init__(self, message="Deploy API unavailable!"):
        super().__init__(message)


class APIError(Exception):
    # TODO: Combine Upload and Deploy API errors into this singular error
    """
    Handles issues with the RIO-API backend.
    """

    def __init__(self, module="", message="API unavailable!"):
        if module:
            super().__init__(module + " " + message)
        else:
            super().__init__(message)


class PackagePathError(Exception):
    """
    Handles bad OS paths being input for deployments.
    """

    def __init__(self, message="Package not found. Please check name and try again."):
        super().__init__(message)


class PackageExistenceError(Exception):
    """
    Handles when a package name is given that does not exist in Docker/RIO-API
    """

    def __init__(self, package_name, message=" not found. Please check the package name and retry."):
        super().__init__(package_name + message)


class NoRunningPackagesError(Exception):
    """
    Handles when a request has been made but no packages are running.
    """

    def __init__(self, message="No running packages."):
        super().__init__(message)


class MissingPackageInputError(Exception):
    """
    Handles when a function that requires a package or --all gets neither input
    """

    def __init__(self, message="Please specify a package name or --all."):
        super().__init__(message)


class PackagingError(Exception):
    """
    Handles when creating a zipped version of the package fails
    """

    def __init__(self, message="Failed to create .zip version of package. Please check package name."):
        super().__init__(message)


class PackageStopError(Exception):
    """
    Handles when the API fails to stop a package
    """

    def __init__(self, package_name):
        message = f"Unable to stop {package_name} package. Please retry or report this as a bug."
        super().__init__()
