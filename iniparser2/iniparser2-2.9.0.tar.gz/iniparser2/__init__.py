"""An INI parser or a Config parser"""

import re
import io
import ast

from typing import Union
from typing import Optional
from typing import Any

__version__ = "2.9.0"
__all__ = ["ParsingError", "INI", "PropertyError", "DuplicateError", "SectionError"]


class ParsingError(Exception):
    """base exception for parsing error"""

    def __init__(self, message: str, line: int, text: Optional[str] = ""):
        self.message = message
        self.text = text
        self.line = line
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}, {self.text} [line {self.line}]"


class ParseDuplicateError(ParsingError):
    """dupe error raised while parsing"""


class PropertyError(Exception):
    pass


class DuplicateError(Exception):
    pass


class SectionError(Exception):
    pass


class ParsePropertyError(ParsingError):
    """raised when failed parsing property"""


class ParseSectionError(ParsingError):
    """raised when failed parsing section"""


class INI:
    """main class for parsing ini"""

    # parser patterns
    _section_pattern = re.compile(r"^\s*\[(?P<header>.*)\]\s*(?P<rest>.*)$")

    # converter patterns
    _float_pattern = re.compile(r"^[-+]?(\d+[.])\d+$")
    _int_pattern = re.compile(r"^[-+]?\d+$")
    _str_pattern = re.compile(r'".*(?<!\\)(?:\\\\)*"')

    LITERAL_TYPES = (int, float, bool, str)
    BOOL_STATES = {
        "true": True,
        "1": True,
        "on": True,
        "yes": True,
        "false": False,
        "0": False,
        "off": False,
        "no": False,
    }

    def __init__(
        self,
        delimiters: Optional[tuple] = ("=", ":"),
        comment_prefix: Optional[tuple] = (";", "#"),
        convert_property: Optional[bool] = False,
        inline_comments: Optional[bool] = True,
    ):
        """
        Parameters:
            - delimiters:
                property delimiters
            - convert_property:
                convert property value into specific data types
            - inline_comments:
                strip inline comments
        """
        self.ini = dict()
        self.delimiters = delimiters
        self.comment_prefix = comment_prefix
        self.convert_property = convert_property
        self.inline_comments = inline_comments
        self._sections = list()

        self._incom_pattern = re.compile(fr".*\s[{''.join(comment_prefix)}]")
        self._val_pattern = re.compile(
            fr".^[{''.join(comment_prefix)}]|\s[{''.join(comment_prefix)}]"
        )

        self._property_pattern = re.compile(
            rf"^\s*(?P<key>.*)\s*[{''.join(delimiters)}]\s*(?P<value>.*)\s*$"
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return self

    def __str__(self):
        return f"{self.ini}"

    def __iter__(self):
        yield from self.ini

    def __getitem__(self, key: str):
        return self.ini[key]

    def __setitem__(self, key: str, value: Union[int, str, bool, float, None]):
        if type(value) not in self.LITERAL_TYPES and value is not None:
            raise ValueError("value must be a literal or NoneType")

        if key in self.ini:
            if isinstance(self.ini[key], dict) and key in self._sections:
                raise SectionError("Cannot assign values to section header")

        self.ini[key] = value

    def __delitem__(self, key: str):
        if key in self._sections and isinstance(self.ini[key], dict):
            self._sections.remove(key)
            del self.ini[key]

        else:
            del self.ini[key]

    def update(self, dict_: dict):
        if not isinstance(dict_, dict):
            raise TypeError("value must be a dict")

        for sect in dict_:
            if sect in self._sections and type(dict_[sect]) is not dict:
                raise SectionError(f"Cannot update section header value [{sect}]")

            if isinstance(dict_[sect], dict):
                if sect not in self._sections:
                    self._sections.append(sect)
                    self.ini.update({sect: {}})

                for opt in dict_[sect]:
                    if (
                        type(dict_[sect][opt]) not in self.LITERAL_TYPES
                        and dict_[sect][opt] is not None
                    ):
                        raise PropertyError(
                            f"value must be a literal or NoneType [{sect}][{opt}]"
                        )

                    self.ini[sect].update({opt: dict_[sect][opt]})

            else:
                if (
                    type(dict_[sect]) not in self.LITERAL_TYPES
                    and dict_[sect] is not None
                ):
                    raise PropertyError(f"value must be a literal or NoneType [{sect}]")

                self.ini.update({sect: dict_[sect]})

    def __contains__(self, item: str):
        return item in self.ini

    def __len__(self):
        return len(self.ini)

    def read(self, string: str) -> None:
        """read ini from string"""
        self.ini = self._parse(string)
        self._sections = []
        for prop in self.ini:
            if isinstance(self.ini[prop], dict):
                self._sections.append(prop)

    def sections(self) -> list:
        """returns section headers"""
        return self._sections

    def has_section(self, name: str) -> bool:
        """check if section is exists"""
        return name in self._sections

    def has_property(self, name: str, section: Optional[str] = None) -> bool:
        """check if property is exists in a section or global"""
        if section is None:
            return name in self.ini

        return name in self.ini[section]

    def read_file(self, file: Union[io.TextIOWrapper, str]) -> None:
        """read sections and properties"""
        if type(file) is str:
            # file path in string
            self.ini = self._parse(open(file, "r").read())
        elif type(file) is io.TextIOWrapper:
            self.ini = self._parse(file.read())
        self._sections = []
        for prop in self.ini:
            if isinstance(self.ini[prop], dict):
                self._sections.append(prop)

    def remove_section(self, name: str) -> None:
        if not self.has_section(name):
            raise SectionError("section %s not found" % name)

        del self.ini[name]
        self._sections.remove(name)

    def remove_property(self, name: str, section: Optional[str] = None) -> None:
        if section is None:
            if not self.has_property(name):
                raise PropertyError("property %s not found" % name)

            del self.ini[name]
        else:
            if not self.has_section(section):
                raise SectionError("section %s not found" % section)
            if not self.has_property(name, section):
                raise PropertyError(f"property {name} not found in section {section}")

            del self.ini[section][name]

    def set(
        self,
        name: str,
        value: Union[str, int, float, bool, None] = None,
        section: Optional[str] = None,
    ) -> None:
        """set new property or update existing property value in a section or global"""
        if section is None:
            self.ini.update({name: value})
        else:
            if not self.has_section(section):
                raise SectionError("section %s not found" % section)

            self.ini[section].update({name: value})

    def get(self, name: str, section: Optional[str] = None) -> Any:
        """get property value from a section or global"""
        if section is None:
            if not self.has_property(name):
                raise PropertyError("property %s not found" % name)

            return self.ini[name]

        if not self.has_section(section):
            raise SectionError("section %s not found" % section)
        if not self.has_property(name, section):
            raise PropertyError(f"property {name} not found in section {section}")

        return self.ini[section][name]

    def get_str(self, name: str, section: Optional[str] = None) -> str:
        """get property value in `str` type"""
        return str(self.get(name, section))

    def get_int(self, name: str, section: Optional[str] = None) -> int:
        """get property value in `int` type"""
        val = self.get(name, section)
        if isinstance(val, int):
            return val

        return int(val)

    def get_float(self, name: str, section: Optional[str] = None) -> float:
        """get property value in `float` type"""
        val = self.get(name, section)
        if isinstance(val, float):
            return val

        return float(val)

    def get_bool(self, name: str, section: Optional[str] = None) -> bool:
        """get property value in `bool` type"""
        val = self.get(name, section)

        if isinstance(val, bool):
            return val

        val = val.lower()

        if val not in self.BOOL_STATES:
            raise TypeError("unknown bool state for: %s" % (val))

        return self.BOOL_STATES[val]

    def items(self, section: Optional[str] = None):
        result = []

        if section is None:
            for key in self.ini:
                if not isinstance(self.ini[key], dict):
                    result.append((key, self.ini[key]))
        else:
            if not self.has_section(section):
                raise SectionError("section %s not found" % section)

            for key in self.ini[section]:
                if self.ini[section][key] is not None:
                    result.append((key, self.ini[section][key]))

        return result

    def keys(self, section: Optional[str] = None):
        result = []

        if section is None:
            for key in self.ini:
                result.append(key)
        else:
            if not self.has_section(section):
                raise SectionError("section %s not found" % section)

            for key in self.ini[section]:
                result.append(key)

        return result

    def set_section(self, name: str) -> None:
        if self.has_section(name):
            raise DuplicateError("section %s already exists" % name)

        self.ini.update({name: {}})
        self._sections.append(name)

    def write(self, file: Union[io.TextIOWrapper, str]) -> None:
        """write properties and sections to file"""
        dump(file, self.ini)

    def _parse_property(self, string: str) -> tuple:
        """parse property returns property key and property value"""
        prop = self._property_pattern.match(string)
        if prop:
            key, val = prop.group("key", "value")
            if self.inline_comments is False:
                return key, val

            if not self._incom_pattern.match(key):
                return key, self._val_pattern.split(val)[0]

    def _parse_section(self, string: str) -> str:
        """parse section returns section name"""
        sec = self._section_pattern.match(string)
        if sec:
            header, rest = sec.group("header", "rest")
            if rest.strip():
                if rest.strip().startswith(
                    self.comment_prefix
                ) and not self._incom_pattern.match(header):
                    return header
            else:
                if not self._incom_pattern.match(header):
                    return header

    def _parse(self, string: Union[io.StringIO, str]) -> dict:
        """parse ini string returns ini dictionary"""
        result = {}

        if type(string) is str:
            lines = io.StringIO(string).readlines()
        elif type(string) is io.StringIO:
            lines = string.readlines()

        prev_section = None
        prev_property = (None, {"key_only": False})

        for lineno, line in enumerate(lines):
            lineno += 1

            if line.strip().startswith(self.comment_prefix) or not line.strip():
                continue

            section = self._parse_section(line.strip())

            if section:
                prev_section = section

                if not prev_section:
                    raise ParseSectionError(
                        "section header does not have a name", lineno, line.strip()
                    )

                if prev_section in result:
                    raise ParseDuplicateError(
                        "section already exists", lineno, prev_section
                    )

                result.update({prev_section: {}})
                continue

            property_ = self._parse_property(line.strip())

            if property_:
                key, val = property_

                if not key:
                    raise ParsePropertyError(
                        "property does not have a key name", lineno, line.strip()
                    )

                prev_property = (key.strip(), {"key_only": False})

                if prev_section:
                    if prev_property[0] in result[prev_section]:
                        raise ParseDuplicateError(
                            "property already exists", lineno, prev_property[0]
                        )

                    result[prev_section].update({key.strip(): val.strip()})
                else:
                    if prev_property[0] in result:
                        raise ParseDuplicateError(
                            "property already exists", lineno, prev_property[0]
                        )

                    result.update({key.strip(): val.strip()})

            else:  # allow value only property, the dict value set to None
                if re.match(r"^\s", line):
                    if prev_section and prev_property[0]:
                        if prev_property[1]["key_only"] is False:
                            result[prev_section][prev_property[0]] += (
                                "\n" + self._val_pattern.split(line.strip())[0]
                            )
                            continue
                    else:
                        if prev_property[0]:
                            if prev_property[1]["key_only"] is False:
                                result[prev_property[0]] += (
                                    "\n" + self._val_pattern.split(line.strip())[0]
                                )
                                continue

                if prev_section:
                    if line.strip() in result[prev_section]:
                        raise ParseDuplicateError(
                            "property already exists", lineno, line.strip()
                        )

                    key = self._val_pattern.split(line.strip())[0]
                    prev_property = (key, {"key_only": True})

                    result[prev_section].update({key: None})
                else:
                    if line.strip() in result:
                        raise ParseDuplicateError(
                            "property already exists", lineno, line.strip()
                        )
                    key = self._val_pattern.split(line.strip())[0]
                    prev_property = (key, {"key_only": True})

                    result.update({key: None})

        if self.convert_property:
            return self._convert_property(result)

        return result

    def _convert_property(self, ini_dict: dict) -> dict:
        """converter"""
        eval_codes = [
            (self._float_pattern, float),
            (self._int_pattern, int),
            (self._str_pattern, ast.literal_eval),
        ]

        for sectf in ini_dict:
            if isinstance(ini_dict[sectf], dict):
                for prop in ini_dict[sectf]:
                    for eval_code in eval_codes:
                        if eval_code[0].match(ini_dict[sectf][prop]):
                            try:
                                ini_dict[sectf][prop] = eval_code[1](
                                    ini_dict[sectf][prop]
                                )
                            except Exception:
                                break
                            else:
                                break

                    if type(ini_dict[sectf][prop]).__name__ != "str":
                        continue

                    if ini_dict[sectf][prop].lower() == "true":
                        ini_dict[sectf][prop] = True
                    elif ini_dict[sectf][prop].lower() == "false":
                        ini_dict[sectf][prop] = False
            else:
                for eval_code in eval_codes:
                    if eval_code[0].match(ini_dict[sectf]):
                        try:
                            ini_dict[sectf] = eval_code[1](ini_dict[sectf])
                        except Exception:
                            break
                        else:
                            break

                if type(ini_dict[sectf]).__name__ != "str":
                    continue

                if ini_dict[sectf].lower() == "true":
                    ini_dict[sectf] = True
                elif ini_dict[sectf].lower() == "false":
                    ini_dict[sectf] = False

        return ini_dict


def dump(file: Union[io.TextIOWrapper, str], ini_dict: dict) -> None:
    """dump a dictionary or a set to INI file format"""
    found_sect = False
    found_prop = False

    if type(file) is str:
        # file path in string
        file = open(file, "w")
    elif type(file) is not io.TextIOWrapper:
        raise IOError("file must be either file path in string or file pointer")

    for sect in ini_dict:
        if isinstance(ini_dict[sect], dict):
            if found_sect is False and found_prop is False:
                file.write(f"[{sect}]\n")
            else:
                file.write(f"\n[{sect}]\n")
            found_sect = True
            for prop in ini_dict[sect]:
                found_prop = True
                if ini_dict[sect][prop] is not None:
                    file.write(
                        f"{prop} = "
                        + "\n\t".join(str(ini_dict[sect][prop]).split("\n"))
                        + "\n"
                    )
                else:
                    file.write(f"{prop}\n")
        else:
            found_prop = True
            if ini_dict[sect] is not None:
                file.write(
                    f"{sect} = " + "\n\t".join(str(ini_dict[sect]).split("\n")) + "\n"
                )
            else:
                file.write(f"{sect}\n")

    file.close()
