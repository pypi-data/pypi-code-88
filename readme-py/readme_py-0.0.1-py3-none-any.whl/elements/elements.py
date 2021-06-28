from dataclasses import dataclass
from typing import List
from abc import abstractmethod, ABCMeta


class Element(metaclass=ABCMeta):

    @abstractmethod
    def to_markdown(self) -> str:
        pass


@dataclass
class Link(Element):
    text: str
    href: str

    def to_markdown(self) -> str:
        return f"[{self.text}]({self.href})"


@dataclass
class Image(Element):
    alt: str
    src: str

    def to_markdown(self) -> str:
        return f"![{self.alt}]({self.src})"


class Li(Element):
    elements: List[Element] = []

    def __init__(self, elements: List[Element] = []) -> None:
        self.elements = elements

    def add(self, element: Element) -> None:
        self.elements.append(element)

    def to_markdown(self) -> None:
        pass


class ULi(Li):
    def to_markdown(self) -> str:
        from ..generator import md
        return "\n".join([f"-\t{md(el)}" for el in self.elements])


class OLi(Li):
    def to_markdown(self) -> str:
        from ..generator import md
        return "\n".join([f"{i+1}.\t{md(self.elements[i])}" for i in range(len(self.elements))])


@dataclass
class P(Element):
    text: str = ""

    def to_markdown(self) -> str:
        return self.text


@dataclass
class Header(Element):
    size: int
    text: str

    def to_markdown(self) -> str:
        return f"{'#'*self.size} {self.text}"


class Br(Element):
    def to_markdown(self) -> str:
        return "\n"


class Hr(Element):
    def to_markdown(self) -> str:
        return "---"


class Table(Element):
    data: List[dict]
    keys: List[str]
    capitalized_headers: bool = True

    def __init__(self, data: List[dict], keys: List[str], capitalized_headers: bool = True) -> None:
        self.data = data
        self.keys = keys
        self.capitalized_headers = capitalized_headers

    def to_markdown(self) -> str:
        markdown_text = ""
        markdown_text += "| "+" | ".join([key.capitalize() if self.capitalized_headers else key for key in self.keys]) + " |\n"
        markdown_text += '| ----------- '*len(self.keys)+"|\n"
        for d in self.data:
            markdown_text += "| "+" | ".join([d.get(key, "") for key in self.keys]) + " |\n"
        return markdown_text.strip("\n")


@dataclass
class CodeBlock(Element):
    lang: str
    code: str

    def to_markdown(self) -> str:
        from ..generator import md
        return f"""```{self.lang}\n{self.code.strip()}\n```"""


class TaskList(Element):
    @dataclass
    class Task:
        text: str
        checked: bool = False

    tasks: List[Task]

    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    def to_markdown(self) -> str:
        return "\n".join([f"- [{'x' if task.checked else ' '}] {task.text}" for task in self.tasks])


@dataclass
class BlockQuote(Element):
    text: str

    def to_markdown(self) -> str:
        return f"> {self.text}"


@dataclass
class Strikethrough(Element):
    text: str

    def to_markdown(self) -> str:
        return f"~~{self.text}~~"


class DefinitionList(Element):
    text: str
    items: List[Element]

    def __init__(self, text: str, items: List[Element]) -> None:
        self.text = text
        self.items = items

    def to_markdown(self) -> str:
        from ..generator import md
        return "\n".join([self.text, *[f":\t{md(item)}" for item in self.items]])

@dataclass
class Footnote(Element):
    text: str
    definition: Element

    def to_markdown(self) -> str:
        from .utils import gen_random
        from ..generator import md
        random_smth = gen_random()
        return f"{self.text} [^{random_smth}]\n [^{random_smth}]: {md(self.definition)}"
