from .nodes import ArgTree
from .nodes import TopicNode
from .nodes import ParamNode
from .nodes import AvailNode
from .nodes import ExampleNode
from .nodes import CondNode
from .nodes import SubTopicNode
# from .nodes import OptionNode

from collections import defaultdict
import re

class TreeParser():


    def __init__(self):

        self.topic_nodes_dict = dict()
        self.sub_topic_nodes_dict = dict()
        self.param_nodes_dict = defaultdict(list)
        self.option_nodes_dict = defaultdict(list)
        self.preset_params = list()

        self.tree = None

    def parse_tree(self, string):
        
        current_topic = None
        current_sub_topic = None
        current_param = None

        self.tree = ArgTree(name='tree', depth=-2)

        node_count = 0
        current_pos_dict = {}


        topic_choice_node = None
        available_topics = []


        for line in string.splitlines():

            tab_depth = line.count('\t')
            space_depth = int((len(line) - len(line.lstrip(' ')))/4)
            depth = tab_depth + space_depth

            line = line.strip()


            if line=='':
                continue


            if line[0]=='@':
                topic_choice = line[1:]
                
                continue
            elif (topic_choice is not None) & (line[0]=='='):
                available_topics.append(line[1:])

                self.tree.topic_choices = available_topics
                self.tree.topic_choice_node = topic_choice

                continue
            elif (topic_choice is not None):

                print('{} = {}\n'.format(topic_choice, self.tree.topic_choices))

                topic_choice = None

            # else:
            #     pass

            



            if line[0] == '-':
                node_type = 'param'
            elif line[0] == '+':
                node_type = 'option'
            elif line[0:2] == '==':
                node_type = 'example'
            elif line[0] == '=':
                node_type = 'avail'
            elif line[0] == '?':
                node_type = 'cond'
            elif depth == 1:
                node_type = 'sub_topic'
            else:
                node_type = 'topic'









            name = re.sub('^[\s=+-?]+', '', line)


            # print(name, depth, tab_depth, space_depth)


            if node_type=='topic':

                if name != current_topic:
                    current_topic = name
                    topic_node = TopicNode(name, depth=-1)
                    self.tree.add_topic(topic_node)

                    current_pos_dict[-1] = topic_node

                    self.topic_nodes_dict[name] = topic_node


            elif node_type=='sub_topic':

                if name != current_sub_topic:
                    current_sub_topic = name

                    
                    prev_node = current_pos_dict[-1]

                    sub_topic_node = SubTopicNode(name, depth)
                    prev_node.add_sub_topic(sub_topic_node)

                    current_pos_dict[depth-1] = sub_topic_node

                    self.sub_topic_nodes_dict[name] = sub_topic_node



            elif node_type=='param':


                if ':' in name:
                    
                    

                    name, preset_value = name.split(':')
                    preset_value = eval(preset_value)
                    self.preset_params.append(name)
                

                else:
                    preset_value = None


                current_param = name

                prev_node = current_pos_dict[depth-1]

                # print(prev_node.node_type)

                current_node = ParamNode(name, depth)
                prev_node.add_param(current_node)


                if preset_value is not None:

                    # print(name, '::::::')

                    current_node.set_preset_value(preset_value)
                    current_node.make_preset()
                    preset_value = None

                current_pos_dict[depth] = current_node


                self.param_nodes_dict[name].append(current_node)






            elif node_type=='cond':


                if name in self.param_nodes_dict:

                    for node in self.param_nodes_dict[name]:

                        preset_value = node.preset_value
                        

                current_param = name

                prev_node = current_pos_dict[depth-1]

                current_node = CondNode(name, depth)
                prev_node.add_param(current_node)

                current_pos_dict[depth] = current_node

                if preset_value is not None:

                    current_node.set_preset_value(preset_value)
                    preset_value = None


                self.param_nodes_dict[name].append(current_node)


            elif node_type=='avail':

                prev_node = current_pos_dict[depth-1]

                current_node = AvailNode(name, depth)
                current_node.set_param(current_param)

                prev_node.add_avail(current_node)

                current_pos_dict[depth] = current_node

            elif node_type=='example':



                prev_node = current_pos_dict[depth-1]



                current_node = ExampleNode(name, depth)
                prev_node.add_example(current_node)

                # print(name, 'aaaaaa', prev_node.name, prev_node.node_type, prev_node.has_examples())

                current_pos_dict[depth] = current_node

            elif node_type=='option':  # only valid until here, afterwards, node type is param

                prev_node = current_pos_dict[depth-1]

                current_node = ParamNode(name, depth)
                prev_node.add_option(current_node)

                current_pos_dict[depth] = current_node

                self.option_nodes_dict[name].append(current_node)
                
        return self.tree












