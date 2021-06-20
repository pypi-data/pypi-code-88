#!/usr/bin/python3
"""main file to see execution"""

from contextlib import closing
from io import StringIO, TextIOWrapper
import os
from pyjsonedit.tokenizer import tokenize
from pyjsonedit.parser import parse
from pyjsonedit.matcher import match_as_list
from pyjsonedit.editor import edit, editor_build_for_matching_nodes
from pyjsonedit.node_modify_action import build_node_modify_action


def __get_json_reader(json:str, writeable=False) -> TextIOWrapper:
    """ create reader from either raw string or file path"""
    if os.path.isfile(json):
        return closing(open(json, 'r+' if writeable else 'r'))
    return closing(StringIO(json))

def __read_tree(reader:TextIOWrapper):
    """ read JsonNode tree from json reader """
    return parse(list(tokenize(reader)))

def modify(pattern:str,
           json_string_or_file_name:str,
           template_string_or_file_name_or_char:str,
           insert:bool = False,
           print_out=True):
    """
    interface to access 'modify_matched_nodes_with_callback'
    with both file and sting as input

    pattern -
        string with patern to match one on multiple nodes
    json_string_or_file_name -
        json, either raw string or full file path of json
    template_string_or_file_name_or_char -
        this will replace each marched node, either raw string of full file path of python code
    insert -
        if true save chanes to file, else print
    """
    node_action = build_node_modify_action(template_string_or_file_name_or_char)

    with __get_json_reader(json_string_or_file_name,
                           writeable=insert) as json_reader:

        #step1 - read all tokens -> tree
        tree = __read_tree(json_reader)

        matched_nodes = match_as_list(tree, pattern)

        #step2 - match nodes by pattern and run user action on each match
        file_name = json_reader.name if hasattr(json_reader, 'name') else ''
        modifications = editor_build_for_matching_nodes(matched_nodes, file_name)

        #step3 - write modified output to temporary buffer
        with StringIO() as json_writer:
            json_reader.seek(0)
            edit(json_reader,
                 modifications,
                 node_action,
                 json_writer)

            #step3 - show results
            json_reader.seek(0)
            json_writer.seek(0)

            output_to = None
            save_to_file = insert and hasattr(json_reader, 'name')
            if save_to_file:
                json_reader.truncate(0)
                output_to = json_reader

            if print_out or save_to_file:
                print(json_writer.getvalue(),
                      file=output_to,
                      end='')
                return ''

            return json_writer.getvalue()


def string_match_mark(json, pattern, symbol='X'):
    """ easy interface for api/user """
    return modify(pattern,
                  json,
                  symbol,
                  insert=False,
                  print_out=False)

def string_tokenize(json_string:str):
    """ return list of tokens from string """
    with StringIO(json_string) as reader:
        return list(tokenize(reader))

def string_match(json_string:str, pattern:str):
    """ return list of tokens from string """
    matched_nodes = None
    with __get_json_reader(json_string,
                           writeable=False) as json_reader:

        #step1 - read all tokens -> tree
        tree = __read_tree(json_reader)

        matched_nodes = match_as_list(tree, pattern)

    return matched_nodes
