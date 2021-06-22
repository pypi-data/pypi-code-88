from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path

from checksumdir import dirhash

from grid.core.base import GridObject
from grid.sdk.record import Record


class StorageType(Enum):
    S3 = "s3"
    GIT = "git"


class SourceType(Enum):
    LOCAL = "local"
    GIT = "git"


class UploadStatus(Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"
    UPLOADING = "uploading"
    DELETED = "deleted"


@dataclass
class RepositoryRecord(Record):
    id: str
    name: str
    version: str
    cluster_id: str
    created_at: datetime
    deleted_at: datetime
    uploaded_at: datetime
    upload_status: UploadStatus
    source_type: SourceType
    storage_type: StorageType


class Repository(GridObject):
    """Represents local or remote source-code used for creating Runs."""
    format: SourceType = SourceType.LOCAL

    def __init__(self, identifier: str):
        self.identifier = identifier

    def refresh(self):
        pass

    def to_record(self):
        pass

    @staticmethod
    def checksum(path: Path):
        """
        Calculates the checksum of a local path.

        Parameters
        ----------
        path: Path
            Reference to a path.
        """
        # TODO: use excluded_files with a list of files that are excluded
        return dirhash(path, "md5")
