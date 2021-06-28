# !/usr/bin/env python
# coding: utf-8
# version: 1.0
# author: Fennel
# contact: gongkangjia@gmail.com
# date: 2021/5/13
import re
import ast

_coord = ['COORDTYPE', 'P_ALP', 'P_BET', 'P_GAM', 'XCENT', 'YCENT']
_grid = [
    'COORDNAME', 'XORIG', 'YORIG', 'XCELL', 'YCELL', 'NCOLS', 'NROWS', 'NTHIK'
]


class Coord:
    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return "<Coord.{}>".format(self.__dict__)

    def __repr__(self):
        return "<Coord.{}>".format(self.__dict__)


class Grid:
    def __init__(self, name, coord, **kwargs):
        self.name = name
        self.coord = coord
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return "<Grid.{}>".format(self.__dict__)

    def __repr__(self):
        return "<Grid.{}>".format(self.__dict__)


class GRIDDESC:
    def __init__(self, filepath):
        self.filepath = filepath
        self._coords = {}
        self._grids = {}
        self._parse()

    def get_coord(self, coord_name):
        return self._coords[coord_name]

    def get_grid(self, grid_name):
        return self._grids[grid_name]

    @property
    def coords(self):
        return self._coords.keys()

    @property
    def grids(self):
        return self._grids.keys()

    def _parse(self):

        with open(self.filepath) as f:
            griddesc = f.read()

        griddesc = re.sub(r'!.*?(?=(\n|$))', '', griddesc)

        griddesc_lines = [i.strip() for i in griddesc.strip().split('\n') if i]

        assert griddesc_lines[-1] == "' '"

        blank_counter = 0

        i = 0
        while i < len(griddesc_lines):
            line = griddesc_lines[i]

            if line == "' '":
                blank_counter += 1
            else:
                i += 1
                cells = []
                for c in griddesc_lines[i].split():
                    c = c.strip("', ")
                    try:
                        print(c)
                        cells.append(ast.literal_eval(c))
                    except Exception as e:
                        cells.append(c)

                key = eval(line)

                if blank_counter == 1:
                    self._coords[key] = Coord(name=key, **dict(zip(_coord, cells)))
                elif blank_counter == 2:
                    print(cells)
                    grid_dict = dict(zip(_grid, cells))
                    print(grid_dict)
                    self._grids[key] = Grid(name=key, coord=self.get_coord(grid_dict["COORDNAME"]), **grid_dict)
            i += 1


if __name__ == '__main__':
    griddesc = GRIDDESC("../examples/GRIDDESC2")
    print(griddesc.coords)
    print(griddesc.grids)
    print("*" * 10)
    grid = griddesc.get_grid("YRD12_LYG")
    print(grid)
    print(grid.coord.name)