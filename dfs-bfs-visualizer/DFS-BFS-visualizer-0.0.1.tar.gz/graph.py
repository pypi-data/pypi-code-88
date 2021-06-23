class Node:
    def __init__(self, value=None):
        self.value = value
        self.connections = []
        
    def insert(self, value):
        if value != self.value:
            self.connections.append(Node(value))
        else:
            print('Node is already insertred!')
    
    def __str__(self):
        str_connections = '[ '
        for node in self.connections:
            str_connections += str(node.value) + ' '
        str_connections += ']'
        return 'value: ' +  str(self.value) + ' connections: ' + str_connections
    
node = Node(4)

node.insert(3)
node.insert(6)
node.insert(0)


print(node)