from os import path
from robot304.parsing.model import ResourceFile
from .testDataVisitor import FindVisitor, TestDataNode, TestDataVisitor
class TestDataDependencyBuilder:
    """
    This func is used to classify testData with import dependency.
    testDataDir: the testData object after parsing.It could be `TestDataDirectory` or `TestCaseFile`.
    return: a tree's root node. It is a `TestDataNode` object.
    """
    def build(self,testDataDir):
        """
        This func is used to merge the `ResourceFile` Trees into a tree.
        resourceTrees: the `ResourceFile` Trees.
        return: a tree's root node.
        """
        def merge_resources_tree(resourceTrees):
            """
            This func is used to find the `ResourceFile` tree which is not imported by other `ResourceFile` tree.
            trees: the `ResourceFile` trees.
            return: the unimported `ResourceFile` or the first `ResourceFile`.
            """
            def get_unimported_resource(trees):
                for tree in trees:
                    source = tree.source
                    if all([not FindVisitor(target, source).has_result() for target in trees if target.source!=source]):
                        return tree
                return trees[0]
            trees = [tree for tree in resourceTrees.values()]
            trees_after_sort = []
            # Sort the `ResourceFile` trees order by their import dependency.
            # The unimported `ResourceFile` would be the first.
            for index in range(len(trees)):
                un_import_tree = get_unimported_resource(trees)
                trees_after_sort.append(un_import_tree)
                trees.remove(un_import_tree)
            root = TestDataNode(testDataDir)
            root.add_child(trees_after_sort.pop(0))
            # Merge trees with the order.
            for resource_root in trees_after_sort:
                find_visitor = FindVisitor(root, resource_root.source)
                # Found the same `ResourceFile` node been in the tree.
                if find_visitor.has_result():
                    # Replace the node with the `ResourceFile` tree for all nodes found in the tree. 
                    for node in find_visitor.get_result():
                        parent = node.parent
                        if parent:
                            parent.remove_child(node)
                            parent.add_child(resource_root)
                # No correspond node in the tree.
                # Add the `ResourceFile` tree as a child to root.
                else:
                    root.add_child(resource_root)
            return root
        """
        This func is used to build the import dependency of `ResourceFile` and `TestCaseFile`.
            `TestCaseFile` which import the `ResourceFile` would be that `ResourceFile` child.
        testData: the testData object after parsing.It could be `TestDataDirectory` or `TestCaseFile`.
        resourceTrees: a dict contains `TestDataNode` objects.
            All `TestDataNode` been in the dict are `ResourceFile`.
        """
        def build_resourceFile_trees(testData, resourceTrees):   
            for lib in testData.imports:
                source = path.normpath(testData.directory+'/'+lib.name)
                extension = path.splitext(source)[1]
                # Check whether the `ResourceFile` is existed.
                if path.exists(source) and extension !=".py":
                    # Check whether the `ResourceFile` had been parsed.
                    # It can save the parsing time.
                    if source not in resourceTrees.keys():
                        resource = ResourceFile(source=source).populate()
                        node = TestDataNode(resource)
                        node.add_child(TestDataNode(testData))
                        resourceTrees[source] = node
                        build_resourceFile_trees(resource, resourceTrees)
                    else:
                        # Add the testData as a child to the ResourceFile. 
                        resourceTrees[source].add_child(TestDataNode(testData))
            for child in testData.children:
                build_resourceFile_trees(child, resourceTrees)

        resource_trees = {}
        build_resourceFile_trees(testDataDir,resource_trees)
        return merge_resources_tree(resource_trees)