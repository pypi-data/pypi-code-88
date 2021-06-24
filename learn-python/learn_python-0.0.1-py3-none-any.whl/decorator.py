import functools

# function : is first-class object e.g it can be passed around and
# and used as arguments


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


def parent(num):

    def first():
        return "Hi from first"

    def second():
        return "Hi from second"
    if num == 1:
        return first
    else:
        return second


def my_decorator(func):
    # For introspection (we use function)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("do something before")
        func(*args, **kwargs)
        print("do something after")
    return wrapper


@my_decorator
def say_yes():
    print("Yes!")


@my_decorator
def say_hello_to_someone(name):
    print("Hello {}".format(name))


if __name__ == '__main__':
    print(greet_bob(say_hello))
    first = parent(1)
    print(first())
    say_yes()
    print(say_yes.__name__)
    say_hello_to_someone("Massipssa")