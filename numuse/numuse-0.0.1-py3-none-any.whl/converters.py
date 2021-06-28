from .tools import ranged_modulus_operator
import re
import pprint
from typing import Tuple, Set, List, Optional
from fractions import Fraction
from .notation import RootedIntervalCollection, NoteCollection
from .music import MusicMoment, MusicLine, MusicMeasure, Music


def parse_music(music_shorthand: List[List[Tuple[str, List[Fraction]]]]):
    """Converts hand-written music into Music (see `Abbrs`_)

    :param music_shorthand: Music written in shorthand
    :type music_shorthand: List[List[Tuple[str, List[Fraction]]]]

    :return: Music which can be easily analyzed
    :rtype: Music

    :Example:

    >>> idea = [
    ...     [("0' 4' 7' 11' R", [tt, t, tt, t+b, b])], [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
    ...     [("9' 6' R", [b + tt, t + b, b])], [("6' 2' 9' 6' 0'' 9' R",[tt, t, tt, t, tt, t, b])],
    ...     ["(4 | 0 3 7 10) (9 | 0 3 7 10)",[2*b, 2*b])], [("(2 | 0 4 7 10)",[4*b])], [("(7 | 0 4 7 11)", [4*b])],
    ...     ["(4 7 11 2) (9 0 4 7)",[2*b, 2*b])], [("(2 6 9 0)",[4*b])], [("(7 11 2 6)", [4*b])],
    ...     ["<9 | 0 3 7 10> <2 | 0 3 7 10>",[2*b, 2*b])], [("<7 | 0 4 7 10>",[4*b])], [("<0 | 0 4 7 11>", [4*b])],
    ...     ["<9 0 4 7> <2 5 9 0>",[2*b, 2*b])], [("<7 11 2 5>",[4*b])], [("<0 4 7 11>", [4*b])]
    ... ]
    >>> parse_music(idea)
    """
    measures = []
    current_time = 0
    for measure in music_shorthand:
        music_lines = []
        for line_shorthand in measure:
            new_time, line = parse_line_shorthand(current_time, line_shorthand)
            current_time = new_time
            music_lines.append(MusicLine(line))
        measures.append(MusicMeasure(music_lines))
    return Music(measures)


def parse_line_shorthand(
    current_time: float, line_shorthand: Tuple[str, List[Fraction]]
):
    """Converts a handwritten line into a line (see `Abbrs`_)"""
    line = []
    # Rhythm information is the duration of the harmonic information
    harmonic_information_shorthand, rhythm_information = line_shorthand
    # This means that they have to have the same size
    harmonic_information = generate_NCs_from_harmonic_shorthand(
        harmonic_information_shorthand
    )
    h_to_r = zip(harmonic_information, rhythm_information)
    for h, r in h_to_r:
        # If h is none, than it's a rest
        print([str(x) for x in harmonic_information])
        line.append(MusicMoment(current_time, h, r))

        current_time += r

    new_time = current_time
    return new_time, line


def generate_NCs_from_harmonic_shorthand(
    harmonic_shorthand: str, key_root: int = 0
) -> List[NoteCollection]:
    """Converts handwritten harmonic shorthand into a list of note collections


    :param harmonic_shorthand: Harmonic information written by a human
    :type harmonic_shorthand: str

    :param key_root: The current keys root
    :type key_root: int

    :return: A list of note collections
    :rtype: List[NoteCollection]
    """
    NCs = []
    matches = re.findall(
        '\[[^\]]*\]|\([^\)]*\)|"[^"]*"|\<[^\>]*\>|\S+', harmonic_shorthand
    )
    for match in matches:
        if match[0] == "<":
            if is_RIC_notation(match):
                NCs.append(
                    RootedIntervalCollection(*parse_KRIC_shorthand(match, key_root))
                )
            else:
                middle = re.findall("\<(.*?)\>", match)[0]
                NCs.append(NoteCollection(add_key_to_notes(middle, key_root)))
        elif match[0] == "(":
            if is_RIC_notation(match):
                NCs.append(RootedIntervalCollection(*parse_RIC_shorthand(match)))
            else:
                middle = re.findall("\((.*?)\)", match)[0]
                NCs.append(NoteCollection(get_notes(middle)))
        else:
            for unit in match.split():
                if unit == "R":
                    NCs.append(NoteCollection(set()))
                else:
                    NCs.append(NoteCollection({parse_shorthand_unit(unit)}))

    return NCs


def parse_KRIC_shorthand(KRIC_shorthand: str, key_root: int) -> Tuple[int, Set[int]]:
    """Converts KRIC shorthand to a root and set of NCs"""
    root, intervals = parse_RIC_shorthand(KRIC_shorthand)
    return key_root + root, intervals


def parse_RIC_shorthand(RIC_shorthand: str) -> Tuple[int, Set[int]]:
    """Converts RIC shorthand to a root and set of NCs"""
    str_root, str_intervals = RIC_shorthand.split("|")
    root = int(str_root)
    intervals = {parse_shorthand_unit(unit) for unit in str_intervals.split(" ")}
    return root, intervals


def parse_shorthand_unit(RIC_shorthand_unit: str) -> int:
    """Given a unit of RIC shorthand, we convert it to an interval"""

    # It will always have a digit
    d = re.search(r"[0-9R]+", RIC_shorthand_unit)
    found = RIC_shorthand_unit[d.start() : d.end()]

    digit = int(found)

    # octave displacement
    m = re.search(r"[,'ud]", RIC_shorthand_unit)

    if m:
        direction = RIC_shorthand_unit[m.start()]
        count = len(RIC_shorthand_unit[m.start() :])
        multiplier = -1 if direction in ["d", ","] else 1

        return digit + multiplier * count * 12
    else:
        return digit


def is_RIC_notation(notation):
    return "|" in notation


def get_notes(str_notes):
    return {parse_shorthand_unit(unit) for unit in str_notes.split(" ")}


def add_key_to_notes(str_notes, key_root):
    return {n + key_root for n in get_notes(str_notes)}

if __name__ == "__main__":
    print('got in')
    b = 1
    # half
    h = 1 / 2
    # thirds
    t = Fraction(b, 3)
    # two thirds
    tt = 2 * t

    jens_solo_arps = [
        [("0' 4' 7' 11' R", [tt, t, tt, t + b, b])],
        [("R 7' 4' 7' 7'", [tt, t, tt, t + b, b])],
        [("9' 6' R", [b + tt, t + b, b])],
        [("6' 2' 9' 6' 0'' 9' R", [tt, t, tt, t, tt, t, b])],
        [("5' 2' 9' 0'' 5'", [tt, t, tt, t + b, b])],
        [("2' 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
        [("4' 4' 4' 0'", [b, tt, t + b, b])],
        [("11 7 11 2' 5' 2' R", [tt, t, tt, t, tt, t, b])],
        [("4' 0' R 4' R 4' R 4'", [tt, t, tt, t, tt, t, tt, t])],
        [("7' 4' 7' 7' R 11'", [tt, t, tt, t, 1 + tt, t])],
        [("0'' 0'' 9' R 9' 6'", [b, tt, t, tt, t, b])],
        [("R 2' 2' 2' R", [b, b, tt, t, b])],
        [("0'' 0'' 9' R 9' 5'", [b, tt, t, tt, t, b])],
        [("R 2' 11 5' 2' 11 7", [b, tt, t, tt, t, tt, t])],
        [("4' 0' R 4' 0' R", [tt, t, tt, t, b, b])],
        [("7' 4' 7' 10' R", [tt, t, tt, t + b, b])],
        [("R 9 0' 9 0' 9", [b, b, tt, t, tt, t])],
        [("5 9 0' 4' R", [tt, t, tt, t + b, b])],
        [("R 0' 4' 0' R", [b, b, tt, t, b])],
        [("9 0' 5 R", [b, tt, t + b, b])],
        [("2' R 0'' 6' 9' 6'", [b, b, tt, t, tt, t])],
        [("0'' 0'' 9' R", [b, tt, t + b, b])],
        [("9' R 9' 2' 5' 2'", [b, b, tt, t, tt, t])],
        [("11 11 2' R", [b, tt, t + b, b])],
        [("4' 0' 7' 0' R 4' 7' 11'", [tt, t, tt, t, tt, t, tt, t + b])],
        [("7' 11' R", [tt, t + b, b])],
        [("6' 2' 9' 2' R 9'", [tt, t, tt, t, b, b])],
        [("0'' 6' R 9' R", [tt, t, tt, t + b, b])],
        [("9' 2' R 5' 2'", [tt, t, tt, t + b, b])],
        [("5' 11 R 2' 5'", [tt, t, tt, t + b, b])],
        [("4' 0' 7' 4' 7' 11'", [tt, t, tt, t, tt, t + b])],
        [("R", [4 * b])],
    ]

    m = parse_music(jens_solo_arps)
    for measure in m.measures:
        for line in measure.m_lines:
            for moment in line.m_moments:
                print(moment)
