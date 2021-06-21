#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019-2021 garrick. Some rights reserved.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import math
from slugify import slugify
from appdirs import *

name = "palpageproducer"
author = "gargargarrick"
__author__ = "gargargarrick"
__version__ = "1.3.0"
__copyright__ = "Copyright 2019-2020 Matthew Ellison"
__license__ = "GPL"
__maintainer__ = "gargargarrick"


def getFile():
    """Get the file to process."""
    columncount = None
    if len(sys.argv) > 1:
        f = sys.argv[1]
        if len(sys.argv) > 2:
            columncount = sys.argv[2]
            try:
                columncount = int(columncount)
            except ValueError:
                print("{columncount} doesn't seem to be a number of columns.")
                columncount = None
    else:
        f = input("Path to the SASS/LESS/GPL/Oomox file? > ")
    f_abspath = os.path.abspath(f)
    return (f_abspath, columncount)


def openSass(sasspath):
    """Read from a SASS .scss file."""
    with open(sasspath, "r", encoding="utf-8") as fin:
        sass_s = fin.read().splitlines()
    return sass_s


def openLess(lesspath):
    """Read from a LESS .less file."""
    with open(lesspath, "r", encoding="utf-8") as fin:
        less_s = fin.read().splitlines()
    less_replaced = []
    # P. much convert the important parts to SASS.
    for line in less_s:
        if line != "":
            line = line.strip()
            if line[0] == "@":
                newl = "${line}".format(line=line[1:])
                less_replaced.append(newl)
    return less_replaced


def openOomox(oomoxpath):
    """Read from an Oomox theme."""
    with open(oomoxpath, "r", encoding="utf-8") as fin:
        oomox_s = fin.read().splitlines()
    oomox_replaced = []
    if oomox_s[0][0:9] != "ACCENT_BG":
        print(
            "palpageproducer thought {oomoxpath} was an oomox file, but it is not formatted like one. Please try again.".format(
                oomoxpath=oomoxpath
            )
        )
        return False
    # Ignore some colors.
    # Feel free to remove the ones you *do* want from this list.
    ignored_keys = [
        "ARC_WIDGET_BORDER_COLOR",
        "ICONS_ARCHDROID",
        "ICONS_DARK",
        "ICONS_LIGHT",
        "ICONS_LIGHT_FOLDER",
        "ICONS_MEDIUM",
        "ICONS_SYMBOLIC_ACTION",
        "ICONS_SYMBOLIC_PANEL",
        "MENU_BG",
        "MENU_FG",
        "SURUPLUS_GRADIENT1",
        "SURUPLUS_GRADIENT2",
        "TERMINAL_ACCENT_COLOR",
        "TERMINAL_BACKGROUND",
        "TERMINAL_BASE_TEMPLATE",
        "TERMINAL_COLOR0",
        "TERMINAL_COLOR1",
        "TERMINAL_COLOR2",
        "TERMINAL_COLOR3",
        "TERMINAL_COLOR4",
        "TERMINAL_COLOR5",
        "TERMINAL_COLOR6",
        "TERMINAL_COLOR7",
        "TERMINAL_COLOR8",
        "TERMINAL_COLOR9",
        "TERMINAL_COLOR10",
        "TERMINAL_COLOR11",
        "TERMINAL_COLOR12",
        "TERMINAL_COLOR13",
        "TERMINAL_COLOR14",
        "TERMINAL_COLOR15",
        "TERMINAL_FOREGROUND",
    ]
    seen_colors = set()
    for line in oomox_s:
        if not line:
            continue
        line = line.strip()
        k, v = line.split("=")
        # Check if the item is a hex color or not
        if len(v) != 6:
            continue
        try:
            vtest = int(v, 16)
        except ValueError:
            continue
        if k in ignored_keys:
            continue
        # The main purpose of PPP is getting unique colors, and oomox
        # is prone to duplicates (especially for text colors).
        if v in seen_colors:
            continue
        seen_colors.add(v)
        key_id = "$" + k.lower()
        value_c = "#" + v
        newl = "{key_id}: {value_c};".format(key_id=key_id, value_c=value_c)
        oomox_replaced.append(newl)
    return oomox_replaced


def rgbToHex(rgb):
    """Convert RGB colors into hex."""
    rgb_list = list(rgb)
    while len(rgb_list) < 3:
        rgb_list.append("0")
    r = int(rgb_list[0])
    g = int(rgb_list[1])
    b = int(rgb_list[2])
    h = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return h


def openGimp(gpl_f):
    """Open a GIMP .gpl palette and process it."""
    with open(gpl_f, "r", encoding="utf-8") as fin:
        gpl_raw = fin.read()
    gpl_s = gpl_raw.split("\n")[4:]
    new = []
    for x in gpl_s:
        if x and x[0] != "#" and "\t" in x:
            pair = x.strip().rsplit("\t", 1)
            rgb = pair[0]
            name = pair[1]
            rgb = " ".join(rgb.split())
            rgb = tuple(rgb.split(" "))
            hex = rgbToHex(rgb)
            slugname = slugify(name, separator="_", lowercase=True, max_length=200)
            finalu = "${name}: {hex}".format(name=slugname, hex=hex)
            new.append(finalu)
    return new


def findDivisor(count):
    """Find divisors below 5 (for determining column count)"""
    foo = reversed(range(1, 6))
    for i in foo:
        if count % i == 0:
            return i


def getColumns(count):
    """Set the number of columns for the output."""
    columns = findDivisor(count)
    if columns == 1:
        columns = 5
        vw = "20"
    else:
        vw = str(int(100 // columns))
    return (vw, str(columns))


def wrapInTag(content, tag):
    """Wrap something in an HTML tag"""
    return "<{tag}>{content}</{tag}>".format(tag=tag, content=content)


def getLuminance(hex):
    """Get the luminance of a hex color"""
    hex_nohash = hex.lstrip("#")
    if len(hex_nohash) == 3:
        hex_nohash = "".join([item * 2 for item in hex_nohash])
    r, g, b = tuple(int(hex_nohash[i : i + 2], 16) for i in (0, 2, 4))
    rgbs = [r, g, b]
    rgbgs = []
    for component in rgbs:
        if component <= 10:
            adjusted = component / 3294
        else:
            adjusted = (component / 269 + 0.0513) ** 2.4
        rgbgs.append(adjusted)
    lum = 0.2126 * rgbgs[0] + 0.7152 * rgbgs[1] + 0.0722 * rgbgs[2]
    return lum


def checkContrast(hex):
    """Check the contrast between a hex color and black"""
    foreground = 0.0
    background = getLuminance(hex)
    colors = [foreground, background]
    ratio = (max(colors) + 0.05) / (min(colors) + 0.05)
    return ratio


def processColorValue(colorvalue):
    """Convert a color value to appear consistent."""
    all_lower = colorvalue.lower()
    try:
        (unique_values,) = set(all_lower[1:])
        return "".join(["#", unique_values * 6])
    except ValueError:
        try:
            r, g, b = all_lower[1:]
            return "".join(["#", r * 2, g * 2, b * 2])
        except ValueError:
            return all_lower


def namedColorToHex(named):
    """Convert a CSS named color to a normal hex color."""
    named_colors = {
        "aliceblue": "#f0f8ff",
        "antiquewhite": "#faebd7",
        "aqua": "#00ffff",
        "aquamarine": "#7fffd4",
        "azure": "#f0ffff",
        "beige": "#f5f5dc",
        "bisque": "#ffe4c4",
        "black": "#000000",
        "blanchedalmond": "#ffebcd",
        "blue": "#0000ff",
        "blueviolet": "#8a2be2",
        "brown": "#a52a2a",
        "burlywood": "#deb887",
        "cadetblue": "#5f9ea0",
        "chartreuse": "#7fff00",
        "chocolate": "#d2691e",
        "coral": "#ff7f50",
        "cornflowerblue": "#6495ed",
        "cornsilk": "#fff8dc",
        "crimson": "#dc143c",
        "cyan": "#00ffff",
        "darkblue": "#00008b",
        "darkcyan": "#008b8b",
        "darkgoldenrod": "#b8860b",
        "darkgray": "#a9a9a9",
        "darkgreen": "#006400",
        "darkgrey": "#a9a9a9",
        "darkkhaki": "#bdb76b",
        "darkmagenta": "#8b008b",
        "darkolivegreen": "#556b2f",
        "darkorange": "#ff8c00",
        "darkorchid": "#9932cc",
        "darkred": "#8b0000",
        "darksalmon": "#e9967a",
        "darkseagreen": "#8fbc8f",
        "darkslateblue": "#483d8b",
        "darkslategray": "#2f4f4f",
        "darkslategrey": "#2f4f4f",
        "darkturquoise": "#00ced1",
        "darkviolet": "#9400d3",
        "deeppink": "#ff1493",
        "deepskyblue": "#00bfff",
        "dimgray": "#696969",
        "dimgrey": "#696969",
        "dodgerblue": "#1e90ff",
        "firebrick": "#b22222",
        "floralwhite": "#fffaf0",
        "forestgreen": "#228b22",
        "fuchsia": "#ff00ff",
        "gainsboro": "#dcdcdc",
        "ghostwhite": "#f8f8ff",
        "gold": "#ffd700",
        "goldenrod": "#daa520",
        "gray": "#808080",
        "green": "#008000",
        "greenyellow": "#adff2f",
        "grey": "#808080",
        "honeydew": "#f0fff0",
        "hotpink": "#ff69b4",
        "indianred": "#cd5c5c",
        "indigo": "#4b0082",
        "ivory": "#fffff0",
        "khaki": "#f0e68c",
        "lavender": "#e6e6fa",
        "lavenderblush": "#fff0f5",
        "lawngreen": "#7cfc00",
        "lemonchiffon": "#fffacd",
        "lightblue": "#add8e6",
        "lightcoral": "#f08080",
        "lightcyan": "#e0ffff",
        "lightgoldenrodyellow": "#fafad2",
        "lightgray": "#d3d3d3",
        "lightgreen": "#90ee90",
        "lightgrey": "#d3d3d3",
        "lightpink": "#ffb6c1",
        "lightsalmon": "#ffa07a",
        "lightseagreen": "#20b2aa",
        "lightskyblue": "#87cefa",
        "lightslategray": "#778899",
        "lightslategrey": "#778899",
        "lightsteelblue": "#b0c4de",
        "lightyellow": "#ffffe0",
        "lime": "#00ff00",
        "limegreen": "#32cd32",
        "linen": "#faf0e6",
        "magenta": "#ff00ff",
        "maroon": "#800000",
        "mediumaquamarine": "#66cdaa",
        "mediumblue": "#0000cd",
        "mediumorchid": "#ba55d3",
        "mediumpurple": "#9370db",
        "mediumseagreen": "#3cb371",
        "mediumslateblue": "#7b68ee",
        "mediumspringgreen": "#00fa9a",
        "mediumturquoise": "#48d1cc",
        "mediumvioletred": "#c71585",
        "midnightblue": "#191970",
        "mintcream": "#f5fffa",
        "mistyrose": "#ffe4e1",
        "moccasin": "#ffe4b5",
        "navajowhite": "#ffdead",
        "navy": "#000080",
        "oldlace": "#fdf5e6",
        "olive": "#808000",
        "olivedrab": "#6b8e23",
        "orange": "#ffa500",
        "orangered": "#ff4500",
        "orchid": "#da70d6",
        "palegoldenrod": "#eee8aa",
        "palegreen": "#98fb98",
        "paleturquoise": "#afeeee",
        "palevioletred": "#db7093",
        "papayawhip": "#ffefd5",
        "peachpuff": "#ffdab9",
        "peru": "#cd853f",
        "pink": "#ffc0cb",
        "plum": "#dda0dd",
        "powderblue": "#b0e0e6",
        "purple": "#800080",
        "rebeccapurple": "#663399",
        "red": "#ff0000",
        "rosybrown": "#bc8f8f",
        "royalblue": "#4169e1",
        "saddlebrown": "#8b4513",
        "salmon": "#fa8072",
        "sandybrown": "#f4a460",
        "seagreen": "#2e8b57",
        "seashell": "#fff5ee",
        "sienna": "#a0522d",
        "silver": "#c0c0c0",
        "skyblue": "#87ceeb",
        "slateblue": "#6a5acd",
        "slategray": "#708090",
        "slategrey": "#708090",
        "snow": "#fffafa",
        "springgreen": "#00ff7f",
        "steelblue": "#4682b4",
        "tan": "#d2b48c",
        "teal": "#008080",
        "thistle": "#d8bfd8",
        "tomato": "#ff6347",
        "turquoise": "#40e0d0",
        "violet": "#ee82ee",
        "wheat": "#f5deb3",
        "white": "#ffffff",
        "whitesmoke": "#f5f5f5",
        "yellow": "#ffff00",
        "yellowgreen": "#9acd32",
    }
    color_names = {
        "aliceblue",
        "antiquewhite",
        "aqua",
        "aquamarine",
        "azure",
        "beige",
        "bisque",
        "black",
        "blanchedalmond",
        "blue",
        "blueviolet",
        "brown",
        "burlywood",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "cornsilk",
        "crimson",
        "cyan",
        "darkblue",
        "darkcyan",
        "darkgoldenrod",
        "darkgray",
        "darkgreen",
        "darkgrey",
        "darkkhaki",
        "darkmagenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "darkred",
        "darksalmon",
        "darkseagreen",
        "darkslateblue",
        "darkslategray",
        "darkslategrey",
        "darkturquoise",
        "darkviolet",
        "deeppink",
        "deepskyblue",
        "dimgray",
        "dimgrey",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "fuchsia",
        "gainsboro",
        "ghostwhite",
        "gold",
        "goldenrod",
        "gray",
        "green",
        "greenyellow",
        "grey",
        "honeydew",
        "hotpink",
        "indianred",
        "indigo",
        "ivory",
        "khaki",
        "lavender",
        "lavenderblush",
        "lawngreen",
        "lemonchiffon",
        "lightblue",
        "lightcoral",
        "lightcyan",
        "lightgoldenrodyellow",
        "lightgray",
        "lightgreen",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategray",
        "lightslategrey",
        "lightsteelblue",
        "lightyellow",
        "lime",
        "limegreen",
        "linen",
        "magenta",
        "maroon",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "mintcream",
        "mistyrose",
        "moccasin",
        "navajowhite",
        "navy",
        "oldlace",
        "olive",
        "olivedrab",
        "orange",
        "orangered",
        "orchid",
        "palegoldenrod",
        "palegreen",
        "paleturquoise",
        "palevioletred",
        "papayawhip",
        "peachpuff",
        "peru",
        "pink",
        "plum",
        "powderblue",
        "purple",
        "rebeccapurple",
        "red",
        "rosybrown",
        "royalblue",
        "saddlebrown",
        "salmon",
        "sandybrown",
        "seagreen",
        "seashell",
        "sienna",
        "silver",
        "skyblue",
        "slateblue",
        "slategray",
        "slategrey",
        "snow",
        "springgreen",
        "steelblue",
        "tan",
        "teal",
        "thistle",
        "tomato",
        "turquoise",
        "violet",
        "wheat",
        "white",
        "whitesmoke",
        "yellow",
        "yellowgreen",
    }
    try:
        return named_colors[named.lower()]
    except KeyError:
        return named


def main():
    """Read a stylesheet/palette and generate an HTML page."""
    save_path = os.path.join(user_data_dir(name, author), "output")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    sass_f, u_cc = getFile()
    sass_basename = os.path.basename(sass_f)
    sass_splitext = os.path.splitext(sass_basename)
    sass_noext, sass_ext = sass_splitext
    sass_noext_safe = slugify(sass_noext, separator="_", lowercase=True, max_length=200)
    # TODO: Let users manually set the language
    if sass_ext == ".scss":
        sass = openSass(sass_f)
    elif sass_ext == ".gpl":
        sass = openGimp(sass_f)
    elif sass_ext == ".less":
        sass = openLess(sass_f)
    # Oomox doesn't use a file extension ¯\_(ツ)_/¯
    elif not sass_ext:
        sass = openOomox(sass_f)
    else:
        return False

    title = wrapInTag(tag="title", content=sass_basename)
    h1 = wrapInTag(tag="h1", content=sass_basename)

    # Make sure the colors really are colors.
    really_colors = []
    for color in sass:
        # Remove sass comments
        color = color.split(" //")[0]
        color = color.replace(";", "").strip()
        if color != "" and color[0] == "$":
            colorid, colorvalue = color.split(": ", 1)
            # Check for named colors
            colorvalue = namedColorToHex(colorvalue)
            if colorvalue[0] == "#":
                really_colors.append((colorid, colorvalue))
            # RGB colors are converted. RGBA colors are ignored.
            elif colorvalue[0:3] == "rgb" and colorvalue[0:4] != "rgba":
                norgb = colorvalue.strip("rgb()")
                justrgb = norgb.split(", ")
                hex = rgbToHex(justrgb)
                really_colors.append(
                    "{colorid}: {hex}".format(colorid=colorid, hex=hex)
                )
            else:
                pass
    # Count the colors.
    colors = len(really_colors)
    # That determines the size of each box and the number of columns.
    # Unless you specified it yourself!
    if not u_cc:
        # I use vw rather than vh to keep the boxes relatively squarish.
        # Also, did you just pronounce that as "vee-dubya"? I am disgusted.
        vw, columns = getColumns(colors)
    else:
        columns = u_cc
        vw = str(int(100 // u_cc))

    css_template = """body {{box-sizing: border-box}} h1 {{margin: 0em}} main {{display: grid; grid-template-columns: repeat({columns}, 1fr); grid-auto-rows: {vw}vw; grid-gap: 1em}} .colorbox {{padding: 1em; margin: 0.5em; overflow: visible}} p {{margin: 0em}}""".format(
        columns=columns, vw=vw
    )
    cssbox_template = "#{colorid} {{background-color: {colorvalue}; color: {borw}}}"
    html_header = [
        "<!DOCTYPE HTML>",
        """<html lang="zxx">""",
        "<head>",
        """<meta charset="utf-8">""",
        title,
        "<style>",
        css_template,
    ]
    html_body = ["</style>", "</head>", "<body>", h1, "<main>"]
    html_close = ["</main>", "</body>", "</html>", ""]

    knownids = set()
    knowncolors = set()
    colorindex = 0
    for colorid, colorvalue in really_colors:
        colorid = colorid[1:]
        colorvalue = processColorValue(colorvalue)
        # Add new colors.
        if colorid not in knownids and colorvalue not in knowncolors:
            knownids.add(colorid)
            knowncolors.add(colorvalue)
            contrast = checkContrast(colorvalue)
            if contrast < 4.5:
                borw = "#ffffff"
            else:
                borw = "#000000"
            cssbox = cssbox_template.format(
                colorid=colorid, colorvalue=colorvalue, borw=borw
            )
            html = """<div class="colorbox" id="{colorid}"><p>{colorid}: {colorvalue}</p></div>""".format(
                colorid=colorid, colorvalue=colorvalue
            )
            c = {
                "colorid": colorid,
                "colorvalue": colorvalue,
                "cssbox": cssbox,
                "html": html,
            }
            html_header.append(cssbox)
            html_body.append(html)
        # GIMP palettes don't necessarily have unique color names,
        # so rename colors as needed to avoid overlap.
        elif colorid in knownids and colorvalue not in knowncolors:
            colorid = "{colorid}{colorindex}".format(
                colorid=colorid, colorindex=str(colorindex)
            )
            colorindex += 1
            contrast = checkContrast(colorvalue)
            if contrast < 4.5:
                borw = "#ffffff"
            else:
                borw = "#000000"
            cssbox = cssbox_template.format(
                colorid=colorid, colorvalue=colorvalue, borw=borw
            )
            html = """<div class="colorbox" id="{colorid}"><p>{colorid}: {colorvalue}</p></div>""".format(
                colorid=colorid, colorvalue=colorvalue
            )
            c = {
                "colorid": colorid,
                "colorvalue": colorvalue,
                "cssbox": cssbox,
                "html": html,
            }
            html_header.append(cssbox)
            html_body.append(html)

    all_html_elements = html_header + html_body + html_close
    html = "\n".join(all_html_elements)

    outname = "{noext}_palette.html".format(noext=sass_noext_safe)
    outpath = os.path.join(save_path, outname)
    with open(outpath, "w", encoding="utf-8") as fout:
        fout.write(html)
    print("Wrote {outpath}.".format(outpath=outpath))


if __name__ == "__main__":
    main()
