class linkedlist:

    def __init__(self):
        pass
    """
        Node class and its methods
    """
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        """
            Returns the linked list length
        """
        def length(self):
            len = 0
            currNode = self
            while(currNode != None):
                len = len + 1
                currNode = currNode.next
            return len
        
        """
            Prints the linked list in Human Readable way
        """
        def show(self):
            currNode = self
            while(currNode.next != None):
                print(currNode.data, end='->')
                currNode = currNode.next
            print(currNode.data)
            currNode = currNode.next


    """
        Creates linkedlist from the provided list
        Returns linkedlist
    """
    def createFromList(self, list_of_numbers):
        headNode = None
        currNode = None
        for data in list_of_numbers:
            node = self.Node(data)
            if headNode == None:
                headNode = node
            elif headNode.next is None:
                headNode.next = node
                currNode = headNode.next
            else:
                currNode.next = node
                currNode = node
        return headNode