from pydoc import locate


def get_all_fields(fields: list, rest: dict) -> list:
    for key in rest:
        fields.append(key)
    return fields


def str_to_class(path: str):
    """
    if your class name is MyClass and located in my_app.models.MyClass then:

    Example:
        path = "my_app.models.MyClass"
        my_class = to_class(path)

    :param path: String path of the module's class
    :return my_class: Object or None
    """
    try:
        my_class = locate(path)
    except ImportError:
        raise ValueError('>> Module does not exist')
    return my_class or None
