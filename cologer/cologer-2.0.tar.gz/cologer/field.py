import re
import typing
import colorama
from cologer.lib import get_time, get_lineno, get_filename

colorama.init(autoreset=True)
Fore = colorama.Fore
Back = colorama.Back
Style = colorama.Style

pattern = re.compile(r'(?<=\{)[^}]*(?=\})+')


class Field:
    def __init__(self, name: str, level: str) -> None:
        self.name = name
        self.lv = level
        self._default = self._default_adapter()
        self.fore = ''
        self.back = ''
        self.style = ''

    def set_fore(self, fore: Fore):
        self.fore = fore
        return self

    def set_back(self, back: Back):
        self.back = back
        return self

    def set_style(self, style: Style):
        self.style = style
        return self

    @property
    def default(self):
        if callable(self._default):
            return self._default()
        return self._default

    def set_default(self, default: typing.Any):
        self._default = default
        return self

    def _default_adapter(self):
        name = self.name.lower()
        if name == 'time':
            return get_time
        elif name == 'level':
            return self.lv
        elif name == 'filename':
            return get_filename
        elif name == 'lineno':
            return get_lineno
        else:
            return ''

    def __str__(self) -> str:
        return self.fore + self.back + self.style + '{' + self.name + '}' + Style.RESET_ALL


class Fields:
    def __init__(self, fmt: str, level: str) -> None:
        self.lv = level
        self.field_names = []
        self._set_field(fmt)

    def _set_field(self, fmt: str):
        for f_n in pattern.findall(fmt):
            self.field_names.append(f_n)
            setattr(self, f_n, Field(f_n, self.lv))

    def _get_color_str(self, *args, **kwargs):
        color = {}
        raw = {}
        for f_n in self.field_names:
            field: Field = getattr(self, f_n)
            if f_n == 'message':
                u = ' '.join([str(u) for u in args])
                value = kwargs.get(f_n, u or field.default)
            else:
                value = kwargs.get(f_n, field.default)
            color[f_n] = str(field).format(**{f_n: value})
            raw[f_n] = value
        return color, raw
