from .tree.tree_parser import TreeParser

import inspect
import os
import functools

def initializer_error_handler(func):
    def wrapped_init(*args, **kwargs):
        
        try:
            func(*args, **kwargs)
            
        except Exception as e:
            
            sub_str = 'takes 1 positional argument but'
            
            if sub_str in str(e):
                raise Exception('Argteller disallows positional arguments. Please only use keyword arguments.')
                
            else:
                raise type(e)(str(e))
            
    return wrapped_init


class ArgtellerClassDecorator():
    
    def __init__(self, map_str, override=False):
        
        if os.path.exists(map_str):
            with open(map_str) as f:
                self.map_str = f.read()

        elif isinstance(map_str, str):
            self.map_str = map_str
                
        self.override = override
        
    def __call__(self, cls):
        
        class Wrapped(cls):
            
            @initializer_error_handler
            def __init__(cls_self, **kwargs):


                self.tree_parser = TreeParser()
                self.arg_tree = self.tree_parser.parse_tree(self.map_str)  # preset values set here


                tmp_cls_obj = cls.__new__(cls)
                names, _, _, defaults, _, _, _ = inspect.getfullargspec(tmp_cls_obj.__init__)

                if defaults is not None:
                    for name, default in zip(reversed(names), reversed(defaults)):

                        if not hasattr(cls_self, name):
                            setattr(cls_self, name, default)


                for k, v in kwargs.items():

                    if k == self.arg_tree.topic_choice_node and v is not None:
                        self.arg_tree.topic_choices = v



                
                # set node values
                for k, v in kwargs.items():
                    
                    if k in self.tree_parser.param_nodes_dict:
                        for node in self.tree_parser.param_nodes_dict[k]:
                            node.set_value(v)

                # for optional arguments
                for k, v in kwargs.items():
                    
                    if k in self.tree_parser.option_nodes_dict:

                        for node in self.tree_parser.option_nodes_dict[k]:
                            node.set_value(v)


                self.arg_tree.traverse_tree_find_used_params()


                for name, preset_value in self.arg_tree.messenger_node_pre.used_conditional_params:

                    if preset_value is None or name in kwargs:
                        continue

                    for node in self.tree_parser.param_nodes_dict[name]:

                        # print(name, preset_value)

                        node.value = preset_value

                    for node in self.tree_parser.option_nodes_dict[name]:

                        node.value = preset_value

                    preset_value = None


                # set cls fields
                for k, v in self.tree_parser.param_nodes_dict.items():
                    
                    if self.override:
                        setattr(cls_self, k, v[0].value)
                        
                    else:
                        
                        if not hasattr(cls_self, k):
                            setattr(cls_self, k, v[0].value)

                for k, v in self.tree_parser.option_nodes_dict.items():
                    
                    if self.override:
                        setattr(cls_self, k, v[0].value)
                        
                    else:
                        
                        if not hasattr(cls_self, k):
                            setattr(cls_self, k, v[0].value)


                self.arg_tree.traverse_tree_tell()

                if self.arg_tree.total_num_missing_args > 0:

                    self.tree_parser.tree.reset_param_node_values()
                    self.arg_tree.total_num_missing_args = 0  # must reset 
                    
                    return

                tmp_kwargs = {k: v for k, v in kwargs.items() if k in names[1:]}
                super(Wrapped, cls_self).__init__(**tmp_kwargs)

                self.tree_parser.tree.reset_param_node_values()
                
            cls.injected_method = self.injected_method
            
        return Wrapped
            
    def injected_method(self, a):
        return(a)

        
def ArgtellerMethodDecorator(source_name):
    
    def decorator(func):

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            
            new_signature = inspect.signature(func)
            
            new_args = [self]
    
            params = list(new_signature.parameters.values())
            
            if source_name in kwargs:
                
                source_obj = kwargs[source_name]
                source_obj_dict = source_obj.__dict__
                del kwargs[source_name]
                
            else:
                
                source_obj_dict = dict()

            missing_positional_arguments = []
                
            for i, param in enumerate(params):
                
                if i==0:
                    
                    continue
                
                if param.kind==inspect.Parameter.POSITIONAL_OR_KEYWORD:
                    
                    if len(args)>=i:
                        
                        new_args.append(args[i-1])
                    
                    elif param.name in kwargs:
                        
                        new_args.append(kwargs[param.name])
                        del kwargs[param.name]
                        
                    else:
                        
                        if param.name in source_obj_dict:
                            
                            new_args.append(source_obj_dict[param.name])
                            
                        else:
                            
                            if param.default==inspect._empty:
                                
                                missing_positional_arguments.append("'{}'".format(param.name))
                            
                            new_args.append(param.default)

            if len(missing_positional_arguments) > 0:

                missing_args = " and ".join(missing_positional_arguments)

                raise TypeError("__init__() missing {} required positional arguments: {} !".format(len(missing_positional_arguments), missing_args))
                        
            cr = func(*new_args, **kwargs) # call original function

            return cr

        return wrapper
    
    return decorator



