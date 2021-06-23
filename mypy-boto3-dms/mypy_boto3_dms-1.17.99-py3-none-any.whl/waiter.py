"""
Type annotations for dms service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_dms import DatabaseMigrationServiceClient
    from mypy_boto3_dms.waiter import (
        EndpointDeletedWaiter,
        ReplicationInstanceAvailableWaiter,
        ReplicationInstanceDeletedWaiter,
        ReplicationTaskDeletedWaiter,
        ReplicationTaskReadyWaiter,
        ReplicationTaskRunningWaiter,
        ReplicationTaskStoppedWaiter,
        TestConnectionSucceedsWaiter,
    )

    client: DatabaseMigrationServiceClient = boto3.client("dms")

    endpoint_deleted_waiter: EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
    replication_instance_available_waiter: ReplicationInstanceAvailableWaiter = client.get_waiter("replication_instance_available")
    replication_instance_deleted_waiter: ReplicationInstanceDeletedWaiter = client.get_waiter("replication_instance_deleted")
    replication_task_deleted_waiter: ReplicationTaskDeletedWaiter = client.get_waiter("replication_task_deleted")
    replication_task_ready_waiter: ReplicationTaskReadyWaiter = client.get_waiter("replication_task_ready")
    replication_task_running_waiter: ReplicationTaskRunningWaiter = client.get_waiter("replication_task_running")
    replication_task_stopped_waiter: ReplicationTaskStoppedWaiter = client.get_waiter("replication_task_stopped")
    test_connection_succeeds_waiter: TestConnectionSucceedsWaiter = client.get_waiter("test_connection_succeeds")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import FilterTypeDef, WaiterConfigTypeDef

__all__ = (
    "EndpointDeletedWaiter",
    "ReplicationInstanceAvailableWaiter",
    "ReplicationInstanceDeletedWaiter",
    "ReplicationTaskDeletedWaiter",
    "ReplicationTaskReadyWaiter",
    "ReplicationTaskRunningWaiter",
    "ReplicationTaskStoppedWaiter",
    "TestConnectionSucceedsWaiter",
)


class EndpointDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.endpoint_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#endpointdeletedwaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#endpointdeleted)
        """


class ReplicationInstanceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_instance_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstanceavailablewaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailableWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstanceavailable)
        """


class ReplicationInstanceDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_instance_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstancedeletedwaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstancedeleted)
        """


class ReplicationTaskDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskdeletedwaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeletedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskdeleted)
        """


class ReplicationTaskReadyWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_ready)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskreadywaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReadyWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskready)
        """


class ReplicationTaskRunningWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskrunningwaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunningWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskrunning)
        """


class ReplicationTaskStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.replication_task_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskstoppedwaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStoppedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskstopped)
        """


class TestConnectionSucceedsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.test_connection_succeeds)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#testconnectionsucceedswaiter)
    """

    def wait(
        self,
        *,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceedsWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#testconnectionsucceeds)
        """
