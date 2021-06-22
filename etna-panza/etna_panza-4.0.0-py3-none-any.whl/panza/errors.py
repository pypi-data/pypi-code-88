class JobError(Exception):
    """
    Base exception class for errors related to a job
    """


class BlueprintLoadError(Exception):
    """
    Exception class representing an error related to loading a blueprint
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot load blueprint: {str(self.__cause__)}"


class WorkspaceCreationError(JobError):
    """
    Exception class representing an error related to creating a workspace for a job
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        if isinstance(self.__cause__, OSError):
            return f"cannot create workspace: {self.__cause__.strerror}: {self.__cause__.filename}"
        else:
            return f"cannot create workspace: {str(self.__cause__)}"


class EnvironmentBuildError(JobError):
    """
    Exception class representing an error related to the construction of an environment
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot build environment: {str(self.__cause__)}"


class DataFetchingError(JobError):
    """
    Exception class representing an error related to the fetching of data needed by the job
    """

    def __init__(self, cause):
        self.__cause__ = cause

    def __str__(self):
        return f"cannot fetch data to analyze: {str(self.__cause__)}"


class JobExecutionError(JobError):
    """
    Exception class representing an error related to the execution of the job
    """


class InspectionError(JobExecutionError):
    """
    Exception class representing an error that happened during the execution of the inspection phase
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f"an error occurred when running the inspection phase: {self.message}"


class ResultLoadingError(JobExecutionError):
    """
    Exception class representing an error that happened during the loading of the result file
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        return f"an error occurred when loading the result file: {self.__cause__}"


class JobExecutionTimeout(JobExecutionError):
    """
    Exception class representing an error related to the timeout expiration of a job
    """

    def __init__(self, timeout: float):
        self.timeout = timeout

    def __str__(self):
        return f"job killed after the {self.timeout}-second timeout expired"


class JobExecutionBackendError(JobExecutionError):
    """
    Base exception class representing errors related to a backend
    """
