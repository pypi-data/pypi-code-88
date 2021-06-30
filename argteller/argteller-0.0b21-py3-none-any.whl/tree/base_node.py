


class BaseNode():
    
    def __init__(self, name, depth, node_type):
        
        self.name = name
        self.node_type = node_type  # topic, param, 
        self.depth = depth

        self.value = None
        
        self.topics = []
        self.sub_topics = []
        self.params = []
        self.avails = []
        self.examples = []
        self.options = []
        
    def add_topic(self, topic_node):
        self.topics.append(topic_node)
        
    def has_topics(self):
        return len(self.topics)>0

    def add_sub_topic(self, sub_topic_node):
        self.sub_topics.append(sub_topic_node)
        
    def has_sub_topics(self):
        return len(self.sub_topics)>0
        
    def add_param(self, param_node):
        self.params.append(param_node)
        
    def has_params(self):
        return len(self.params)>0
        
    def add_avail(self, avail_node):
        self.avails.append(avail_node)
        
    def has_avails(self):
        return len(self.avails)>0
    
    def add_example(self, example_node):
        self.examples.append(example_node)
        
    def has_examples(self):
        return len(self.examples)>0
    
    def add_option(self, option_node):
        self.options.append(option_node)
        
    def has_options(self):
        return len(self.options)>0

    def reset_param_node_values(self):

        def applied_method(node):
            if node.node_type=='param' and not node.is_preset():
                node.value=None

        self.traverse_tree_apply(applied_method) 

    
    def traverse_tree_apply(self, method):

        BaseNode._traverse_tree_apply(self, method)


    @staticmethod
    def _traverse_tree_apply(self, method):

        if self.has_topics():
        
            for topic in self.topics:
            
                method(topic)
                
                BaseNode._traverse_tree_apply(topic, method)
                
        if self.has_params():
            
            for param in self.params:
                
                method(param)
                
                BaseNode._traverse_tree_apply(param, method)
                
        if self.has_avails():
            
            for avail in self.avails:
                
                method(avail)
                
                BaseNode._traverse_tree_apply(avail, method)
                
        if self.has_examples():
            
            for example in self.examples:
                
                method(example)
                
                BaseNode._traverse_tree_apply(example, method)
                
        if self.has_options():
            
            for option in self.options:
                
                method(option)
                
                BaseNode._traverse_tree_apply(option, method)



    def traverse_tree_print(self):
        
        BaseNode._traverse_tree_print(self)
    
    @staticmethod
    def _traverse_tree_print(self):
        
        if self.has_topics():
        
            for topic in self.topics:
            
                print('\n{}'.format(topic.name))
                
                BaseNode._traverse_tree_print(topic)
                
        if self.has_params():
            
            for param in self.params:
                
                print('{}-{} : {}'.format(' '*param.depth*4, param.name, param.value))
                
                BaseNode._traverse_tree_print(param)
                
        if self.has_avails():
            
            for avail in self.avails:
                
                print('{}={}'.format(' '*avail.depth*4, avail.name))
                
                BaseNode._traverse_tree_print(avail)
                
        if self.has_examples():
            
            for example in self.examples:
                
                print('{}=={}'.format(' '*example.depth*4, example.name))
                
                BaseNode._traverse_tree_print(example)
                
        if self.has_options():
            
            for option in self.options:
                
                print('{}+{}'.format(' '*option.depth*4, option.name))
                
                BaseNode._traverse_tree_print(option)



                