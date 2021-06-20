"""
Wrapper for C++ extension.
"""

try:
    from factory import (
        imagefile as cpp_imagefile,
        number_of_buffers as cpp_number_of_buffers,
        buffer_headers as cpp_buffer_headers,
    )
except ModuleNotFoundError:
    error_msg = "C++ extension of the oap library was not compiled"
    print("Catching ModuleNotFoundError:", error_msg)
    # raise ModuleNotFoundError(error_msg)


# ToDo Anständige Wrapper schreiben mit DocString + Exception Handling
def imagefile(*args, **kwargs):
    return cpp_imagefile(*args, **kwargs)


def number_of_buffers(filepath):
    return cpp_number_of_buffers(filepath)


def buffer_headers(filepath):
    output = []
    cpp_buffer_headers(filepath, output=output)
    return output
