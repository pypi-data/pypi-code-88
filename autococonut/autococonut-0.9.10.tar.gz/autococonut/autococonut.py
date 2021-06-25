#!/usr/bin/env python3

"""
AutoCoconut - a recording tool to map your workflow.

This is the main script for the application.

Created by Lukáš Růžička (lruzicka@redhat.com). Licensed under GPLv3.
"""

from .engine import event_handler as event_handler
from .engine import interpreter as interpreter
from .engine import translator as translator
import argparse
import glob
import json
import os
import sys
import shutil
import time

from jinja2 import Environment, FileSystemLoader




class Parser():
    """ CLI Parser """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-s","--stopkey", default="f10", help="The dedicated key to stop listening to events.")
        self.parser.add_argument("-r","--resolution", default=None, help="To which screen resolution to switch before starting listening to the events.")
        self.parser.add_argument("-e","--offset", default="1", help="How long in seconds to wait before screenshot is taken.")
        #self.parser.add_argument("-t", "--printkey", default="f9", help="The dedicated key to print extra screenshots.")
        self.parser.add_argument("-o","--output", default="adoc", help="The form of the output (adoc, html, openqa, raw, json).")
        self.parser.add_argument("-f","--file", default=None,help="Store the output into a file instead of the screen.")
        self.parser.add_argument("-c","--caption", default="AutoCoconut - workflow report",help="The title of the output document.")
        #self.parser.add_argument("","", default="",help="")
        #self.parser.add_argument("","", default="",help="")

    def return_arguments(self):
        """ Return arguments used on CLI """
        args = self.parser.parse_args()
        return args

def create_pool_directory(dirname=None):
    """ Create a new directory and if successful, return its name. """
    if not dirname:
        time_ = time.ctime().replace(' ','_')
        dirname = f"screenshots_{time_}"
    cwd = os.getcwd()
    path = os.path.join(cwd, dirname)
    print("DIRECTORY TO CREATE: ",path)
    try:
        os.mkdir(path)
    except FileExistsError:
        print("The directory for this report's name exists already. Skipping the operation.")
    except OSError:
        print("Could not create the pool directory, leaving stuff in the working directory.")
    return dirname

def clean_working_directory(reportname=None, dirname=None, purge=False):
    """ Move all files created in this run into the dedicated directory. """
    needles = glob.glob("*.png")
    needle_json = glob.glob("*.json")
    if reportname:
        reports = glob.glob(reportname)
    else:
        reports = []
    workflow_files = needles + needle_json + reports
    if purge:
        print("Removing older files:")
        for f in workflow_files:
            print("\tRemoving ", f)
            os.remove(f)
    else:
        cdcontent = os.listdir()
        if not dirname:
            dirname = "hchkrdtn"
        if dirname in cdcontent:
            for f in workflow_files:
                shutil.move(f, f"{dirname}/{f}")
            print(f"Needles files and saved reports were moved to {dirname}.") 
        else:
            print("The target directory does not exist. Leaving files in the working directory.")
    

def main():
    """ The main method for the AutoCoconut script. """
    # Invoke the CLI Parser
    args_cli = Parser()
    cli = args_cli.return_arguments()

    # Use CLI arguments to specify the app run.
    stopkey = cli.stopkey
    offset = float(cli.offset)
    output = cli.output
    output = output.split(',')
    filename = cli.file
    caption = cli.caption

    # Delete older files that remained in the working directory
    clean_working_directory(filename, purge=True)
    # Start the collector
    collector = event_handler.Collector(stopkey, offset)
    try:
        collector.start()
    # Get the raw_report from the collector
    except KeyboardInterrupt:
        collector.stop()
    raw = collector.return_report()
    final_result = None
    # If we only want the raw output from the event handler.
    if "raw" in output:
        final_result = json.dumps(raw, indent=4, ensure_ascii=False)
    # Or we need to continue with better outputs.
    else:
        # Load the templates for output
        template_path = os.path.dirname(os.path.realpath(__file__))
        fload = FileSystemLoader(os.path.join(template_path, 'templates'))
        templates = Environment(loader=fload)
        # Start the interpreter over the collected data
        interpret = interpreter.Interpreter(raw, stop_key = stopkey)
        # Collect the json report from the interpreter
        json_report = interpret.create_clean_report()
        # Start the translator for more readable output
        translatte = translator.Translator(json_report)
        # If we want to get this json
        if "json" in output:
            # Make the json readable by humans.
            final_result = json.dumps(json_report, ensure_ascii=False, indent=4)
        # If other ouput is requested, use the appropriate template to generate it.
        elif "openqa" in output:
            lines = translatte.polish_data(lang="openqa")
            template = templates.get_template('page.pm')
        elif "html" in output:
            lines = translatte.polish_data(lang="html")
            template = templates.get_template('page.html')
        elif "adoc" in output:
            lines = translatte.polish_data(lang="adoc")
            template = templates.get_template('page.adoc')
        try:
            final_result = template.render(title=caption, report=lines)
        except UnboundLocalError:
            if final_result:
                print(final_result)
            else:
                print(f'It seems that the template for the selected format {output} is missing.')
    if not filename:
        print(f"============= {caption.upper()} =================================")
        print(final_result)
    else:
        # If a file is required.
        if filename:
            with open(filename, 'w') as out:
                out.write(final_result)
            # Clean the working directory by moving the files in a newly created subdir.
            prefix = filename.split('.')[0]
            directory = create_pool_directory(prefix)
            clean_working_directory(filename, directory)
        else:
            directory = create_pool_directory()
            clean_working_directory(filename, directory)


if __name__ == '__main__':
    main()
