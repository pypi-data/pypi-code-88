'''
# Welcome to cdk-vscode-fargate

`cdk-vscode-fargate` is a JSII construct library for AWS CDK that allows you to deploy [Code-server](https://github.com/orgs/linuxserver/packages/container/package/code-server) running VS Code remotely, on a AWS Fargate container.

By deploying the `VSCodeFargate` construct, the following resources will be created:

1. VPC (if not passed in as a prop)
2. ACM DNS validated certificate
3. ECS Cluster
4. EFS file system
5. ALB Fargate Service
6. Security Groups
7. Secrets Manager secret (for login authorization)

![diagram](./diagram.png)

## Howto

Create a new project with AWS CDK

```sh
$ mkdir my-vscode-fargate && cd my-vscode-fargate
# initialize the AWS CDK project
$ cdk init -l typescript
# install the cdk-vscode-fargate npm module
$ yarn add cdk-vscode-fargate
```

# AWS CDK sample

Building your serverless VS Code service with the `VSCodeFargate` construct:

Update `./lib/my-vscode-fargate-stack.ts`

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_ec2 as ec2
import aws_cdk.core as cdk
from cdk_vscode_fargate import VSCodeFargate

class CdkStack(cdk.Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting)

        subdomain = process.env.VSCODE_SUBDOMAIN ?? "vscode"
        domain_name = process.env.VSCODE_DOMAIN_NAME ?? "mydomain.com"

        vpc = ec2.Vpc.from_lookup(self, "Vpc",
            is_default=True
        )

        VSCodeFargate(self, "MyVSCodeFargate",
            domain_name=domain_name,
            subdomain=subdomain,
            vpc=vpc
        )
```

diff the CDK stack:

```sh
$ cdk deploy
```

deploy the CDK stack:

```sh
$ cdk diff
```

On deploy completion, the subdomain/domain name assigned to the load balancer will be returned in the Output. Click the URL and you will see the login page:

![vscode-fargate-login](./images/vscode-fargate-login.png)
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
import aws_cdk.aws_route53
import aws_cdk.core


class VSCodeFargate(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-vscode-fargate.VSCodeFargate",
):
    '''A construct that consists of an ECS Service and related infrastructure to host a VSCode instance using a container (defaults to ghcr.io/linuxserver/code-server). Data is persisted via an EFS volume.'''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        subdomain: builtins.str,
        container_image: typing.Optional[builtins.str] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain_name: A full domain to register the new endpoint in.
        :param subdomain: A subdomain for the new endpoint.
        :param container_image: An optional container image to use. If not provided, then 'ghcr.io/linuxserver/code-server' is used. Default: ghcr.io/linuxserver/code-server
        :param hosted_zone: An optional HostedZone to use. If not provided, then ``domainName`` is used to look one up using context
        :param vpc: An optional VPC to put ECS in. Default: default VPC from lookup
        '''
        props = VSCodeFargateProps(
            domain_name=domain_name,
            subdomain=subdomain,
            container_image=container_image,
            hosted_zone=hosted_zone,
            vpc=vpc,
        )

        jsii.create(VSCodeFargate, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))


@jsii.data_type(
    jsii_type="cdk-vscode-fargate.VSCodeFargateProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "subdomain": "subdomain",
        "container_image": "containerImage",
        "hosted_zone": "hostedZone",
        "vpc": "vpc",
    },
)
class VSCodeFargateProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        subdomain: builtins.str,
        container_image: typing.Optional[builtins.str] = None,
        hosted_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param domain_name: A full domain to register the new endpoint in.
        :param subdomain: A subdomain for the new endpoint.
        :param container_image: An optional container image to use. If not provided, then 'ghcr.io/linuxserver/code-server' is used. Default: ghcr.io/linuxserver/code-server
        :param hosted_zone: An optional HostedZone to use. If not provided, then ``domainName`` is used to look one up using context
        :param vpc: An optional VPC to put ECS in. Default: default VPC from lookup
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "subdomain": subdomain,
        }
        if container_image is not None:
            self._values["container_image"] = container_image
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''A full domain to register the new endpoint in.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            myprojects.com
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subdomain(self) -> builtins.str:
        '''A subdomain for the new endpoint.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            vscode
        '''
        result = self._values.get("subdomain")
        assert result is not None, "Required property 'subdomain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_image(self) -> typing.Optional[builtins.str]:
        '''An optional container image to use.

        If not provided, then 'ghcr.io/linuxserver/code-server' is used.

        :default: ghcr.io/linuxserver/code-server
        '''
        result = self._values.get("container_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone(self) -> typing.Optional[aws_cdk.aws_route53.IHostedZone]:
        '''An optional HostedZone to use.

        If not provided, then ``domainName`` is used to look one up using context

        :optional: true
        '''
        result = self._values.get("hosted_zone")
        return typing.cast(typing.Optional[aws_cdk.aws_route53.IHostedZone], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''An optional VPC to put ECS in.

        :default: default VPC from lookup
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VSCodeFargateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VSCodeFargate",
    "VSCodeFargateProps",
]

publication.publish()
