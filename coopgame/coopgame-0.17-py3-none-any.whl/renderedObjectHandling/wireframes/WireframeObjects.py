from coopgame.renderedObjectHandling.wireframes.Wireframe import Wireframe
from typing import Tuple
import numpy as np
import logging
import MatrixManipulation as mm

class Cube(Wireframe):

    def __init__(self, origin: Tuple[int, int, int], size: int):
        super().__init__()
        self.size = size
        cube_nodes = [(x, y, z) for x in (origin[0], origin[0] + size) for y in (origin[1], origin[1] + size) for z in (origin[2], origin[2] + size)]
        self.addNodes(np.array(cube_nodes))
        self.addEdges(np.array([(n, n + 4) for n in range(0, 4)]))
        self.addEdges(np.array([(n, n + 1) for n in range(0, 8, 2)]))
        self.addEdges(np.array([(n, n + 2) for n in (0, 1, 4, 5)]))

class Triangle(Wireframe):

    def __init__(self, v1, v2, v3):
        super().__init__()
        self.addNodes(np.array([v1, v2, v3]))
        self.addEdges([(n, n + 1) for n in range(0, 2)])
        self.addEdges([(0, 2)])
        self.tuple = (v1, v2, v3)

class TriangleGridMesh(Wireframe):

    def __init__(self, grid_width: int, grid_height: int, scale: int):
        super().__init__()
        cols: int = int(grid_width / scale)
        rows: int = int(grid_height / scale)
        self.triangles = np.empty((0, 3), float)

        # self.triangles = []
        logging.info(f"Mesh being created: [{rows}] x [{cols}]")

        for ii in range(0, rows - 1):
            for jj in range(0, cols - 1):
                tri1 = Triangle((jj * scale, ii * scale, 0), ((jj + 1) * scale, ii * scale, 0),
                                    (jj * scale, (ii + 1) * scale, 0))
                tri2 =Triangle((jj * scale, (ii + 1) * scale, 0), ((jj + 1) * scale, (ii + 1) * scale, 0),
                                    ((jj + 1) * scale, ii * scale, 0))

                np.append(self.triangles, np.array(tri1.tuple), axis=0)
                np.append(self.triangles, np.array(tri2.tuple), axis=0)
                # self.triangles.append(tri1)
                # self.triangles.append(tri2)

                self.merge(tri1)
                self.merge(tri2)

    def update_mesh_heights(self, height_array):
        self.nodes[:, 2] = height_array
        # print (self.nodes)

if __name__ == "__main__":
    # cube = Cube((0,0,0), 1)
    # print(cube.edges)
    # cube.outputEdges()
    # cube.outputNodes()


    # triangle = Triangle((0, 0, 0), (25, 10, 50), (100, 125, 20))
    triangle = TriangleGridMesh(20, 20, 10)
    triangle.outputEdges()
    triangle.outputNodes()

    for ii in range(0, 10000):
        rotate = mm.rotateAroundPoint(triangle.findCentre(), [-.1, 0, 0])
        triangle.transform(rotate)

        triangle.outputNodes()

        rotate = mm.rotateAroundPoint(triangle.findCentre(), [.1, 0, 0])
        print(rotate)
        triangle.transform(rotate)

        triangle.outputNodes()