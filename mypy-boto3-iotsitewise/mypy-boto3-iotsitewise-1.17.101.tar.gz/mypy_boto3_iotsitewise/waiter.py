"""
Type annotations for iotsitewise service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iotsitewise import IoTSiteWiseClient
    from mypy_boto3_iotsitewise.waiter import (
        AssetActiveWaiter,
        AssetModelActiveWaiter,
        AssetModelNotExistsWaiter,
        AssetNotExistsWaiter,
        PortalActiveWaiter,
        PortalNotExistsWaiter,
    )

    client: IoTSiteWiseClient = boto3.client("iotsitewise")

    asset_active_waiter: AssetActiveWaiter = client.get_waiter("asset_active")
    asset_model_active_waiter: AssetModelActiveWaiter = client.get_waiter("asset_model_active")
    asset_model_not_exists_waiter: AssetModelNotExistsWaiter = client.get_waiter("asset_model_not_exists")
    asset_not_exists_waiter: AssetNotExistsWaiter = client.get_waiter("asset_not_exists")
    portal_active_waiter: PortalActiveWaiter = client.get_waiter("portal_active")
    portal_not_exists_waiter: PortalNotExistsWaiter = client.get_waiter("portal_not_exists")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "AssetActiveWaiter",
    "AssetModelActiveWaiter",
    "AssetModelNotExistsWaiter",
    "AssetNotExistsWaiter",
    "PortalActiveWaiter",
    "PortalNotExistsWaiter",
)


class AssetActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.asset_active)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetactivewaiter)
    """

    def wait(self, *, assetId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActiveWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetactive)
        """


class AssetModelActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.asset_model_active)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelactivewaiter)
    """

    def wait(self, *, assetModelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActiveWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelactive)
        """


class AssetModelNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.asset_model_not_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelnotexistswaiter)
    """

    def wait(self, *, assetModelId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExistsWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelnotexists)
        """


class AssetNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.asset_not_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetnotexistswaiter)
    """

    def wait(self, *, assetId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExistsWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetnotexists)
        """


class PortalActiveWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.portal_active)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalactivewaiter)
    """

    def wait(self, *, portalId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActiveWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalactive)
        """


class PortalNotExistsWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.portal_not_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalnotexistswaiter)
    """

    def wait(self, *, portalId: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.101/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExistsWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalnotexists)
        """
