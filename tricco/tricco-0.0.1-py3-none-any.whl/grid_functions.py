# xarray dataset that holds the grid
grid = None

# get_neighbors_of_cell:
#   returns edge neighbors of a given triangle
def get_neighbors_of_cell(triangle):
    return grid.neighbor_cell_index[:,triangle].values
   
# get_edges_of_cell:
#   returns the three edges of a given triangle
def get_edges_of_cell(triangle):
    return grid.edge_of_cell[:, triangle].values

# get_vertices_of_edge:
#   returns the two vertices of a given edge
def get_vertices_of_edge(edge):
    return grid.edge_vertices[:, edge].values
