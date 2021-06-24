def parent(num):
    def func1():
        print("Hello from func - 1")

    def func2():
        print("Hello from func - 2")
    if num == 1:
        return func1
    else:
        return func2


def my_decorator(fun):

    def wrapper():
        print("Before func")

        fun()
        print("After func")
    return wrapper


@my_decorator
def say_hello():
    print("Hello from say_hello")
    print("Say bye")
