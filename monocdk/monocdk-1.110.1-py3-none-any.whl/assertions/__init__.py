'''
# Assertions

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

Functions for writing test asserting against CDK applications, with focus on CloudFormation templates.

The `TemplateAssertions` class includes a set of methods for writing assertions against CloudFormation templates. Use one of the `TemplateAssertions.fromXxx()` static methods to create an instance of this class.

To create `TemplateAssertions` from CDK stack, start off with:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk import Stack
from aws_cdk_lib.assertions import TemplateAssertions


stack = Stack(...)
assert = TemplateAssertions.from_stack(stack)
```

Alternatively, assertions can be run on an existing CloudFormation template -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
template = fs.read_file_sync("/path/to/template/file")
assert = TemplateAssertions.from_string(template)
```

## Full Template Match

The simplest assertion would be to assert that the template matches a given
template.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
assert.template_matches(
    Resources={
        "Type": "Foo::Bar",
        "Properties": {
            "Baz": "Qux"
        }
    }
)
```

## Counting Resources

This module allows asserting the number of resources of a specific type found
in a template.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
assert.resource_count_is("Foo::Bar", 2)
```

## Resource Matching

Beyond resource counting, the module also allows asserting that a resource with
specific properties are present.

The following code asserts that the `Properties` section of a resource of type
`Foo::Bar` contains the specified properties -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
assert.has_resource_properties("Foo::Bar",
    Foo="Bar",
    Baz=5,
    Qux=["Waldo", "Fred"]
)
```

The same method allows asserting the complete definition of the 'Resource'
which can be used to verify things other sections like `DependsOn`, `Metadata`,
`DeletionProperty`, etc.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
assert.has_resource_definition("Foo::Bar",
    Properties={"Foo": "Bar"},
    DependsOn=["Waldo", "Fred"]
)
```

## Special Matchers

The expectation provided to the `hasResourceXXX()` methods, besides carrying
literal values, as seen in the above examples, can also have special matchers
encoded.
They are available as part of the `Matchers` class and can be used as follows -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
assert.has_resource_properties("Foo::Bar",
    Foo="Bar",
    Baz=Match.absent_property()
)
```

The list of available matchers are -

* `absentProperty()`: Specifies that this key must not be present.

## Strongly typed languages

Some of the APIs documented above, such as `templateMatches()` and
`hasResourceProperties()` accept fluently an arbitrary JSON (like) structure
its parameter.
This fluency is available only in dynamically typed languages like javascript
and Python.

For strongly typed languages, like Java, you can achieve similar fluency using
any popular JSON deserializer. The following Java example uses `Gson` -

```java
// In Java, using text blocks and Gson
import com.google.gson.Gson;

String json = """
  {
    "Foo": "Bar",
    "Baz": 5,
    "Qux": [ "Waldo", "Fred" ],
  } """;

Map expected = new Gson().fromJson(json, Map.class);
assert.hasResourceProperties("Foo::Bar", expected);
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

from .._jsii import *

from .. import Stack as _Stack_9f43e4a3


class Match(metaclass=jsii.JSIIMeta, jsii_type="monocdk.assertions.Match"):
    '''(experimental) Partial and special matching during template assertions.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(Match, self, [])

    @jsii.member(jsii_name="absentProperty") # type: ignore[misc]
    @builtins.classmethod
    def absent_property(cls) -> builtins.str:
        '''(experimental) Use this matcher in the place of a field's value, if the field must not be present.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "absentProperty", []))


class TemplateAssertions(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.assertions.TemplateAssertions",
):
    '''(experimental) Suite of assertions that can be run on a CDK stack.

    Typically used, as part of unit tests, to validate that the rendered
    CloudFormation template has expected resources and properties.

    :stability: experimental
    '''

    @jsii.member(jsii_name="fromStack") # type: ignore[misc]
    @builtins.classmethod
    def from_stack(cls, stack: _Stack_9f43e4a3) -> "TemplateAssertions":
        '''(experimental) Base your assertions on the CloudFormation template synthesized by a CDK ``Stack``.

        :param stack: the CDK Stack to run assertions on.

        :stability: experimental
        '''
        return typing.cast("TemplateAssertions", jsii.sinvoke(cls, "fromStack", [stack]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, template: builtins.str) -> "TemplateAssertions":
        '''(experimental) Base your assertions from an existing CloudFormation template formatted as a string.

        :param template: the CloudFormation template in.

        :stability: experimental
        '''
        return typing.cast("TemplateAssertions", jsii.sinvoke(cls, "fromString", [template]))

    @jsii.member(jsii_name="fromTemplate") # type: ignore[misc]
    @builtins.classmethod
    def from_template(
        cls,
        template: typing.Mapping[builtins.str, typing.Any],
    ) -> "TemplateAssertions":
        '''(experimental) Base your assertions from an existing CloudFormation template formatted as a nested set of records.

        :param template: the CloudFormation template formatted as a nested set of records.

        :stability: experimental
        '''
        return typing.cast("TemplateAssertions", jsii.sinvoke(cls, "fromTemplate", [template]))

    @jsii.member(jsii_name="hasResourceDefinition")
    def has_resource_definition(self, type: builtins.str, props: typing.Any) -> None:
        '''(experimental) Assert that a resource of the given type and given definition exists in the CloudFormation template.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the entire defintion of the resource as should be expected in the template.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "hasResourceDefinition", [type, props]))

    @jsii.member(jsii_name="hasResourceProperties")
    def has_resource_properties(self, type: builtins.str, props: typing.Any) -> None:
        '''(experimental) Assert that a resource of the given type and properties exists in the CloudFormation template.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param props: the 'Properties' section of the resource as should be expected in the template.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "hasResourceProperties", [type, props]))

    @jsii.member(jsii_name="resourceCountIs")
    def resource_count_is(self, type: builtins.str, count: jsii.Number) -> None:
        '''(experimental) Assert that the given number of resources of the given type exist in the template.

        :param type: the resource type; ex: ``AWS::S3::Bucket``
        :param count: number of expected instances.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "resourceCountIs", [type, count]))

    @jsii.member(jsii_name="templateMatches")
    def template_matches(
        self,
        expected: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''(experimental) Assert that the CloudFormation template matches the given value.

        :param expected: the expected CloudFormation template as key-value pairs.

        :stability: experimental
        '''
        return typing.cast(None, jsii.invoke(self, "templateMatches", [expected]))


__all__ = [
    "Match",
    "TemplateAssertions",
]

publication.publish()
