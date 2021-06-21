import itertools
import re

import black.linegen as black
from black import main
from black.strings import STRING_PREFIX_CHARS, sub_twice

_fix_docstring = black.fix_docstring


# copied from https://github.com/psf/black/blob/main/src/black/lines.py#L382
# replace 4 spaces with 2 spaces


def __str__(self) -> str:
  if not self:
    return '\n'

  indent = '  ' * self.depth
  leaves = iter(self.leaves)
  first = next(leaves)
  res = f'{first.prefix}{indent}{first.value}'
  for leaf in leaves:
    res += str(leaf)
  for comment in itertools.chain.from_iterable(self.comments.values()):
    res += str(comment)

  return res + '\n'


def fixDocString(docstring: str, prefix: str) -> str:
  return _fix_docstring(docstring, ' ' * (len(prefix) >> 1))


# copied from https://github.com/psf/black/blob/main/src/black/strings.py#L145
# change " to '
# comment out 'Prefer double quotes'


def singleQuote(s: str) -> str:
  """Prefer double quotes but only if it doesn't cause more escaping.

  Adds or removes backslashes as appropriate. Doesn't parse and fix
  strings nested in f-strings.
  """
  value = s.lstrip(STRING_PREFIX_CHARS)
  if value[:3] == '"""':
    return s

  elif value[:3] == "'''":
    orig_quote = "'''"
    new_quote = '"""'
  elif value[0] == '"':
    orig_quote = '"'
    new_quote = "'"
  else:
    orig_quote = "'"
    new_quote = "'"  # '"'
  first_quote_pos = s.find(orig_quote)
  if first_quote_pos == -1:
    return s  # There's an internal error

  prefix = s[:first_quote_pos]
  unescaped_new_quote = re.compile(rf'(([^\\]|^)(\\\\)*){new_quote}')
  escaped_new_quote = re.compile(rf'([^\\]|^)\\((?:\\\\)*){new_quote}')
  escaped_orig_quote = re.compile(rf'([^\\]|^)\\((?:\\\\)*){orig_quote}')
  body = s[first_quote_pos + len(orig_quote) : -len(orig_quote)]
  if 'r' in prefix.casefold():
    if unescaped_new_quote.search(body):
      # There's at least one unescaped new_quote in this raw string
      # so converting is impossible
      return s

    # Do not introduce or remove backslashes in raw strings
    new_body = body
  else:
    # remove unnecessary escapes
    new_body = sub_twice(escaped_new_quote, rf'\1\2{new_quote}', body)
    if body != new_body:
      # Consider the string without unnecessary escapes as the original
      body = new_body
      s = f'{prefix}{orig_quote}{body}{orig_quote}'
    new_body = sub_twice(escaped_orig_quote, rf'\1\2{orig_quote}', new_body)
    new_body = sub_twice(unescaped_new_quote, rf'\1\\{new_quote}', new_body)
  if 'f' in prefix.casefold():
    matches = re.findall(
      r"""
      (?:[^{]|^)\{  # start of the string or a non-{ followed by a single {
          ([^{].*?)  # contents of the brackets except if begins with {{
      \}(?:[^}]|$)  # A } followed by end of the string or a non-}
      """,
      new_body,
      re.VERBOSE,
    )
    for m in matches:
      if '\\' in str(m):
        # Do not introduce backslashes in interpolated expressions
        return s

  if new_quote == '"""' and new_body[-1:] == '"':
    # edge case:
    new_body = new_body[:-1] + '\\"'
  orig_escape_count = body.count('\\')
  new_escape_count = new_body.count('\\')
  if new_escape_count > orig_escape_count:
    return s  # Do not introduce more escaping

  # if new_escape_count == orig_escape_count and orig_quote == '"':
  #     return s  # Prefer double quotes

  return f'{prefix}{new_quote}{new_body}{new_quote}'


black.Line.__str__ = __str__
black.fix_docstring = fixDocString
black.normalize_string_quotes = singleQuote

if __name__ == '__main__':
  main()
