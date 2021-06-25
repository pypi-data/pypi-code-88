# from dataclasses import dataclass

from common_client_scheduler import TeralityError


class TeralityNetworkError(TeralityError):
    pass


class TeralityDataUploadError(TeralityError):
    pass


class TeralityDataDownloadError(TeralityError):
    pass
