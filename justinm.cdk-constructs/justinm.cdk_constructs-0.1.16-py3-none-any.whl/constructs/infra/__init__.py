import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import aws_cdk.aws_ec2
import aws_cdk.core


class AwsVpc(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.infra.AwsVpc",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cidr: builtins.str,
        enable_nat_gateway: typing.Optional[builtins.bool] = None,
        max_axs: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cidr: -
        :param enable_nat_gateway: -
        :param max_axs: -
        '''
        props = AwsVpcProps(
            cidr=cidr, enable_nat_gateway=enable_nat_gateway, max_axs=max_axs
        )

        jsii.create(AwsVpc, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.Vpc:
        return typing.cast(aws_cdk.aws_ec2.Vpc, jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@justinm/cdk-constructs.infra.AwsVpcProps",
    jsii_struct_bases=[],
    name_mapping={
        "cidr": "cidr",
        "enable_nat_gateway": "enableNatGateway",
        "max_axs": "maxAxs",
    },
)
class AwsVpcProps:
    def __init__(
        self,
        *,
        cidr: builtins.str,
        enable_nat_gateway: typing.Optional[builtins.bool] = None,
        max_axs: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cidr: -
        :param enable_nat_gateway: -
        :param max_axs: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cidr": cidr,
        }
        if enable_nat_gateway is not None:
            self._values["enable_nat_gateway"] = enable_nat_gateway
        if max_axs is not None:
            self._values["max_axs"] = max_axs

    @builtins.property
    def cidr(self) -> builtins.str:
        result = self._values.get("cidr")
        assert result is not None, "Required property 'cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_nat_gateway(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("enable_nat_gateway")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def max_axs(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("max_axs")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsVpcProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsVpc",
    "AwsVpcProps",
]

publication.publish()
