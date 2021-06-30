from os import path

def is_source_equal(source1, source2):
    return path.normpath(source1) == path.normpath(source2)

class TestDataNode:
    def __init__(self, testData):
        self.test_data = testData
        self.source = testData.source
        self.childs = []

    def get_data(self):
        return self.test_data

    def set_parent(self,parent):
        self.parent = parent

    def remove_child(self, child):
        self.childs.remove(child)
        child.set_parent(None)        

    def add_child(self, child):
        self.childs.append(child)
        child.set_parent(self)

    def accept(self, visitor):
        visitor.visit(self)

class TestDataVisitor(object):
    def __init__(self, func):
        self.func = func
    
    def visit(self,testData):
        is_continue = self.func(testData)
        if is_continue:
            for child in testData.childs:
                child.accept(self)

class FindVisitor(TestDataVisitor):
    def __init__(self, root, source):
        self.result = []
        def visit(node):
            if is_source_equal(node.source, source):
                self.result.append(node)
            return True
        super(FindVisitor, self).__init__(visit)
        root.accept(self)

    def get_result(self):
        return self.result
    
    def has_result(self):
        return len(self.result)>0