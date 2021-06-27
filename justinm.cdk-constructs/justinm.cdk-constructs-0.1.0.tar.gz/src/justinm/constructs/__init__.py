'''
# Welcome to your CDK TypeScript project!

This is a blank project for TypeScript development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template
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
import aws_cdk.aws_iam
import aws_cdk.core


class AwsAccountBudgetsStack(
    aws_cdk.core.NestedStack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.AwsAccountBudgetsStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param budget_limit: -
        :param email_addresses: -
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        '''
        props = AwsAccountBudgetsStackProps(
            budget_limit=budget_limit,
            email_addresses=email_addresses,
            notification_arns=notification_arns,
            parameters=parameters,
            removal_policy=removal_policy,
            timeout=timeout,
        )

        jsii.create(AwsAccountBudgetsStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@justinm/cdk-constructs.AwsAccountBudgetsStackProps",
    jsii_struct_bases=[aws_cdk.core.NestedStackProps],
    name_mapping={
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "removal_policy": "removalPolicy",
        "timeout": "timeout",
        "budget_limit": "budgetLimit",
        "email_addresses": "emailAddresses",
    },
)
class AwsAccountBudgetsStackProps(aws_cdk.core.NestedStackProps):
    def __init__(
        self,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        :param budget_limit: -
        :param email_addresses: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "budget_limit": budget_limit,
            "email_addresses": email_addresses,
        }
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Simple Notification Service (SNS) topics to publish stack related events.

        :default: - notifications are not sent for this stack.
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.

        Each parameter has a name corresponding
        to a parameter defined in the embedded template and a value representing
        the value that you want to set for the parameter.

        The nested stack construct will automatically synthesize parameters in order
        to bind references from the parent stack(s) into the nested stack.

        :default: - no user-defined parameters are passed to the nested stack
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        '''Policy to apply when the nested stack is removed.

        The default is ``Destroy``, because all Removal Policies of resources inside the
        Nested Stack should already have been set correctly. You normally should
        not need to set this value.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.core.RemovalPolicy], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state.

        When CloudFormation detects that the nested stack has reached the
        CREATE_COMPLETE state, it marks the nested stack resource as
        CREATE_COMPLETE in the parent stack and resumes creating the parent stack.
        If the timeout period expires before the nested stack reaches
        CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls
        back both the nested stack and parent stack.

        :default: - no timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def budget_limit(self) -> jsii.Number:
        result = self._values.get("budget_limit")
        assert result is not None, "Required property 'budget_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def email_addresses(self) -> typing.List[builtins.str]:
        result = self._values.get("email_addresses")
        assert result is not None, "Required property 'email_addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAccountBudgetsStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsAccountCloudTrailStack(
    aws_cdk.core.NestedStack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.AwsAccountCloudTrailStack",
):
    def __init__(self, scope: aws_cdk.core.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        jsii.create(AwsAccountCloudTrailStack, self, [scope, id])


class AwsAccountStack(
    aws_cdk.core.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.AwsAccountStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[aws_cdk.core.Environment] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.core.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
        developer_policies: typing.Sequence[aws_cdk.aws_iam.PolicyStatement],
        admin_for_developer: typing.Optional[builtins.bool] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param budget_limit: -
        :param email_addresses: -
        :param developer_policies: -
        :param admin_for_developer: -
        :param metadata_document: -
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        '''
        props = AwsAccountStackProps(
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
            budget_limit=budget_limit,
            email_addresses=email_addresses,
            developer_policies=developer_policies,
            admin_for_developer=admin_for_developer,
            metadata_document=metadata_document,
            notification_arns=notification_arns,
            parameters=parameters,
            removal_policy=removal_policy,
            timeout=timeout,
        )

        jsii.create(AwsAccountStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@justinm/cdk-constructs.AwsOktaSamlProps",
    jsii_struct_bases=[aws_cdk.core.NestedStackProps],
    name_mapping={
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "removal_policy": "removalPolicy",
        "timeout": "timeout",
        "developer_policies": "developerPolicies",
        "admin_for_developer": "adminForDeveloper",
        "metadata_document": "metadataDocument",
    },
)
class AwsOktaSamlProps(aws_cdk.core.NestedStackProps):
    def __init__(
        self,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        developer_policies: typing.Sequence[aws_cdk.aws_iam.PolicyStatement],
        admin_for_developer: typing.Optional[builtins.bool] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
    ) -> None:
        '''
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        :param developer_policies: -
        :param admin_for_developer: -
        :param metadata_document: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "developer_policies": developer_policies,
        }
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if admin_for_developer is not None:
            self._values["admin_for_developer"] = admin_for_developer
        if metadata_document is not None:
            self._values["metadata_document"] = metadata_document

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Simple Notification Service (SNS) topics to publish stack related events.

        :default: - notifications are not sent for this stack.
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.

        Each parameter has a name corresponding
        to a parameter defined in the embedded template and a value representing
        the value that you want to set for the parameter.

        The nested stack construct will automatically synthesize parameters in order
        to bind references from the parent stack(s) into the nested stack.

        :default: - no user-defined parameters are passed to the nested stack
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        '''Policy to apply when the nested stack is removed.

        The default is ``Destroy``, because all Removal Policies of resources inside the
        Nested Stack should already have been set correctly. You normally should
        not need to set this value.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.core.RemovalPolicy], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state.

        When CloudFormation detects that the nested stack has reached the
        CREATE_COMPLETE state, it marks the nested stack resource as
        CREATE_COMPLETE in the parent stack and resumes creating the parent stack.
        If the timeout period expires before the nested stack reaches
        CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls
        back both the nested stack and parent stack.

        :default: - no timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def developer_policies(self) -> typing.List[aws_cdk.aws_iam.PolicyStatement]:
        result = self._values.get("developer_policies")
        assert result is not None, "Required property 'developer_policies' is missing"
        return typing.cast(typing.List[aws_cdk.aws_iam.PolicyStatement], result)

    @builtins.property
    def admin_for_developer(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("admin_for_developer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def metadata_document(
        self,
    ) -> typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument]:
        result = self._values.get("metadata_document")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsOktaSamlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsOktaSamlStack(
    aws_cdk.core.NestedStack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.AwsOktaSamlStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        developer_policies: typing.Sequence[aws_cdk.aws_iam.PolicyStatement],
        admin_for_developer: typing.Optional[builtins.bool] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param developer_policies: -
        :param admin_for_developer: -
        :param metadata_document: -
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        '''
        props = AwsOktaSamlProps(
            developer_policies=developer_policies,
            admin_for_developer=admin_for_developer,
            metadata_document=metadata_document,
            notification_arns=notification_arns,
            parameters=parameters,
            removal_policy=removal_policy,
            timeout=timeout,
        )

        jsii.create(AwsOktaSamlStack, self, [scope, id, props])


class AwsVpc(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-constructs.AwsVpc",
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
    jsii_type="@justinm/cdk-constructs.AwsVpcProps",
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


@jsii.data_type(
    jsii_type="@justinm/cdk-constructs.AwsAccountStackProps",
    jsii_struct_bases=[
        aws_cdk.core.StackProps, AwsAccountBudgetsStackProps, AwsOktaSamlProps
    ],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "removal_policy": "removalPolicy",
        "timeout": "timeout",
        "budget_limit": "budgetLimit",
        "email_addresses": "emailAddresses",
        "developer_policies": "developerPolicies",
        "admin_for_developer": "adminForDeveloper",
        "metadata_document": "metadataDocument",
    },
)
class AwsAccountStackProps(
    aws_cdk.core.StackProps,
    AwsAccountBudgetsStackProps,
    AwsOktaSamlProps,
):
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[aws_cdk.core.Environment] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[aws_cdk.core.IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
        developer_policies: typing.Sequence[aws_cdk.aws_iam.PolicyStatement],
        admin_for_developer: typing.Optional[builtins.bool] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
    ) -> None:
        '''
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        :param budget_limit: -
        :param email_addresses: -
        :param developer_policies: -
        :param admin_for_developer: -
        :param metadata_document: -
        '''
        if isinstance(env, dict):
            env = aws_cdk.core.Environment(**env)
        self._values: typing.Dict[str, typing.Any] = {
            "budget_limit": budget_limit,
            "email_addresses": email_addresses,
            "developer_policies": developer_policies,
        }
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if timeout is not None:
            self._values["timeout"] = timeout
        if admin_for_developer is not None:
            self._values["admin_for_developer"] = admin_for_developer
        if metadata_document is not None:
            self._values["metadata_document"] = metadata_document

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            # Use a concrete account and region to deploy this stack to:
            # `.account` and `.region` will simply return these values.
            Stack(app, "Stack1",
                env={
                    "account": "123456789012",
                    "region": "us-east-1"
                }
            )
            
            # Use the CLI's current credentials to determine the target environment:
            # `.account` and `.region` will reflect the account+region the CLI
            # is configured to use (based on the user CLI credentials)
            Stack(app, "Stack2",
                env={
                    "account": process.env.CDK_DEFAULT_ACCOUNT,
                    "region": process.env.CDK_DEFAULT_REGION
                }
            )
            
            # Define multiple stacks stage associated with an environment
            my_stage = Stage(app, "MyStage",
                env={
                    "account": "123456789012",
                    "region": "us-east-1"
                }
            )
            
            # both of these stacks will use the stage's account/region:
            # `.account` and `.region` will resolve to the concrete values as above
            MyStack(my_stage, "Stack1")
            YourStack(my_stage, "Stack2")
            
            # Define an environment-agnostic stack:
            # `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            # which will only resolve to actual values by CloudFormation during deployment.
            MyStack(app, "Stack1")
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[aws_cdk.core.Environment], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[aws_cdk.core.IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
        is set, ``LegacyStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[aws_cdk.core.IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Simple Notification Service (SNS) topics to publish stack related events.

        :default: - notifications are not sent for this stack.
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.

        Each parameter has a name corresponding
        to a parameter defined in the embedded template and a value representing
        the value that you want to set for the parameter.

        The nested stack construct will automatically synthesize parameters in order
        to bind references from the parent stack(s) into the nested stack.

        :default: - no user-defined parameters are passed to the nested stack
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        '''Policy to apply when the nested stack is removed.

        The default is ``Destroy``, because all Removal Policies of resources inside the
        Nested Stack should already have been set correctly. You normally should
        not need to set this value.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.core.RemovalPolicy], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state.

        When CloudFormation detects that the nested stack has reached the
        CREATE_COMPLETE state, it marks the nested stack resource as
        CREATE_COMPLETE in the parent stack and resumes creating the parent stack.
        If the timeout period expires before the nested stack reaches
        CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls
        back both the nested stack and parent stack.

        :default: - no timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def budget_limit(self) -> jsii.Number:
        result = self._values.get("budget_limit")
        assert result is not None, "Required property 'budget_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def email_addresses(self) -> typing.List[builtins.str]:
        result = self._values.get("email_addresses")
        assert result is not None, "Required property 'email_addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def developer_policies(self) -> typing.List[aws_cdk.aws_iam.PolicyStatement]:
        result = self._values.get("developer_policies")
        assert result is not None, "Required property 'developer_policies' is missing"
        return typing.cast(typing.List[aws_cdk.aws_iam.PolicyStatement], result)

    @builtins.property
    def admin_for_developer(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("admin_for_developer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def metadata_document(
        self,
    ) -> typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument]:
        result = self._values.get("metadata_document")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAccountStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsAccountBudgetsStack",
    "AwsAccountBudgetsStackProps",
    "AwsAccountCloudTrailStack",
    "AwsAccountStack",
    "AwsAccountStackProps",
    "AwsOktaSamlProps",
    "AwsOktaSamlStack",
    "AwsVpc",
    "AwsVpcProps",
]

publication.publish()
