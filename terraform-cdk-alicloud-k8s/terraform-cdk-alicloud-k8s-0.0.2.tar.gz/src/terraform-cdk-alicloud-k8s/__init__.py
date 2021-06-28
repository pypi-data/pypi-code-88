'''
# replace this
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


class Hello(metaclass=jsii.JSIIMeta, jsii_type="terraform-cdk-alicloud-k8s.Hello"):
    def __init__(self) -> None:
        jsii.create(Hello, self, [])

    @jsii.member(jsii_name="sayHello")
    def say_hello(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "sayHello", []))


__all__ = [
    "Hello",
]

publication.publish()
