"""lsf.py  -- Lion's Sectioned Format

LSF (Lion's Sectioned Format) is a plain-text container format.

It features:
* a header section,
* unlimited content sections,
* titles for content sections,
* tags for all sections,
* body text for each section,
* UTF-8 encoding.

More information:  https://github.com/LionKimbro/lsf


loadfile(p)  -- load an LSF file into data structures from path
loadstr(s)  -- load an LSF-formatted string into data structures

savefile(L, p)  -- save data structures to an LSF file at a path
savestr(L)  -- write data structures to an LSF-formatted string

find_titled(L, title)  -- return sublist of sections with matching title
find_tagged(L, key, tags)  -- return sublist including these tags
find_matching(L, key, value)  -- return sublist including key-val pair

append(L, title, D, body)  -- add a new section to a list

sections  -- list of dictionaries, x1 per section, in sequence
  TITLE  -- str, title of the section (or None, if header section)
  TITLELN  -- line# of title (or None, if header section)
  KEYS  -- dictionary, keys-to-string values (can be empty)
  BODY  -- string, body for the section (or None)
  BODYLN  -- line# of beginning of body (if there is one; else None)

encoding  -- encoding for file reading, writing (default: utf-8)
"""


TITLE = "TITLE"
TITLELN = "TITLELN"
KEYS = "KEYS"
BODY = "BODY"
BODYLN = "BODYLN"

encoding = "utf-8"


def loadfile(p):
    """Load an LSF file, and return it's list of sections.

    :param p: path to file to load
    :type p: full or relative path, string
    :return: list of section dictionaries representing the LSF file
    :rtype: list of dictionaries with keys TITLE, KEYS, and BODY
    """
    return loadstr(open(p, "r", encoding=encoding).read())


def loadstr(s):
    """Interpret an LSF string, and return it's list of sections.

    :param s: string content to interpret
    :type s: string (unicode)
    :return: list of section dictionaries representing the LSF file
    :rtype: list of dictionaries with keys TITLE, KEYS, and BODY
    """
    lineno = 0  # line number processing
    L = []  # results
    title = None  # first section has no title
    titleln = None  # first section has no title
    D = {}  # key-value dictionary being read
    B = []  # body accumulator
    bodyln = None  # never guaranteed
    def store():
        L.append({TITLE: title,
                  TITLELN: titleln,
                  KEYS: D.copy(),
                  BODY: "\n".join(B),
                  BODYLN: bodyln if B else None})
    state = "D"  # state "D": (loading dictionary w/ k-v pairs)
    for line in s.splitlines():
        if state == "D":
            if line == "":
                state = "B"; bodyln = lineno+1  # -> state "B": (body)
            else:
                try: k, v = line.split(": ", 1); D[k] = v
                except ValueError:
                    raise ValueError("bad k-v pair: "+line)
        else:
            if line.startswith("== ") and line.endswith(" =="):
                store()  # store previously noted entry
                D.clear(); del B[:]; title = line[3:-3]
                titleln = lineno; state = "D"
            else: B.append(line)
        lineno += 1
    store()
    return L


def savefile(L, p):
    """Save a list of sections to an LSF file.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :param p: path to file to save to
    :type p: full or relative path, string
    """
    open(p, "w", encoding=encoding).write(savestr(L))


def savestr(L):
    """Save a list of sections to a string.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :return: string content to interpret
    :rtype: string (unicode)
    """
    R = []  # results output
    def lsfout(title, D, body):
        if title is not None: R.append("== " + title + " ==")
        for k in D: R.append(k + ": " + str(D[k]))
        R.append("");
        R.extend((body+"\n").splitlines())
    if L: lsfout(None, L[0][KEYS], L[0][BODY])
    for section in L[1:]:
        lsfout(section[TITLE], section[KEYS], section[BODY])
    return "\n".join(R)+"\n"


def find_titled(L, title):
    """Return list of all sections with the given title.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :param title: title to locate in list of dictionaries
    :type title: str (title)
    :return: list of matching section dictionaries
    :rtype: list of dictionaries with keys TITLE, KEYS, and BODY
    """
    return [section for section in L if section[TITLE] == title]


def find_tagged(L, key, tags):
    """Return list of all sections with a given tag.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :param key: name of key that lists tags
    :type key: string (key identifier)
    :param tags: space delimited list of tags to require in results
    :type tags: string (space delimited tags list)
    :return: list of matching section dictionaries
    :rtype: list of dictionaries with keys TITLE, KEYS, and BODY
    """
    tags_set = set(tags.split())
    return [sec for sec in L  # sec: a section dictionary
            if tags_set.issubset(set(sec[KEYS].get(key, "").split()))]


def find_matching(L, key, value):
    """Return list of all sections with a given key-value match.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :param key: name of key that lists tags
    :type key: string (key identifier)
    :param value: exact string value to locate
    :type value: string (match string)
    :return: list of matching section dictionaries
    :rtype: list of dictionaries with keys TITLE, KEYS, and BODY
    """
    return [sec for sec in L if sec[KEYS].get(key) == value]


def append(L, title, D, body):
    """Add a new section to a list.

    :param L: list of section dictionaries representing the LSF file
    :type L: list of dictionaries with keys TITLE, KEYS, and BODY
    :param title: title of new section
    :type title: str (title)
    :param D: key-value pairs of new section
    :type D: dict (string key: string value)
    :param body: body content
    :type body: str
    """
    L.append({TITLE: title, KEYS: D, BODY: body})

