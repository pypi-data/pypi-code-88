from pink_accents import Match, Accent

from ._shared import DISCORD_MESSAGE_END


class Arabic(Accent):
    WORD_REPLACEMENTS = {
        "god": "Allah",
        "good": "halal",
        "bad": "haram",
        # TODO
        "(man|orange)": "Ben Shapiro",
        "the": (
            "arabic",
            "arabe",
        ),
    }

    REPLACEMENTS = {
        r"ic": "e",
        r"c": "g",
        r"t\b": "to",
    }


class TrumpScript(Accent):
    WORD_REPLACEMENTS = {
        "true": "fact",
        "false": "lie",
        "print": (
            "tell",
            "say",
        ),
        "while": "as long as",
    }

    REPLACEMENTS = {
        r"\+": "plus",
        r"\-": "minus",
        r"(?<=\s)\*(?=\s)": "times",
        r"/": "over",
        r"(?<=\s)<(?=\s)": (
            "less",
            "fewer",
            "smaller",
        ),
        r"(?<=\s)>(?=\s)": (
            "more",
            "greater",
            "larger",
        ),
        DISCORD_MESSAGE_END: " America is great",
    }


class Japanese(Accent):
    REPLACEMENTS = {
        r"th": "d",
        r"[^a-z]ai[^a-z]": "e",
        r"\Bt\b": "tto",
        r"\Bs\b": "su",
    }


def debug(m: Match) -> str:
    print(m)
    return m.original


class Debug(Accent):
    REPLACEMENTS = {
        r"\w": {
            debug: 1,
        }
    }
