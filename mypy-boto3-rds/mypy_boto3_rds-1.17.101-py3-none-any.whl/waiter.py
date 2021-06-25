"""
Type annotations for rds service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rds import RDSClient
    from mypy_boto3_rds.waiter import (
        DBClusterSnapshotAvailableWaiter,
        DBClusterSnapshotDeletedWaiter,
        DBInstanceAvailableWaiter,
        DBInstanceDeletedWaiter,
        DBSnapshotAvailableWaiter,
        DBSnapshotCompletedWaiter,
        DBSnapshotDeletedWaiter,
    )

    client: RDSClient = boto3.client("rds")

    db_cluster_snapshot_available_waiter: DBClusterSnapshotAvailableWaiter = client.get_waiter("db_cluster_snapshot_available")
    db_cluster_snapshot_deleted_waiter: DBClusterSnapshotDeletedWaiter = client.get_waiter("db_cluster_snapshot_deleted")
    db_instance_available_waiter: DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
    db_instance_deleted_waiter: DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")
    db_snapshot_available_waiter: DBSnapshotAvailableWaiter = client.get_waiter("db_snapshot_available")
    db_snapshot_completed_waiter: DBSnapshotCompletedWaiter = client.get_waiter("db_snapshot_completed")
    db_snapshot_deleted_waiter: DBSnapshotDeletedWaiter = client.get_waiter("db_snapshot_deleted")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = (
    "DBClusterSnapshotAvailableWaiter",
    "DBClusterSnapshotDeletedWaiter",
    "DBInstanceAvailableWaiter",
    "DBInstanceDeletedWaiter",
    "DBSnapshotAvailableWaiter",
    "DBSnapshotCompletedWaiter",
    "DBSnapshotDeletedWaiter",
)


class DBClusterSnapshotAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbclustersnapshotavailablewaiter)
    """

    def wait(
        self,
        *,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotAvailableWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbclustersnapshotavailable)
        """


class DBClusterSnapshotDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_cluster_snapshot_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbclustersnapshotdeletedwaiter)
    """

    def wait(
        self,
        *,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBClusterSnapshotDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbclustersnapshotdeleted)
        """


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_instance_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbinstanceavailablewaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBInstanceAvailableWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbinstanceavailable)
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_instance_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbinstancedeletedwaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBInstanceDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbinstancedeleted)
        """


class DBSnapshotAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_snapshot_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotavailablewaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBSnapshotAvailableWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotavailable)
        """


class DBSnapshotCompletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_snapshot_completed)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotcompletedwaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBSnapshotCompletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotcompleted)
        """


class DBSnapshotDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.db_snapshot_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotdeletedwaiter)
    """

    def wait(
        self,
        *,
        DBInstanceIdentifier: str = None,
        DBSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
        DbiResourceId: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/rds.html#RDS.Waiter.DBSnapshotDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/waiters.html#dbsnapshotdeleted)
        """
