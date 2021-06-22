class UserMeta(type):
    def __init__(cls, *args, **kwargs):
        super(UserMeta, cls).__init__(*args, **kwargs)
        if not cls.__apis__:
            raise ValueError(args[0] + ': missing __apis__')

    def __call__(cls, *args, **kwargs):
        instance = super(UserMeta, cls).__call__(*args, **kwargs)
        for api in cls.__apis__:
            setattr(instance, api.__name__, api(args[0]))
        return instance


class UserOperation(metaclass=UserMeta):
    __apis__ = ("test",)

    def __init__(self, user):
        self.user = user

    def __getattr__(self, item):
        raise AssertionError("no attr named %s" % item)
