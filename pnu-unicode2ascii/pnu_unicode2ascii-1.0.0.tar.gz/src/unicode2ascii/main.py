#!/usr/bin/env python
""" Unicode 2 Ascii command-line tool and library
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Hubert Tournier
"""

import getopt
import logging
import os
import sys
import unicodedata

# Version string used by the what(1) and ident(1) commands:
ID = "@(#) $Id: unicode2ascii - Unicode to Ascii command-line tool and library v1.0.0 (June 19, 2021) by Hubert Tournier $"

# Conversion table for Unicode characters incorrectly translated to ASCII:
corrected_unicode_to_ascii = {
    "¼": "1/4",
    "½": "1/2",
    "¾": "3/4",
    "⅐": "1/7",
    "⅑": "1/9",
    "⅒": "1/10",
    "⅓": "1/3",
    "⅔": "2/3",
    "⅕": "1/5",
    "⅖": "2/5",
    "⅗": "3/5",
    "⅘": "4/5",
    "⅙": "1/6",
    "⅚": "5/6",
    "⅛": "1/8",
    "⅜": "3/8",
    "⅝": "5/8",
    "⅞": "7/8",
    "⅟": "1/",
    "↉": "0/3",
}

# Conversion table for Unicode characters with no translation to ASCII:
additional_unicode_to_ascii = {
    "‱": " ",  # PER TEN THOUSAND SIGN
    "—": "-",  # EM DASH
    "–": "-",  # EN DASH
    "‒": "-",  # FIGURE DASH
    "―": "-",  # HORIZONTAL BAR
    "‐": "-",  # HYPHEN
    "⁃": "-",  # HYPHEN BULLET
    "‧": "-",  # HYPHENATION POINT
    "˗": "-",  # MODIFIER LETTER MINUS SIGN
    "‑": "-",  # NON-BREAKING HYPHEN
    "ʽ": ",",  # MODIFIER LETTER REVERSED COMMA
    "ʻ": ",",  # MODIFIER LETTER TURNED COMMA
    "⁏": ";",  # REVERSED SEMICOLON
    "ˑ": ":",  # MODIFIER LETTER HALF TRIANGULAR COLON
    "˸": ":",  # MODIFIER LETTER RAISED COLON
    "ː": ":",  # MODIFIER LETTER TRIANGULAR COLON
    "⁝": ":",  # TRICOLON
    "⁞": ":",  # VERTICAL FOUR DOTS
    "¡": "!",  # INVERTED EXCLAMATION MARK
    "¬": "!",  # NOT SIGN
    "‽": "?!",  # INTERROBANG
    "¿": "?",  # INVERTED QUESTION MARK
    "⁙": ".....",  # FIVE DOT PUNCTUATION
    "⁛": "....",  # FOUR DOT MARK
    "⁘": "....",  # FOUR DOT PUNCTUATION
    "⁖": "...",  # THREE DOT PUNCTUATION
    "⁚": "..",  # TWO DOT PUNCTUATION
    "•": ".",  # BULLET
    "·": ".",  # MIDDLE DOT
    "⁜": ".+.",  # DOTTED CROSS
    "※": ".x.",  # REFERENCE MARK
    "⁗": "''''",  # QUADRUPLE PRIME
    "‷": "'''",  # REVERSED TRIPLE PRIME
    "‴": "'''",  # TRIPLE PRIME
    "″": "''",  # DOUBLE PRIME
    "˶": "''",  # MODIFIER LETTER MIDDLE DOUBLE ACUTE ACCENT
    "‶": "''",  # REVERSED DOUBLE PRIME
    "ˊ": "'",  # MODIFIER LETTER ACUTE ACCENT
    "ʼ": "'",  # MODIFIER LETTER APOSTROPHE
    "ˏ": "'",  # MODIFIER LETTER LOW ACUTE ACCENT
    "ʹ": "'",  # MODIFIER LETTER PRIME
    "′": "'",  # PRIME
    "‵": "'",  # REVERSED PRIME
    "’": "'",  # RIGHT SINGLE QUOTATION MARK
    "‚": "'",  # SINGLE LOW-9 QUOTATION MARK
    "°": "°",  # DEGREE SIGN
    "©": "(c)",  # COPYRIGHT SIGN
    "¶": "(p)",  # PILCROW SIGN
    "⁋": "(q)",  # REVERSED PILCROW SIGN
    "®": "(r)",  # REGISTERED SIGN
    "§": "(s)",  # SECTION SIGN
    "⁅": "[",  # LEFT SQUARE BRACKET WITH QUILL
    "⁆": "]",  # RIGHT SQUARE BRACKET WITH QUILL
    "⁌": "*",  # BLACK LEFTWARDS BULLET
    "⁍": "*",  # BLACK RIGHTWARDS BULLET
    "⁕": "*",  # FLOWER PUNCTUATION MARK
    "⁎": "*",  # LOW ASTERISK
    "×": "*",  # MULTIPLICATION SIGN
    "‣": "*",  # TRIANGULAR BULLET
    "⁑": "**",  # TWO ASTERISKS ALIGNED VERTICALLY
    "⁂": "***",  # ASTERISM
    "÷": "/",  # DIVISION SIGN
    "⁄": "/",  # FRACTION SLASH
    "‟": '"',  # DOUBLE HIGH-REVERSED-9 QUOTATION MARK
    "„": '"',  # DOUBLE LOW-9 QUOTATION MARK
    "ˮ": '"',  # MODIFIER LETTER DOUBLE APOSTROPHE
    "ʺ": '"',  # MODIFIER LETTER DOUBLE PRIME
    "”": '"',  # RIGHT DOUBLE QUOTATION MARK
    "⁒": "%",  # COMMERCIAL MINUS SIGN
    "‰": "%0",  # PER MILLE SIGN
    "‘": "`",  # LEFT SINGLE QUOTATION MARK
    "ˋ": "`",  # MODIFIER LETTER GRAVE ACCENT
    "ˎ": "`",  # MODIFIER LETTER LOW GRAVE ACCENT
    "˴": "`",  # MODIFIER LETTER MIDDLE GRAVE ACCENT
    "‛": "`",  # SINGLE HIGH-REVERSED-9 QUOTATION MARK
    "“": "``",  # LEFT DOUBLE QUOTATION MARK
    "˵": "``",  # MODIFIER LETTER MIDDLE DOUBLE GRAVE ACCENT
    "‸": "^",  # CARET
    "ˆ": "^",  # MODIFIER LETTER CIRCUMFLEX ACCENT
    "˰": "^",  # MODIFIER LETTER LOW UP ARROWHEAD
    "˄": "^",  # MODIFIER LETTER UP ARROWHEAD
    "˖": "+",  # MODIFIER LETTER PLUS SIGN
    "±": "+/-",  # PLUS-MINUS SIGN
    "˿": "<-",  # MODIFIER LETTER LOW LEFT ARROW
    "˂": "<",  # MODIFIER LETTER LEFT ARROWHEAD
    "˱": "<",  # MODIFIER LETTER LOW LEFT ARROWHEAD
    "‹": "<",  # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    "«": "<<",  # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    "˲": ">",  # MODIFIER LETTER LOW RIGHT ARROWHEAD
    "˃": ">",  # MODIFIER LETTER RIGHT ARROWHEAD
    "›": ">",  # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    "»": ">>",  # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    "¦": "|",  # BROKEN BAR
    "‖": "||",  # DOUBLE VERTICAL LINE
    "˷": "~",  # MODIFIER LETTER LOW TILDE
    "⁓": "~",  # SWUNG DASH
    "↊": "2",  # TURNED DIGIT TWO
    "↋": "3",  # TURNED DIGIT THREE
    "¢": "c",  # CENT SIGN
    "¤": "currency",  # CURRENCY SIGN
    "£": "GBP",  # POUND SIGN
    "¥": "JPY",  # YEN SIGN
    "µ": "mu",  # MICRO SIGN
    "˅": "v",  # MODIFIER LETTER DOWN ARROWHEAD
    "˯": "v",  # MODIFIER LETTER LOW DOWN ARROWHEAD
    "ↀ": "_I",  # ROMAN NUMERAL ONE THOUSAND C D
    "ↁ": "_V",  # ROMAN NUMERAL FIVE THOUSAND
    "ↂ": "_X",  # ROMAN NUMERAL TEN THOUSAND
    "ↆ": "L",  # ROMAN NUMERAL FIFTY EARLY FORM
    "ↇ": "_L",  # ROMAN NUMERAL FIFTY THOUSAND
    "ↈ": "_C",  # ROMAN NUMERAL ONE HUNDRED THOUSAND
    "ↅ": "6",  # ROMAN NUMERAL SIX LATE FORM
    "Æ": "AE",  # LATIN CAPITAL LETTER AE
    "Ǽ": "AE",  # LATIN CAPITAL LETTER AE WITH ACUTE
    "Ǣ": "AE",  # LATIN CAPITAL LETTER AE WITH MACRON
    "æ": "ae",  # LATIN SMALL LETTER AE
    "ǽ": "ae",  # LATIN SMALL LETTER AE WITH ACUTE
    "ǣ": "ae",  # LATIN SMALL LETTER AE WITH MACRON
    "Ⱥ": "A",  # LATIN CAPITAL LETTER A WITH STROKE
    "Ƀ": "B",  # LATIN CAPITAL LETTER B WITH STROKE
    "ƀ": "b",  # LATIN SMALL LETTER B WITH STROKE
    "Ɓ": "B",  # LATIN CAPITAL LETTER B WITH HOOK
    "Ƃ": "B",  # LATIN CAPITAL LETTER B WITH TOPBAR
    "ƃ": "b",  # LATIN SMALL LETTER B WITH TOPBAR
    "Ȼ": "C",  # LATIN CAPITAL LETTER C WITH STROKE
    "ȼ": "c",  # LATIN SMALL LETTER C WITH STROKE
    "Ƈ": "C",  # LATIN CAPITAL LETTER C WITH HOOK
    "ƈ": "c",  # LATIN SMALL LETTER C WITH HOOK
    "ↄ": "c",  # LATIN SMALL LETTER REVERSED C
    "Ↄ": "C",  # ROMAN NUMERAL REVERSED ONE HUNDRED
    "Đ": "D",  # LATIN CAPITAL LETTER D WITH STROKE
    "đ": "d",  # LATIN SMALL LETTER D WITH STROKE
    "Ð": "ETH",  # LATIN CAPITAL LETTER ETH
    "ð": "eth",  # LATIN SMALL LETTER ETH
    "ȸ": "db",  # LATIN SMALL LETTER DB DIGRAPH
    "Ɖ": "D",  # LATIN CAPITAL LETTER AFRICAN D
    "Ɗ": "D",  # LATIN CAPITAL LETTER D WITH HOOK
    "Ƌ": "D",  # LATIN CAPITAL LETTER D WITH TOPBAR
    "ƌ": "d",  # LATIN SMALL LETTER D WITH TOPBAR
    "ȡ": "d",  # LATIN SMALL LETTER D WITH CURL
    "Ɇ": "E",  # LATIN CAPITAL LETTER E WITH STROKE
    "ɇ": "e",  # LATIN SMALL LETTER E WITH STROKE
    "Ǝ": "E",  # LATIN CAPITAL LETTER REVERSED E
    "ǝ": "e",  # LATIN SMALL LETTER TURNED E
    "Ə": "SCHWA",  # LATIN CAPITAL LETTER SCHWA
    "ə": "schwa",  # LATIN SMALL LETTER SCHWA
    "Ɛ": "E",  # LATIN CAPITAL LETTER OPEN E
    "Ƒ": "F",  # LATIN CAPITAL LETTER F WITH HOOK
    "ƒ": "f",  # LATIN SMALL LETTER F WITH HOOK
    "Ǥ": "G",  # LATIN CAPITAL LETTER G WITH STROKE
    "ǥ": "g",  # LATIN SMALL LETTER G WITH STROKE
    "Ɠ": "G",  # LATIN CAPITAL LETTER G WITH HOOK
    "Ɣ": "g",  # LATIN CAPITAL LETTER GAMMA
    "Ƣ": "OI",  # LATIN CAPITAL LETTER OI
    "ƣ": "oi",  # LATIN SMALL LETTER OI
    "Ħ": "H",  # LATIN CAPITAL LETTER H WITH STROKE
    "ħ": "h",  # LATIN SMALL LETTER H WITH STROKE
    "ƕ": "hv",  # LATIN SMALL LETTER HV
    "Ƕ": "HWAIR",  # LATIN CAPITAL LETTER HWAIR
    "ʱ": "h",  # MODIFIER LETTER SMALL H WITH HOOK
    "ı": "i",  # LATIN SMALL LETTER DOTLESS I
    "Ɨ": "I",  # LATIN CAPITAL LETTER I WITH STROKE
    "Ɩ": "I",  # LATIN CAPITAL LETTER IOTA
    "ȷ": "j",  # LATIN SMALL LETTER DOTLESS J
    "Ɉ": "J",  # LATIN CAPITAL LETTER J WITH STROKE
    "ɉ": "j",  # LATIN SMALL LETTER J WITH STROKE
    "Ƙ": "K",  # LATIN CAPITAL LETTER K WITH HOOK
    "ƙ": "k",  # LATIN SMALL LETTER K WITH HOOK
    "Ł": "L",  # LATIN CAPITAL LETTER L WITH STROKE
    "ł": "l",  # LATIN SMALL LETTER L WITH STROKE
    "Ƚ": "L",  # LATIN CAPITAL LETTER L WITH BAR
    "ƚ": "l",  # LATIN SMALL LETTER L WITH BAR
    "ȴ": "l",  # LATIN SMALL LETTER L WITH CURL
    "ƛ": "l",  # LATIN SMALL LETTER LAMBDA WITH STROKE
    "Ɲ": "N",  # LATIN CAPITAL LETTER N WITH LEFT HOOK
    "Ƞ": "N",  # LATIN CAPITAL LETTER N WITH LONG RIGHT LEG
    "ƞ": "n",  # LATIN SMALL LETTER N WITH LONG RIGHT LEG
    "ȵ": "n",  # LATIN SMALL LETTER N WITH CURL
    "Ŋ": "ENG",  # LATIN CAPITAL LETTER ENG
    "ŋ": "eng",  # LATIN SMALL LETTER ENG
    "Ø": "O",  # LATIN CAPITAL LETTER O WITH STROKE
    "Ǿ": "O",  # LATIN CAPITAL LETTER O WITH STROKE AND ACUTE
    "ø": "o",  # LATIN SMALL LETTER O WITH STROKE
    "ǿ": "o",  # LATIN SMALL LETTER O WITH STROKE AND ACUTE
    "Œ": "OE",  # LATIN CAPITAL LIGATURE OE
    "œ": "oe",  # LATIN SMALL LIGATURE OE
    "Ɔ": "O",  # LATIN CAPITAL LETTER OPEN O
    "Ɵ": "O",  # LATIN CAPITAL LETTER O WITH MIDDLE TILDE
    "Ȣ": "OU",  # LATIN CAPITAL LETTER OU
    "ȣ": "ou",  # LATIN SMALL LETTER OU
    "Ƥ": "P",  # LATIN CAPITAL LETTER P WITH HOOK
    "ƥ": "p",  # LATIN SMALL LETTER P WITH HOOK
    "ȹ": "qp",  # LATIN SMALL LETTER QP DIGRAPH
    "Ɋ": "Q",  # LATIN CAPITAL LETTER SMALL Q WITH HOOK TAIL
    "ɋ": "q",  # LATIN SMALL LETTER Q WITH HOOK TAIL
    "ĸ": "kra",  # LATIN SMALL LETTER KRA
    "Ʀ": "YR",  # LATIN LETTER YR
    "Ɍ": "R",  # LATIN CAPITAL LETTER R WITH STROKE
    "ɍ": "r",  # LATIN SMALL LETTER R WITH STROKE
    "ʴ": "r",  # MODIFIER LETTER SMALL TURNED R
    "ʵ": "r",  # MODIFIER LETTER SMALL TURNED R WITH HOOK
    "ɼ": "r",  # LATIN SMALL LETTER R WITH LONG LEG
    "ʶ": "R",  # MODIFIER LETTER SMALL CAPITAL INVERTED R
    "ß": "ss",  # LATIN SMALL LETTER SHARP S
    "ȿ": "s",  # LATIN SMALL LETTER S WITH SWASH TAIL
    "Ʃ": "ESH",  # LATIN CAPITAL LETTER ESH
    "ƪ": "esh",  # LATIN LETTER REVERSED ESH LOOP
    "Ŧ": "T",  # LATIN CAPITAL LETTER T WITH STROKE
    "ŧ": "t",  # LATIN SMALL LETTER T WITH STROKE
    "Ⱦ": "T",  # LATIN CAPITAL LETTER T WITH DIAGONAL STROKE
    "ƫ": "t",  # LATIN SMALL LETTER T WITH PALATAL HOOK
    "Ƭ": "T",  # LATIN CAPITAL LETTER T WITH HOOK
    "ƭ": "t",  # LATIN SMALL LETTER T WITH HOOK
    "Ʈ": "T",  # LATIN CAPITAL LETTER T WITH RETROFLEX HOOK
    "ȶ": "t",  # LATIN SMALL LETTER T WITH CURL
    "Ʉ": "U",  # LATIN CAPITAL LETTER U BAR
    "Ɯ": "M",  # LATIN CAPITAL LETTER TURNED M
    "Ʊ": "U",  # LATIN CAPITAL LETTER UPSILON
    "Ʋ": "V",  # LATIN CAPITAL LETTER V WITH HOOK
    "Ʌ": "V",  # LATIN CAPITAL LETTER TURNED V
    "Ɏ": "Y",  # LATIN CAPITAL LETTER Y WITH STROKE
    "ɏ": "y",  # LATIN SMALL LETTER Y WITH STROKE
    "Ƴ": "Y",  # LATIN CAPITAL LETTER Y WITH HOOK
    "ƴ": "y",  # LATIN SMALL LETTER Y WITH HOOK
    "Ȝ": "YOGH",  # LATIN CAPITAL LETTER YOGH
    "ȝ": "yogh",  # LATIN SMALL LETTER YOGH
    "ƍ": "d",  # LATIN SMALL LETTER TURNED DELTA
    "Ƶ": "Z",  # LATIN CAPITAL LETTER Z WITH STROKE
    "ƶ": "z",  # LATIN SMALL LETTER Z WITH STROKE
    "Ȥ": "Z",  # LATIN CAPITAL LETTER Z WITH HOOK
    "ȥ": "z",  # LATIN SMALL LETTER Z WITH HOOK
    "ɀ": "z",  # LATIN SMALL LETTER Z WITH SWASH TAIL
    "Ʒ": "EZH",  # LATIN CAPITAL LETTER EZH
    "Ǯ": "EZH",  # LATIN CAPITAL LETTER EZH WITH CARON
    "ʒ": "ezh",  # LATIN SMALL LETTER EZH
    "ǯ": "ezh",  # LATIN SMALL LETTER EZH WITH CARON
    "Ƹ": "EZH",  # LATIN CAPITAL LETTER EZH REVERSED
    "ƹ": "ezh",  # LATIN SMALL LETTER EZH REVERSED
    "ƺ": "ezh",  # LATIN SMALL LETTER EZH WITH TAIL
    "Þ": "THORN",  # LATIN CAPITAL LETTER THORN
    "þ": "thorn",  # LATIN SMALL LETTER THORN
    "Ƿ": "WYNN",  # LATIN CAPITAL LETTER WYNN
    "ƿ": "wynn",  # LATIN LETTER WYNN
    "ƻ": "2",  # LATIN LETTER TWO WITH STROKE
    "Ƨ": "2",  # LATIN CAPITAL LETTER TONE TWO
    "ƨ": "2",  # LATIN SMALL LETTER TONE TWO
    "Ƽ": "5",  # LATIN CAPITAL LETTER TONE FIVE
    "ƽ": "5",  # LATIN SMALL LETTER TONE FIVE
    "Ƅ": "6",  # LATIN CAPITAL LETTER TONE SIX
    "ƅ": "6",  # LATIN SMALL LETTER TONE SIX
    "ǃ": "!",  # LATIN LETTER RETROFLEX CLICK
}

# Conversion table from Unicode categories to text:
categories_to_text = {
    "L": "Letter",
    "Lu": "Letter, uppercase",
    "Ll": "Letter, lowercase",
    "Lt": "Letter, titlecase",
    "Lm": "Letter, modifier",
    "Lo": "Letter, other",
    "M": "Mark",
    "Mn": "Mark, nonspacing",
    "Mc": "Mark, spacing combining",
    "Me": "Mark, enclosing",
    "N": "Number",
    "Nd": "Number, decimal digit",
    "Nl": "Number, letter",
    "No": "Number, other",
    "P": "Punctuation",
    "Pc": "Punctuation, connector",
    "Pd": "Punctuation, dash",
    "Ps": "Punctuation, open",
    "Pe": "Punctuation, close",
    "Pi": "Punctuation, initial quote",
    "Pf": "Punctuation, final quote",
    "Po": "Punctuation, other",
    "S": "Symbol",
    "Sm": "Symbol, math",
    "Sc": "Symbol, currency",
    "Sk": "Symbol, modifier",
    "So": "Symbol, other",
    "Z": "Separator",
    "Zs": "Separator, space",
    "Zl": "Separator, line",
    "Zp": "Separator, paragraph",
    "C": "Other",
    "Cc": "Other, control",
    "Cf": "Other, format",
    "Cs": "Other, surrogate",
    "Co": "Other, private use",
    "Cn": "Other, not assigned",
}

# Default parameters. Can be overcome by command line options
parameters = {
    "Filter": True,
    "Analyze": False,
    "Translated": False,
    "Untranslated": False,
}


################################################################################
def display_help():
    """Displays usage and help"""
    print(
        "usage: unicode2ascii [-a|--analyze] [-t|--translated] [-u|--untranslated]",
        file=sys.stderr,
    )
    print("       [--debug] [--help|-?] [--version] [--]", file=sys.stderr)
    print(
        "  ------------------  --------------------------------------------------",
        file=sys.stderr,
    )
    print("  -a|--analyze        Analyze Unicode characters", file=sys.stderr)
    print("  -t|--translated     Report translated Unicode characters", file=sys.stderr)
    print(
        "  -u|--untranslated   Report untranslated Unicode characters", file=sys.stderr
    )
    print("  --debug             Enable debug mode", file=sys.stderr)
    print(
        "  --help|-?           Print usage and this help message and exit",
        file=sys.stderr,
    )
    print("  --version           Print version and exit", file=sys.stderr)
    print("  --                  Options processing terminator", file=sys.stderr)
    print(file=sys.stderr)


################################################################################
def process_environment_variables():
    """Process environment variables"""

    if "UNICODE2ASCII_DEBUG" in os.environ.keys():
        logging.disable(logging.NOTSET)

    logging.debug("process_environment_variables(): parameters:")
    logging.debug(parameters)


################################################################################
def process_command_line():
    """Process command line options"""
    # pylint: disable=C0103
    global parameters
    # pylint: enable=C0103

    # option letters followed by : expect an argument
    # same for option strings followed by =
    character_options = "atu?"
    string_options = [
        "analyze",
        "debug",
        "help",
        "translated",
        "untranslated",
        "version",
    ]

    try:
        options, remaining_arguments = getopt.getopt(
            sys.argv[1:], character_options, string_options
        )
    except getopt.GetoptError as error:
        logging.critical("Syntax error: %s", error)
        display_help()
        sys.exit(1)

    for option, _ in options:

        if option in ("-a", "--analyze"):
            parameters["Filter"] = False
            parameters["Analyze"] = True

        elif option in ("-t", "--translated"):
            parameters["Filter"] = False
            parameters["Translated"] = True

        elif option in ("-u", "--untranslated"):
            parameters["Filter"] = False
            parameters["Untranslated"] = True

        elif option == "--debug":
            logging.disable(logging.NOTSET)

        elif option in ("--help", "-?"):
            display_help()
            sys.exit(0)

        elif option == "--version":
            print(ID.replace("@(" + "#)" + " $" + "Id" + ": ", "").replace(" $", ""))
            sys.exit(0)

    logging.debug("process_command_line(): parameters:")
    logging.debug(parameters)
    logging.debug("process_command_line(): remaining_arguments:")
    logging.debug(remaining_arguments)

    return remaining_arguments


################################################################################
def _print_in_table_format(character, ascii_equivalent=""):
    """Internal - print character in ready to use conversion table format"""

    logging.debug("character = '%s'", character)
    logging.debug('ascii_equivalent = "%s"', ascii_equivalent)

    if ascii_equivalent:
        print(
            "    '{}': \"{}\", # {}".format(
                character, ascii_equivalent, unicodedata.name(character)
            )
        )
    else:
        print("    '{}': \"\", # {}".format(character, unicodedata.name(character)))


################################################################################
def is_unicode_category(character, category):
    """Return True if character belongs to the specified Unicode category"""
    if ord(character) > 127:
        return unicodedata.category(character)[0] == category

    return False


################################################################################
def is_unicode_letter(character):
    """Return True if character is a Unicode letter"""
    return is_unicode_category(character, "L")


################################################################################
def is_unicode_mark(character):
    """Return True if character is a Unicode mark"""
    return is_unicode_category(character, "M")


################################################################################
def is_unicode_number(character):
    """Return True if character is a Unicode number"""
    return is_unicode_category(character, "N")


################################################################################
def is_unicode_punctuation(character):
    """Return True if character is a Unicode punctuation"""
    return is_unicode_category(character, "P")


################################################################################
def is_unicode_symbol(character):
    """Return True if character is a Unicode symbol"""
    return is_unicode_category(character, "S")


################################################################################
def is_unicode_separator(character):
    """Return True if character is a Unicode separator"""
    return is_unicode_category(character, "Z")


################################################################################
def is_unicode_other(character):
    """Return True if character is a Unicode other"""
    return is_unicode_category(character, "C")


################################################################################
def unicode_category(category):
    """Return Unicode category description"""
    try:
        return categories_to_text[category]
    except ValueError:
        return ""


################################################################################
def unicode_to_ascii_character(character, default=""):
    """Return Unicode letters to their ASCII equivalent and the rest unchanged"""
    if ord(character) < 128:
        return character

    if character in corrected_unicode_to_ascii:
        return corrected_unicode_to_ascii[character]

    ascii_equivalent = (
        unicodedata.normalize("NFKD", character)
        .encode("ASCII", "ignore")
        .decode("utf-8")
    )
    if ascii_equivalent:
        return ascii_equivalent

    if character in additional_unicode_to_ascii:
        return additional_unicode_to_ascii[character]

    return default


################################################################################
def unicode_to_ascii_string(characters, default=""):
    """Return Unicode letters to their ASCII equivalent and the rest unchanged"""
    new_string = ""
    for character in characters:
        new_string = new_string + unicode_to_ascii_character(character, default)
    return new_string


################################################################################
def analyze_unicode_character(character):
    """Return all information about a Unicode character"""
    if ord(character) > 127:
        print("Character: '{}'".format(character))
        print("Name: {}".format(unicodedata.name(character)))
        try:
            print("Decimal value: {}".format(unicodedata.decimal(character)))
        except ValueError:
            pass
        try:
            print("Digit value: {}".format(unicodedata.digit(character)))
        except ValueError:
            pass
        try:
            print("Numeric value: {}".format(unicodedata.numeric(character)))
        except ValueError:
            pass
        category = unicodedata.category(character)
        print("Category: {} / {}".format(category, unicode_category(category)))
        print("Bidirectional class: {}".format(unicodedata.bidirectional(character)))
        print("Combining class: {}".format(unicodedata.combining(character)))
        print("East Asian width: {}".format(unicodedata.east_asian_width(character)))
        print("Mirrored property: {}".format(unicodedata.mirrored(character)))
        print('Decomposition: "{}"'.format(unicodedata.decomposition(character)))
        print('Normal NFC form: "{}"'.format(unicodedata.normalize("NFC", character)))
        print('Normal NFKC form: "{}"'.format(unicodedata.normalize("NFKC", character)))
        print('Normal NFD form: "{}"'.format(unicodedata.normalize("NFD", character)))
        print('Normal NFKD form: "{}"'.format(unicodedata.normalize("NFKD", character)))
        print(
            'ASCII NFC form: "{}"'.format(
                unicodedata.normalize("NFC", character)
                .encode("ASCII", "ignore")
                .decode("utf-8")
            )
        )
        print(
            'ASCII NFKC form: "{}"'.format(
                unicodedata.normalize("NFKC", character)
                .encode("ASCII", "ignore")
                .decode("utf-8")
            )
        )
        print(
            'ASCII NFD form: "{}"'.format(
                unicodedata.normalize("NFD", character)
                .encode("ASCII", "ignore")
                .decode("utf-8")
            )
        )
        print(
            'ASCII NFKD form: "{}"'.format(
                unicodedata.normalize("NFKD", character)
                .encode("ASCII", "ignore")
                .decode("utf-8")
            )
        )
        print(
            'unicode_to_ascii_character(): "{}"'.format(
                unicode_to_ascii_character(character)
            )
        )
        print()


################################################################################
def main():
    """The program's main entry point"""
    program_name = os.path.basename(sys.argv[0])
    console_log_format = program_name + ": %(levelname)s: %(message)s"
    logging.basicConfig(format=console_log_format, level=logging.DEBUG)
    logging.disable(logging.INFO)

    process_environment_variables()
    process_command_line()

    for line in sys.stdin:
        for character in line:
            ascii_equivalent = unicode_to_ascii_character(character)
            if parameters["Filter"]:
                print(ascii_equivalent, end="")
            elif character != os.linesep:
                if parameters["Analyze"]:
                    analyze_unicode_character(character)

                if not ascii_equivalent:
                    if parameters["Untranslated"]:
                        _print_in_table_format(character)
                else:
                    if parameters["Translated"]:
                        _print_in_table_format(character, ascii_equivalent)

    sys.exit(0)


if __name__ == "__main__":
    main()
