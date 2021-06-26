"""
html_tools.py

Tools for building HTML strings.
"""

import traceback
import difflib
import html
import os

from . import phrasing
from . import file_utils


STATUS_SYMBOLS = {
    "unknown": " ", # non-breaking space
    "not applicable": "–",
    "failed": "✗",
    "partial": "~",
    "accomplished": "✓",
}
"""
The symbols used as shorthand icons for each goal accomplishment status.
"""

SHORT_REPR_LIMIT = 160
"""
Limit in terms of characters before we try advanced formatting.
"""


def create_help_button(help_content):
    """
    Returns an HTML string for a button that can be clicked to display
    help. The button will have a question mark when collapsed and a dash
    when expanded, and the help will be displayed in a box on top of
    other content to the right of the help button.
    """
    return (
        '<details class="help_button">\n'
      + '<summary aria-label="More details"></summary>\n'
      + '<div class="help">{}</div>\n'
      + '</details>\n'
    ).format(help_content)


def build_list(items, ordered=False):
    """
    Builds an HTML <ul> tag, or an <ol> tag if `ordered` is set to True.
    Items must be a list of (possibly HTML) strings.
    """
    tag = "ol" if ordered else "ul"
    return (
        f"<{tag}>"
      + "\n".join(f"<li>{item}</li>" for item in items)
      + f"\n</{tag}>"
    )


def build_html_details(title, content, classes=None):
    """
    Builds an HTML details element with the given title as its summary
    and content inside. The classes are attached to the details element
    if provided, and should be a string.
    """
    return (
        '<details{}><summary>{}</summary>{}</details>'
    ).format(
        ' class="{}"'.format(classes) if classes is not None else "",
        title,
        content
    )


def build_html_tabs(tabs):
    """
    Builds an HTML structure incorporating JS code which uses several tab
    elements and a scrollable region to implement a multiple-tabs
    structure. The given tabs list should contain title, content pairs,
    where both titles and contents are strings that may contain HTML
    code.
    """
    tab_pieces = [
        (
            f"""
<li
 class='tab{" selected" if i == 0 else ""}' onclick='toggleTab();'
 tabindex="0"
 aria-label="Activate to display {title} after this list."
>
{title}
</li>
""",
            f"""
<section
 class='tab-content{" selected" if i == 0 else ""}'
 tabindex="0"
>
{content}
</section>
"""
        )
        for i, (title, content) in enumerate(tabs)
    ]
    tabs = '\n\n'.join([piece[0] for piece in tab_pieces])
    contents = '\n\n'.join([piece[1] for piece in tab_pieces])
    return f"""
<div class="tabs" role="presentation">
  <ul class="tabs-top">
{tabs}
  </ul>
  <div class="tabs-bot" aria-live="polite">
{contents}
  </div>
</div>
"""

def fileslug(filename):
    """
    Returns a safe-for-HTML-ID version of the given filename.
    """
    return filename\
        .replace(os.path.sep, '-')\
        .replace('.py', '')\
        .replace('.', '-')


def line_id(taskid, filename, lineno):
    """
    Generates an HTML ID for a code line, given the task ID, file name,
    and line number.
    """
    return f"{taskid}_{fileslug(filename)}_codeline_{lineno}"


def block_id(taskid, filename):
    """
    Generates an HTML ID for a code block, given the task ID and file
    name.
    """
    return f"{taskid}_code_{fileslug(filename)}"


def html_link_to_line(taskid, filename, lineno):
    """
    Returns an HTML <a> tag (as a string) that links to the specified
    line of code in the specified file of the specified task.
    """
    lineid = line_id(taskid, filename, lineno)
    return f'<a class="lineref" href="#{lineid}">{lineno}</a>'


def html_output_details(raw_output, title="Output"):
    """
    Takes raw program output and turns it into an expandable <details> tag
    with <pre> formatting.
    """
    return (
        '<details>\n'
      + '<summary>{}</summary>\n'
      + '<pre class="printed_output">{}</pre>\n'
        '</details>'
    ).format(
        title,
        raw_output
    )


def html_diff_table(
    output,
    reference,
    out_title='Actual output',
    ref_title='Expected output',
    joint_title=None,
    line_limit=300,
    trim_lines=1024
):
    """
    Uses difflib to create and return an HTML string that encodes a table
    comparing two (potentially multi-line) outputs. If joint_title is
    given, the result is wrapped into a <details> tag with that title and
    class diff_table.

    If line_limit is not None (the default is 300) then only that many
    lines of each output will be included, and a message about the
    limitation will be added.

    If the trim_lines value is None (the default is 1024) then the full
    value of every line will be included no matter how long it is,
    otherwise lines beyond that length will be trimmed to that length
    (with three periods added to indicate this).
    """
    if isinstance(output, str):
        output = output.split('\n')
    if isinstance(reference, str):
        reference = reference.split('\n')

    if line_limit and len(output) > line_limit or len(reference) > line_limit:
        result = "(comparing the first {})<br>\n".format(
            phrasing.obj_num(line_limit, "line")
        )
        output = output[:line_limit]
        reference = reference[:line_limit]
    else:
        result = ""

    if (
        trim_lines
    and (
            any(len(line) > trim_lines for line in output)
         or any(len(line) > trim_lines for line in reference)
        )
    ):
        result += (
            "(comparing the first {} on each line)<br>\n"
        ).format(phrasing.obj_num(trim_lines, "character"))
        output = [
            line[:trim_lines] + ('...' if len(line) > trim_lines else '')
            for line in output
        ]
        reference = [
            line[:trim_lines] + ('...' if len(line) > trim_lines else '')
            for line in reference
        ]

    result += difflib.HtmlDiff().make_table(
        output,
        reference,
        fromdesc=out_title,
        todesc=ref_title,
    )
    if joint_title is None:
        return result
    else:
        return build_html_details(joint_title, result, classes="diff_table")


def status_css_class(status):
    """
    Returns the CSS class used to indicate the given status.
    """
    return "status_" + status.replace(' ', '_')


def build_status_indicator(status):
    """
    Builds a single div that indicates the given goal accomplishment
    status.
    """
    status_class = status_css_class(status)
    status_symbol = STATUS_SYMBOLS.get(status, "!")
    return '<div class="goal_status {stc}">{sy}</div>'.format(
        stc=status_class,
        sy=status_symbol
    )


def indent(string, indent):
    """
    Indents a string using spaces. Newlines will be '\\n' afterwards.
    """
    lines = string.splitlines()
    return '\n'.join(' ' * indent + line for line in lines)


def big_repr(thing):
    """
    A function that works like repr, but with some extra formatting for
    special known cases when the results would be too large.
    """
    base = repr(thing)
    if len(base) > SHORT_REPR_LIMIT:
        if type(thing) in (tuple, list, set): # NOT isinstance
            # left and right delimeters
            ld, rd = repr(type(thing)())
            stuff = ',\n'.join(big_repr(elem) for elem in thing)
            return ld + '\n' + indent(stuff, 2) + '\n' + rd
        elif type(thing) is dict: # NOT isinstance
            stuff = ',\n'.join(
                big_repr(key) + ": " + big_repr(value)
                for key, value in thing.items()
            )
            return '{\n' + indent(stuff, 2) + '\n}'
        # else we fall out and return base

    return base


def truncate(text, limit=50000, tag='\n...truncated...'):
    """
    Truncates the given text so that it does not exceed the given limit
    (in terms of characters; default 50K)

    If the text actually is truncated, the string '\\n...truncated...'
    will be added to the end of the result to indicate this, but an
    alternate tag may be specified; the tag characters are not counted
    against the limit, so it's possible for this function to actually
    make a string longer if it starts out longer than the limit by less
    than the length of the tag.
    """
    if len(text) > limit:
        return text[:limit] + tag
    else:
        return text


def build_display_box(text):
    """
    Creates a disabled textarea element holding the given text. This
    allows for a finite-size element to contain (potentially a lot) of
    text that the user can scroll through or even search through.
    """
    # TODO: A disabled textarea is such a hack! Instead, use an inner pre
    # inside an outer div with CSS to make it scrollable.
    return f'<textarea class="display_box" disabled>{text}</textarea>'


def dynamic_html_repr(thing, reasonable=300, limit=10000):
    """
    A dynamic representation of an object which is simply a pre-formatted
    string for objects whose representations are reasonably small, and
    which turns into a display box for representations which are larger,
    with text being truncated after a (very large) limit.

    The threshold for reasonably small representations as well as the
    hard limit may be customized; use None for the hard limit to disable
    truncation entirely (but don't complain about file sizes if you do).
    """
    rep = big_repr(thing)
    if len(rep) <= reasonable:
        return f'<pre class="short_repr">{rep}</pre>'
    else:
        return build_display_box(truncate(rep, limit))


def html_traceback(title=None):
    """
    In an exception handler, returns an HTML string that includes the
    exception type, message, and traceback. Must be called from an except
    clause.

    If title is given and not None, a <details> tag will be returned
    using that title, which can be expanded to show the traceback,
    otherwise just a <pre> tag is returned containing the traceback.
    """
    result = string_traceback()
    pre = '<pre class="traceback">\n{}\n</pre>'.format(result)
    if title is not None:
        return build_html_details(title, pre, "error")
    else:
        return pre


def string_traceback():
    """
    When called in an exception handler, returns a multi-line string
    including what Python would normally print: the exception type,
    message, and a traceback.

    The traceback gets obfuscated by replacing full file paths that start
    with the potluck directory with just the package directory and
    filename, and by replacing full file paths that start with the spec
    directory with just the task ID and then the file path from the spec
    directory (usually starter/, soln/, or the submitted file itself).
    """
    psd = file_utils.potluck_src_dir()
    sfd = os.path.split(file_utils.get_spec_file_name())[0]

    raw = traceback.format_exc()

    # TODO: What about submitted files?
    return rewrite_traceback_filenames(
        raw,
        {
            psd: "potluck",
            sfd: "<task>"
        }
    )


def rewrite_traceback_filenames(raw_traceback, prefix_map):
    """
    Accepts a traceback as a string, and returns a modified string where
    filenames have been altered by replacing the keys of the given
    prefix_map with their values.
    """
    result = raw_traceback
    for prefix in prefix_map:
        replace = prefix_map[prefix]
        result = result.replace(f'File "{prefix}', f'File "{replace}')

    return result


def function_def_code_tags(fn_name, args_pattern, announce=None):
    """
    Returns a tuple containing two strings of HTML code used to represent
    the given function definition in both short and long formats. The
    short format just lists the first acceptable definition, while the
    long format lists all of them. Note that both fn_name and
    args_pattern may be lists of strings instead of strings; see
    function_def_patterns.
    """
    if isinstance(fn_name, str):
        names = [fn_name]
    else:
        names = list(fn_name)

    # If there are specific args we can give users more info about what
    # they need to do.
    if isinstance(args_pattern, str):
        specific_names = [
            "{}({})".format(name, args_pattern) for name in names
        ]
    else:
        specific_names = names

    # Figure out what we're announcing as:
    if announce is None:
        announce = specific_names[0]

    # Make code tag and detailed code tag:
    code_tag = "<code>{}</code>".format(announce)
    details_code = phrasing.comma_list(
        ["<code>{}</code>".format(n) for n in specific_names],
        junction="or"
    )

    return code_tag, details_code


def function_call_code_tags(fn_name, args_pattern, is_method=False):
    """
    Works like `potluck.patterns.function_call_patterns`, but generates a
    pair of HTML strings with summary and detailed descriptions of the
    function call. In that sense it's also similar to
    `function_def_code_tags`, except that it works for a function call
    instead of a function definition.
    """
    if isinstance(fn_name, str):
        names = [fn_name]
    else:
        names = list(fn_name)

    # If there are specific args we can give users more info about what
    # they need to do.
    if isinstance(args_pattern, str):
        if is_method:
            specific_names = [
                ".{}({})".format(name, args_pattern)
                for name in names
            ]
        else:
            specific_names = [
                "{}({})".format(name, args_pattern)
                for name in names
            ]
    else:
        specific_names = names

    # Make code tag and detailed code tag:
    code_tag = "<code>{}</code>".format(
        html.escape(specific_names[0])
    )

    details_code = phrasing.comma_list(
        [
            "<code>{}</code>".format(html.escape(name))
            for name in specific_names
        ],
        junction="or"
    )

    return code_tag, details_code


def args_repr_list(args, kwargs):
    """
    Creates an HTML string representation of the given positional and
    keyword arguments, as a bulleted list.
    """
    arg_items = []
    for arg in args:
        arg_items.append(dynamic_html_repr(arg))

    for kw in kwargs:
        key_repr = dynamic_html_repr(kw)
        val_repr = dynamic_html_repr(kwargs[kw])
        arg_items.append(key_repr + "=" + val_repr)

    return build_list(arg_items)
