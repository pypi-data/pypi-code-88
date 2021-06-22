import plotly.graph_objects as go
import numpy as np
import itertools


def PointCloud(array, color=None, size=1, name=""):
    assert array.ndim == 2 and array.shape[1] >= 3
    if array.shape[1] == 4 and color is True:
        color = array[:, 3]
    return go.Scatter3d(x=array[:, 0],
                        y=array[:, 1],
                        z=array[:, 2],
                        name=name,
                        mode='markers',
                        marker=dict(size=size, color=color))


def SimplicesMesh(simplices, color=None):
    print(simplices)
    vertices = dict()
    coordinates = []
    n = 0
    for simplex in simplices:
        for vertex in simplex:
            v = tuple(vertex)
            if v not in vertices:
                vertices[v] = n
                coordinates.append(vertex)
                n += 1

    simplices_by_vertex_index = np.array([
        [vertices[tuple(v)] for v in simplex] for simplex in simplices
    ])
    coordinates = np.array(coordinates)
    
    return  go.Mesh3d(x=coordinates[:, 0],
                      y=coordinates[:, 1],
                      z=coordinates[:, 2],
                      i=simplices_by_vertex_index[:, 0],
                      j=simplices_by_vertex_index[:, 1],
                      k=simplices_by_vertex_index[:, 2],
                      name="",
                      color=color,
                      showlegend=False)
    
    
def Simplices(simplices, color=None, width=1):
    d = len(simplices[0])
    ij_pairs = [(i, j) for j in range(d) for i in range(j + 1, d)]
    xs = []
    ys = []
    zs = []
    for simplex in simplices:
        for (i, j) in ij_pairs:
            xs.extend([simplex[i][0], simplex[j][0], None])
            ys.extend([simplex[i][1], simplex[j][1], None])
            zs.extend([simplex[i][2], simplex[j][2], None])
    return go.Scatter3d(
        x=xs, y=ys, z=zs, mode="lines", name="", showlegend=False, line=dict(color=color, width=width),
    )


def Loop(vertices, color=None, width=1):
    vs = np.concatenate([vertices, [vertices[0]]])
    return go.Scatter3d(x=vs[:, 0], y=vs[:, 1], z=vs[:, 2], mode="lines",
                        line=dict(color=color, width=width), name="",
                        showlegend=False)


def SimpleScene(xrange=None, yrange=None, zrange=None):
    return go.layout.Scene(
        xaxis=dict(range=xrange, visible=False),
        yaxis=dict(range=yrange, visible=False),
        zaxis=dict(range=zrange, visible=False),
    )
