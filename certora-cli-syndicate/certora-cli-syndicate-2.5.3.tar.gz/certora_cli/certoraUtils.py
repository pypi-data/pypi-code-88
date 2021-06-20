import argparse
import json
import os
from enum import Enum
import pkg_resources
import sys
import platform
import shlex
import shutil
import re
import queue
import math
from typing import Any, Callable, Dict, List, Optional, Set, Union
from certora_cli.certoraTester import compareResultsWithExpected, get_errors, has_violations, get_violations

LEGAL_CERTORA_KEY_LENGTHS = [32, 40]

# bash colors
BASH_ORANGE_COLOR = "\033[33m"
BASH_END_COLOR = "\033[0m"
BASH_GREEN_COLOR = "\033[32m"
BASH_RED_COLOR = "\033[31m"

VERIFICATION_ERR_MSG_PREFIX = "Prover found violations:"
VERIFICATION_SUCCESS_MSG = "No errors found by Prover!"

DEFAULT_SOLC = "solc"
DEFAULT_CLOUD_ENV = 'production'
DEFAULT_STAGING_ENV = 'master'
OPTION_OUTPUT_VERIFY = "output_verify"
ENVVAR_CERTORA = "CERTORA"

CERTORA_CONFIG_DIR = ".certora_config"  # folder
CERTORA_BUILD_FILE = ".certora_build.json"
CERTORA_VERIFY_FILE = ".certora_verify.json"
PACKAGE_FILE = "package.json"
RECENT_JOBS_FILE = ".certora_recent_jobs.json"


class SolcCompilationException(Exception):
    pass


COINBASE_FEATURES_MODE_CONFIG_FLAG = '-coinbaseFeaturesMode'

MIN_JAVA_VERSION = 11  # minimal java version to run the local type checker jar


def get_version() -> str:
    """
    @return: The version of the Certora CLI's python package in format XX.YY if found, an error message otherwise
    """
    # Note: the only valid reason not to have an installed certora-cli package is in circleci
    try:
        version = pkg_resources.get_distribution("certora-cli").version
        return version
    except pkg_resources.DistributionNotFound:
        return "couldn't find certora-cli distributed package. Try\n pip install certora-cli"


def check_results_from_file(output_path: str) -> bool:
    with open(output_path) as output_file:
        actual = json.load(output_file)
        return check_results(actual)


def check_results(actual: Dict[str, Any]) -> bool:
    actual_results = actual
    expected_filename = "expected.json"
    based_on_expected = os.path.exists(expected_filename)
    if based_on_expected:  # compare actual results with expected
        with open(expected_filename) as expectedFile:
            expected = json.load(expectedFile)
            if "rules" in actual_results and "rules" in expected:
                is_equal = compareResultsWithExpected("test", actual_results["rules"], expected["rules"], {}, {})
            elif "rules" not in actual_results and "rules" not in expected:
                is_equal = True
            else:
                is_equal = False

        if is_equal:
            print_completion_message(f"{VERIFICATION_SUCCESS_MSG} (based on expected.json)")
            return True
        # not is_equal:
        error_str = get_errors()
        if error_str:
            print_error(VERIFICATION_ERR_MSG_PREFIX, error_str)
        if has_violations():
            print_error(VERIFICATION_ERR_MSG_PREFIX)
            get_violations()
        return False

    # if expected results are not defined
    # traverse results and look for violation
    errors = []
    result = True

    if "rules" not in actual_results:
        errors.append("No rules in results")
        result = False
    elif len(actual_results["rules"]) == 0:
        errors.append("No rule results found. Please make sure you wrote the rule and method names correctly.")
        result = False
    else:
        for rule in actual_results["rules"].keys():
            rule_result = actual_results["rules"][rule]
            if isinstance(rule_result, str) and rule_result != 'SUCCESS':
                errors.append("[rule] " + rule)
                result = False
            elif isinstance(rule_result, dict):
                # nested rule - ruleName: {result1: [functions list], result2: [functions list] }
                nesting = rule_result
                violating_functions = ""
                for method in nesting.keys():
                    if method != 'SUCCESS' and len(nesting[method]) > 0:
                        violating_functions += '\n  [func] ' + '\n  [func] '.join(nesting[method])
                        result = False
                if violating_functions:
                    errors.append("[rule] " + rule + ":" + violating_functions)

    if not result:
        print_error(VERIFICATION_ERR_MSG_PREFIX)
        print('\n'.join(errors))
        return False

    print_completion_message(VERIFICATION_SUCCESS_MSG)
    return True


def debug_print_(s: str, debug: bool = False) -> None:
    # TODO: delete this when we have a logger
    if debug:
        print("DEBUG:", s, flush=True)


def print_error(title: str, txt: str = "", flush: bool = False) -> None:
    print(BASH_RED_COLOR + title + BASH_END_COLOR, txt, flush=flush)


def fatal_error(s: str, debug: bool = False) -> None:
    print_error("Fatal error:", s, True)
    if debug:
        raise Exception(s)
    sys.exit(1)


def print_warning(txt: str, flush: bool = False) -> None:
    print(BASH_ORANGE_COLOR + "WARNING:" + BASH_END_COLOR, txt, flush=flush)


def print_completion_message(txt: str, flush: bool = False) -> None:
    print(BASH_GREEN_COLOR + txt + BASH_END_COLOR, flush=flush)


def is_windows() -> bool:
    return platform.system() == 'Windows'


def get_file_basename(file: str) -> str:
    return ''.join(file.split("/")[-1].split(".")[0:-1])


def replace_file_name(file_with_path: str, new_file_name: str) -> str:
    """
    :param file_with_path: the full original path
    :param new_file_name: the new base name of the file
    :return: file_with_path with the base name of the file replaced with new_file_name,
             preserving the file extension and the base path
    """
    return '/'.join(file_with_path.split("/")[:-1] + [f"{new_file_name}.{get_file_extension(file_with_path)}"])


def get_file_extension(file: str) -> str:
    return file.split("/")[-1].split(".")[-1]


def get_path_as_list(file: str) -> List[str]:
    return os.path.normpath(file).split(os.path.sep)


def safe_create_dir(path: str, revert: bool = True, debug: bool = False) -> None:
    if os.path.isdir(path):
        debug_print_(f"directory {path} already exists", debug)
        return
    try:
        os.mkdir(path)
    except OSError as e:
        debug_print_(f"Failed to create directory {path}: {e}", debug)
        if revert:
            raise e


def as_posix(path: str) -> str:
    """
    Converts path from windows to unix
    :param path: Path to translate
    :return: A unix path
    """
    return path.replace("\\", "/")


def abs_posix_path(path: str) -> str:
    """
    Returns the absolute path, unix style
    :param path: Path to change
    :return: A posix style absolute path
    """
    return as_posix(os.path.abspath(os.path.expanduser(path)))


def getcwd() -> str:
    return as_posix(os.getcwd())


def remove_and_recreate_dir(path: str, debug: bool = False) -> None:
    if os.path.isdir(path):
        shutil.rmtree(path)
    safe_create_dir(path, debug=debug)


def prepare_call_args(cmd: str) -> List[str]:
    split = shlex.split(cmd)
    if split[0].endswith('.py'):
        # sys.executable returns a full path to the current running python, so it's good for running our own scripts
        certora_root = get_certora_root_directory()
        args = [sys.executable] + [as_posix(os.path.join(certora_root, split[0]))] + split[1:]
    else:
        args = split
    return args


def get_certora_root_directory() -> str:
    return os.getenv(ENVVAR_CERTORA, os.getcwd())


def which(filename: str) -> Optional[str]:
    if is_windows() and not re.search(r"\.exe$", filename):
        filename += ".exe"

    # TODO: find a better way to iterate over all directories in path
    for dirname in os.environ['PATH'].split(os.pathsep) + [os.getcwd()]:
        candidate = os.path.join(dirname, filename)
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return filename

    return None


def read_json_file(file_name: str) -> Dict[str, Any]:
    with open(file_name) as json_str:
        json_obj = json.load(json_str)
        return json_obj


def write_json_file(data: Union[Dict[str, Any], List[Dict[str, Any]]], file_name: str) -> None:
    with open(file_name, "w+") as json_str:
        json.dump(data, json_str)


class NoValEnum(Enum):
    """
    A class for an enum where the numerical value has no meaning.
    """

    def __repr__(self) -> str:
        """
        Do not print the value of this enum, it is meaningless
        """
        return f'<{self.__class__.__name__}.{self.name}>'


class Mode(NoValEnum):
    """
    Mode of operation - the 5 modes are mutually exclusive:

    1. CLI parameters consist of a single .tac file.
        We check the verification condition given by that file.
    2. CLI parameters consist of a single .conf file.
        A .conf file is created on each tool run inside the .certora_config directory. It contains the command line
        options that were used for the run (in a parsed format).
        We take the options given from that file as a basis for this run; additionally given command line options
        override options given in the .conf file.
    3. CLI parameters consist of one or more Solidity (.sol) files and the `--assert` option is set.
        We create and check verification conditions based on the `assert` statements in the given solidity contracts.
    4. CLI parameters consist of one or more Solidity (.sol) files and the `--verify` option is set (the option takes
        an additional .spec/.cvl file).
        We use the given .spec/.cvl file to create and check verification conditions for the given solidity contracts.
    5. CLI parameters consist of a single .json file.
        The .json file must be in the format created e.g. by SmtTimeoutReporting.kt. This mode will take the
        .certoraBuild, .certoraVerify, and .certora_config, contents, as well as the configuration information (command
        line arguments) that are stored inside the json and start a CVT run using those files/parameters.
    """
    TAC = "a single .tac file"
    CONF = "a single .conf file"
    VERIFY = "using --verify"
    ASSERT = "using --assert"
    REPLAY = "a single .json file"


def is_hex_or_dec(s: str) -> bool:
    """
    @param s: A string
    @return: True if it a decimal or hexadecimal number
    """
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def is_hex(number: str) -> bool:
    """
    @param number: A string
    @return: True if the number is a hexadecimal number:
        - Starts with 0
        - Second character is either x or X
        - All other characters are digits 0-9, or letters a-f or A-F
    """
    match = re.search(r'^0[xX][0-9a-fA-F]+$', number)
    return match is not None


def hex_str_to_cvt_compatible(s: str) -> str:
    """
    @param s: A string representing a number in base 16 with '0x' prefix
    @return: A string representing the number in base 16 but without the '0x' prefix
    """
    assert is_hex(s)
    return re.sub(r'^0[xX]', '', s)


def decimal_str_to_cvt_compatible(s: str) -> str:
    """
    @param s: A string representing a number in base 10
    @return: A string representing the hexadecimal representation of the number, without the '0x' prefix
    """
    assert s.isnumeric()
    return re.sub(r'^0[xX]', '', hex(int(s)))


def split_by_commas_ignore_parenthesis(s: str) -> List[str]:
    """
    Split `s` by top-level commas only. Commas within parentheses are ignored. Handles nested parentheses.

    s = "-b=2, -assumeUnwindCond, -rule=bounded_supply, -m=withdrawCollateral(uint256, (bool, bool)), -regressionTest"

    will return:
    ['-b=2',
    '-assumeUnwindCond',
    '-rule=bounded_supply',
    '-m=withdrawCollateral(uint256, (bool, bool))',
    '-regressionTest']

    @param s a string
    @returns a list of strings
    """

    # Parse the string tracking whether the current character is within parentheses.
    balance = 0
    parts = []
    part = ''

    for c in s:
        part += c
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
            if balance < 0:
                raise argparse.ArgumentTypeError(f"Imbalanced parenthesis in --settings str: {s}")
        elif c == ',' and balance == 0:
            parts.append(part[:-1].strip())
            part = ''

    # Capture last part
    if len(part):
        parts.append(part.strip())

    return parts


def input_string_distance(input_str: str, dictionary_str: str) -> float:
    """
    Calculates a modified levenshtein distance between two strings. The distance function is modified to penalize less
    for more common user mistakes.
    Each subtraction, insertion or replacement of a character adds 1 to the distance of the two strings, unless:
    1. The input string is a prefix of the dictionary string or vice versa - the distance is 0.1 per extra letter.
    2. The replacement is between two equal letter except casing - adds nothing to the distance
    3. The subtraction/addition is of an underscore, adds 0.1 to the distance

    :param input_str: the string the user gave as input, error-prone
    :param dictionary_str: a legal string we compare the wrong input to
    :return a distance measure between the two string. A low number indicates a high probably the user to give the
            dictionary string as input
    """
    # treat special cases first:

    input_str = input_str.lower()
    dictionary_str = dictionary_str.lower()

    if input_str == dictionary_str:
        return 0
    if dictionary_str.startswith(input_str) or input_str.startswith(dictionary_str):
        diff = abs(len(input_str) - len(dictionary_str))
        return 0.1 * diff

    # Initialize matrix of zeros
    rows = len(input_str) + 1
    cols = len(dictionary_str) + 1

    distance_matrix = []
    for row in range(rows):
        column = []
        for j in range(cols):
            column.append(0.0)
        distance_matrix.append(column)

    # Populate matrix of zeros with the indices of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance_matrix[i][0] = i
            distance_matrix[0][k] = k

    for _col in range(1, cols):
        for row in range(1, rows):
            if input_str[row - 1] == dictionary_str[_col - 1]:
                # No cost if the characters are the same up to casing in the two strings in a given position [i,j]
                cost: float = 0
            elif input_str[row - 1] == '_' or dictionary_str[_col - 1] == '_':
                cost = 0.1
            else:
                cost = 1
            distance_matrix[row][_col] = min(distance_matrix[row - 1][_col] + cost,           # Cost of deletions
                                             distance_matrix[row][_col - 1] + cost,         # Cost of insertions
                                             distance_matrix[row - 1][_col - 1] + cost)     # Cost of substitutions

    return distance_matrix[row][_col]


def get_closest_strings(input_word: str, word_dictionary: List[str],
                        distance: Callable[[str, str], float] = input_string_distance,
                        max_dist: float = 4, max_dist_ratio: float = 0.5, max_suggestions: int = 2,
                        max_delta: float = 0.2) -> List[str]:
    """
    Gets an input word, which doesn't belong to a dictionary of predefined words, and returns a list of closest words
    from the dictionary, with respect to a distance function.

    :param input_word: The word we look for closest matches of.
    :param word_dictionary: A collection of words to suggest matches from.
    :param distance: The distance function we use to measure proximity of words.
    :param max_dist: The maximal distance between words, over which no suggestions will be made.
    :param max_dist_ratio: A maximal ratio between the distance and the input word's length. No suggestions will be made
                           over this ratio.
    :param max_suggestions: The maximal number of suggestions to return.
    :param max_delta: We stop giving suggestions if the next best suggestion is worse than the one before it by more
                      than the maximal delta.
    :return: A list of suggested words, ordered from the best match to the worst.
    """
    distance_queue: queue.PriorityQueue = queue.PriorityQueue()  # Ordered in a distance ascending order

    for candidate_word in word_dictionary:
        dist = distance(input_word, candidate_word)
        distance_queue.put((dist, candidate_word))

    all_suggestions: List[str] = []
    last_dist = None

    while not distance_queue.empty() and len(all_suggestions) <= max_suggestions:
        suggested_dist, suggested_rule = distance_queue.get()
        if suggested_dist <= max_dist and suggested_dist / len(input_word) < max_dist_ratio \
                and ((last_dist is None) or (suggested_dist - last_dist <= max_delta)):
            all_suggestions.append(suggested_rule)
            last_dist = suggested_dist

    return all_suggestions


def get_readable_time(milliseconds: int) -> str:
    # calculate (and subtract) whole hours
    milliseconds_in_hour = 3600000  # 1000 * 60 * 60
    hours = math.floor(milliseconds / milliseconds_in_hour)
    milliseconds -= hours * milliseconds_in_hour

    # calculate (and subtract) whole minutes
    milliseconds_in_minute = 60000  # 1000 * 60
    minutes = math.floor(milliseconds / milliseconds_in_minute)
    milliseconds -= minutes * milliseconds_in_minute

    # seconds
    seconds = math.floor(milliseconds / 1000)

    milliseconds -= seconds * 1000
    duration = ""

    if hours > 0:
        duration += f"{hours}h "
    duration += f"{minutes}m {seconds}s {milliseconds}ms"
    return duration


def flush_stdout() -> None:
    print("", flush=True)


def flatten_set_list(set_list: List[Set[Any]]) -> List[Any]:
    """
    Gets a list of sets, returns a list that contains all members of all sets without duplicates
    :param set_list: A list containing sets of elements
    :return: A list containing all members of all sets. There are no guarantees on the order of elements.
    """
    ret_set = set()
    for _set in set_list:
        for member in _set:
            ret_set.add(member)
    return list(ret_set)
