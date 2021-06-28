from ..elements import Element, Link, Header, Br
from typing import List, Any


class Section:
    title: str = ""
    inner: List[Element] = []
    header_size: int = 2
    have_header: bool = True
    space_between_elements = True

    def to_markdown(self):
        from ..generator import md
        markdown_text: str = ""
        markdown_text += (md(Header(self.header_size, self.title)) + md(Br())*2) if self.have_header else ""

        for el in self.inner:
            markdown_text += md(el) + ((md(Br())*2) if self.space_between_elements else "")

        return markdown_text


class Readme:
    title: str = ""
    description: str = ""
    badges: List[Any] = []
    sections: List[Section] = []
    have_header: bool = True

    def __init__(self, title: str = "", description: str = "", sections: List[Section] = [], badges: List[Any] = [], have_header: bool = True) -> None:
        self.title = title
        self.description = description
        self.badges = badges
        self.sections = sections
        self.have_header = have_header

    def to_markdown(self):
        from ..generator import md
        markdown_text: str = ""
        markdown_text += (md(Header(1, self.title)) + md(Br())*2) if self.have_header else ""

        for section in self.sections:
            markdown_text += md(section)

        return markdown_text


class LicenseSection(Section):
    def __init__(self, license_type: str, license_link: str) -> None:
        self.title = "License"
        self.inner.append(Link(license_type, license_link))
