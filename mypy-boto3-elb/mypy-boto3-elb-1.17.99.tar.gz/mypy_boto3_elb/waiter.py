"""
Type annotations for elb service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_elb import ElasticLoadBalancingClient
    from mypy_boto3_elb.waiter import (
        AnyInstanceInServiceWaiter,
        InstanceDeregisteredWaiter,
        InstanceInServiceWaiter,
    )

    client: ElasticLoadBalancingClient = boto3.client("elb")

    any_instance_in_service_waiter: AnyInstanceInServiceWaiter = client.get_waiter("any_instance_in_service")
    instance_deregistered_waiter: InstanceDeregisteredWaiter = client.get_waiter("instance_deregistered")
    instance_in_service_waiter: InstanceInServiceWaiter = client.get_waiter("instance_in_service")
    ```
"""
from typing import List

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import InstanceTypeDef, WaiterConfigTypeDef

__all__ = ("AnyInstanceInServiceWaiter", "InstanceDeregisteredWaiter", "InstanceInServiceWaiter")


class AnyInstanceInServiceWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.any_instance_in_service)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#anyinstanceinservicewaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.AnyInstanceInServiceWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#anyinstanceinservice)
        """


class InstanceDeregisteredWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.instance_deregistered)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#instancederegisteredwaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceDeregisteredWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#instancederegistered)
        """


class InstanceInServiceWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.instance_in_service)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#instanceinservicewaiter)
    """

    def wait(
        self,
        *,
        LoadBalancerName: str,
        Instances: List["InstanceTypeDef"] = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.99/reference/services/elb.html#ElasticLoadBalancing.Waiter.InstanceInServiceWaiter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/waiters.html#instanceinservice)
        """
