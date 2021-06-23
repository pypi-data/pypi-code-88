#!/usr/bin/python3

from .engine import event_handler as event_handler
from .engine import interpreter as interpreter
from .engine import translator as translator
import glob
import json
import os
import re
import sys
import shutil
import threading
import time
import webbrowser

from jinja2 import Environment, FileSystemLoader
from tkinter import *
from tkinter import filedialog


class AppGui:
    def __init__(self, root):

        # Variables to store runtime status
        self.master = root
        self.menu = Menu(root)
        self.master.config(menu=self.menu)
        self.changed_status = False
        self.saved_file = False
        self.raw_output = {}
        self.clean_output = {}
        self.collector = event_handler.Collector("gui", 1)
        self.collector_report = {}
        self.running_thread = None
        self.workdir = "."
        self.saved_status = "not saved"
        # Global choices are a place to hold the file name, format and path.
        self.choices = {
                "path": ".",
                "format": "json",
                "filename": "recorded_workflow",
                "report": "create",
            }

        # Here, we define the widgets for the menu.
        # Main menu items
        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.action_menu = Menu(self.menu)
        self.menu.add_cascade(label="Actions", menu=self.action_menu)
        self.format_menu = Menu(self.menu)
        self.menu.add_cascade(label="Format", menu=self.format_menu)
        self.about_menu = Menu(self.menu)
        self.menu.add_cascade(label="About", menu=self.about_menu)

        # File Menu items
        self.file_menu.add_command(label="Open file", command=self.open_existing)
        self.file_menu.add_command(label="New file", command=self.open_new)
        self.file_menu.add_command(label="Save file", command=self.save_file)
        self.file_menu.add_command(label="Quit", command=self.quit)

        # Action Menu items
        self.action_menu.add_command(label="Record", command=self.init_record_frame)
        self.action_menu.add_command(label="Edit", command=self.edit_events)
        self.action_menu.add_command(label="Create", command=self.create_events)

        # Format Menu items

        self.format_menu.add_command(label="adoc", command=lambda: self.set_format("adoc"))
        self.format_menu.add_command(label="html", command=lambda: self.set_format("html"))
        self.format_menu.add_command(label="json", command=lambda: self.set_format("json"))
        self.format_menu.add_command(label="openqa", command=lambda: self.set_format("pm"))
        self.format_menu.add_command(label="raw", command=lambda: self.set_format("raw"))

        # About Menu items
        self.about_menu.add_command(label="Help", command=self.open_help)
        self.about_menu.add_command(label="About", command=self.show_about)

        # Here, we define the main application frames and their widgets
        # Application frames
        self.functions = Frame(self.master, width=700, height=500)
        self.functions.grid(column=0, row=0, padx=1, pady=1, sticky=(N,W))
        self.info = Frame(self.master, borderwidth=1, width=324, height=600)
        self.info.grid(column=1, row=0, padx=1, pady=1, sticky=(N,E))

        #Functions frame definitions
        self.reclines = "Ready to track your activity.\n\nClick 'Start' to start tracking. Click 'Stop' when you have finished.\n\n"
        # The basic frame is created by calling the following method which holds the widgets.
        self.init_record_frame()

        #Info frame defitions
        self.info_title = Label(self.info, text="Status info:", font='sans 10 bold')
        self.info_title.grid(column=0, row=0, sticky=(W))
        self.filename = Label(self.info, text="Filename:")
        self.filename.grid(column=0, row=1, sticky=(W))
        self.efilename = Entry(self.info, width=20)
        self.efilename.grid(column=1, row=1, sticky=(W))
        self.efilename.insert(0, "not selected")
        self.efilename.configure(state='readonly')

        self.format = Label(self.info, text="Format:")
        self.format.grid(column=0, row=2, sticky=(W))
        self.eformat = Entry(self.info, width=20)
        self.eformat.grid(column=1, row=2, sticky=(W))
        self.eformat.insert(0, "not selected")
        self.eformat.configure(state='readonly')

        self.action = Label(self.info, text="Action:")
        self.action.grid(column=0, row=3, sticky=(W))
        self.enaction = Entry(self.info, width=20)
        self.enaction.grid(column=1, row=3, sticky=(W))
        self.enaction.insert(0, "record events")
        self.enaction.configure(state='readonly')

        self.progress = Label(self.info, text="Progress:")
        self.progress.grid(column=0, row=4, sticky=(W))
        self.eprogress = Entry(self.info, width=20)
        self.eprogress.grid(column=1, row=4, sticky=(W))
        self.eprogress.insert(0, "recording not started")
        self.eprogress.configure(state='readonly')

        self.rtotal = Label(self.info, text="Recorded raw events:")
        self.rtotal.grid(column=0, row=5, sticky=(W))
        self.ertotal = Entry(self.info, width=20)
        self.ertotal.grid(column=1, row=5, sticky=(W))
        self.ertotal.insert(0, "recording not started")
        self.ertotal.configure(state='readonly')
        self.ctotal = Label(self.info, text="Available clean events:")
        self.ctotal.grid(column=0, row=6, sticky=(W))
        self.ectotal = Entry(self.info, width=20)
        self.ectotal.grid(column=1, row=6, sticky=(W))
        self.ectotal.insert(0, "recording not started")
        self.ectotal.configure(state='readonly')
        self.savedone = Label(self.info, text="Recording saved:")
        self.savedone.grid(column=0, row=7, sticky=(W))
        self.esavedone = Entry(self.info, width=20)
        self.esavedone.insert(0, self.saved_status)
        self.esavedone.grid(column=1, row=7, sticky=(W))
        self.esavedone.configure(state='readonly')

    # Helper methods are methods to do various stuff not exactly related to various
    # parts of the GUI.
    def get_screen_size(self):
        """ Get screen resolution from tkinter. """
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        return (width, height)

    def update_locked_field(self, widget, text, opened=False):
        """ Opens the widget, updates it and locks it. """
        widget.configure(state='normal')
        widget.delete(0, END)
        widget.insert(0, text)
        # If opened is False, then close the button again.
        if opened == False:
            widget.configure(state='readonly')

    def needs_update(self, value, field):
        """ Compares the values with the currently saved value end returns True if field needs update. """
        allow_deletion = ['combined']
        try:
            if value and value != self.current_event[field]:
                return True
            # If the value is empty but the field is allowed to be delete
            # (see allow_deletion above) this will return True.
            elif not value and field in allow_deletion:
                return True
            else:
                return False
        # If the key to update does not exist in the event,
        # we surely do not want to update it.
        except KeyError:
            return False

    def fix_timestamp(self, timestamp):
        # As timestamps generated by the collector are floats (good to sort chronologically),
        # they are strings when coming from updated GUI entry widgets and that breaks the
        # interaction with the dictionaries (self.clean_output). Therefore, we need to make sure
        # that the timestamp is fixed before using it.we need to make sure, the input from the GUI is correctly handled, since they only are
        # available as strings.
        # When the timestamp looks like a float, let's make it a float again. If it looks like an integer, we will make it an integer to
        # increase user's experience with them.
        if re.match("\d+\.\d+", timestamp):
            timestamp = float(timestamp)
        else:
            timestamp = int(timestamp)
        return timestamp

    # Menu commands

    def dummy(self):
        """ This method is a dummy method to connect buttons for testing.  """
        print("Widget connected to a dummy command.")

    def quit(self):
        """ Cleans the working directory and quits."""
        # If the status are "not saved" then the leftover files are safe to be purged.
        if self.saved_status == "not saved":
            for png in glob.glob("./*.png"):
                os.remove(png)
            for jsn in glob.glob("./*.json"):
                os.remove(jsn)
        # Destroy the main application window
        self.master.destroy()

    def handle_filenames(self, filename):
        """ Splits the path into a path part and the file name and updates self.choices. """
        # The filename holds the path to the file and we need to display that info
        # in a more user friendly way.
        fileinfo = os.path.split(filename)
        # the path to the file
        self.choices['path'] = fileinfo[0]
        # the name
        name = fileinfo[1].split('.')[0]
        # the file suffix
        suffix = fileinfo[1].split('.')[1]
        self.choices['filename'] = name
        self.choices['format'] = suffix
        # Update the GUI widget for Filename
        self.update_locked_field(self.efilename, self.choices['filename'])
        # Update the GUI widget for Format.
        self.update_locked_field(self.eformat, self.choices['format'])

    def open_new(self):
        """ Uses the file dialog to get the location and type of the future new file.

            Note, that this method does not create the file per se, file creation will happen later,
            when the Save menu item is used to actually save it.
        """
        filename = filedialog.asksaveasfilename(filetypes=[("json file","*.json"),("adoc file","*.adoc"),("html file","*.html"),("openqa file","*.pm"),("raw file","*.raw")])
        self.handle_filenames(filename)
        # Update the file status on Info panel
        self.saved_status = "not saved"
        self.update_locked_field(self.esavedone, self.saved_status)

    def open_existing(self):
        """ Opens an existing json file, loads the data, and populates the output variable
        depending on the type of the file. """
        filename = filedialog.askopenfilename(filetypes=[("json file", "*.json"), ("raw file", "*.raw")])
        with open(filename, 'r') as sourcefile:
            file_content = sourcefile.read()
            file_content = json.loads(file_content)
        # Split the filename and update self.choices.
        self.handle_filenames(filename)
        # Populate output variables depending on the file type.
        if self.choices['format'] == "raw":
            self.raw_output = file_content
            # For raw content, we need to run the interpreter and translate it for
            # further processing.
            self.interpret = interpreter.Interpreter(self.raw_output, stop_key="gui")
            self.clean_output = self.interpret.create_clean_report()
        elif self.choices['format'] == "json":
            self.clean_output = file_content
        else:
            print("Bad file format.")
        # Update the file status on Info panel
        self.saved_status = "saved"
        self.update_locked_field(self.esavedone, "saved")
        self.update_locked_field(self.enaction, "data loaded")
        self.update_locked_field(self.ertotal, len(self.raw_output))
        self.update_locked_field(self.ectotal, len(self.clean_output))
        # Reinit the frame to open buttons
        self.init_record_frame()

    def format_output(self):
        """ Use jinja templates to format output according to selection. """
        # Some of the formats are created with the help of jinja templates. The following lines
        # initiate the template environment.
        template_path = os.path.dirname(os.path.realpath(__file__))
        fload = FileSystemLoader(os.path.join(template_path, 'templates'))
        templates = Environment(loader=fload)
        # The translator that is used to convert the json report to formatted outputs
        # needs to know the screen size to calculate coordinates, so we use a method to
        # get them from the main tkinter widget.
        scr_resolution = self.get_screen_size()
        # Load the translator module and have the output created if needed.
        translate = translator.Translator(self.clean_output, scr_resolution)
        # Format the output.
        # If raw or json format is required, we will just pass the stored
        # data, that we have got from the recording session.
        if self.choices['format'] == "raw":
            source = self.raw_output
        elif self.choices['format'] == "json":
            source = self.clean_output
        # For other formats, we use the translator.
        elif self.choices['format'] == "adoc":
            lines = translate.polish_data(lang="adoc", skip=True)
            template = templates.get_template('page.adoc')
            source = template.render(title="Recorded workflow", report=lines)
        elif self.choices['format'] == "html":
            lines = translate.polish_data(lang="html", skip=True)
            template = templates.get_template('page.html')
            source = template.render(title="Recorded workflow", report=lines)
        elif self.choices['format'] == "pm":
            lines = translate.polish_data(lang="openqa", skip=True)
            template = templates.get_template('page.pm')
            source = template.render(title="Recorded workflow", report=lines)
        # Return formatted output
        return source

    def save_file(self):
        """ Saves the file into the selected location. """
        print(self.choices['filename'], self.choices['format'])
        # Use the self.choices to construct the path and target to save the data.
        filename = f"{self.choices['filename']}.{self.choices['format']}"
        filename = os.path.join(self.choices['path'], filename)
        # Format the output
        source = self.format_output()
        # Write it into the file
        with open(filename, 'w') as target:
            if self.choices['format'] == "raw" or self.choices['format'] == "json":
                json.dump(source, target)
            else:
                target.write(source)
        # Show the save status to the user.
        self.saved_status = "saved"
        self.update_locked_field(self.esavedone, self.saved_status)
        # Normally, the application stores the screenshot files into the working directory,
        # but if we save the workflow data elsewhere, we want to move the PNGs and JSONs
        # to that new location and not leave them in the working directory.
        for png in glob.glob('./*.png'):
            shutil.move(png, os.path.join(self.choices['path'], png))
        for needle in glob.glob('./*.json'):
            shutil.move(needle, os.path.join(self.choices['path'], needle))

    def set_inputfile(self):
        """ Use filedialog to get the path and name of the input file. """
        filename = filedialog.askopenfilename(filetypes=[("json file", "*.json")])
        self.choices['inputfile'] = filename
        print(self.choices['inputfile'])
        self.handle_filenames(filename)

    def set_format(self, form):
        """ Update the format entry widget. """
        self.choices['format'] = form
        self.update_locked_field(self.eformat, form)

    def show_about(self):
        """ Show the About information. """
        self.about = Toplevel()
        self.about.title("About")
        l = Label(self.about, text="Autococonut, version 1.5", font="sams 10 bold")
        info = [" ", " ",
                "This is a simple mouse and keyboard",
                "events tracker to record",
                "a workflow or a reproducer.",
                " ",
                "Created by Lukáš Růžička",
                "(lruzicka@redhat.com)",
                "Fedora QA",
                "Copyright Red Hat",
                " ",
                "Licensed under GPLv3."]
        l.grid(column=0, row=0)
        r = 1
        for i in info:
            t = Label(self.about, text = i)
            t.grid(column=0, row=r)
            r += 1
        b = Button(self.about, width=10, text="Thanks!", command=self.about.destroy)
        b.grid(column=0, row=r+1)

    def open_help(self):
        """ Open the documentation file. """
        webbrowser.open('docs/autococonut.html')


    # To be able to switch between two windows, we need to destroy the widgets,
    # so that they can be recreated again.
    def destroy_widgets(self, frame):
        """ Destroy widgets in the frame. """
        for widget in frame.winfo_children():
            widget.destroy()

    # Record frame stuff
    def init_record_frame(self):
        """ Initiate the widgets for the Recording frame. """
        self.destroy_widgets(self.functions)
        self.text = Text(self.functions, width=85, height=30)
        self.text.grid(column=0,row=0, columnspan=5)
        self.text.delete("0.1", END)
        self.text.insert("0.1", self.reclines)
        self.start = Button(self.functions, width=10, text="Start", background="#00DD33", command=self.start_recording)
        self.start.grid(column=0, row=1, pady=5)
        self.stop = Button(self.functions, width=10, text="Stop", background="#DD0033", command=self.stop_recording)
        self.stop.grid(column=1, row=1, pady=5)
        self.stop.configure(state='disabled')
        self.showraw = Button(self.functions, width=10, text="Show raw", command=self.show_raw_json)
        self.showraw.grid(column=2, row=1, pady=5)
        self.showclean = Button(self.functions, width=10, text="Show clean", command=self.show_clean_json)
        self.showclean.grid(column=3, row=1, pady=5)
        self.showformatted = Button(self.functions, width=10, text="Show formatted", command=self.show_formatted)
        self.showformatted.grid(column=4, row=1, pady=5)
        # Disable "Show" buttons if no output is ready.
        if not self.clean_output:
            self.showraw.configure(state='disabled')
            self.showclean.configure(state='disabled')
            self.showformatted.configure(state='disabled')


    # Revise frame stuff
    def init_edit_frame(self):
        """ Creates widgets for Edit Frame and assigns variables. """
        self.destroy_widgets(self.functions)
        self.ftitle = Label(self.functions, text="Recorded Event:", font="sans 10 bold")
        self.ftitle.grid(column=0,row=0,pady=5, sticky=(W))
        self.ltimestamp = Label(self.functions, text="Event time stamp:")
        self.ltimestamp.grid(column=0, row=1, sticky=(W))
        self.etimestamp = Entry(self.functions, width=50)
        self.etimestamp.grid(column=1, row=1, sticky=(W+E), padx=10)
        self.ltype = Label(self.functions, text="Event type:")
        self.ltype.grid(column=0, row=2, sticky=(W))
        self.etype = Entry(self.functions, width=50)
        self.etype.grid(column=1, row=2, sticky=(W+E), padx=10)
        self.lsubtype = Label(self.functions, text="Event subtype:")
        self.lsubtype.grid(column=0, row=3, sticky=(W))
        self.esubtype = Entry(self.functions, width=50)
        self.esubtype.grid(column=1, row=3, sticky=(W+E), padx=10)
        self.laction = Label(self.functions, text="Event action:")
        self.laction.grid(column=0, row=4, sticky=(W))
        self.eaction = Entry(self.functions, width=50)
        self.eaction.grid(column=1, row=4, sticky=(W+E), padx=10)
        self.lbutton = Label(self.functions, text="Used button:")
        self.lbutton.grid(column=0, row=5, sticky=(W))
        self.ebutton = Entry(self.functions, width=50)
        self.ebutton.grid(column=1, row=5, sticky=(W+E), padx=10)
        self.lkey = Label(self.functions, text="Used key:")
        self.lkey.grid(column=0, row=6, sticky=(W))
        self.ekey = Entry(self.functions, width=50)
        self.ekey.grid(column=1, row=6, sticky=(W+E), padx=10)
        self.ltext = Label(self.functions, text="Typed text:")
        self.ltext.grid(column=0, row=7, sticky=(W))
        self.etext = Entry(self.functions, width=50)
        self.etext.grid(column=1, row=7, sticky=(W+E), padx=10)
        self.lstartx = Label(self.functions, text="Start X:")
        self.lstartx.grid(column=0, row=8, sticky=(W))
        self.estartx = Entry(self.functions, width=50)
        self.estartx.grid(column=1, row=8, sticky=(W+E), padx=10)
        self.lstarty = Label(self.functions, text="Start Y:")
        self.lstarty.grid(column=0, row=9, sticky=(W))
        self.estarty = Entry(self.functions, width=50)
        self.estarty.grid(column=1, row=9, sticky=(W+E), padx=10)
        self.lendx = Label(self.functions, text="End X:")
        self.lendx.grid(column=0, row=10, sticky=(W))
        self.eendx = Entry(self.functions, width=50)
        self.eendx.grid(column=1, row=10, sticky=(W+E), padx=10)
        self.lendy = Label(self.functions, text="End Y:")
        self.lendy.grid(column=0, row=11, sticky=(W))
        self.eendy = Entry(self.functions, width=50)
        self.eendy.grid(column=1, row=11, sticky=(W+E), padx=10)
        self.lvertical = Label(self.functions, text="Vertical scroll:")
        self.lvertical.grid(column=0, row=12, sticky=(W))
        self.evertical = Entry(self.functions, width=50)
        self.evertical.grid(column=1, row=12, sticky=(W+E), padx=10)
        self.lhorizontal = Label(self.functions, text="Horizontal scroll:")
        self.lhorizontal.grid(column=0, row=13, sticky=(W))
        self.ehorizontal = Entry(self.functions, width=50)
        self.ehorizontal.grid(column=1, row=13, sticky=(W+E), padx=10)
        self.lcombo = Label(self.functions, text="Combined with:")
        self.lcombo.grid(column=0, row=14, sticky=(W))
        self.ecombo = Entry(self.functions, width=50)
        self.ecombo.grid(column=1, row=14, sticky=(W+E), padx=10)
        self.lprimary = Label(self.functions, text="Primary image name:")
        self.lprimary.grid(column=0, row=15, sticky=(W))
        self.eprimary = Entry(self.functions, width=50)
        self.eprimary.grid(column=1, row=15, sticky=(W+E), padx=10)
        self.lalternative = Label(self.functions, text="Alternative image name:")
        self.lalternative.grid(column=0, row=16, sticky=(W))
        self.ealternative = Entry(self.functions, width=50)
        self.ealternative.grid(column=1, row=16, sticky=(W+E), padx=10)
        # In Edit mode, we do not want to allow to open fields that are not
        # part of the edited event, so we will close all of them and only
        # open those available for editting later.
        if self.choices['report'] == 'edit':
            self.etimestamp.configure(state="readonly")
            self.etype.configure(state="readonly")
            self.esubtype.configure(state="readonly")
            self.eaction.configure(state="readonly")
            self.ebutton.configure(state="readonly")
            self.ekey.configure(state="readonly")
            self.etext.configure(state="readonly")
            self.estartx.configure(state="readonly")
            self.estarty.configure(state="readonly")
            self.eendx.configure(state="readonly")
            self.eendy.configure(state="readonly")
            self.evertical.configure(state="readonly")
            self.ehorizontal.configure(state="readonly")
            self.ecombo.configure(state="readonly")
            self.eprimary.configure(state="readonly")
            self.ealternative.configure(state="readonly")

        # Update Action field in the Status frame
        self.enaction.configure(state='normal')
        self.enaction.delete(0, END)
        if self.choices['report'] == 'create':
            self.enaction.insert(0, "create events")
        else:
            self.enaction.insert(0, "edit events")
        self.enaction.configure(state='readonly')
        # Create buttons with images, if the images exist. NOT IMPLEMENTED YET!
        #self.screens = Label(self.functions, text="Screenshots:")
        #self.screens.grid(column=0, row=14, sticky=(W))
        #try:
        #    self.aimage = PhotoImage(file="active.png")
        #    self.aimage = self.aimage.subsample(3, 3)
        #    self.pimage = PhotoImage(file="passive.png")
        #    self.pimage = self.pimage.subsample(3, 3)
        #except:
        #    self.aimage = None
        #    self.pimage = None
        #if self.aimage and self.pimage:
        #    self.active_screen = Button(self.functions, image=self.aimage)
        #    self.alternative_screen = Button(self.functions, image=self.pimage)
        #else:
        #    self.active_screen = Button(self.functions, text="Primary image")
        #    self.alternative_screen = Button(self.functions, text="Alternative image")
        #self.active_screen.grid(column=1, row=15, pady=5)
        #self.alternative_screen.grid(column=1, row=16, pady=5)
        # Create buttons to control the editation
        self.controls = Frame(self.functions)
        self.controls.grid(column=1, row=17, pady=10)
        self.saveit = Button(self.controls, width=10, text="Update", background="#DD9933", command=self.update_event)
        self.saveit.grid(column=1, row=0)
        self.previous = Button(self.controls, width=10, text="Previous", command=self.skip_previous)
        self.previous.grid(column=0, row=0)
        self.createit = Button(self.controls, width=10, text="Create", background="#00DD33", command=self.create_event)
        self.createit.grid(column=2, row=0)
        self.deleteit = Button(self.controls, width=10, text="Delete", background="#DD0033", command=self.delete_event)
        self.deleteit.grid(column=3, row=0)
        self.next = Button(self.controls, width=10, text="Next", command=self.skip_next)
        self.next.grid(column=4, row=0)

        # Zero out a pointer
        self.pointer = 0
        # Set the current event variable to {}, it will be filled with data but we still need
        # the empty one, too
        self.current_event = {}
        # Try to get the list of keys from self.clean_output
        try:
            self.datakeys = list(self.clean_output.keys())
            self.datakeys.sort()
        except AttributeError:
            self.datakeys = {}
        # Disable buttons and do stuff depending on chosen action.
        # If we want to edit existing data, do not allow the create button.
        if self.datakeys and self.choices['report'] == 'edit':
            self.createit.configure(state="disabled")
            first_key = self.datakeys[self.pointer]
            # Store the data in the object accessible variable, for further
            # tweaking.
            self.current_event = self.clean_output[first_key]
            self.display_event(first_key, self.current_event)
            print("Datakeys exist, editing them.")
        # If there are data, but we do want to add an entry
        elif self.datakeys and self.choices['report'] == 'create':
            self.createit.configure(state='normal')
            self.deleteit.configure(state='disable')
            self.previous.configure(state="disabled")
            self.next.configure(state="disabled")
            self.saveit.configure(state="disabled")
            print("Datakeys exist, creating more.")
        # If no data are available for editting, do not allow any interaction
        elif not self.datakeys and self.choices['report'] == 'edit':
            self.saveit.configure(state="disabled")
            self.previous.configure(state="disabled")
            self.next.configure(state="disabled")
            self.deleteit.configure(state='disabled')
            self.createit.configure(state='disabled')
            print("No datakeys but call for edit.")
        # If there are no data, we cannot delete them.
        elif not self.datakeys and self.choices['report'] == 'create':
            print("No datakeys, want to create")
            self.deleteit.configure(state='disabled')
            self.saveit.configure(state="disabled")
            self.previous.configure(state="disabled")
            self.next.configure(state="disabled")
        else:
            # This should not happen.
            print("Special setting in buttons occurred. Check.")
        # Read from the clean output and create a list of its keys for
        # navigating in the data.
        # Database pointer
        self.pointer = 0
        # If no clean output exists, there is no need to operate these buttons,
        # so we will disable them to prevent users from clicking it and creating
        # errors in GUI.
        # If there are some data, read the first event and display it.

    def display_event(self, timestamp, event):
        # Display info, but do a check for individual keys in order to be able to open
        # entry fields for available info only and leave the rest blocked, so that nothing
        # can be added above what is already in the event.
        keys = event.keys()
        if timestamp:
            self.update_locked_field(self.etimestamp, timestamp)
        if 'type' in keys:
            self.update_locked_field(self.etype, event['type'], opened=True)
        if 'subtype' in keys:
            self.update_locked_field(self.esubtype, event['subtype'], opened=True)
        if 'action' in keys:
            self.update_locked_field(self.eaction, event['action'], opened=True)
        if 'button' in keys:
            self.update_locked_field(self.ebutton, event['button'], opened=True)
        if 'key' in keys:
            self.update_locked_field(self.ekey, event['key'], opened=True)
        if 'coordinates' in keys:
            self.update_locked_field(self.estartx, event['coordinates'][0], opened=True)
            self.update_locked_field(self.estarty, event['coordinates'][1], opened=True)
        if 'end_coordinates' in keys:
            self.update_locked_field(self.eendx, event['end_coordinates'][0], opened=True)
            self.update_locked_field(self.eendy, event['end_coordinates'][1], opened=True)
        if 'combined' in keys:
            self.ecombo.configure(state='normal')
            self.ecombo.delete(0, END)
            if event['combined']:
                self.ecombo.insert(0, event['combined'])
        if 'screens' in keys:
            if event['screens']:
                self.eprimary.configure(state="normal")
                self.eprimary.delete(0, END)
                self.ealternative.configure(state="normal")
                self.ealternative.delete(0, END)
                if event['screens'][0]:
                    self.eprimary.insert(0, event['screens'][0])
                if event['screens'][1]:
                    self.ealternative.insert(0, event['screens'][1])
        if 'vertical' in keys:
            self.update_locked_field(self.evertical, event['vertical'], opened=True)
        if 'horizontal' in keys:
            self.update_locked_field(self.ehorizontal, event['horizontal'], opened=True)
        if 'text' in keys:
            self.update_locked_field(self.etext, event['text'], opened=True)
        print(event)

    def edit_events(self):
        """ Starts editing existing events. """
        # Set the editing flag, if there is anything to edit,
        # otherwise switch to create.
        if self.clean_output:
            self.choices['report'] = "edit"
        else:
            self.choices['report'] = "create"
        self.datakeys = list(self.clean_output.keys())
        self.datakeys.sort()
        self.init_edit_frame()

    def clear_edit_widgets(self, state):
        """ Delete all buttons and switch their status to read only. """
        self.etimestamp.delete(0, END)
        self.etimestamp.configure(state=state)
        self.etype.delete(0, END)
        self.etype.configure(state=state)
        self.esubtype.delete(0, END)
        self.esubtype.configure(state=state)
        self.eaction.delete(0, END)
        self.eaction.configure(state=state)
        self.ebutton.delete(0, END)
        self.ebutton.configure(state=state)
        self.ekey.delete(0, END)
        self.ekey.configure(state=state)
        self.estartx.delete(0, END)
        self.estartx.configure(state=state)
        self.estarty.delete(0, END)
        self.estarty.configure(state=state)
        self.eendx.delete(0, END)
        self.eendx.configure(state=state)
        self.eendy.delete(0, END)
        self.eendy.configure(state=state)
        self.ecombo.delete(0, END)
        self.ecombo.configure(state=state)
        self.eprimary.delete(0, END)
        self.eprimary.configure(state=state)
        self.ealternative.delete(0, END)
        self.ealternative.configure(state=state)
        self.evertical.delete(0, END)
        self.evertical.configure(state=state)
        self.ehorizontal.delete(0, END)
        self.ehorizontal.configure(state=state)
        self.etext.delete(0, END)
        self.etext.configure(state=state)

    def create_events(self):
        # Mark that we explicitely want to create an empty report.
        self.choices['report'] = 'create'
        self.datakeys = list(self.clean_output.keys())
        self.datakeys.sort()
        # Start the edit page
        self.init_edit_frame()


## Record Screen Commands

    def threaded(self):
        """ Represents the thread to be started. """
        self.collector.start()

    def start_thread(self):
        """ Start the thread. """
        self.running_thread = threading.Thread(target=self.threaded, daemon=True)
        self.running_thread.start()

    def start_recording(self):
        """ Start recording the events and deal with GUI events. """
        # Deal with UI stuff
        self.start.configure(state="disabled")
        self.stop.configure(state="normal")
        self.text.delete("1.0", END)
        self.text.insert(END, "---- The recording has been started. ----\n")
        self.showraw.configure(state="disable")
        self.showclean.configure(state="disable")
        self.showformatted.configure(state="disable")
        self.update_locked_field(self.eprogress, "Recording in progress")
        self.update_locked_field(self.ertotal, "Recording in progress")
        self.update_locked_field(self.ectotal, "Recording in progress")

        # Restore the report variables, to prevent events from being recorded if
        # recording is provided consecutively.
        self.raw_output = {}
        self.clean_output = {}

        # Start the collector.
        #if not self.running_thread:
        self.start_thread()
        #elif not self.running_thread.is_alive():
        #    self.start_thread()
        #    print(self.running_thread.native_id)
        #else:
        #    print(self.running_thread.native_id)

    def stop_recording(self):
        """ Stop recording and deal with necessary stuff.  """
        # Stop the collector
        self.collector.stop()
        # Store the raw output which is basically a collection of all events
        # returned from the collector.
        self.raw_output = self.collector.return_report()
        # Run the raw output through the interpreter to have cleaned report
        # created (supported events and meta events only).
        self.interpret = interpreter.Interpreter(self.raw_output, stop_key="gui")
        self.clean_output = self.interpret.create_clean_report()
        # Deal with UI
        self.start.configure(state="normal")
        self.stop.configure(state="disabled")
        self.showraw.configure(state="normal")
        self.showclean.configure(state="normal")
        self.showformatted.configure(state="normal")
        self.text.insert(END, "---- The recording has been stopped. ----\n")
        self.update_locked_field(self.eprogress, "Recording stopped")
        self.update_locked_field(self.ertotal, len(self.raw_output.keys()))
        self.update_locked_field(self.ectotal, len(self.clean_output.keys()))
        # Join the thread and let it stop.
        self.running_thread.join()
        # Now make sure, the report is known as "full"
        self.choices['report'] = "full"

    def show_raw_json(self):
        """ Display the raw report in the text window. """
        self.text.delete("1.0", END)
        self.text.insert("1.0", "---- List of all captured events. ----\n\n")
        self.text.insert(END, json.dumps(self.raw_output, indent=4))

    def show_clean_json(self):
        """ Display the clean report in the text window. """
        self.text.delete("1.0", END)
        self.text.insert("1.0", "---- List of interpreted events. ----\n\n")
        self.text.insert(END, json.dumps(self.clean_output, indent=4))

    def show_formatted(self):
        """ Show the formatted report in the text window. """
        # The format is selected based on the value in self.choices.
        # It can be altered using the Format menu, or using the New
        # File menu item.
        output = self.format_output()
        self.text.delete("1.0", END)
        self.text.insert("1.0", f"---- Workflow report in {self.choices['format']} ----\n\n")
        self.text.insert(END, output)

# Edit screen commands

    def update_event(self):
        """ Save edited values. """
        # Let us go over entry widgets and collect information from them,
        # and save the information in the self.current_event. From there,
        # it will propagate to the self.clean_output and be ready to save
        # it in the file.
        if self.needs_update(self.etype.get(), 'type'):
            self.current_event['type'] = self.etype.get()
        if self.needs_update(self.esubtype.get(), 'subtype'):
            self.current_event['subtype'] = self.esubtype.get()
        if self.needs_update(self.eaction.get(), 'action'):
            self.current_event['action'] = self.eaction.get()
        if self.needs_update(self.ebutton.get(), 'button'):
            self.current_event['button'] = self.ebutton.get()
        if self.needs_update(self.ekey.get(), 'key'):
            self.current_event['key'] = self.ekey.get()
        if self.needs_update(self.etext.get(), 'text'):
            self.current_event['text'] = self.etext.get()
        # Coordinates are a little bit troublesome, therefore some
        # magic is needed.
        if self.estartx.get() and self.estarty.get():
            coordinates = (int(self.estartx.get()), int(self.estarty.get()))
            if self.needs_update(coordinates, 'coordinates'):
                self.current_event['coordinates'] = coordinates
        if self.eendx.get() and self.eendy.get():
            coordinates = (int(self.eendx.get()), int(self.eendy.get()))
            if self.needs_update(coordinates, 'coordinates'):
                self.current_event['end_coordinates'] = coordinates
        if self.needs_update(self.evertical.get(), 'vertical'):
            self.current_event['vertical'] = int(self.evertical.get())
        if self.needs_update(self.ehorizontal.get(), 'horizontal'):
            self.current_event['horizontal'] = int(self.ehorizontal.get())
        if self.needs_update(self.ecombo.get(), 'combined'):
            self.current_event['combined'] = self.ecombo.get().split("-")

        screens = [self.eprimary.get(), self.ealternative.get()]
        if self.needs_update(screens, 'screens'):
            self.current_event['screens'] = screens
        # Update the Saved status field to indicate that the changes are
        # not saved.
        self.update_locked_field(self.esavedone, "not saved")

    def skip_previous(self):
        """ Navigate to a previous entry in the database of events. """
        # Decrease pointer in order to arrive at a previous item.
        self.pointer -= 1
        # Do not let it go into negative values in order not
        # skip to the end of list.
        if self.pointer < 0:
            self.pointer = 0
        # If we have data available
        if self.datakeys:
            # Try to read from the pointer if possible
            try:
                timestamp = self.datakeys[self.pointer]
                self.current_event = self.clean_output[timestamp]
                # Delete old values and replace them with new.
                self.clear_edit_widgets("readonly")
                self.display_event(timestamp, self.current_event)
            except IndexError:
                print("The data list seems to be empty.")

    def skip_next(self):
        """ Navigate to a next entry in the database of events. """
        # Increase pointer in order to arrive at a later item
        self.pointer += 1
        # If there are some data available
        if self.datakeys:
            # Try to read from the pointer if it is possible.
            try:
                timestamp = self.datakeys[self.pointer]
                self.current_event = self.clean_output[timestamp]
                # Delete old values and replace them with new.
                self.clear_edit_widgets("readonly")
                self.display_event(timestamp, self.current_event)
            except IndexError:
                # To make sure the pointer does not point outside of the list
                self.pointer -= 1
                print("Already at the end of report.")

    def delete_event(self):
        """ Deletes currently displayed event from the self.clean_output
        and displays the next item, if it is available. If not, it jumps
        to the previous item."""

        # Read the timestamp
        timestamp = self.fix_timestamp(self.etimestamp.get())
        # Unfortunately, when Json is opened from a file and not recorded,
        # timestamps are strings, so we need to fiddle with exceptions.
        # Delete the event based on its timestamp
        self.current_event = {}
        try:
            del(self.clean_output[timestamp])
        except KeyError:
            del(self.clean_output[str(timestamp)])
        # Update the data keys
        self.datakeys = list(self.clean_output.keys())
        self.datakeys.sort()
        # Update the Info about clean events
        self.update_locked_field(self.ectotal, len(self.datakeys))
        # Display the next event
        # Let us see, if there is an event at the same pointer, which
        # actually is the next event now, when the datakeys got renumerated.
        try:
            timestamp = self.datakeys[self.pointer]
        except IndexError:
            # If there still are some datakeys, then return one step back
            # to the previous event.
            if self.datakeys:
                # Move pointer one step back
                self.pointer -= 1
                timestamp = self.datakeys[self.pointer]
            else:
                timestamp = None
        # Lock all entry fields before we will start to open it for another event
        self.clear_edit_widgets("readonly")
        # If event exists, read it and display it.
        if timestamp:
            self.current_event = self.clean_output[timestamp]
            self.display_event(timestamp, self.current_event)
        else:
            # Block the button and make self.current_event empty.
            self.deleteit.configure(state='disabled')
            self.current_event = {}
        # Update Saved field
        self.update_locked_field(self.esavedone, "not saved")

    def create_event(self):
        """ Create an event from data entered into a form. """
        # Let us go over entry widgets and collect information from them,
        # and save the information in the self.current_event.
        # Then store it in the self.clean_output.
        # Let users use their own timestamps, but if they do not enter
        # anything, provide timestamp automatically.
        if self.etimestamp.get():
            timestamp = self.etimestamp.get()
        else:
            timestamp = time.time()
        # Make timestamps either floats or ints.
        if re.match("\d+\.\d+", timestamp):
            timestamp = float(timestamp)
        else:
            timestamp = int(timestamp)

        # Only create keys for non-empty values.
        if self.etype.get():
            self.current_event['type'] = self.etype.get()
        if self.esubtype.get():
            self.current_event['subtype'] = self.esubtype.get()
        if self.eaction.get():
            self.current_event['action'] = self.eaction.get()
        if self.ebutton.get():
            self.current_event['button'] = self.ebutton.get()
        if self.ekey.get():
            self.current_event['key'] = self.ekey.get()
        if self.etext.get():
            self.current_event['text'] = self.etext.get()
        if self.estartx.get() and self.estarty.get():
            coordinates = (int(self.estartx.get()), int(self.estarty.get()))
            self.current_event['coordinates'] = coordinates
        if self.eendx.get() and self.eendy.get():
            coordinates = (int(self.eendx.get()), int(self.eendy.get()))
            self.current_event['end_coordinates'] = coordinates
        if self.evertical.get():
            self.current_event['vertical'] = int(self.evertical.get())
        if self.ehorizontal.get():
            self.current_event['horizontal'] = int(self.ehorizontal.get())
        if self.ecombo.get():
            self.current_event['combined'] = self.ecombo.get().split("-")
        else:
            self.current_event['combined'] = []
        if self.eprimary.get() and self.ealternative.get():
            screens = [self.eprimary.get(), self.ealternative.get()]
            self.current_event['screens'] = screens
        # Save the current event into the self.clean_output.
        # We will not do any check for existing events, if an event
        # has the same timestamp, it will be overwritten without
        # any warning.
        self.clean_output[timestamp] = self.current_event
        self.update_locked_field(self.etimestamp, timestamp, opened=True)
        # Delete current event
        self.current_event = {}
        self.clear_edit_widgets("normal")
        # Deal with the updating the UI
        self.update_locked_field(self.ectotal, len(self.clean_output))
        self.update_locked_field(self.eprogress, "Manually entered")
        # Reset focus on the timestamp field again
        self.etimestamp.focus_set()

# Main application

appwin = Tk()
appwin.title("AutoCoconut - a workflow tracking tool.")
appwin.minsize(width=1024, height=550)
appwin.resizable(False, False)

appgui = AppGui(appwin)

appwin.mainloop()
