from typing import Callable, Any


def builder(*attributes: list[str]) -> Callable[type, type]:
    """Builder decorator like Lombok

    Builder decorator to constract instance

    Args:
        attributes (list[str]): Attributes of class

    Returns:
        Callable[type, type]: Decorator to add Builder class

    Examples:
        @builder("id", "name", "age", "email")
        class User:
            def __init__(self, id: int, name: str, age: int, email: str) -> None:
                self.id = id
                self.name = name
                self.age = age
                self.email = email

        user = User.Builder().id(0).name("Shuntaro Shimizu").age(99).email("ut.s.shimizu@gmail.com").build()
    """
    def decorator(Class: type) -> type:
        class Builder:
            def __init__(self) -> None:
                self.kwargs = {}
                for attribute in attributes:
                    self.kwargs[attribute] = None
                    setattr(self, attribute, self.generate_setter(attribute))

            def generate_setter(self, key: str) -> Callable[Any, "Builder"]:
                def set_value(value: Any) -> "Builder":
                    self.kwargs[key] = value
                    return self
                return set_value

            def build(self) -> Class:
                return Class(**self.kwargs)

        Class.Builder = Builder

        return Class
    return decorator
