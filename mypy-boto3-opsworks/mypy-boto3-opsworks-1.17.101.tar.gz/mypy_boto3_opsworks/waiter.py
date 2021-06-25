"""
Type annotations for opsworks service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworks import OpsWorksClient
    from mypy_boto3_opsworks.waiter import (
        AppExistsWaiter,
        DeploymentSuccessfulWaiter,
        InstanceOnlineWaiter,
        InstanceRegisteredWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
    )

    client: OpsWorksClient = boto3.client("opsworks")

    app_exists_waiter: AppExistsWaiter = client.get_waiter("app_exists")
    deployment_successful_waiter: DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
    instance_online_waiter: InstanceOnlineWaiter = client.get_waiter("instance_online")
    instance_registered_waiter: InstanceRegisteredWaiter = client.get_waiter("instance_registered")
    instance_stopped_waiter: InstanceStoppedWaiter = client.get_waiter("instance_stopped")
    instance_terminated_waiter: InstanceTerminatedWaiter = client.get_waiter("instance_terminated")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)


class AppExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.app_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#appexistswaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.AppExistsWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#appexists)
        """


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.deployment_successful)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#deploymentsuccessfulwaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.DeploymentSuccessfulWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#deploymentsuccessful)
        """


class InstanceOnlineWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.instance_online)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceonlinewaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.InstanceOnlineWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceonline)
        """


class InstanceRegisteredWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.instance_registered)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceregisteredwaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.InstanceRegisteredWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceregistered)
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.instance_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instancestoppedwaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.InstanceStoppedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instancestopped)
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.instance_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceterminatedwaiter)
    """

    def wait(
        self,
        *,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/opsworks.html#OpsWorks.Waiter.InstanceTerminatedWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceterminated)
        """
