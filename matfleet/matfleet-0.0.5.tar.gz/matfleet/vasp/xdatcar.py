#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/19"

import re
import logging
from typing import Sequence
import numpy as np

from dancingcell.utility.io_file import gopen, clean_lines
from dancingcell.vasp.poscar import Poscar
from dancingcell.mongodb.dancingdb import DancingDb

LOG = logging.getLogger(__file__)
LOG.setLevel(logging.INFO)


class XDATCAR(object):
    vasp_version = 5

    def __init__(self, cells: dict, natoms: int, head_info: str=None, xdatcar_labels=None):

        self._all_cell = cells
        self._natoms = natoms
        self._index = list(cells.keys())
        self._head_info = head_info if head_info else \
            '\n'.join(Poscar(cell=self._all_cell[self._index[0]]).get_string().split('\n')[:7])
        self._cell = cells[self._index[0]]
        self._xdatcar_labels = xdatcar_labels if xdatcar_labels else self._cell.labels

    @property
    def all_cell(self):
        return self._all_cell

    def update_key(self, old_new_dict):
        """
        更新all_cell的key值索引
        Args:
            old_new_dict: 旧key值对应的新key值构成的字典, 每隔元素都为int
                            将旧的1, 2, 3换成 4, 5, 6, old_new_dict={1:4, 2:5, 3:6}

        Returns: None，更新了self.all_cell

        """
        assert len(self._index) == len(old_new_dict)
        tmp_cell = {}
        for key, value in self._all_cell.items():
            tmp_cell[old_new_dict[key]] = value
        self._all_cell = tmp_cell

    @property
    def xdatcar_labels(self):
        return self._xdatcar_labels

    @xdatcar_labels.setter
    def xdatcar_labels(self, labels):
        self._xdatcar_labels = labels

    @property
    def natoms(self):
        return self._natoms

    @property
    def index(self):
        return self._index

    @property
    def head_info(self):
        return self._head_info

    @classmethod
    def from_str(cls, lines, comment=None):
        # lines = clean_lines(lines, remove_empty_lines=True, remove_return=True)
        tmp_cc = re.split(r"\n\s*\n", lines.rstrip(), flags=re.MULTILINE)
        if tmp_cc[0] == "":
            raise ValueError("Empty Xdatcar")
        # Parse positions
        lines = tuple(clean_lines(tmp_cc[0].split("\n"), False))

        head = lines[:7]
        comment = comment if comment else lines[0]
        if cls.vasp_version == 5:
            natoms =  sum([int(i) for i in lines[6].split()])
        else:
            raise ValueError("Only support vasp version == 5")

        tmp_cells = {}
        _pattern_steps = re.compile(r"Direct configuration=(.*)")

        for n in range(7, len(lines), natoms+1):
            step = _pattern_steps.search(lines[n])
            step = int(step.group(1))
            sss = '\n'.join(head) + '\n' + '\n'.join(lines[n:n+natoms+1])
            tmp_cells[step] = Poscar.from_str(data=sss, comment=comment).cell

        return cls(tmp_cells, natoms=natoms, head_info='\n'.join(head))

    @classmethod
    def from_file(cls, filename):
        with gopen(filename, 'r') as f:
            cls.from_str(''.join(f.readlines()))

    def set_index(self, nstart=1, nstop=-1, ninterval=1):
        if nstop > max(self._index) or nstop < 0:
            nstop = max(self._index)

        number = list(range(nstart, nstop + 1, ninterval))
        return number

    def from_large_file_todb(self):
        """
        读取包含10万个结构的xdatcar存在数据库中
        Returns:

        """
        pass

    def to_str(self, index=None, have_head_info: bool=True, rearrange_index: bool=True,
               start_num: int=1, set_all_num:Sequence[int]=None):
        """

        Args:
            index: 设置一个索引,可以是'1,10,2' 可以是[1,2,3,5]
            have_head_info: 输出的时候是否包头部信息
            rearrange_index: 在输出的时候是否重排所有的索引（因为XDATCAR中可能没有跳跃的数字索引）
            start_num:重排索引的话从几开始
            set_all_num: 按照指定的索引设置输出的序号（会覆盖掉重排指令）
        Returns:

        """
        if isinstance(index, str):
            nstart, nstop, ninterval =  map(int, index.split(','))
            number = self.set_index(nstart, nstop, ninterval)
        elif isinstance(index, (list, tuple)):
            number = index
        else:
            number = self.index
            # raise ValueError("Index must be: 1,10,3  or [1, 2, 3]")
        if have_head_info:
            lines = [self.head_info]
        else:
            lines = []

        if set_all_num:
            assert len(set_all_num) == len(number)

        for i in range(len(number)):
            if set_all_num:
                _nn = set_all_num[i]
            else:
                if rearrange_index:
                    _nn = i + start_num
                else:
                    _nn = number[i]

            config_step = 'Direct configuration=%6.d' % _nn

            sss = Poscar(cell=self._all_cell[number[i]]).get_string(direct=True).split('\n')[8:-1]
            lines.append(config_step)
            lines.append('\n'.join(sss))

        return '\n'.join(lines) + '\n'

    @staticmethod
    def _clean_line(content):
        return content.strip().replace('\n', '').split()

    def get_natoms_nelements(self):
        """
        获取XDATCAR中原子个数和Direct configuration起始行号，适应不同的vasp版本

        Returns: 元素符号，对应的原子个数，总的元素种类，总的原子个数，第一个config起始行，XDATCAR头几行

        """
        if self.vasp_version == 4:
            _read_nline = 6
        else:
            _read_nline = 8

        # with open(self.path, 'r') as f:
        #     tmp_content = [f.readline() for _ in range(_read_nline)]
        #
        # # elements = self._clean_line(tmp_content[-3])
        # atoms = list(map(int, self._clean_line(tmp_content[-2])))
        # return sum(atoms), _read_nline, tmp_content[:_read_nline - 1]

    def to_db(self,xdatcar_labels=None, need_init=False, update_label=False):
        """

        Args:
            xdatcar_labels: 唯一标识，作为从数据库索引时候使用
            need_init: 是否初始化数据库
            update_label：向某一个已经存在的XDATCAR中添加数据

        Returns:

        """
        fir = True

        if xdatcar_labels:
            self.xdatcar_labels = xdatcar_labels

        collection_name = 'xdatcar_document'
        db = DancingDb.from_dict({})
        if need_init:
            db.init()
        self.xdatcar_labels_collections = db['xdatcar_labels_index']

        a = self.xdatcar_labels_collections.find_one({"labels": self.xdatcar_labels})
        new_index = list(self._all_cell.keys())

        if a is None:
            self.xdatcar_labels_collections.insert_one({'labels': self.xdatcar_labels,
                                                        'index_num': ' '.join(list(np.array(new_index, dtype=np.str)))})
        else:
            if update_label:
                done_index = list(map(int, a['index_num'].split()))

                for i in new_index:
                    if i in done_index:
                        raise KeyError(" cell key: %d has exist, please change keys!" % i)

                a['index_num'] = a['index_num'] + ' ' + ' '.join(list(np.array(new_index, dtype=np.str)))
                self.xdatcar_labels_collections.find_one_and_replace({"labels": self.xdatcar_labels}, a)
                fir = False
            else:
                raise ValueError("This label exists, please change xdatcar_labels!")

        for key, value in self._all_cell.items():
            if fir:
                simple = False
            else:
                simple = True
            value.labels = '%s-%d' % (self.xdatcar_labels, key)
            sss = value.to_db(simple=simple)
            db[collection_name].insert_one(sss)
            fir = False

