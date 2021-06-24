def get_fire_wall_rule_args(wall):
    if not isinstance(wall, list):
        return None
    return list(set(wall))


class Color:
    """
    控制台字体颜色更改
    """

    ADD_COLOR = True

    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BlUE = '\033[94m'
    END = '\033[0m'

    @classmethod
    def red(cls, string):
        return cls._color_strings(string, cls.RED)

    @classmethod
    def green(cls, string):
        return cls._color_strings(string, cls.GREEN)

    @classmethod
    def yellow(cls, string):
        return cls._color_strings(string, cls.YELLOW)

    @classmethod
    def cyan(cls, string):
        return cls._color_strings(string, cls.BlUE)

    @classmethod
    def _color_strings(cls, string, color_string=''):
        if not cls.ADD_COLOR:
            return str(string)
        return str(color_string) + str(string) + cls.END
