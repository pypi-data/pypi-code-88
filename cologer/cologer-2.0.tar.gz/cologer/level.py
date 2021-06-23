import sys

from cologer.field import Fields


class Level:
    def __init__(self, name: str, fmt: str) -> None:
        self.fmt = fmt
        self.name = name.upper()
        self._visible = True
        self.fields = Fields(fmt, self.name)
        self._hook = None

    def invisible(self):
        self._visible = False

    def __call__(self, *args, **kwargs):
        c, r = self.fields._get_color_str(*args, **kwargs)
        if self._visible:
            sys.stdout.write(self.fmt.format(**c)+'\n')
        if self._hook:
            self._hook(**r)
