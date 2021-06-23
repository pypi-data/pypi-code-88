from random import randint


class SplitRectangleError(Exception):
    pass


# Binary tree node
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

    # An iterative process to print preorder traveral of BT
    def print(self):

        # Base CAse
        if self is None:
            return

            # create an empty stack and push root to it
        nodeStack = []
        nodeStack.append(self)

        # Pop all items one by one. Do following for every popped item
        # a) print it
        # b) push its right child
        # c) push its left child
        # Note that right child is pushed first so that left
        # is processed first */
        while (len(nodeStack) > 0):

            # Pop the top item from stack and print it
            node = nodeStack.pop()
            print(node.data)

            # Push right and left children of the popped node
            # to stack
            if node.right is not None and node.right not in nodeStack:
                nodeStack.append(node.right)
            if node.left is not None and node.left not in nodeStack:
                nodeStack.append(node.left)
            # Function to print leaf

    def get_leaf_nodes(self):
        leafs = []

        def _get_leaf_nodes(node):
            if node is not None:
                if node.is_leaf:
                    leafs.append(node.data)
                if node.left:
                    _get_leaf_nodes(node.left)
                if node.right:
                    _get_leaf_nodes(node.right)

        _get_leaf_nodes(self)
        return leafs
