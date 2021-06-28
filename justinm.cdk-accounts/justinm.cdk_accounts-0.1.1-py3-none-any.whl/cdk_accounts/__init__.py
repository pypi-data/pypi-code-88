'''
# justinm/cdk-accounts

... a collection of CDK constructs for managing AWS infrastructure.

![Build Status](https://github.com/justinm/cdk-constructs/actions/workflows/build.yml/badge.svg)
![License](https://img.shields.io/github/license/justinm/cdk-constructs)
![Node](https://img.shields.io/node/v/@justinm/cdk-accounts/latest)
![Python](https://img.shields.io/pypi/pyversions/justinm.cdk-accounts)

## Installing

NodeJS

```shell
yarn add @justinm/cdk-accounts

npm install @justinm/cdk-accounts
```

Python

```shell
pip3 install justinm.cdk-accounts
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

import aws_cdk.aws_iam
import aws_cdk.core


class OktaSamlStack(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-accounts.OktaSamlStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        admin_for_developer: typing.Optional[builtins.bool] = None,
        developer_policies: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param admin_for_developer: -
        :param developer_policies: -
        :param metadata_document: -
        '''
        props = OktaSamlStackProps(
            admin_for_developer=admin_for_developer,
            developer_policies=developer_policies,
            metadata_document=metadata_document,
        )

        jsii.create(OktaSamlStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@justinm/cdk-accounts.OktaSamlStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "admin_for_developer": "adminForDeveloper",
        "developer_policies": "developerPolicies",
        "metadata_document": "metadataDocument",
    },
)
class OktaSamlStackProps:
    def __init__(
        self,
        *,
        admin_for_developer: typing.Optional[builtins.bool] = None,
        developer_policies: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
    ) -> None:
        '''
        :param admin_for_developer: -
        :param developer_policies: -
        :param metadata_document: -
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if admin_for_developer is not None:
            self._values["admin_for_developer"] = admin_for_developer
        if developer_policies is not None:
            self._values["developer_policies"] = developer_policies
        if metadata_document is not None:
            self._values["metadata_document"] = metadata_document

    @builtins.property
    def admin_for_developer(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("admin_for_developer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def developer_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        result = self._values.get("developer_policies")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], result)

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
        return "OktaSamlStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SimpleAccountBudgetsStack(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-accounts.SimpleAccountBudgetsStack",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param budget_limit: -
        :param email_addresses: -
        '''
        props = SimpleAccountBudgetsStackProps(
            budget_limit=budget_limit, email_addresses=email_addresses
        )

        jsii.create(SimpleAccountBudgetsStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@justinm/cdk-accounts.SimpleAccountBudgetsStackProps",
    jsii_struct_bases=[],
    name_mapping={"budget_limit": "budgetLimit", "email_addresses": "emailAddresses"},
)
class SimpleAccountBudgetsStackProps:
    def __init__(
        self,
        *,
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param budget_limit: -
        :param email_addresses: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "budget_limit": budget_limit,
            "email_addresses": email_addresses,
        }

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
        return "SimpleAccountBudgetsStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SimpleAccountCloudTrail(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-accounts.SimpleAccountCloudTrail",
):
    def __init__(self, scope: aws_cdk.core.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        jsii.create(SimpleAccountCloudTrail, self, [scope, id])


class SimpleAccountStack(
    aws_cdk.core.Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@justinm/cdk-accounts.SimpleAccountStack",
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
        admin_for_developer: typing.Optional[builtins.bool] = None,
        developer_policies: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
        metadata_document: typing.Optional[aws_cdk.aws_iam.SamlMetadataDocument] = None,
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
        :param admin_for_developer: -
        :param developer_policies: -
        :param metadata_document: -
        '''
        props = SimpleAccountStackProps(
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
            budget_limit=budget_limit,
            email_addresses=email_addresses,
            admin_for_developer=admin_for_developer,
            developer_policies=developer_policies,
            metadata_document=metadata_document,
        )

        jsii.create(SimpleAccountStack, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@justinm/cdk-accounts.SimpleAccountStackProps",
    jsii_struct_bases=[
        aws_cdk.core.StackProps, SimpleAccountBudgetsStackProps, OktaSamlStackProps
    ],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
        "budget_limit": "budgetLimit",
        "email_addresses": "emailAddresses",
        "admin_for_developer": "adminForDeveloper",
        "developer_policies": "developerPolicies",
        "metadata_document": "metadataDocument",
    },
)
class SimpleAccountStackProps(
    aws_cdk.core.StackProps,
    SimpleAccountBudgetsStackProps,
    OktaSamlStackProps,
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
        budget_limit: jsii.Number,
        email_addresses: typing.Sequence[builtins.str],
        admin_for_developer: typing.Optional[builtins.bool] = None,
        developer_policies: typing.Optional[typing.Sequence[aws_cdk.aws_iam.PolicyStatement]] = None,
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
        :param budget_limit: -
        :param email_addresses: -
        :param admin_for_developer: -
        :param developer_policies: -
        :param metadata_document: -
        '''
        if isinstance(env, dict):
            env = aws_cdk.core.Environment(**env)
        self._values: typing.Dict[str, typing.Any] = {
            "budget_limit": budget_limit,
            "email_addresses": email_addresses,
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
        if admin_for_developer is not None:
            self._values["admin_for_developer"] = admin_for_developer
        if developer_policies is not None:
            self._values["developer_policies"] = developer_policies
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
    def admin_for_developer(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("admin_for_developer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def developer_policies(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]]:
        result = self._values.get("developer_policies")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.PolicyStatement]], result)

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
        return "SimpleAccountStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OktaSamlStack",
    "OktaSamlStackProps",
    "SimpleAccountBudgetsStack",
    "SimpleAccountBudgetsStackProps",
    "SimpleAccountCloudTrail",
    "SimpleAccountStack",
    "SimpleAccountStackProps",
]

publication.publish()
