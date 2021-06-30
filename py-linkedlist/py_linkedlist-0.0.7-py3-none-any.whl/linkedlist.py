class linkedlist:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    
    def __getNode(self,data=None):
        """
        Returns a Node
        """
        return linkedlist(data)
    
    
               
    def removeAll(self):
        """
        Remove all nodes in linkedlist
        """ 
        self.data = None
        self.next = None

    
    def length(self):
        """
        Returns the linked list length
        """
        len = 0
        currNode = self
        while(currNode != None):
            len = len + 1
            currNode = currNode.next
        return len
    
    
    def show(self):
        """
        Prints the linked list in Human Readable way
        """
        currNode = self
        while(currNode.next != None):
            print(currNode.data, end='->')
            currNode = currNode.next
        print(currNode.data)
        currNode = currNode.next

    
    def addAtHead(self, val):
        """
        Add New Element at the head
        """
        if self.isEmpty():
            node = self.__create(val)
            self.data, node.data = node.data, self.data
        else:
            if type(val) not in [list, tuple]:
                val = [val]
            for value in val[::-1]:
                node = self.__create(value)
                node.next = self.next
                self.next = node
                self.data, node.data = node.data, self.data
            

    def add(self, val):
        """
        Append new Element to the linkedlist
        """
        node = self.__create(val)
        currNode = self
        if self.isEmpty():
            self.data, self.next = node.data, node.next
        else:
            while(currNode.next != None):
                currNode = currNode.next
            currNode.next = node

    
    def removeTail(self):
        """
        Removes the Tail element in the linkedlist
        """
        currNode = self
        prevNode = None
        while(currNode.next!= None):
            prevNode = currNode
            currNode = currNode.next

        if self == currNode:
            self.removeAll()
        else:
            prevNode.next = None

    
    def removeHead(self):
        """
        Removes the Head element in the linkedlist
        """
        currNode = self.next
        if currNode == None:
            self.removeAll()
        else:
            self.data, self.next = currNode.data, currNode.next     


    
    def removeElement(self, val):
        """
        Removes the first occurance of element in the linkedlist
        """ 
        currNode = self
        count = 0
        prev = None
        while(currNode.data != val):
            prev = currNode
            currNode = currNode.next
            if currNode == None:
                break

        if currNode == None:    # value not found
            pass
        elif currNode == self:  #Removing first element
            if self.next == None:
                self.data, self.next = None, None
            else:
                self.data, self.next = self.next.data, self.next.next
        elif currNode.next == None: # Removing last element
            prev.next = None
        elif prev.next == currNode: # removing middle element
            prev.next = currNode.next


         
    def removeAtLoc(self, loc):
        """
        Removes the element at given location in the linkedlist
        """  
        currNode = self
        prevNode = None
        while(loc > 1):
            prevNode = currNode
            currNode = currNode.next
            loc -=1

        if self == currNode:
            if self.next == None:
                self.removeAll()
            else:
                self.data, self.next = self.next.data, self.next.next
        else:
            prevNode.next = currNode.next

           
    def isEmpty(self):
        """
        Checks the linked list is empty or not
        """  
        return True if self.data is None and self.next is None else False

    
    def __create(self, list_of_numbers):
        """
        Creates linkedlist from the provided list
        Return: linkedlist
        """
        headNode = self.__getNode(None)
        currNode = None
        if type(list_of_numbers) not in [list, tuple]:
            list_of_numbers = [list_of_numbers]
        for data in list_of_numbers:
            node = self.__getNode(data)
            if currNode == None:
                headNode = node
                currNode = headNode
            elif headNode.next is None:
                headNode.next = node
                currNode = headNode.next
            else:
                currNode.next = node
                currNode = node
        return headNode