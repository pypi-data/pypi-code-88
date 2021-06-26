import os
from typing import List, Dict


class CommentProcessor():
    def __init__(self, codetags: List[str], ignore_directories: List[str]):
        """

        :param codetags: List of valid code tags
        :param ignore_directories: List of directories that should be ignored, by basename of directory.
            All children of such a directory are also ignored.
        """
        self.codetags = codetags
        self.ignore_directories = ignore_directories

    def check_ignored(self, path):
        """
        Checks if any ignored directory strings are in path
        :param path: The path to check
        :return: True if contained, else otherwise
        """
        while path != '':
            head, tail = os.path.split(path)
            if tail in self.ignore_directories:
                return True
            old_path = path
            path = head
            if old_path == path:
                return False
        return False

    def get_all_filenames(self, path: str) -> List[str]:
        """
        Returns all filenames that are directly under path
        directory or subdirectories.

        :param path: Path to a folder
        :return: List of all files in folder
        """
        walk_gen = os.walk(path, topdown=False)
        walks = []
        for walk in walk_gen:
            walks += [os.path.join(walk[0], x) for x in walk[2] if not self.check_ignored(walk[0])]
        return walks

    def filter_list_ending(self, path_list: List[str], ending: str) -> List[str]:
        """
        Filters out all strings from list which do not end with ending
        :param path_list: List of strings w/path
        :param ending: Only paths ending with ending are kept
        :return: Filtered list
        """
        return [x for x in path_list if x.endswith(ending)]

    def list_in_list(self, list1: List, list2: List) -> bool:
        """
        Returns true if list1 or list2 have any elements in common
        :param list1: List1, elements must implement __equals__
        :param list2: List2, elements must implement __equals__
        :return: True if lists have any element in common
        """
        return any([x in list2 for x in list1])

    def get_consecutive_comments(self, file_path: str) -> List[List[str]]:
        """
        Finds all consecutive comments in a python file
        :param file_path: Path to python file
        :return: List of all consecutive comments in file, each comment
            block is it's own list, containing one line of comments with
            the # removed. List[List[str]]
        """
        output = []
        with open(file_path, 'r') as f:
            lines = f.readlines()
            line_index = 0
            temp_list = []
            in_block_double_quote = False
            in_block_single_quote = False
            # Runs through py-file, adds """ """ and # and ''' '''
            # style comments
            while line_index < len(lines):
                line = lines[line_index]
                line = line.strip('\n')
                # To avoid crashes with lines containing only newline
                if line == '':
                    line = 'EMPTY'
                if in_block_double_quote:
                    if line[0:3] == '"""' or\
                            line.endswith('"""'):
                        temp_list.append(line)
                        in_block_double_quote = False
                        output.append(temp_list)
                        temp_list = []
                    else:
                        temp_list.append(line)

                elif in_block_single_quote:
                    if line[0:3] == "'''" or\
                            line.endswith("'''"):
                        temp_list.append(line)
                        in_block_single_quote = False
                        output.append(temp_list)
                        temp_list = []
                    else:
                        temp_list.append(line)

                elif line[0] == '#':
                    # Not last line and has a comment and next line does not have a codetag
                    # Note need to split on space, ex. to avoid non-existant code-tags, like
                    # TODOCTOR as in Testing_FOlder/Fish/Aliens/AlphaCentauri.py
                    if not line_index == len(lines)-1 and\
                            lines[line_index+1][0] == '#' and\
                            not self.list_in_list(self.codetags, line.split(" ")):
                        temp_list.append(line)
                    else:
                        temp_list.append(line)
                        output.append(temp_list)
                        temp_list = []

                elif line[0:3] == '"""':
                    temp_list.append(line)
                    in_block_double_quote = True
                    if line.endswith('"""') and line != '"""':
                        output.append(temp_list)
                        temp_list = []
                        in_block_double_quote = False

                elif line[0:3] == "'''":
                    temp_list.append(line)
                    in_block_single_quote = True
                    if line.endswith("'''") and line != "'''":
                        output.append(temp_list)
                        temp_list = []
                        in_block_single_quote = False

                line_index += 1
        return output

    def extract_comments(self, base_path: str, file_paths: List[str]) -> Dict[str, List[List[str]]]:
        """
        Calls get_consecutive_comments on all files in file_paths
        :param base_path: The folder that comments are extracted from
        :param file_paths: A list of file paths
        :return: Extracted comments from all files, indexed by file name
        """
        # FIXME Does not support several identical filenames
        return {os.path.relpath(x, base_path): self.get_consecutive_comments(x) for x in file_paths}

    def filter_out_comment_starts(self, stringlist: List[str]) -> List[str]:
        """
        Filters out all # and triple " and ' at end and start of list and string
        :param stringlist: List containing string
        :return: stringlist with removed starting #, ', " and ending ', "
        """
        hash_string = stringlist[0].startswith('#')
        single_dash_string = stringlist[0].startswith("'''")
        double_dash_string = stringlist[0].startswith('"""')

        output = []
        for string in stringlist:
            if hash_string:
                string = string.lstrip('#')
                output.append(string)
            elif single_dash_string:
                string = string.strip("'''")
                output.append(string)
            elif double_dash_string:
                string = string.strip('"""')
                output.append(string)
        output = [x.strip() for x in output]
        output = [x for x in output if x != '']
        return output

    def filter_out_comment_starts_all(self, dlls: Dict[str, List[List[str]]]) -> Dict[str, List[List[str]]]:
        """
        Calls filter_out_comment_starts on each list in lls
        :param dlls: Dictionary indexed by filename of list of list of strings
        :return: dlls filtered through filter_out_comment_starts
        """
        return {key: [self.filter_out_comment_starts(x) for x in dlls[key]] for key in dlls}

    def filter_out_non_codetag_comments(self, lls: List[List[str]], codetags: List[str]) -> List[List[str]]:
        """
        Filters out all comments not starting with a codetag.
        :param lls: List of all consecutive comments in file, represented as a list of strings
        :param codetags: List of all accepted codetags
        :return: lss with non-codetag comments removed
        """
        def _firstword_is_tag(firstword):
            return firstword in codetags
        output = [x for x in lls if _firstword_is_tag(x[0].split(' ')[0])]
        return output

    def filter_out_non_codetag_comments_all(self, dlls: Dict[str, List[List[str]]],
                                            codetags: List[str]) -> \
                                            Dict[str, List[List[str]]]:
        """
        Filters out all comments not starting with a codetag.
        :param dlls: Dictionary indexed by filename of list of list of strings.
        :param codetags: List of all accepted codetags
        :return: dlls with non-codetag comments removed
        """
        output = {key: self.filter_out_non_codetag_comments(dlls[key], codetags) for key in dlls}
        output = {key: output[key] for key in output if not len(output[key]) == 0}
        return output


# TODO Click interface
#      - Should support selecting desired code-tags and some sensible default, ex.
#        TODO, FIXME, BUG, REF, IDEA, !!!, HACK, TODOC (May only support a subset of all
#        codetags) WIP
# TODO Allow loading in from Azure, s.t. each comment gets the correct tag added
# TODO Implement updating from changes, s.t. a removed comment with a tag in relation
#      to an Azure export file with the _ag_ tag gets automatically set to done
# RFE Implement more code tags from comments, e.x. Fields from PEP 350, or azure fields
#     - Azure fields is probably the best, unless they overlap. PEP 350 was not approved, after all
# TODO Implement interpretation of fields as mentioned above as metadata
# TODO move out tags as metadata WIP


