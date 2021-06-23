'''
[![NPM version](https://badge.fury.io/js/cdk-fargate-patterns.svg)](https://badge.fury.io/js/cdk-fargate-patterns)
[![PyPI version](https://badge.fury.io/py/cdk-fargate-patterns.svg)](https://badge.fury.io/py/cdk-fargate-patterns)
[![Release](https://github.com/pahud/cdk-fargate-patterns/actions/workflows/release.yml/badge.svg)](https://github.com/pahud/cdk-fargate-patterns/actions/workflows/release.yml)

# cdk-fargate-patterns

CDK patterns for serverless container with AWS Fargate

# `DualAlbFargateService`

Inspired by *Vijay Menon* from the [AWS blog post](https://aws.amazon.com/blogs/containers/how-to-use-multiple-load-balancer-target-group-support-for-amazon-ecs-to-access-internal-and-external-service-endpoint-using-the-same-dns-name/) introduced in 2019, `DualAlbFargateService` allows you to create one or many fargate services with both internet-facing ALB and internal ALB associated with all services. With this pattern, fargate services will be allowed to intercommunicat via internal ALB while external inbound traffic will be spread across the same service tasks through internet-facing ALB.

The sample below will create 3 fargate services associated with both external and internal ALBs. The internal ALB will have an alias(`internal.svc.local`) auto-configured from Route 53 so services can communite through the private ALB endpoint.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
DualAlbFargateService(stack, "Service",
    spot=True, # FARGATE_SPOT only cluster
    tasks=[{
        "listener_port": 80,
        "task": order_task,
        "desired_count": 2,
        # customize the service autoscaling policy
        "scaling_policy": {
            "max_capacity": 20,
            "request_per_target": 1000,
            "target_cpu_utilization": 50
        }
    }, {"listener_port": 8080, "task": customer_task, "desired_count": 2}, {"listener_port": 9090, "task": product_task, "desired_count": 2}
    ],
    route53_ops={
        "zone_name": zone_name, # svc.local
        "external_alb_record_name": external_alb_record_name, # external.svc.local
        "internal_alb_record_name": internal_alb_record_name
    }
)
```

## Fargate Spot Support

By enabling the `spot` property, 100% fargate spot tasks will be provisioned to help you save up to 70%. Check more details about [Fargate Spot](https://aws.amazon.com/about-aws/whats-new/2019/12/aws-launches-fargate-spot-save-up-to-70-for-fault-tolerant-applications/?nc1=h_ls). This is a handy catch-all flag to force all tasks to be `FARGATE_SPOT` only.

To specify mixed strategy with partial `FARGATE` and partial `FARGATE_SPOT`, specify the `capacityProviderStrategy` for individual tasks like

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
DualAlbFargateService(stack, "Service",
    tasks=[{
        "listener_port": 8080,
        "task": customer_task,
        "desired_count": 2,
        "capacity_provider_stretegy": [{
            "capacity_provider": "FARGATE",
            "base": 1,
            "weight": 1
        }, {
            "capacity_provider": "FARGATE_SPOT",
            "base": 0,
            "weight": 3
        }
        ]
    }
    ]
)
```

The custom capacity provider strategy will be applied if `capacityProviderStretegy` is specified, otherwise, 100% spot will be used when `spot: true`. The default policy is 100% Fargate on-demand.

## Sample Application

This repository comes with a sample applicaiton with 3 services in Golang. On deployment, the `Order` service will be exposed externally on external ALB port `80` and all requests to the `Order` service will trigger sub-requests internally to another other two services(`product` and `customer`) through the internal ALB and eventually aggregate the response back to the client.

![](images/DualAlbFargateService.svg)

## Deploy

To deploy the sample application in you default VPC:

```sh
// compile the ts to js
$ yarn build
$ npx cdk --app lib/integ.default.js -c use_default_vpc=1 diff
$ npx cdk --app lib/integ.default.js -c use_default_vpc=1 deploy
```

On deployment complete, you will see the external ALB endpoint in the CDK output. `cURL` the external HTTP endpoint and you should be able to see the aggregated response.

```sh
$ curl http://demo-Servi-EH1OINYDWDU9-1397122594.ap-northeast-1.elb.amazonaws.com

{"service":"order", "version":"1.0"}
{"service":"product","version":"1.0"}
{"service":"customer","version":"1.0"}
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.core


class DualAlbFargateService(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-fargate-patterns.DualAlbFargateService",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        tasks: typing.Sequence["FargateTaskProps"],
        route53_ops: typing.Optional["Route53Options"] = None,
        spot: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param tasks: 
        :param route53_ops: 
        :param spot: create a FARGATE_SPOT only cluster. Default: false
        :param vpc: 
        '''
        props = DualAlbFargateServiceProps(
            tasks=tasks, route53_ops=route53_ops, spot=spot, vpc=vpc
        )

        jsii.create(DualAlbFargateService, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="externalAlb")
    def external_alb(
        self,
    ) -> aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer:
        return typing.cast(aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer, jsii.get(self, "externalAlb"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="internalAlb")
    def internal_alb(
        self,
    ) -> aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer:
        return typing.cast(aws_cdk.aws_elasticloadbalancingv2.ApplicationLoadBalancer, jsii.get(self, "internalAlb"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        return typing.cast(aws_cdk.aws_ec2.IVpc, jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="cdk-fargate-patterns.DualAlbFargateServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "tasks": "tasks",
        "route53_ops": "route53Ops",
        "spot": "spot",
        "vpc": "vpc",
    },
)
class DualAlbFargateServiceProps:
    def __init__(
        self,
        *,
        tasks: typing.Sequence["FargateTaskProps"],
        route53_ops: typing.Optional["Route53Options"] = None,
        spot: typing.Optional[builtins.bool] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param tasks: 
        :param route53_ops: 
        :param spot: create a FARGATE_SPOT only cluster. Default: false
        :param vpc: 
        '''
        if isinstance(route53_ops, dict):
            route53_ops = Route53Options(**route53_ops)
        self._values: typing.Dict[str, typing.Any] = {
            "tasks": tasks,
        }
        if route53_ops is not None:
            self._values["route53_ops"] = route53_ops
        if spot is not None:
            self._values["spot"] = spot
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def tasks(self) -> typing.List["FargateTaskProps"]:
        result = self._values.get("tasks")
        assert result is not None, "Required property 'tasks' is missing"
        return typing.cast(typing.List["FargateTaskProps"], result)

    @builtins.property
    def route53_ops(self) -> typing.Optional["Route53Options"]:
        result = self._values.get("route53_ops")
        return typing.cast(typing.Optional["Route53Options"], result)

    @builtins.property
    def spot(self) -> typing.Optional[builtins.bool]:
        '''create a FARGATE_SPOT only cluster.

        :default: false
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DualAlbFargateServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-fargate-patterns.FargateTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "listener_port": "listenerPort",
        "task": "task",
        "capacity_provider_stretegy": "capacityProviderStretegy",
        "desired_count": "desiredCount",
        "scaling_policy": "scalingPolicy",
    },
)
class FargateTaskProps:
    def __init__(
        self,
        *,
        listener_port: jsii.Number,
        task: aws_cdk.aws_ecs.FargateTaskDefinition,
        capacity_provider_stretegy: typing.Optional[typing.Sequence[aws_cdk.aws_ecs.CapacityProviderStrategy]] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        scaling_policy: typing.Optional["ServiceScalingPolicy"] = None,
    ) -> None:
        '''
        :param listener_port: 
        :param task: 
        :param capacity_provider_stretegy: 
        :param desired_count: desired number of tasks for the service. Default: 1
        :param scaling_policy: service autoscaling policy.
        '''
        if isinstance(scaling_policy, dict):
            scaling_policy = ServiceScalingPolicy(**scaling_policy)
        self._values: typing.Dict[str, typing.Any] = {
            "listener_port": listener_port,
            "task": task,
        }
        if capacity_provider_stretegy is not None:
            self._values["capacity_provider_stretegy"] = capacity_provider_stretegy
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if scaling_policy is not None:
            self._values["scaling_policy"] = scaling_policy

    @builtins.property
    def listener_port(self) -> jsii.Number:
        result = self._values.get("listener_port")
        assert result is not None, "Required property 'listener_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def task(self) -> aws_cdk.aws_ecs.FargateTaskDefinition:
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(aws_cdk.aws_ecs.FargateTaskDefinition, result)

    @builtins.property
    def capacity_provider_stretegy(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ecs.CapacityProviderStrategy]]:
        result = self._values.get("capacity_provider_stretegy")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ecs.CapacityProviderStrategy]], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        '''desired number of tasks for the service.

        :default: 1
        '''
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def scaling_policy(self) -> typing.Optional["ServiceScalingPolicy"]:
        '''service autoscaling policy.'''
        result = self._values.get("scaling_policy")
        return typing.cast(typing.Optional["ServiceScalingPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-fargate-patterns.Route53Options",
    jsii_struct_bases=[],
    name_mapping={
        "external_alb_record_name": "externalAlbRecordName",
        "internal_alb_record_name": "internalAlbRecordName",
        "zone_name": "zoneName",
    },
)
class Route53Options:
    def __init__(
        self,
        *,
        external_alb_record_name: typing.Optional[builtins.str] = None,
        internal_alb_record_name: typing.Optional[builtins.str] = None,
        zone_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param external_alb_record_name: the external ALB record name. Default: external
        :param internal_alb_record_name: the internal ALB record name. Default: internal
        :param zone_name: private zone name. Default: svc.local
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if external_alb_record_name is not None:
            self._values["external_alb_record_name"] = external_alb_record_name
        if internal_alb_record_name is not None:
            self._values["internal_alb_record_name"] = internal_alb_record_name
        if zone_name is not None:
            self._values["zone_name"] = zone_name

    @builtins.property
    def external_alb_record_name(self) -> typing.Optional[builtins.str]:
        '''the external ALB record name.

        :default: external
        '''
        result = self._values.get("external_alb_record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_alb_record_name(self) -> typing.Optional[builtins.str]:
        '''the internal ALB record name.

        :default: internal
        '''
        result = self._values.get("internal_alb_record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_name(self) -> typing.Optional[builtins.str]:
        '''private zone name.

        :default: svc.local
        '''
        result = self._values.get("zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53Options(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-fargate-patterns.ServiceScalingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_capacity": "maxCapacity",
        "request_per_target": "requestPerTarget",
        "target_cpu_utilization": "targetCpuUtilization",
    },
)
class ServiceScalingPolicy:
    def __init__(
        self,
        *,
        max_capacity: typing.Optional[jsii.Number] = None,
        request_per_target: typing.Optional[jsii.Number] = None,
        target_cpu_utilization: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_capacity: max capacity for the service autoscaling. Default: 10
        :param request_per_target: request per target. Default: 1000
        :param target_cpu_utilization: target cpu utilization. Default: 50
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if request_per_target is not None:
            self._values["request_per_target"] = request_per_target
        if target_cpu_utilization is not None:
            self._values["target_cpu_utilization"] = target_cpu_utilization

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''max capacity for the service autoscaling.

        :default: 10
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def request_per_target(self) -> typing.Optional[jsii.Number]:
        '''request per target.

        :default: 1000
        '''
        result = self._values.get("request_per_target")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_cpu_utilization(self) -> typing.Optional[jsii.Number]:
        '''target cpu utilization.

        :default: 50
        '''
        result = self._values.get("target_cpu_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceScalingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DualAlbFargateService",
    "DualAlbFargateServiceProps",
    "FargateTaskProps",
    "Route53Options",
    "ServiceScalingPolicy",
]

publication.publish()
