"""
The AutoCoconut Project - Module 'Translator'
===============================================================================
The Translator module takes the dictionary of super events created by the 
Interpreter module and converts it into a human readable formats (md, html), 
or into perl scripting language that can be used to create OpenQA based tests.

Created by Lukáš Růžička (lruzicka@redhat.com), 2020 and provided under the
General Public License v3.
"""

import glob
import json
import os
import tkinter

from jinja2 import Environment, FileSystemLoader
from PIL import Image, ImageDraw
from math import sqrt
from shutil import copy

class Translator:
    def __init__(self, report, screen_resolution=None):
        """ Initiate the method. """
        self.report = report
        if not screen_resolution:
            self.screen_resolution = self.get_screen_size()
        else:
            self.screen_resolution = screen_resolution
        self.openqa_keys = {
            'caps_lock': 'caps',
            'enter':'ret',
            'page_up':'pgup',
            'page_down':'pgdn',
            'cmd':'super'
        }

    def get_screen_size(self):
        """ Get screen resolution from tkinter. """
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        return (width, height)

    def create_needle_area(self, coordinates):
        """ Calculate an area around the mouse click $coordinates (tuple).

        If the area lies behind the visible part of the screen resolution, 
        it will be cut. Otherwise a small rectangle is calculated and
        returned. """
        width, height = self.screen_resolution
        # When no coordinates are given, take the whole screensize as coordinates
        # otherwise calculate the area around the given coordinates.
        if not coordinates:
            area = (0, 0, width, height)
        else:
            x = coordinates[0]
            y = coordinates[1]
            xleft = x - 20
            if xleft < 0:
                xleft = 0
            xright = x + 20
            if xright > width:
                xright = width
            ynorth = y - 15
            if ynorth < 0:
                ynorth = 0
            ysouth = y + 15
            if ysouth > height:
                ysouth = height
            area = (xleft, ynorth, xright, ysouth)
        return area

    def create_needle_json(self, coordinates, needlename):
        """ Create an OpenQA json needle file from the given coordinates and 
        the given needle name. """
        content = {"area":[], "properties":[], "tags":[]}
        if not coordinates:
            xpoint = 0
            ypoint = 0
            width, height = self.screen_resolution
        else:
            xpoint = coordinates[0]
            ypoint = coordinates[1]
            width = 40
            height = 30
        needle_area = [{"height": height, "width": width, "type":"match", "xpos":xpoint, "ypos":ypoint}]
        tags = [f"{needlename}"]
        content['area'] = needle_area
        content['tags'] = tags
        return content

    def draw_needle_area(self, area, input_file, lang):
        """ Draw a given needle area onto the $input_file and store a new altered 
        $needled_file. 

        """
        # For OpenQA, we do not want to alter the files, because OpenQA uses needle files
        # instead. So we only copy that file under a new name.
        if lang == "openqa":
            # We also create the json needle file content and write the file    
            needle_json = self.create_needle_json(area, input_file)
            jsonfile = input_file.split('.')[0]
            jsonfile = f"{jsonfile}.json"
            with open(jsonfile, 'w') as outfile:
                p = json.dumps(needle_json, indent=4)
                outfile.write(p)
            result = "needle_created"
        # Else, we will draw the area over the picture.
        else:
            try:
                image = Image.open(input_file)
                if area:
                    pen = ImageDraw.Draw(image)
                    pen.rectangle(area, outline=(255, 0, 0, 255), width=5)
                else:
                    pass
                image.save(input_file)
                result = "redrawn"
            except FileNotFoundError:
                result = "failed"
        return (result)

    def check_combo(self, data, lang):
        """ Look for a combination key and return the corresponding prefix. """
        try:
           combo = data['combined-with']
        except KeyError:
            combo = None    
        return combo

    def rename_files(self, numbering, used, alternative, skip=False):
        """ Renames files to make the names more readable. 

        The files are always connected to a particular step in the report.
        They are named with the timestamp of their creation, which makes it
        hard to read. This will rename them according to their place in the
        report. This only applies to when the application is used from the 
        console, because in a GUI, files can be renamed manually.

        Takes $number for number of the step, $used to name the file with
        the regular name, $alternative to name it with alternative name."""
        if not skip:
            usedname = f"step{numbering}-needle.png"
            altname = f"step{numbering}-needle_alternative.png"
            if used:
                try:
                    os.rename(used, usedname)
                except FileNotFoundError:
                    print(f"I was looking for {used} but could not find it.")
            if alternative:
                try:
                    os.rename(alternative, altname)
                except FileNotFoundError:
                    print(f"I was looking for {alternative} but could not find it.")
        else:
            # In a GUI, leave the names as they are.
            usedname = used
            altname = alternative
        # Return the values.    
        return (usedname, altname)


    def polish_data(self, lang, skip=False):
        """ Iterate over the json data and polish them for output. 

        It manipulates the screenshot files and adds some overlays to it and updates some of the information in the json data. """

        # Create an empty list of lines.
        report_lines = []

        if not self.report:
            report_lines.append("Error! No report has been found.")
        else:
            # Numbering will be used to number the steps in the output and also for naming the needle screenshots.
            numbering = 0
            # Iterate over the dictionary, any changes of the events WILL GET PROPAGATED BACK to the original
            # self.report which is very handy when using this module in a GUI.
            for timestamp in self.report:
                # Add to numbering immediately, as we do not want receive a zero numbered step.
                numbering += 1
                # Read the current event.
                data = self.report[timestamp]
                # Combination comes in the form of a list. We need to join it into string in order to show it
                # in the formatted output.
                combo = data["combined"]
                # For openqa, the names must be replaced with openqa standards.
                if combo and lang == 'openqa':
                    combo = [x if x not in self.openqa_keys.keys() else self.openqa_keys[x] for x in combo]
                    combo = "-".join(combo)
                elif combo:
                    combo = "-".join(combo)
                data['combined'] = combo
                # Mouse and keyboard events have different json information, so we will handle mouse and keyboard separately.
                if 'mouse' in data['type']:
                    coordinates = data['coordinates']
                    screens = data['screens'] 
                    area = self.create_needle_area(coordinates)
                    if 'click' in data['action']:
                        # For clicks,  we want to use an overlain screenshot. We will pick up a corrected screenshot, 
                        # because we need to see the screenshot from before the click itself. The click corrected screenshot
                        # comes earlier than the regular according to the $time_offset. We also overlay that screenshot
                        # with a rectangle showing the approximate click area.
                        regular, corrected = screens
                        corrected, regular = self.rename_files(numbering, corrected, regular, skip)
                        self.draw_needle_area(area, corrected, lang)
                        # then we update the event data
                        data['screens'] = [corrected, regular]

                    elif data['action'] == "scroll":
                        # For scrolls, we want to make it even more readable, so we will not only pass the amount of
                        # scrolling steps, but we will also add in which direction they were done. The directions resemble
                        # the map, which means that "north" is up and "east" is on the right.
                        horizontal = data['horizontal']
                        vertical = data['vertical']
                        # Calculate the direction of the scroll movement
                        direction = ""
                        if horizontal > 0:
                            direction = "east"
                        elif horizontal < 0:
                            direction = "west"
                        if vertical > 0:
                            direction = f"north{direction}"
                        elif vertical < 0:
                            direction = f"south{direction}"
                        # We want the steps be absolute values.
                        data['horizontal'] = abs(horizontal)
                        data['vertical'] = abs(vertical)
                        data["direction"] = direction
                        # We also overlay the image. This time, we use the regular screenshot, because we want to show
                        # the situation at the time when it was taken.
                        regular, corrected = screens
                        area = self.create_needle_area(None)
                        regular, corrected = self.rename_files(numbering, regular, corrected, skip)
                        self.draw_needle_area(area, regular, lang)
                        data['screens'] = [regular, corrected]
                    # For drags, we want to draw a different overlay, i.e. not only where it was clicked, but also where it 
                    # was released. Therefore we will recalculate the area and create the overlay with the new data.
                    elif data['action'] == "drag":
                        # Read drag related info
                        end = data['end_coordinates']
                        # Get the coordinates differently (for the whole drag area and not just a click point)
                        drag_coordinates = (coordinates[0], coordinates[1], end[0], end[1])
                        area = self.create_needle_area(drag_coordinates)
                        # Take the screenshot and needle it with the drag area.
                        regular, corrected = screens
                        regular, corrected = self.rename_files(numbering, regular, corrected, skip)
                        self.draw_needle_area(drag_coordinates, regular, lang)
                        data['screens'] = [regular, corrected]
                # In case of pressing various keys.
                elif "key" in data['type']:
                    combo = data['combined']
                    action = data['action']
                    key = data['key']
                    # The names of some keys are different for openqa, so this will make the necessary replacements
                    if lang == 'openqa': 
                        if key in self.openqa_keys.keys():
                            key = self.openqa_keys[key]
                            data['key'] = key
                    screens = data['screens']
                    # This is a combo hack that deals with multiple pressed modifiers where no other key was pressed.
                    if combo == key:
                        data['combined'] = None
                    # For events with a modifier pressed.
                    if data['subtype'] == "modifier" and data['action'] == "release":
                        # With keys, there will be no area specified so we will take the whole image
                        # as one area and create the overlay for the entire screen size.
                        area = self.create_needle_area(None)
                        regular, corrected = screens
                        corrected, regular = self.rename_files(numbering, corrected, regular, skip)
                        # Also, we want to work the corrected screenshot that shows the result of the action
                        # and its delay is set by the $time_offset.
                        self.draw_needle_area(area, corrected, lang)
                        data['screens'] = [corrected, regular]
                    # If one of the special keys is pressed
                    elif data['subtype'] == "special" or data['key'] == "tab":
                        area = self.create_needle_area(None)
                        regular, corrected = screens
                        corrected, regular = self.rename_files(numbering, corrected, regular, skip)
                        self.draw_needle_area(area, corrected, lang)
                        data['screens'] = [corrected, regular]
                    elif data['subtype'] == "stop":
                    # To make sure the stop_key screenshot gets a proper name, too
                        area = self.create_needle_area(None)
                        regular, corrected = screens
                        regular, corrected = self.rename_files(numbering, regular, corrected, skip)
                        self.draw_needle_area(area, regular, lang)
                        data['screens'] = [regular, corrected]
                    else:
                        # This should never happen.
                        line = f"""{numbering}. Do something with the keyboard, but I am not sure what. """
                # If the event is a typing event, handle it here.
                if data['type'] == "typing":
                    text = data['text']
                # Save the event data in the list of data.
                report_lines.append(data)
        return report_lines
