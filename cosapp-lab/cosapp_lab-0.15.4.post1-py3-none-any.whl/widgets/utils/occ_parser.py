import logging
import uuid
from typing import List

import numpy as np

try:
    from OCC import Core as OCC_Core
    from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
    from OCC.Core import Poly
    from OCC.Core.TopExp import TopExp_Explorer
    from OCC.Core.BRepBndLib import brepbndlib
    from OCC.Core.Bnd import Bnd_Box
except ImportError as e:
    print(e)
    OCC_Core = None
    Poly = None
    BRepMesh_IncrementalMesh = None
    TopExp_Explorer = None

logger = logging.getLogger(__name__)


class OccParser:
    """Helper class to create a triangulation of shape."""

    def __init__(
        self, shape_list: "List[OCC_Core.TopoDS.TopoDS_Shape]" = None, mesh_quality=0.75
    ):
        """"""
        if (
            OCC_Core is not None
            and Poly is not None
            and BRepMesh_IncrementalMesh is not None
            and TopExp_Explorer is not None
        ):
            input_shape_list = shape_list
        else:
            input_shape_list = []
            logger.warning(
                "OCC or pyoccad can not be found, geometry viewer module will not work"
            )

        self.threejs_data = {}
        self.binary_data: List[np.ndarray] = []
        self.binary_position = {}
        self._faces = {}
        self._faces_pos = {}
        self.shape_idx = 0
        for shape in input_shape_list:
            if isinstance(shape, OCC_Core.TopoDS.TopoDS_Shape):
                my_deviation = self.compute_default_deviation(shape)

                self.threejs_data[self.shape_idx] = []
                if self.shape_idx == 0:
                    self.binary_position[self.shape_idx] = [0, -1]
                else:
                    last = self.binary_position[self.shape_idx - 1][1]
                    self.binary_position[self.shape_idx] = [last + 1, last]
                self.threejs_data[f"edge_{self.shape_idx}"] = []
                BRepMesh_IncrementalMesh(
                    shape, my_deviation * mesh_quality, False, 0.5 * mesh_quality, True
                )
                self.__build_face_mesh(shape)
                self.__build_edge_mesh(shape)
                self.shape_idx += 1
            else:
                self.threejs_data[self.shape_idx] = []
                if self.shape_idx == 0:
                    self.binary_position[self.shape_idx] = [0, -1]
                else:
                    last = self.binary_position[self.shape_idx - 1][1]
                    self.binary_position[self.shape_idx] = [last + 1, last]
                self.threejs_data[f"edge_{self.shape_idx}"] = []
                self.threejs_data[f"misc_{self.shape_idx}"] = shape.get("misc_data", {})
                if shape["shape"] is not None:
                    BRepMesh_IncrementalMesh(shape["shape"], 0.005, True, 0.5, True)
                    color = shape.get("color", "#156289")
                    trans = shape.get("transparent", False)
                    self.__build_face_mesh(shape["shape"], color, trans)
                    render_edge = shape.get("edge", False)
                    if render_edge:
                        self.__build_edge_mesh(shape["shape"])

                self.shape_idx += 1

    def __build_face_mesh(
        self,
        sh: "OCC_Core.TopoDS.TopoDS_Shape",
        color: str = "#156289",
        transparent: bool = False,
    ):
        """
        Create a triangle mesh of surface of input shape. This is a simplified
        version of the corresponding function in Pyoccad

        Parameters
        ----------
        sh : OCC_Core.TopoDS.TopoDS_Shape
            Input shape to me meshed.

        """
        expl = TopExp_Explorer(sh, OCC_Core.TopAbs.TopAbs_FACE)
        while expl.More():
            face = OCC_Core.TopoDS.topods.Face(expl.Current())
            self.__addFaceMesh(face, color, transparent)
            expl.Next()

    def __addFaceMesh(
        self, face: "OCC_Core.TopoDS.TopoDS_Face", color: str, transparent: bool
    ):
        """
        Helper function to create a triangle mesh of input surface . This is a simplified
        version of the corresponding function in Pyoccad

        Parameters
        ----------
        face : OCC_Core.TopoDS.TopoDS_Face
            Input shape to me meshed.

        """

        loc = OCC_Core.TopLoc.TopLoc_Location()
        T = OCC_Core.BRep.BRep_Tool().Triangulation(face, loc)
        if T is None:
            return

        nTri = T.NbTriangles()
        nVtx = T.NbNodes()
        vtx = []
        idx = []
        nodes = T.Nodes()
        tri = T.Triangles()
        trf = loc.Transformation()
        for pt in nodes:
            for d in range(1, 4):
                vtx.append(pt.Coord(d))
        for t in tri:
            for i in range(1, 4):
                idx.append(t.Value(i) - 1)

        faces = np.array(idx, "uint16")
        ret_faces = faces.tolist()
        self.threejs_data[self.shape_idx].append(
            {
                # "vertices": vtx,
                # "faces": ret_faces,
                "pos": [
                    trf.TranslationPart().X(),
                    trf.TranslationPart().Y(),
                    trf.TranslationPart().Z(),
                ],
                "quat": [
                    trf.GetRotation().X(),
                    trf.GetRotation().Y(),
                    trf.GetRotation().Z(),
                    trf.GetRotation().W(),
                ],
                "color": color,
                "transparent": transparent,
            }
        )
        self.binary_data.append(np.array(vtx, dtype="float64"))
        self.binary_data.append(faces)
        self.binary_position[self.shape_idx][1] += 2
        mesh_id = uuid.uuid4().hex
        self._faces[mesh_id] = face
        self._faces_pos[mesh_id] = vtx

    def __build_edge_mesh(self, sh: "OCC_Core.TopoDS.TopoDS_Shape"):
        """
        Create a the edge mesh input shape. This is a simplified
        version of the corresponding function in Pyoccad

        Parameters
        ----------
        sh : OCC_Core.TopoDS.TopoDS_Shape
            Input shape to me meshed.
        """
        edgeMap = OCC_Core.TopTools.TopTools_IndexedDataMapOfShapeListOfShape()
        OCC_Core.TopExp.topexp.MapShapesAndAncestors(
            sh, OCC_Core.TopAbs.TopAbs_EDGE, OCC_Core.TopAbs.TopAbs_FACE, edgeMap
        )

        for i in range(1, edgeMap.Size() + 1):
            faceList = edgeMap.FindFromIndex(i)
            if faceList.Size() != 0:
                face = OCC_Core.TopoDS.topods.Face(faceList.First())
                edge = OCC_Core.TopoDS.topods.Edge(edgeMap.FindKey(i))
                # Looking for face mesh to recover position buffer and save memory
                for mesh_id, f in self._faces.items():
                    if face.IsSame(f):
                        vertexBuffer = self._faces_pos.get(mesh_id, None)

                if vertexBuffer is not None:
                    loc = OCC_Core.TopLoc.TopLoc_Location()
                    T = OCC_Core.BRep.BRep_Tool().Triangulation(face, loc)
                    # EdPoly = Poly.PolygonOnTriangulation(edge, face, loc)
                    EdPoly = OCC_Core.BRep.BRep_Tool().PolygonOnTriangulation(
                        edge, T, loc
                    )
                    EdIdx = EdPoly.Nodes()
                    edIdx_list = []
                    for i in EdIdx:
                        edIdx_list.append(i - 1)

                    trf = loc.Transformation()
                    self.threejs_data[f"edge_{self.shape_idx}"].append(
                        {
                            "vertices": vertexBuffer,
                            "faces": edIdx_list,
                            "pos": [
                                trf.TranslationPart().X(),
                                trf.TranslationPart().Y(),
                                trf.TranslationPart().Z(),
                            ],
                            "quat": [
                                trf.GetRotation().X(),
                                trf.GetRotation().Y(),
                                trf.GetRotation().Z(),
                                trf.GetRotation().W(),
                            ],
                        }
                    )

    def compute_default_deviation(self, shape):
        """Get the minimum size of bounding box of a shape,
        this function is used to compute the mesh quality in
        tesselation.
        """

        a_box = Bnd_Box()
        brepbndlib.Add(shape, a_box)
        a_Xmin, a_Ymin, a_Zmin, a_Xmax, a_Ymax, a_Zmax = a_box.Get()
        return max(a_Xmax - a_Xmin, a_Ymax - a_Ymin, a_Zmax - a_Zmin) * 2e-2
