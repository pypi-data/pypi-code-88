"""
Class with file-like interface to a file found in provided search path

See top level package docstring for documentation
"""

import logging
import os
import pathlib
import re
import typing

import attr

myself = pathlib.Path(__file__).stem

# configure library-specific logger
logger = logging.getLogger(myself)
logging.getLogger(myself).addHandler(logging.NullHandler())

try:
    import optini
    logger.debug('loaded optional module optini')
except ModuleNotFoundError as e:
    logger.debug(f"optional module not found: {e}")

########################################################################

# exceptions


class Error(Exception):
    pass


class NoMatchError(Error):
    pass


class AmbiguousMatchError(Error):
    def __init__(self, found):
        self.found = found
        self.message = f"matches found: {found}"


########################################################################


@attr.s(auto_attribs=True)
class DisFile:
    """
    Class with file-like interface to a file found in provided search path

    - To get filename of disambiguated file, evaluate in string context
    - Supports `with` context statements
    - Raises exceptions if file is ambiguous
        - All module exceptions inherit from disambigufile.Error

    See `help(disambigufile)` for examples

    Attributes
    ----------

    pattern : str
        Regular expression describing desired match
    expand : bool, default=True
        Expand ~ and environment variables in path components
    path : str, default=None
        Directories to search (colon-separated)
    subpattern : str, default=None
        Regular expression describing secondary match
    pathopt : str, default='path'
        Option name when using configuration data

    Raises
    ------
    NoMatchError
    AmbiguousMatchError
    """
    pattern: str
    expand: bool = True
    path: str = None
    subpattern: str = None
    pathopt: str = 'path'
    pathlist: typing.List[str] = attr.Factory(list)

    def __attrs_post_init__(self):
        """Constructor"""

        self._determine_pathlist()
        self._search()
        if len(self.found) == 0:
            raise NoMatchError
        if len(self.found) > 1:
            raise AmbiguousMatchError(self.found)
        # if no exceptions, there will be an unambiguous match
        # use hit() or open() to interact with the item found

    def _determine_pathlist(self):
        """Determine final path to search"""

        # add any directories provided by parameter
        if self.path is not None:
            self.pathlist += self.path.split(':')

        # add paths from options if present
        try:
            if self.pathopt in optini.opt:
                paths = optini.opt.path.split(':')
                logger.debug(f"adding paths from options: {paths}")
                self.pathlist += paths
        except (AttributeError, NameError):
            pass

        # strip out trailing slashes
        self.pathlist = map(lambda x: x.rstrip('/'), self.pathlist)
        # expand ~ and environment variables
        if self.expand:
            self.pathlist = self._expandpath(self.pathlist)

    def _expandstr(self, x):
        """Expand ~ and then expand environment variables"""
        logger.debug(f"expanding {x}")
        return os.path.expandvars(os.path.expanduser(x))

    def _expandpath(self, pathlist):
        """Expand elements of path"""
        return list(map(lambda x: self._expandstr(x), pathlist))

    def _search_path_for_file(self, pattern, pathlist):
        """Return list of files matching pattern in a path"""

        # filter out missing directories
        pathlist = filter(lambda x: os.path.isdir(x), pathlist)
        files = []
        for dir in pathlist:
            for file in os.listdir(dir):
                if re.search(pattern, file):
                    files.append(f"{dir}/{file}")
        return(files)

    def _search(self):
        """Search path for matching files"""

        logger.debug(f"considering {self.pathlist}")
        # search for matches with each element of path
        found = self._search_path_for_file(self.pattern, self.pathlist)

        if self.subpattern is not None:
            # if unambiguous, found will be a single-item list
            # however, directories might have multiple matches & 1 sub-match
            # example, pattern = asdf, subpattern = data
            # if asdf1/data and asdf2 both exist, asdf1/data is unique
            newfound = []
            for x in found:
                if os.path.isdir(x):
                    submatches = filter(
                        lambda x: re.search(self.subpattern, x),
                        os.listdir(x),
                    )
                    for submatch in submatches:
                        newfound.append(f"{x}/{submatch}")
                else:
                    newfound.append(x)
            found = newfound

        self.found = found

    def hit(self):
        """return filename of disambiguated file"""
        logger.debug(f"hit: {self.found[0]}")
        return self.found[0]

    def open(self, mode='r'):
        """open disambiguated file and return file-like object"""
        self._f = open(self.hit(), mode)
        return self._f

    def __str__(self):
        return self.hit()

    def __enter__(self):
        return self.open()

    def __exit__(self):
        self._f.close()
