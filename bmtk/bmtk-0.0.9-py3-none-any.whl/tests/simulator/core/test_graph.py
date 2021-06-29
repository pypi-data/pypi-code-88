import pytest

from bmtk.simulator.core.graph import SimGraph

class MockNodes(object):
    def __init__(self):
        self.itr_idx = 0

    @property
    def nodes(self):
        return self

    @property
    def population_names(self):
        return ['A', 'B', 'C']

    @property
    def type_ids(self):
        return None

    def __iter__(self):
        self.itr_idx = 0
        return self

    def __next__(self):
        if self.itr_idx >= 100:
            raise StopIteration
        else:
            self.itr_idx += 1
            return 'Node'

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return self



def stest_simgraph_base():
    graph = SimGraph()

    nodes = MockNodes()
    graph.add_nodes(nodes)



if __name__ == '__main__':
    stest_simgraph_base()
