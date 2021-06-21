from pydantic.main import BaseModel
from beanie import Document, PydanticObjectId
from typing import Any, Dict, Optional, List, Union


class Test(Document):
    t: str


async def get_test() -> Union[Test, Dict[str, Any]]:
    return (await Test.find().to_list())[0]


async def d(t: Test):
    print(t)


async def main():
    t = await get_test()
    await d(t)


class C:
    @classmethod
    def c(cls):
        return cls()


class B(C):
    ...


class A:
    def __init__(self, foo: Type):
        self.foo = foo

    def bar(self):
        return self.foo
