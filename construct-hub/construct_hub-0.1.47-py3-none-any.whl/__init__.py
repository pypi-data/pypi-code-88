'''
# Construct Hub

This project maintains a [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) construct library
that can be used to deploy instances of the Construct Hub in any AWS Account.

## Development

The `test/devapp` directory includes an AWS CDK app designed for deploying the
construct hub into a development account. This app is also used as a golden
snapshot, so every time the construct changes, you'll see its snapshot updated.

To bootstrap your developer account, use the following command:

```shell
CDK_NEW_BOOTSTRAP=1 npx cdk bootstrap aws://ACCOUNT/REGION
```

Use the following tasks to work with the dev app. It will always work with the
currently configured CLI account/region:

* `yarn dev:synth` - synthesize into `test/devapp/cdk.out`
* `yarn dev:deploy` - deploy to the current environment
* `yarn dev:diff` - diff against the current environment

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more
information.

## License

This project is licensed under the Apache-2.0 License.
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_iam
import aws_cdk.aws_route53
import aws_cdk.aws_sqs
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="construct-hub.AlarmActions",
    jsii_struct_bases=[],
    name_mapping={
        "high_severity": "highSeverity",
        "normal_severity": "normalSeverity",
    },
)
class AlarmActions:
    def __init__(
        self,
        *,
        high_severity: builtins.str,
        normal_severity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) CloudWatch alarm actions to perform.

        :param high_severity: (experimental) The ARN of the CloudWatch alarm action to take for alarms of high-severity alarms. This must be an ARN that can be used with CloudWatch alarms.
        :param normal_severity: (experimental) The ARN of the CloudWatch alarm action to take for alarms of normal severity. This must be an ARN that can be used with CloudWatch alarms. Default: - no actions are taken in response to alarms of normal severity

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "high_severity": high_severity,
        }
        if normal_severity is not None:
            self._values["normal_severity"] = normal_severity

    @builtins.property
    def high_severity(self) -> builtins.str:
        '''(experimental) The ARN of the CloudWatch alarm action to take for alarms of high-severity alarms.

        This must be an ARN that can be used with CloudWatch alarms.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions
        :stability: experimental
        '''
        result = self._values.get("high_severity")
        assert result is not None, "Required property 'high_severity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def normal_severity(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ARN of the CloudWatch alarm action to take for alarms of normal severity.

        This must be an ARN that can be used with CloudWatch alarms.

        :default: - no actions are taken in response to alarms of normal severity

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions
        :stability: experimental
        '''
        result = self._values.get("normal_severity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_iam.IGrantable)
class ConstructHub(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="construct-hub.ConstructHub",
):
    '''(experimental) Construct Hub.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        alarm_actions: AlarmActions,
        dashboard_name: typing.Optional[builtins.str] = None,
        domain: typing.Optional["Domain"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alarm_actions: (experimental) Actions to perform when alarms are set.
        :param dashboard_name: (experimental) The name of the CloudWatch Dashboard created to observe this application. Must only contain alphanumerics, dash (-) and underscore (_). Default: "construct-hub"
        :param domain: (experimental) Connect the hub to a domain (requires a hosted zone and a certificate).

        :stability: experimental
        '''
        props = ConstructHubProps(
            alarm_actions=alarm_actions, dashboard_name=dashboard_name, domain=domain
        )

        jsii.create(ConstructHub, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ingestionQueue")
    def ingestion_queue(self) -> aws_cdk.aws_sqs.IQueue:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_sqs.IQueue, jsii.get(self, "ingestionQueue"))


@jsii.data_type(
    jsii_type="construct-hub.ConstructHubProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_actions": "alarmActions",
        "dashboard_name": "dashboardName",
        "domain": "domain",
    },
)
class ConstructHubProps:
    def __init__(
        self,
        *,
        alarm_actions: AlarmActions,
        dashboard_name: typing.Optional[builtins.str] = None,
        domain: typing.Optional["Domain"] = None,
    ) -> None:
        '''(experimental) Props for ``ConstructHub``.

        :param alarm_actions: (experimental) Actions to perform when alarms are set.
        :param dashboard_name: (experimental) The name of the CloudWatch Dashboard created to observe this application. Must only contain alphanumerics, dash (-) and underscore (_). Default: "construct-hub"
        :param domain: (experimental) Connect the hub to a domain (requires a hosted zone and a certificate).

        :stability: experimental
        '''
        if isinstance(alarm_actions, dict):
            alarm_actions = AlarmActions(**alarm_actions)
        if isinstance(domain, dict):
            domain = Domain(**domain)
        self._values: typing.Dict[str, typing.Any] = {
            "alarm_actions": alarm_actions,
        }
        if dashboard_name is not None:
            self._values["dashboard_name"] = dashboard_name
        if domain is not None:
            self._values["domain"] = domain

    @builtins.property
    def alarm_actions(self) -> AlarmActions:
        '''(experimental) Actions to perform when alarms are set.

        :stability: experimental
        '''
        result = self._values.get("alarm_actions")
        assert result is not None, "Required property 'alarm_actions' is missing"
        return typing.cast(AlarmActions, result)

    @builtins.property
    def dashboard_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the CloudWatch Dashboard created to observe this application.

        Must only contain alphanumerics, dash (-) and underscore (_).

        :default: "construct-hub"

        :stability: experimental
        '''
        result = self._values.get("dashboard_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional["Domain"]:
        '''(experimental) Connect the hub to a domain (requires a hosted zone and a certificate).

        :stability: experimental
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional["Domain"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConstructHubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="construct-hub.Domain",
    jsii_struct_bases=[],
    name_mapping={"cert": "cert", "zone": "zone"},
)
class Domain:
    def __init__(
        self,
        *,
        cert: aws_cdk.aws_certificatemanager.ICertificate,
        zone: aws_cdk.aws_route53.IHostedZone,
    ) -> None:
        '''(experimental) Domain configuration for the website.

        :param cert: (experimental) The certificate to use for serving the Construct Hub over a custom domain. Default: - a DNS-Validated certificate will be provisioned using the provided ``hostedZone``.
        :param zone: (experimental) The root domain name where this instance of Construct Hub will be served.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cert": cert,
            "zone": zone,
        }

    @builtins.property
    def cert(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) The certificate to use for serving the Construct Hub over a custom domain.

        :default:

        - a DNS-Validated certificate will be provisioned using the
        provided ``hostedZone``.

        :stability: experimental
        '''
        result = self._values.get("cert")
        assert result is not None, "Required property 'cert' is missing"
        return typing.cast(aws_cdk.aws_certificatemanager.ICertificate, result)

    @builtins.property
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''(experimental) The root domain name where this instance of Construct Hub will be served.

        :stability: experimental
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(aws_cdk.aws_route53.IHostedZone, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Domain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlarmActions",
    "ConstructHub",
    "ConstructHubProps",
    "Domain",
]

publication.publish()
