import fnmatch
import glob
import os
from pathlib import Path


# todo: refactor
class Mindmap(object):
    def __init__(self, args, scope, edit_mode):
        self.args = args
        self.edit_mode = edit_mode
        self.working_dir = f"{Path.home()}/mindmap/"
        self.files = self.__get_files_in_scope(scope)
        self.path = self.__get_full_scope_path(scope)
        print(f"working path: {self.path}")

    def __call__(self):
        pass

    # public
    def read_note(self):
        for file in self.files:
            self.read_index(self.files.index(file))

    def read_note_file(self, file):
        self.read_index(self.files.index(file))

    def save_note(self, text):
        note = self.__format_note(text)
        note_file = open(self.files[0], "a+")
        note_file.writelines(note)

        print(f"note saved to {self.files[0]}")
        pass

    def list_scope(self):
        for file in self.files:
            self.__print_file(self.files.index(file), file)

    def query_scope(self, text):
        matches = []
        for filename in fnmatch.filter(self.files, f"*{text}*"):
            matches.append(filename)

        for file in matches:
            if self.args.read:
                self.read_note_file(file)
            else:
                self.__print_file(self.files.index(file), file)

    def read_index(self, index):
        if index > len(self.files):
            print(f"missing index: {index}")
            return
        filename = self.files[index]
        self.__print_file(index, filename)
        print(open(filename).read())

    # private
    def __format_note(self, note):
        return f"{note}\n"

    def __print_file(self, index, file, show_parent_path=True):
        if show_parent_path:
            file = file.replace(self.working_dir, '')

        file_info = f"{index}: {file}"
        print(file_info)

    def __get_full_scope_path(self, scope):
        return self.working_dir + "/".join(scope)

    def __get_files_in_scope(self, scope):
        scope_path = self.__get_full_scope_path(scope)
        if os.path.exists(scope_path):
            return [f for f in glob.glob(scope_path + "**/*.md", recursive=True)]
        elif os.path.exists(f"{scope_path}.md"):
            return [f"{scope_path}.md"]
        elif self.edit_mode:
            return [self.__create_folder(scope)]
        else:
            return []

    def __create_folder(self, scope):

        path = self.working_dir + "/".join(scope[:-1])
        Path(path).mkdir(parents=True, exist_ok=True)
        filepath = self.__get_full_scope_path(scope) + ".md"
        with open(filepath, 'w'):
            pass
        return filepath
