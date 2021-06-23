class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if self.value == None:
            self.value = value
        elif value <  self.value:         
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        else:
            print('Already inside tree!')
    
    def _make_list_tree(self,node):
        binary_tree_list = []

        if node.left:
            binary_tree_list = binary_tree_list + self._make_list_tree(node.left)
        
        if node.value:
            binary_tree_list.append(node.value)
            
        if node.right:
            binary_tree_list = binary_tree_list + self._make_list_tree(node.right)

        return binary_tree_list
    
    def __str__(self):
        
        list_tree = self._make_list_tree(self)
        
        return str(list_tree)
    
node = Node(3)

node.insert(2)

node.insert(4)

node.insert(7)

node.insert(1)

print(node)

