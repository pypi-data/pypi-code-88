from dataclasses import dataclass
from enum import Flag, auto
import inspect
import textwrap
from typing import Any, Tuple

from discord.ext import commands
try:
    from discord.ext.commands.converter import _Greedy as greedy
except ImportError:
    from discord.ext.commands.converter import Greedy as greedy
    

class ArgumentType(Flag):
    """Represents type of argument."""
    required = auto()
    optional = auto()
    variable = auto()
    kwarg = auto()


def is_optional(annotation):
    return type(None) in getattr(annotation, '__args__', [])


class SpaceList(list):
    """
    A special list.
    When you pass this list to ``str``, content will be converted with :func:str, and joins them with space.
    """
    def __str__(self):
        return (" ".join([str(s) for s in self])).strip()


class Syntax(SpaceList):
    """Analyze command and make Syntax object.

    This inherits :class:`SpaceList`, so :func:str will return a formatted syntax.

    Parameters
    ----------
    command : commands.Command
        Command to analyze syntax.
    description : str, optional
        Description of the command.
        If None, use docstring.
    default_format : str, optional
        Format of regular argument, by default "{prefix}{variable_prefix}{command_name}{variable_suffix}{suffix}"
    kwarg_format : str, optional
        Format of keyword argument, by default "{prefix}{variable_prefix}{command_name}{variable_suffix}"
    required_formats : tuple, optional
        Prefix and suffix of required argument, by default ("<", ">")
    optional_formats : tuple, optional
        Prefix and suffix of optional argument, by default ("[", "]")
    variable_formats : tuple, optional
        Prefix and suffix of variable argument, by default ("", "...")
    """

    def __init__(self,
                 command: commands.Command, description: str = None, *,
                 default_format: str = "{prefix}{variable_prefix}{command_name}{variable_suffix}{suffix}",
                 kwarg_format: str = "{prefix}{variable_prefix}{command_name}{variable_suffix}",
                 required_formats: Tuple[str, str] = ("<", ">"),
                 optional_formats: Tuple[str, str] = ("[", "]"),
                 variable_formats: Tuple[str, str] = ("", "...")):
        if description is None:
            description = command.callback.__doc__
        self.name_count = 1
        parsed_desc = []
        for l in textwrap.dedent(description).split("\n"):
            if ": " not in l:
                continue
            parsed_desc.append(l.split(": ", 2))
        pp = None
        for p in reversed(command.parents):
            np = ParentName(p.name, pp)
            self.append(np)
            pp = np
            self.name_count += 1
        self.append(CommandName(command.name, pp))

        index = -1
        if list(inspect.signature(command.callback).parameters.keys())[0] == "self":
            index -= 1
        for pi, (pn, pv) in enumerate(inspect.signature(command.callback).parameters.items(), index):
            # print(pi, (pn, pv))
            if pi < 0:
                continue
            name = pn if pi >= len(parsed_desc) else parsed_desc[pi][0]
            desc = None if pi >= len(parsed_desc) else parsed_desc[pi][1]
            formats = {
                "prefix": "",
                "variable_prefix": "",
                "command_name": name,
                "variable_suffix": "",
                "suffix": ""
            }
            if pv.default != inspect.Signature.empty or is_optional(pv.annotation):
                formats["prefix"] = optional_formats[0]
                formats["suffix"] = optional_formats[1]
                flag = ArgumentType.optional
                default = pv.default
                required = False
            else:
                formats["prefix"] = required_formats[0]
                formats["suffix"] = required_formats[1]
                flag = ArgumentType.required
                default = None
                required = True
            if pv.kind == inspect.Parameter.VAR_POSITIONAL or isinstance(pv.annotation, greedy):
                formats["variable_prefix"] = variable_formats[0]
                formats["variable_suffix"] = variable_formats[1]
                flag |= ArgumentType.variable
            if pv.kind == inspect.Parameter.KEYWORD_ONLY:
                fmt = kwarg_format
                flag |= ArgumentType.kwarg
            else:
                fmt = default_format
            self.append(CommandArgument(name, required, desc, fmt.format(**formats), flag, default, pv))

    @property
    def args(self):
        """Returns SpaceList with command arguments."""
        return SpaceList(self[self.name_count:])

    @property
    def names(self):
        """Return SpaceList with command name and parents."""
        return SpaceList(self[:self.name_count])


@dataclass
class SyntaxElement():
    """Represents a element of a syntax."""
    name: str


@dataclass
class CommandName(SyntaxElement):
    """
    Represents name of a command.

    Parameters
    ----------
    name : str
        Name of the command.
    parent: ParentName
        Parent of the command, None if the command doesn't have a parent.
    """
    name: str
    parent: "ParentName" = None

    def __str__(self):
        return self.name


@dataclass
class ParentName(CommandName):
    """Represents parent name of a command."""
    pass


@dataclass
class CommandArgument(SyntaxElement):
    """Represents a command argument.

    ``str`` returns formatted value.

    Parameters
    ----------
    name : str
        Name of the argument.
    required : bool
        The argument is required or optional.
    description : str
        Description of the argument.
    formatted : str
        Formatted value for the argument.
    flag : int
        Type flag of the argument.
    default : Optional[Any]
        Default value of the argument if any.
    param : :class:inspect.Parameter
        Parameter for the argument.
    """
    name: str
    required: bool
    description: str
    formatted: str
    flag: ArgumentType
    default: Any
    param: inspect.Parameter

    def __str__(self):
        return self.formatted

    @property
    def optional(self):
        """Same as ``not self.required``."""
        return not self.required
