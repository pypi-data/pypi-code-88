# This file is part of pybib2web, a translator of BibTeX to HTML.
# https://gitlab.com/sosy-lab/software/pybib2web
#
# SPDX-FileCopyrightText: 2021 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: Apache-2.0

"""Module concerned with exporting BibTeX entries to HTML."""

import re
from collections import namedtuple, defaultdict
import logging
from pathlib import Path
from typing import Sequence, Iterable, Dict

from . import categories, bibexport, util
from .config import Config

Category = namedtuple("Category", ["name", "link"])

CATEGORY_ARTICLES = Category(
    "Articles in journal or book chapters", "Category/articles.html"
)
CATEGORY_BOOKS = Category("Books and proceedings", "Category/books.html")
BIBTYPE_NAMES = {
    "inproceedings": Category(
        "Articles in conference or workshop proceedings", "Category/conferences.html"
    ),
    "book": CATEGORY_BOOKS,
    "proceedings": CATEGORY_BOOKS,
    "inbook": CATEGORY_ARTICLES,
    "incollection": CATEGORY_ARTICLES,
    "article": CATEGORY_ARTICLES,
    "techreport": Category("Internal reports", "Category/reports.html"),
    "misc": Category(
        "Theses and projects (PhD, MSc, BSc, Project)", "Category/misc.html"
    ),
    "conferencetalk": Category(
        "Conference and other Presentations", "Category/conference-talks.html"
    ),
    "invitedtalk": Category(
        "Guest lectures, invited talks, and tutorials", "Category/invited-talks.html"
    ),
    "defense": Category("Thesis defenses", "Category/defenses.html"),
}


def to_html(entry, *, config: Config, single_indent: int = 2) -> str:
    elements = [
        indent(0, f'<li class="bibentry" id="{html_id(entry)}">'),
        indent(1, '<span class="main-info">'),
        indent(2, authors_to_html(entry, config)),
        indent(2, publication_title_to_html(entry, config)),
        indent(2, talk_type_to_html(entry, config)),
        indent(2, publication_venue_to_html(entry, config)),
        indent(2, publisher_to_html(entry)),
        indent(2, doi_to_html(entry)),
        indent(1, "</span>"),
        indent(
            1,
            f'<a class="bibentry-link" href="#{html_id(entry)}"><img height="12px" width="12px" src="https://www.sosy-lab.org/images/transparent.gif" alt="Link to this entry"></a>',
        ),
        indent(1, '<span class="additional-info">'),
        indent(2, '<span class="inline-info">'),
        indent(3, note_to_html(entry)),
        indent(3, keywords_to_html(entry)),
        indent(3, funders_to_html(entry)),
        indent(2, "</span>"),
        indent(2, '<span class="link-list">'),
        indent(3, publisher_version_to_html(entry)),
        indent(3, articlelink_to_html(entry)),
        indent(3, presentationlink_to_html(entry)),
        indent(3, videolink_to_html(entry)),
        indent(3, materiallink_to_html(entry)),
        indent(2, "</span>"),
        indent(2, artifacts_to_html(entry)),
        indent(2, abstract_to_html(entry)),
        indent(2, bibtex_to_html(entry)),
        indent(2, annotations_to_html(entry)),
        indent(1, "</span>"),
        indent(0, "</li>"),
    ]

    # remove all empty lines
    elements = [e for e in elements if e.strip()]
    return "\n".join(elements)


def indent(n: int, content, single_indent: int = 2):
    lines = content.split("\n")
    spaces = n * single_indent * " "
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)


def publication_title_to_html(entry, config):
    title = entry.get("title")
    if not title:
        return ""
    return f'<span class="publication-title">{title}.</span>'


def talk_type_to_html(entry, config):
    html = ""
    entrytype = entry["ENTRYTYPE"]
    if entrytype == "conferencetalk":
        html = "Conference talk"
    if entrytype == "invitedtalk":
        html = "Invited talk"
    if entrytype == "defense":
        html = "Defense"
    if html:
        html = f'<span class="talk-type">{html}</span>'
    return html


def annotations_to_html(entry):
    annote = entry.get("annote", "")
    if annote:
        return _create_details(
            "Additional Infos", annote, "annote", open_by_default=True
        )
    return ""


def abstract_to_html(entry):
    abstract = entry.get("abstract", "").strip()
    if abstract:
        return _create_details("Abstract", abstract, html_class="abstract")
    return ""


def _create_details(
    summary: str, details: str, html_class: str, open_by_default=False
) -> str:
    summary = f"<summary>{summary}</summary>"
    details = f"<div>\n{indent(1, details)}\n</div>"
    open_html = ""
    if open_by_default:
        open_html = "open"

    return f'<details {open_html} class="{html_class}">\n{indent(1, summary)}\n{indent(1, details)}\n</details>'


def bibtex_to_html(entry):
    if "original" in entry:
        entry = entry["original"]
    return _create_details("BibTeX Entry", bibexport.writes(entry), html_class="bibtex")


def authors_to_html(entry, config: Config):
    try:
        authors = get_authors(entry)
        authors_html = _get_list(authors, css_class="author", config=config) + "."
    except KeyError:
        try:
            authors = get_editors(entry)
            authors_html = (
                _get_list(authors, css_class="author", config=config)
                + ", editors"
                + "."
            )
        except KeyError:
            authors_html = ""
    if not authors_html:
        return ""
    return f'<span class="author-list">\n{indent(1, authors_html)}\n</span>'


def editors_to_html(entry, config: Config):
    try:
        editors = get_editors(entry)
        editors_html = (
            _get_list(editors, css_class="editor", config=config) + ", editors"
        )
    except KeyError:
        editors_html = ""
    if not editors_html:
        return ""
    return f'<span class="editor-list">\n{indent(1, editors_html)}\n</span>'


def funders_to_html(entry):
    try:
        funders = entry["funding"]
    except KeyError:
        return ""
    html_items = list()
    for f in funders:
        html_items.append(
            f'<a class="funding" href="../Funding/{_keyword_to_link(f)}">{f}</a>'
        )
    funders_html = ",\n".join(html_items)
    return f'<span class="funding-list">Funding:\n{indent(1, funders_html)}\n</span>'


def _get_list(
    elems,
    *,
    css_class,
    config: Config,
    delimiter_intermediate=",\n",
    delimiter_last=" and\n",
):
    ls = list()
    for a in elems:
        if config.index_author(a):
            a = f'<a href="../Author/{_author_to_link(a)}">{a}</a>'
        ls.append(f'<span class="{css_class}">{a}</span>')
    if len(ls) > 2:
        ls = [delimiter_intermediate.join(ls[:-1]), ls[-1]]
        if not delimiter_last.startswith(","):
            delimiter_last = ", " + delimiter_last
    assert (
        len(ls) <= 2
    ), f"There shouldn't be more than two elements after joining them with delimiter_intermediate: {ls}"
    return delimiter_last.join(ls)


def publication_venue_to_html(entry, config):
    def get_day_html(entry):
        day = entry.get("day", None)
        if not day:
            return ""
        return f'<span class="day">{day}.</span>'

    def get_month_html(entry):
        month = entry.get("month", None)
        if not month:
            return ""
        return f'<span class="month">{month}</span>'

    def get_year_html(entry):
        year = get_year(entry)
        if not year:
            return ""
        return f'<span class="year">{year}</span>'

    date_html = "\n".join(
        [
            e
            for e in [get_day_html(entry), get_month_html(entry), get_year_html(entry)]
            if e
        ]
    )
    if date_html:
        date = f'<span class="publication-date">\n{indent(1, date_html)}\n</span>'
    else:
        date = ""

    if entry["ENTRYTYPE"] == "techreport" and "number" in entry:
        howpublished = (
            f'Technical report <span class="report-number">{entry["number"]}</span>'
        )
    else:
        howpublished = ""
    try:
        institution = (
            f'<span class="publishing-institution">{entry["institution"]}</span>'
        )
    except KeyError:
        institution = ""
    try:
        venue = f'<span class="venue">at {entry["venue"]}</span>'
    except KeyError:
        venue = ""

    howpublished = ", ".join(
        [
            e
            for e in (venue, entry.get("howpublished", None), howpublished, institution)
            if e
        ]
    )
    if howpublished:
        howpublished = f'<span class="publicationmethod">{howpublished}</span>'
    else:
        howpublished = ""

    try:
        pages = entry["pages"]
    except KeyError:
        pages = ""

    if "journal" in entry:
        if pages:
            journal_pages = f'<span class="pages">:{pages}</span>'
            pages = ""
        else:
            journal_pages = ""
        journal = f"<em class=\"journaltitle\">{entry['journal']}</em>"
        try:
            volume = f", <span class=\"journalvolume\">{entry['volume']}</span>"
        except KeyError:
            volume = ""
        try:
            number = f"<span class=\"journalnumber\">({entry['number']})</span>"
        except KeyError:
            number = ""
        venue = f'<span class="journal">{journal}{volume}{number}{journal_pages}</span>'
    else:
        if "author" in entry:
            editors = editors_to_html(entry, config)
        else:
            editors = ""
        try:
            booktitle = (
                f"<em class=\"booktitle\">\n{indent(1, entry['booktitle'])}\n</em>"
            )
        except KeyError:
            logging.debug("No booktitle for %s", entry)
            booktitle = ""
        if pages:
            pages = f'<span class="pages">pages {pages}</span>'
        try:
            series = f"<span class=\"series\">{entry['series']}</span>"
        except KeyError:
            series = None
        venue = ""
        if booktitle:
            venue += "In "
        venue += ",\n".join([k for k in (editors, booktitle, series, pages) if k])
    all_infos = ",\n".join([e for e in (venue, howpublished, date) if e])
    return f'<span class="howpublished">\n{indent(1, all_infos)}.\n</span>'


def publisher_to_html(entry):
    try:
        return f"<span class=\"publisher\">{entry['publisher']}.</span>"
    except KeyError:
        return ""


def note_to_html(entry):
    try:
        return f'<span class="note">{entry["note"]}</span>'
    except KeyError:
        return ""


def artifacts_to_html(entry):
    artifact_keys = sorted([k for k in entry if re.match(r"artifact[0-9]*", k)])
    if not artifact_keys:
        return ""
    html_lines = list()
    for artifact in [entry[k] for k in artifact_keys]:
        html_lines.append(f'<a href="https://doi.org/{artifact}">doi:{artifact}</a>')
    assert len(html_lines) > 0
    html_lines = [f'<li class="artifact">{line}</li>' for line in html_lines]
    artifacts_html = "\n".join(html_lines)
    artifacts_html = f"<ol>\n{indent(1, artifacts_html)}\n</ol>"
    return _create_details("Artifact(s)", artifacts_html, "artifact-list")


def keywords_to_html(entry):
    keywords = get_keywords(entry)
    if not keywords:
        return ""
    keyword_htmls = [
        f'<a class="keyword" href="../Keyword/{_keyword_to_link(keyword)}">{keyword}</a>'
        for keyword in keywords
    ]
    keyword_html = ",\n".join(keyword_htmls)
    return f'<span class="keyword-list">Keyword(s):\n{indent(1, keyword_html)}\n</span>'


def articlelink_to_html(entry):
    try:
        link = entry["pdf"]
    except KeyError:
        return ""
    return f'<a class="pdf-link" href="{link}"><img alt="" height="17px" width="17px" src="https://www.sosy-lab.org/research/pub/Icons/pdf.gif">PDF</a>'


def presentationlink_to_html(entry):
    try:
        link = entry["presentation"]
    except KeyError:
        return ""
    return f'<a class="presentation-link" href="{link}"><img alt="" height="17px" width="17px" src="https://www.sosy-lab.org/research/pub/Icons/presentation.gif">Presentation</a>'


def materiallink_to_html(entry):
    try:
        link = entry["url"]
    except KeyError:
        return ""
    return f'<a class="material-link" href="{link}"><img alt="" height="15px" width="15px" src="https://www.sosy-lab.org/research/pub/Icons/www.gif">Supplement</a>'


def publisher_version_to_html(entry):
    description = "Link to official version of paper (may be a landing page with more information)"
    try:
        doi = get_doi(entry)
        return f'<a class="doi-link" href="https://doi.org/{doi}" title="{description}"><img alt="" height="17px" width="17px" src="https://www.sosy-lab.org/research/pub/Icons/doi.svg">Publisher\'s Version</a>'
    except KeyError:
        pass
    try:
        urn = get_urn(entry)
        return f'<a class="urn-link" href="https://nbn-resolving.org/process-urn-form?identifier={urn}&verb=REDIRECT" title="{description}">Publisher\'s Version</a>'
    except KeyError:
        return ""


def doi_to_html(entry):
    try:
        doi = get_doi(entry)
    except KeyError:
        return ""
    return f'<a class="doi" href="https://doi.org/{doi}" data-doi="{doi}" title="The digital object identifier permanently identifies a digital article or document.">doi:{doi}</a>'


def videolink_to_html(entry):
    try:
        video_url = entry["video"]
    except KeyError:
        return ""
    return f'<a class="video-link" href="{video_url}" title="Link to video presentation related to paper"><img alt="" height="17px" width="17px" src="https://www.sosy-lab.org/research/pub/Icons/video.gif">Video</a>'


def get_year(entry):
    return entry.get("year", None)


def get_keywords(entry):
    try:
        return [k for k in entry["keyword"] if k]
    except KeyError:
        return None


def get_authors(entry):
    return entry["author"]


def get_editors(entry):
    return entry["editor"]


def get_doi(entry):
    doi = entry["doi"]
    if not doi:
        raise KeyError
    return doi


def get_urn(entry):
    urn = entry["urn"]
    if not urn:
        raise KeyError
    return urn


def html_id(entry):
    return entry["ID"].replace(" ", "")


def writes(
    categorized_entries: Dict[Category, Sequence[dict]], *, config, header_title=None
) -> Iterable[str]:
    for category, entries in categorized_entries.items():
        if category.link:
            yield f'<a href="../{category.link}"><h3>{category.name}</h3></a>'
        else:
            yield f"<h3>{category.name}</h3>"
        yield ""
        yield f'<ol class="list-{header_title.lower().replace(" ", "-")}">'
        yield ""
        for entry in entries:
            yield to_html(entry, config=config)
            yield ""
        yield "</ol>"
    tail = config.tail
    if tail:
        yield tail


def write(
    entries: Dict[Category, Sequence[dict]],
    output_file,
    *,
    config,
    head=None,
    header_title=None,
):
    output_file = Path(output_file)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file, "w") as outp:
        if head:
            outp.write(head)
        outp.writelines(
            (
                f"{line}\n"
                for line in writes(entries, config=config, header_title=header_title)
            )
        )


def _get_header(header, show_link_to_index=True, show_link_to_all=True):
    def maybe_all():
        return ['<a href="../All/index.html">Show all</a>'] if show_link_to_all else []

    def maybe_index():
        return ['<a href="../index.html">Index</a>'] if show_link_to_index else []

    def links():
        links = maybe_all() + maybe_index()
        if not links:
            return ""
        return (
            f'<nav class="publication-navigation">({" &ndash; ".join(links)})</nav>\n'
        )

    return f"""
<input type="checkbox" id="show-compact">
<label for="show-compact">Compact view</label>
<h2 id="publications">{header}</h2>
{links()}"""


def write_html_tree(entries: Sequence[dict], output_root, *, config, header_title):
    output_root = Path(output_root)
    output_root.parent.mkdir(exist_ok=True)
    write_by_year(
        entries,
        output_file=output_root / "All" / "index.html",
        head=_get_header(header=header_title, show_link_to_all=False),
        header_title=header_title,
        config=config,
    )
    created_pages = {
        "all": [
            Category("Complete bibliography as a single HTML page", "All/index.html")
        ],
        "year": write_year_tree(
            entries, output_root / "Year", config=config, header_title=header_title
        ),
        "author": write_author_tree(
            entries,
            output_root / "Author",
            config=config,
            header_title=header_title,
        ),
        "funding": write_funding_tree(
            entries, output_root / "Funding", config=config, header_title=header_title
        ),
        "keyword": write_keyword_tree(
            entries, output_root / "Keyword", config=config, header_title=header_title
        ),
        "category": write_type_tree(
            entries, output_root / "Category", config=config, header_title=header_title
        ),
    }

    def name_sort(cat, key=None, **kwargs):
        if key is None:

            def key(n):
                return n

        return sorted(cat, key=lambda e: key(e.name), **kwargs)

    def index_page(header_title):
        yield _get_header(
            f"Index of {header_title}", show_link_to_all=False, show_link_to_index=False
        )
        yield '<h3 id="years">Selection by year</h3>'
        yield "<ul>"
        for name, link in name_sort(created_pages["year"], reverse=True):
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

        yield '<h3 id="categories">Selection by category</h3>'
        yield "<ul>"
        for name, link in name_sort(created_pages["category"]):
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

        yield '<h3 id="authors">Selection by author</h3>'
        yield "<ul>"
        for name, link in name_sort(
            created_pages["author"], key=lambda e: util.split_name(e)[-1]
        ):
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

        yield '<h3 id="research_interests">Selection by research interest</h3>'
        yield "<ul>"
        for name, link in name_sort(created_pages["keyword"]):
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

        yield '<h3 id="fundings">Selection by funding</h3>'
        yield "<ul>"
        for name, link in name_sort(created_pages["funding"]):
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

        yield '<h3 id="complete">Complete bibliography</h3>'
        yield "<ul>"
        for name, link in created_pages["all"]:
            yield f'<li><a href="{link}">{name}</a></li>'
        yield "</ul>"

    with open(output_root / "index.html", "w") as outp:
        outp.writelines([f"{line}\n" for line in index_page(header_title)])


def write_year_tree(entries: Sequence[dict], output_root, *, config, header_title):
    def _year_to_link(year):
        return f"{year}.html"

    def create():
        by_year = {
            Category(cat, Path(output_root.name) / _year_to_link(cat)): es
            for cat, es in categories.by_year(entries).items()
        }
        for year, es in by_year.items():
            output_file = output_root / year.link.name
            write_by_type(
                es,
                output_file,
                head=_get_header(f"{header_title} of year {year.name}"),
                config=config,
                header_title=header_title,
            )
            yield year

    return list(create())  # to make sure that everything is executed


def _unite_same_authors_long_and_shortform(by_author):
    author_pages = dict()
    Author = namedtuple("Author", ["name", "link", "entries"])
    for author, es in by_author.items():
        link = _author_to_link(author.name)
        if link not in author_pages:
            author_pages[link] = Author(author.name, link, [])
        assert util.equal_author(author.name, author_pages[link].name)
        if len(author.name) > len(author_pages[link].name):
            author_pages[link] = Author(
                author.name, author_pages[link].link, author_pages[link].entries
            )
        author_pages[link] = Author(
            author_pages[link].name,
            author_pages[link].link,
            author_pages[link].entries + es,
        )
    return {Category(a.name, a.link): a.entries for a in author_pages.values()}


def write_author_tree(
    entries: Sequence[dict], output_root, *, config, header_title
) -> Iterable[Category]:
    def create():
        by_author = {
            Category(cat, None): es
            for cat, es in categories.by_author(entries).items()
            if config.index_author(cat)
        }
        by_author = {
            Category(a.name, Path(output_root.name) / a.link): es
            for a, es in _unite_same_authors_long_and_shortform(by_author).items()
        }
        for author, es in by_author.items():
            output_file = output_root / author.link.name
            write_by_type(
                es,
                output_file,
                head=_get_header(f"{header_title} of {author.name}"),
                config=config,
                header_title=header_title,
            )
            yield author

    return list(create())  # to make sure that everything is executed


def write_keyword_tree(
    entries: Sequence[dict], output_root, *, config, header_title
) -> Iterable[Category]:
    def create():
        by_keyword = {
            Category(cat, Path(output_root.name) / _keyword_to_link(cat)): es
            for cat, es in categories.by_keyword(entries).items()
            if cat
        }
        for keyword, es in by_keyword.items():
            output_file = output_root / keyword.link.name
            write_by_type(
                es,
                output_file,
                head=_get_header(f"{header_title} about {keyword.name}"),
                config=config,
                header_title=header_title,
            )
            yield keyword

    return list(create())  # to make sure that everything is executed


def write_funding_tree(
    entries: Sequence[dict], output_root, *, config, header_title
) -> Iterable[Category]:
    def create():
        by_funding = {
            Category(cat, Path(output_root.name) / _keyword_to_link(cat)): es
            for cat, es in categories.by_funding(entries).items()
            if cat
        }
        for funding, es in by_funding.items():
            output_file = output_root / funding.link.name
            write_by_type(
                es,
                output_file,
                head=_get_header(f"Funding by {funding.name}"),
                config=config,
                header_title=header_title,
            )
            yield funding

    return list(create())  # to make sure that everything is executed


def _get_named_types(entries):
    by_type = categories.by_type(entries)
    named_types = defaultdict(list)
    for bibtype, entries in by_type.items():
        name = BIBTYPE_NAMES[bibtype]
        named_types[name] += entries
    return {k: categories.sort_by_year(v) for k, v in named_types.items()}


def write_type_tree(
    entries: Sequence[dict], output_root, *, config, header_title
) -> Iterable[Category]:
    def create():
        for bibtype, es in _get_named_types(entries).items():
            link = Path(bibtype.link)
            assert (
                output_root.name == link.parent.name
            ), f"{output_root.name} != {link.parent.name}"
            output_file = output_root / f"{link.name}"
            output_file = output_root / f"{link.name}"
            write_by_year(es, output_file, config=config, header_title=header_title)
            yield Category(bibtype.name, link)

    return list(create())  # to make sure that everything is executed


def write_by_type(entries: Sequence[dict], output_file, *, config, head, header_title):
    by_type = _get_named_types(entries)
    write(by_type, output_file, head=head, config=config, header_title=header_title)


def write_by_year(entries, output_file, *, config, header_title, head=None):
    def to_link(year):
        return f"Year/{year}.html"

    by_year = {
        Category(cat, to_link(cat)): es
        for cat, es in categories.by_year(entries).items()
    }
    if head is None:
        head = f"<h2>{header_title} by year</h2>"
    write(by_year, output_file, head=head, config=config, header_title=header_title)


def _keyword_to_link(keyword):
    assert keyword
    adjusted = re.sub("[()]", "", keyword.upper().replace(" ", "-"))
    return f"{adjusted}.html"


def _author_to_link(author):
    try:
        first_name, last_name = util.split_name(util.get_shortform(author))
        first_names = "".join(
            [f.upper()[0] for f in util.get_all_name_parts(first_name)]
        )
        return f"{last_name.upper()}-{first_names}.html"
    except IndexError:
        try:
            first_name, _, last_name = author.rpartition("~")
            return f"{last_name.upper()}-{first_name[0].upper()}.html"
        except IndexError:
            logging.exception("Author-link creation failed for %s", author)
            return None
