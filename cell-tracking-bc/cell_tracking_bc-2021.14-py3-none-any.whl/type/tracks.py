# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from __future__ import annotations

import warnings as wrng
from typing import ClassVar, Iterator, Optional, Sequence, Tuple, Union

import networkx as grph

from cell_tracking_BC.in_out.console.uid import ShortID
from cell_tracking_BC.type.cell import cell_t


class track_t(grph.DiGraph):
    def OrderedCells(self) -> Sequence[cell_t]:
        """
        To be called only by single tracks (as opposed to forking tracks)
        """
        output = []

        cell = tuple(_cll for _cll in self.nodes if self.in_degree(_cll) == 0)[0]
        while cell is not None:
            output.append(cell)

            neighbors = tuple(self.neighbors(cell))
            if neighbors.__len__() == 0:
                cell = None
            elif neighbors.__len__() == 1:
                cell = neighbors[0]
            else:
                raise ValueError(
                    f"{track_t.OrderedCells.__name__}: Can be called only by single tracks"
                )

        return output

    def SegmentsIterator(self) -> Iterator[Tuple[int, cell_t, cell_t, bool]]:
        """"""
        time_points = grph.get_node_attributes(self, tracks_t.time_point)

        for edge in self.edges:
            is_last = self.out_degree(edge[1]) == 0
            yield time_points[edge[0]], *edge, is_last

    def __str__(self) -> str:
        """"""
        cell_labels = tuple(_cll.label for _cll in self.OrderedCells())

        return f"{self.__class__.__name__.upper()}: {cell_labels}"


class tracks_t(grph.DiGraph):

    time_point: ClassVar[str] = "time_point"

    def AddTrackSegment(
        self, src_cell: cell_t, tgt_cell: cell_t, src_time_point: int
    ) -> None:
        """"""
        self.add_node(src_cell, time_point=src_time_point)
        self.add_node(tgt_cell, time_point=src_time_point + 1)
        self.add_edge(src_cell, tgt_cell)

    def Clean(self) -> None:
        """"""
        for cell, time_point in self.RootCells(with_time_point=True):
            if time_point > 0:
                unordered_tracks = self._UnorderedTracksContainingCell(cell)
                self.remove_nodes_from(unordered_tracks)
            elif self.out_degree(cell) == 0:
                self.remove_node(cell)

    def IsConform(self, when_fails: str = "warn silently") -> bool:
        """
        when_fails:
            - "warn silently": Return a boolean
            - "warn aloud": Print a message and return a boolean
            - "raise": Raises a ValueError exception
        """
        issues = []

        for cell in self.nodes:
            if (n_predecessors := self.in_degree(cell)) > 1:
                issues.append(f"{cell}: {n_predecessors} predecessors; Expected=0 or 1")
            elif (n_successors := self.out_degree(cell)) > 2:
                issues.append(
                    f"{cell}: {n_successors} successors; Expected=0 or 1 or 2"
                )

        for cell, time_point in self.RootCells(with_time_point=True):
            if time_point > 0:
                issues.append(
                    f"{cell}: Root cell with non-zero time point ({time_point})"
                )
            if self.out_degree(cell) == 0:
                issues.append(f"{cell}: Empty track")

        if issues.__len__() > 0:
            if when_fails == "warn silently":
                return False
            elif when_fails == "warn aloud":
                issues.append(f"{self}: Conformity Check:")
                wrng.warn("\n".join(issues))
                return False
            elif when_fails == "raise":
                issues.append(f"{self}")
                raise ValueError("\n".join(issues))
            else:
                raise ValueError(f'{when_fails}: Invalid "when_fails" argument value')
        else:
            return True

    def RootCells(
        self, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        if with_time_point:
            output = (
                _rcd
                for _rcd in self.nodes.data(tracks_t.time_point)
                if self.in_degree(_rcd[0]) == 0
            )
        else:
            output = (_cll for _cll in self.nodes if self.in_degree(_cll) == 0)

        return tuple(output)

    def DividingCells(
        self, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        if with_time_point:
            output = (
                _rcd
                for _rcd in self.nodes.data(tracks_t.time_point)
                if self.out_degree(_rcd[0]) == 2
            )
        else:
            output = (_cll for _cll in self.nodes if self.out_degree(_cll) == 2)

        return tuple(output)

    def LeafCells(
        self, with_time_point: bool = False
    ) -> Sequence[Union[cell_t, Tuple[cell_t, int]]]:
        """"""
        if with_time_point:
            output = (
                _rcd
                for _rcd in self.nodes.data(tracks_t.time_point)
                if self.out_degree(_rcd[0]) == 0
            )
        else:
            output = (_cll for _cll in self.nodes if self.out_degree(_cll) == 0)

        return tuple(output)

    def TracksIterator(self, /, *, leaf_based: bool = True) -> Iterator[track_t]:
        """"""
        if leaf_based:
            return self._SingleTracksIterator()
        else:
            return self._ForkingTracksIterator()

    def _SingleTracksIterator(self) -> Iterator[track_t]:
        """"""
        for cell in self.LeafCells():
            track = self.TrackToLeaf(cell)
            yield track_t(self.subgraph(track))

    def _ForkingTracksIterator(self) -> Iterator[track_t]:
        """"""
        for track in grph.weakly_connected_components(self):
            yield track_t(self.subgraph(track))

    def TracksCells(self) -> Sequence[Sequence[cell_t]]:
        """"""
        output = []

        for track in self.TracksIterator():
            output.append(track.OrderedCells())

        return output

    def TracksFromRoot(self, root: cell_t) -> Sequence[Sequence[cell_t]]:
        """"""
        unordered = self._UnorderedTracksContainingCell(root)
        if unordered is None:
            return ()

        output = []

        leaves = (_nde for _nde in unordered.nodes if unordered.out_degree(_nde) == 0)
        for leaf in leaves:
            track = grph.shortest_path(unordered, source=root, target=leaf)
            output.append(track)

        return output

    def TrackToLeaf(self, leaf: cell_t) -> Optional[Sequence[cell_t]]:
        """"""
        unordered = self._UnorderedTracksContainingCell(leaf)
        if unordered is None:
            return None

        root = tuple(
            _nde for _nde in unordered.nodes if unordered.in_degree(_nde) == 0
        )[0]

        return grph.shortest_path(unordered, source=root, target=leaf)

    def _UnorderedTracksContainingCell(self, cell: cell_t) -> Optional[grph.DiGraph]:
        """"""
        for track in grph.weakly_connected_components(self):
            if cell in track:
                return self.subgraph(track)

        return None

    def __str__(self) -> str:
        """"""
        return (
            f"{self.__class__.__name__.upper()}.{ShortID(id(self))}\n"
            f"{self.number_of_nodes()=}\n"
            f"{self.number_of_edges()=}"
        )
