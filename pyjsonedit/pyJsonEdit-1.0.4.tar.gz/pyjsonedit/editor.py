"""
modifications/edits done to input json
"""
from typing import Callable,List
from collections import namedtuple
from pyjsonedit.parser import JsonNode


NodeMatchContext = namedtuple("NodeMatchContext", "file_name match_nr node")

class Modification:
    """
    text slice with start&end postion
    """
    def __init__(self, start:int, end:int, context:str):
        self.start= start
        self.end  = end
        self.context = context

    def is_pos_inside(self, pos:int):
        """
        check is given position is inside of this modification
        """
        return self.end> pos >= self.start

    def __repr__(self):
        return f'Modification[{self.start}:{self.end}]='+str(self.context)

class Modifications:
    """list of Modifications"""
    def __init__(self):
        self.modifications = []

    def find_starts_at(self, pos:int) -> Modification:
        """
        find first modification starting at 'pos'
        """
        for i in self.modifications:
            if i.start == pos:
                return i
        return False

    def add(self, start:int, end:int, context, strict=True):
        """
        start    position in input string
        end      position in input string
        context  matching context
        strict if set you can't add overlaping modifications
        returns: Modification on success
        """
        if strict:
            for i in self.modifications:
                if i.is_pos_inside(start) or i.is_pos_inside(end):
                    return False

        mod = Modification(start,end, context)
        self.modifications.append(mod)
        return mod


def editor_build_for_matching_nodes(matched_nodes:List[JsonNode],
                                    context_file_name:str) -> Modifications:
    """
    run user action on all matching tree nodes
    """
    modifications = Modifications()

    for match_nr,node in enumerate(matched_nodes):
        ctx = NodeMatchContext(file_name=context_file_name, match_nr=match_nr, node=node)
        modifications.add(node.start,node.end,ctx)

    return modifications

def edit(input_reader,
         modifications:Modifications,
         node_action:Callable[...,str],
         output_writer):
    """
    apply modification to string
    """
    pos = 0
    while True:
        mod = modifications.find_starts_at(pos)
        if mod:

            jump = mod.end-pos
            raw = input_reader.read(jump)
            pos += jump

            out = node_action(raw, mod.context)

            if mod.context.node.type == ":after":
                output_writer.write(raw)
                output_writer.write(out)
            elif mod.context.node.type == ":before":
                output_writer.write(out)
                output_writer.write(raw)
            else:
                output_writer.write(out if out else raw)
            continue

        char = input_reader.read(1)
        if not char:
            break
        output_writer.write(char)
        pos += 1
