import numpy as np
from coopgame.coordinateConverter import CoordinateConverter as cc

class Wireframe:
    def __init__(self):
        self.nodes = np.zeros((0, 4), dtype=float)
        self.translation_coords = np.array([0, 0, 0], dtype=float)
        self.edge_node_ids = np.zeros((0, 2), dtype=int)
        self.object_centre = None

    def translated_nodes(self, matrix):
        return cc.apply_matrix_to_array(self.nodes, matrix)

    def translated_edges(self, matrix):
        t_nodes = self.translated_nodes(matrix=matrix)

        ret_edges = [(t_nodes[n1][:2], t_nodes[n2][:2]) for n1, n2 in self.edge_node_ids]

        return np.array(ret_edges)

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))
        self.object_centre = self._calculate_object_centre()

    def addEdges(self, edgeList):
        self.edge_node_ids = np.concatenate((self.edge_node_ids, edgeList))
        # self.edges += edgeList

    def outputNodes(self):
        print ("\n --- Nodes --- ")
        for i, (x, y, z, _) in enumerate(self.nodes):
            print(" %d: (%.2f, %.2f, %.2f)" % (i, x, y, z))

    def outputEdges(self):
        print( "\n --- Edges --- ")
        for i, (node1, node2) in enumerate(self.edge_node_ids):
            print (f" {i}: {node1} -> {node2} [({self.nodes[node1][0]}, {self.nodes[node1][1]}) -> ({self.nodes[node2][0]}, {self.nodes[node2][1]})]" )

    def _calculate_object_centre(self):
        """ Find the centre of the wireframe. """
        num_nodes = len(self.nodes)
        meanX = sum([node[0] for node in self.nodes]) / num_nodes
        meanY = sum([node[1] for node in self.nodes]) / num_nodes
        meanZ = sum([node[2] for node in self.nodes]) / num_nodes
        return np.array((meanX, meanY, meanZ, 1))

    def findCentre(self, orientation_matrix):
        """ Find the centre of the wireframe. """
        return cc.apply_matrix_to_array(self.object_centre, orientation_matrix)

    def merge(self, wireframe):
        curLen = np.max([len(self.nodes), 0])
        self.addNodes(wireframe.nodes[:3, :-1])

        # logging.debug(f"Here are the existing edges: {self.edges}, CurLen: [{curLen}]")
        newEdges = np.zeros((0, 4), dtype=float) #[]
        # logging.debug(f"Here are the new edges: {wireframe.edges}")

        wireframe_edge_array = wireframe.edge_node_ids + curLen
        self.edge_node_ids = np.concatenate((self.edge_node_ids, wireframe_edge_array))
        # for edge in wireframe.edges:
        #     newEdge = np.array(edge[0] + curLen, edge[1] + curLen)
        #     newEdges = np.concatenate((newEdges, newEdge))

        # self.addEdges(newEdges)
        # logging.debug(self.edges)


if __name__ == "__main__":
    my_wireframe = Wireframe()
    my_wireframe.addNodes([(0, 0, 0), (1, 2, 3), (3, 2, 1)])
    my_wireframe.addEdges([(1, 2)])