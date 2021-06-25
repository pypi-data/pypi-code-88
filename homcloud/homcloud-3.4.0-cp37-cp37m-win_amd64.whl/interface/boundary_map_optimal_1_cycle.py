from homcloud.visualize_3d import ParaViewSparseCubeDrawer, ParaViewSimplexDrawer
import homcloud.paraview_interface as pv_interface


class Optimal1Cycle(object):
    """The class represents an optimal (not volume-optimal) 1-cycle.

    This class is available only for alpha, cubical, rips, and abstract filtration
    with boundary map information.
    
    You can aquaire an optimal one cycle by :meth:`Pair.optimal_1_cycle`.
    """

    def __init__(self, pair, path):
        self.pair = pair
        self.path_edges = path

    def birth_time(self):
        """Returns the birth time of the pair.

        Returns:
            float: The birth time
        """
        return self.pair.birth_time()

    def death_time(self):
        """Returns the death time of the pair.

        Returns:
            float: The death time
        """
        return self.pair.death_time()

    def birth_position(self):
        """Birth position of the birth-death pair"""
        return self.pair.birth_position

    def path(self):
        """
        Returns:
            list of cell: All edges in the optimal 1-cycle.
        """
        return self.geometry_resolver(False).resolve_cells(self.path_edges)

    def path_symbols(self):
        """
        Returns:
            list of ssimplex: All edges in the optimal 1-cycle
            in the form of the symbolic representation.
        """
        return self.geometry_resolver(True).resolve_cells(self.path_edges)

    def boundary_points(self):
        """
        Returns:
            list of point: All vertices in the optimal 1-cycle.
        """
        return self.geometry_resolver(False).resolve_vertices(self.path_edges)

    def boundary_points_symbols(self):
        """
        Returns:
            list of string: All vertices in the optimal 1-cycle
            in the form of the symbolic representation.
        """
        return self.geometry_resolver(True).resolve_vertices(self.path_edges)

    def geometry_resolver(self, use_symbol):
        return self.pair.diagram.pd.geometry_resolver(use_symbol)

    def to_paraview_node(self, gui_name=None):
        geom_resolver = self.geometry_resolver(False)

        if self.pair.diagram.filtration_type == "cubical":
            drawer = ParaViewSparseCubeDrawer(1, 3, {"isboundary": "1"})
        elif self.pair.diagram.filtration_type == "alpha":
            drawer = ParaViewSimplexDrawer(1, geom_resolver.vertices, {"isboundary": "1"})
        else:
            raise(RuntimeError("Unsupported filtration type"))

        geom_resolver.draw_cells(drawer, self.path_edges, drawer.various_colors[0])

        f = pv_interface.TempFile(".vtk")
        drawer.write(f)
        f.close()
        return pv_interface.VTK(f.name, gui_name, f).set_representation("Wireframe")

    to_pvnode = to_paraview_node
