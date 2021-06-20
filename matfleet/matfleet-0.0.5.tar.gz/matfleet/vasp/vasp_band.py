#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2020/11/09 21:37:10'

import re
import math
import numpy as np
import argparse
from tqdm import tqdm
from itertools import islice
from copy import deepcopy

"""
Used to generate bands and atom contributes
Also can be used to plot picture (support python3.*)
使用方法：
    1.第一次使用，必须带有-c的参数，从PROCAR中读取文件，并且会存储在tmp文件中
    2.第二次使用，不需要-c参数，会自动从tmp中读取数据（默认不带-c参数）
    3.-n参数每次使用必须制定，且用逗号隔开，否则会报错
    4.从POSCAR中读取第二行scale参数，通过-s指定，默认是1.0
    5.每个参数贡献值会通过散点画出来，点的大小通过脚本后面的参数控制，默认是200（因为有些原子贡献小，可以自己修改默认值）
    例子：
        第一次使用必须有-c：bppb.py -c 1 -n 1,20 -s 1.2 300
        已经有存储好的tmp，会自动读取，直接运行：bppb.py -n 1,20 200
        如果存在一个tmp文件想直接画图，运行 bppb.py即可
        如果存在多个tmp文件，运行bppb.py -n 指定原子序号即可
    TODO：
        本脚本不考虑自旋，即spin=1，后面会加上自旋的情况
    Debug：
        If you have any problem， please send email to author.
"""


class Bands(object):
    
    alter = {'t': [-1],
             's': [1],
             'p': [2, 3, 4], 'py': [2], 'pz': [3], 'px': [4],
             'd': range(5, 10), 'dxy': [5], 'dyz': [6], 'dz2': [7], 'dxz': [8], 'x2-y2': [9],
             'sp': [1, 2, 3, 4],
             'sd': range(1, 10),
             'pd': range(2, 10)
             }
    
    back_orbit = {'-1_-1': 't',
                  '1_1': 's',
                  '2_4': 'p', '2_2': 'py', '3_3': 'pz', '4_4': 'px',
                  "5_9": 'd', '5_5': 'dxy', '6_6': 'dyz', '7_7': 'dz2', '8_8': 'dxz', '9_9': 'x2-y2',
                  "1_4": 'sp',
                  "1_9": 'sd',
                  "2_9": 'pd'}
    
    def __init__(self, procar="PROCAR", outcar="OUTCAR", scale=1.0):
        self.procar = procar
        self.outcar = outcar
        self.nscale = scale
        self.band_data, self.band_contribution = {}, {}
        
        self.write_fn = []
        self.valuefn2writefn = {}
        
        with open(self.procar, 'r') as f:
            _, _, _, self.__nkpoints, _, _, _, self.__nbands, _, _, _, self.__nions = \
                self.read_point_lines(f, 2, is_list=True)[-1].split()
        
        self.ispin, self.__efermi, self.kpoint_path = self._get_kpoint_path(nscale=self.nscale)
        # 预估总的行数，可以显示进度条
        self.total_line = self.estimate_total_nlines()
        self.head_info()
        
    @property
    def nkpoints(self):
        return int(self.__nkpoints)
    
    @property
    def nbands(self):
        return int(self.__nbands)
    
    @property
    def nions(self):
        return int(self.__nions)
    
    @property
    def efermi(self):
        return self.__efermi
    
    @efermi.setter
    def efermi(self, x):
        self.__efermi = float(x)
        print("Reset e-fermi: %.8f \n" % x)
        
    def head_info(self):
        hi = '*' * 20 + " Info of %s " % self.procar + '*' * 20 + '\n'
        hi += 'Total Kpoints was {0},  Total Bands was {1},  Total atom was {2}\n'.format(self.nkpoints, self.nbands,
                                                                                          self.nions)
        hi += "Is spin: %s\n" % str(self.ispin)
        hi += "Default e-fermi: %.8f\n" % self.efermi
        hi += "PROCAR total lines: %10d\n" % self.total_line
        print(hi)

    @staticmethod
    def int2str(x, sim=True):
        tt = [str(i) for i in x]
        if sim:
            return [tt[0], tt[-1]]
        else:
            return tt

    def run(self, reduce_efermi=True, number_string='', orbit='', peratom=False, filename=None, get_contrib=False):
        atom_number_list, orbit_list = None, None
        
        if get_contrib:
            if number_string:
                atom_number_list = [self._get_input_number(i) for i in self.clean_split(number_string, ';')]
            else:
                atom_number_list = [list(range(self.nions))]
    
            if orbit:
                orbit_list = self.__orbit2list(orbit)
            else:
                orbit_list = [[-1]]
            
            if atom_number_list == [list(range(self.nions))] and orbit_list == [[-1]]:
                get_contrib = False
        
        if filename:
            self._make_fn(filename, get_contrib, atom_number_list=atom_number_list, orbit_list=orbit_list)
        
        self.get_only_band(reduce_efermi=reduce_efermi, atom_number_list=atom_number_list,
                           orbit_list=orbit_list, get_contrib=get_contrib, peratom=peratom)
        
        if filename:
            self.write_band()
    
    @staticmethod
    def clean_split(data, sep=','):
        return [i.strip() for i in data.replace('\n', '').split(sep)]
    
    def _get_input_number(self, number_string):
        """

        Args:
            number_string:

        Returns:返回输入指定开始和结尾原子的列表

        """
        star, stop, intervel = 0, 0, 1
        _ind = [int(x)-1 for x in self.clean_split(number_string)]
        if len(_ind) == 1:
            return _ind
        elif len(_ind) == 2:
            star, stop = _ind
        elif len(_ind) == 3:
            _ind[2] = _ind[2] + 1
            star, stop, intervel = _ind
        else:
            raise ValueError("Input wrong: %s , reinput number_string, split by ," % number_string)
    
        return [x for x in range(star, stop+1, intervel)]

    def __orbit2list(self, orbit_str):
        return [self.alter[_ti] for _ti in self.clean_split(orbit_str)]
    
    def _make_fn(self, filename, get_contrib=False, atom_number_list=None, orbit_list=None):
        if self.ispin:
            convert_name = {1.0: '_up', 2.0: '_down'}
        else:
            convert_name = {1.0: ''}
            
        for kk, vv in convert_name.items():
            self.valuefn2writefn[kk] = filename + vv + '.dcdat'
        
            if get_contrib:
                for atom_number in atom_number_list:
                    for orbit in orbit_list:
                        _k = str(kk) + '_'.join(self.int2str(atom_number)) + '_' + '_'.join(self.int2str(orbit))
                        _v = '_'.join(['a' + dd for dd in self.int2str([kk + 1 for kk in atom_number])]) + '_' + \
                             self.back_orbit['_'.join(self.int2str(orbit))]
                        self.valuefn2writefn[_k] = filename + vv + '_pband_' + _v + '.dcdat'
        
        self.write_fn = list(self.valuefn2writefn.values())
        
    def get_only_band(self, reduce_efermi=True, get_contrib=False,
                      atom_number_list=None, orbit_list=None, peratom=False):
    
        # info
        atom_info = ', '.join([str([m + 1 for m in dd]) for dd in atom_number_list]) if get_contrib else 'ALL'
        orbit_info = ', '.join([self.back_orbit['_'.join(self.int2str(orbit))] for orbit in orbit_list]) \
            if get_contrib else "ALL"
        orbin_index_info = ', '.join([str([m + 1 for m in dd]) for dd in orbit_list]) if get_contrib else "ALL"
        
        hi = '*'*20 + " Config parameters of bands " + '*' * 20 + '\n'
        hi += "Average to per atom: %s \n" % str(peratom)
        hi += "Get each atom or each orbit: %s \n" % str(get_contrib)
        hi += "Atom list: %s\n" % atom_info
        hi += "Orbit list: %s\n" % orbit_info
        hi += "Orbit index: %s\n" % orbin_index_info
        hi += "Write filename:\n  %s " % '\n  '.join(self.write_fn)
        print(hi)
        
        # 正则匹配模板
        band_pattern = re.compile(r'band(.*)# energy(.*)#.*')
        kpoint_pattern = re.compile(r' k-point(.*):.*weight.*')
        spin_pattern = re.compile(r'# of k-points:(.*)# of bands:(.*)# of ions:(.*)')
        
        # 初始化空字典和空数组
        nowkpoint = 0
        __tmp_kpoints = 0
        final_data = {}
        tmpdata = np.zeros((self.nkpoints, self.nbands), dtype=np.float)
        final_contribtutation = {}
        _subvalue_contribute_dit = np.zeros((self.nkpoints, self.nbands), dtype=np.float)

        if get_contrib:
            contribute_data = {'_'.join(self.int2str(atom_number)) + '_' +
                               '_'.join(self.int2str(orbit)): deepcopy(_subvalue_contribute_dit)
                               for atom_number in atom_number_list for orbit in orbit_list}
        else:
            contribute_data = {}
        # 显示进度条
        if get_contrib:
            total_line = self.total_line - (2 + self.nions) * self.nkpoints * self.nbands * 2
        else:
            total_line = self.total_line
        
        # 读取文件
        with open(self.procar, 'r') as f:
            for el in tqdm(f, total=total_line):
                if spin_pattern.search(el):
                    tmpdata = np.zeros((self.nkpoints, self.nbands), dtype=np.float)
    
                if kpoint_pattern.search(el):
                    nowkpoint = int(kpoint_pattern.search(el).groups()[0]) - 1
                    
                if band_pattern.search(el):
                    _dd = band_pattern.search(el).groups()
                    nband, energy = int(_dd[0])-1, float(_dd[1])
                    __tmp_kpoints += 1
                    tmpdata[nowkpoint][nband] = energy
                    
                    if get_contrib:
                        # skip blank and ion title
                        self.read_point_lines(f, 2, True)
                        contribute_dt = np.fromstring(''.join(self.read_point_lines(f, self.nions)),
                                                      dtype=np.float,
                                                      sep='\n').reshape((self.nions, -1))
                        
                        for atom_number in atom_number_list:
                            for orbit in orbit_list:
                                # 获取所有原子的指定轨道
                                _tmpcrontabdata = contribute_dt[:, orbit]
                                # 获取指定原子的指定轨道，并将所有轨道相加
                                _tmpcrontabdata = np.sum(_tmpcrontabdata[atom_number, :], axis=1)
                                # 是否要将贡献平均到每个原子
                                _tmpcrontabdata = np.average(_tmpcrontabdata) if peratom else np.sum(_tmpcrontabdata)
                                
                                contribute_data['_'.join(self.int2str(atom_number)) + '_' +
                                                '_'.join(self.int2str(orbit))][nowkpoint][nband] = \
                                    deepcopy(_tmpcrontabdata)
                    
                    # # skip blank and ion title
                    # if get_contrib:
                    #     self.read_point_lines(f, 2, True)
                    #     # contribute_dt = np.array([i.replace('\n', '').split()
                    #     #                           for i in self.read_point_lines(f, self.nions)],
                    #     #                          dtype=np.float)
                    #     # _tmpcrontabdata = np.sum(contribute_dt[atom_number, orbit]) if peratom \
                    #     #     else np.average(contribute_dt[atom_number, orbit])
                    #     contribute_dt = np.fromstring(''.join(self.read_point_lines(f, self.nions)),
                    #                                   dtype=np.float,
                    #                                   sep='\n').reshape((self.nions, -1))[:, 1:]
                    #     _tmpcrontabdata = np.sum(contribute_dt[atom_number, orbit]) if peratom \
                    #         else np.average(contribute_dt[atom_number, orbit])
                    #
                    #     _subvalue_contribute_dit[nowkpoint][nband] = _tmpcrontabdata

                    if nowkpoint == (self.nkpoints - 1) and nband == (self.nbands - 1):
                        if reduce_efermi:
                            tmpdata = tmpdata - self.efermi
                            
                        final_data[__tmp_kpoints/self.nkpoints/self.nbands] = deepcopy(tmpdata)
                        
                        if get_contrib:
                            final_contribtutation[__tmp_kpoints/self.nkpoints/self.nbands] = deepcopy(contribute_data)
                
            # for key, values in final_contribtutation.items():
                # print(key, values.shape)

            # for key, values in final_contribtutation.items():
            #     for i, j in values.items():
            #         print(key, i, j.shape)

        self.band_data = final_data
        self.band_contribution = final_contribtutation
        return final_data
    
    def write_band(self):
        if len(self.band_data) > 0:
            for key, values in self.band_data.items():
                fi = np.array(self.kpoint_path).reshape((-1, 1))
                data = np.hstack((fi, values))
                self.write_text(self.valuefn2writefn[key], data)
                
                if len(self.band_contribution) > 0:
                    for sub_name, data in self.band_contribution[key].items():
                        fi = np.array(self.kpoint_path).reshape((-1, 1))
                        write_data = np.hstack((fi, data))
                        self.write_text(self.valuefn2writefn[str(key)+sub_name], write_data)
        else:
            print("Wrong! Set band_data or run self.run()")
            exit()
        
    @staticmethod
    def write_text(filename, data):
        with open(filename, 'w') as f:
            data = np.array(data, dtype=np.str)
            for i in range(data.shape[0]):
                f.write('\t'.join(data[i]) + '\n')

    @staticmethod
    def read_point_lines(f, num, is_list=True):
        tmp = islice(f, 0, num)
        if is_list:
            return list(tmp)
        return tmp
    
    def estimate_total_nlines(self):
        # lines = 0
        # for i in range(self.nkpoints+1):
        nline = 4 + ((self.nions + 4) * self.nbands + self.nbands + 3) * self.nkpoints
        if self.ispin:
            return nline * 2 - 5
        else:
            return nline
    
    @staticmethod
    def _get_distance(data, scale):
        data = np.array(data, dtype=np.float)
        data1 = np.vstack((data[1:, :], np.zeros_like(data[0, :])))
        return [0] + (scale*np.sqrt(np.sum((data1 - data) ** 2, axis=1))[:-1]).tolist()
    
    def _get_kpoint_path(self, nscale=1.0):
        """
        对OUTCAR中kpoint的路径进行处理，PROCARE中记录的是倒空间K点的路径，因此必须从OUTCAR中读取
        返回k路径的列表，和每个路径K点个数

        Args:
            nscale:

        Returns:

        """
        ispin_parttern = re.compile(r'.*ISPIN.*=(.*)spin polarized.*')
        efermi_parttern = re.compile(r'.*E-fermi :(.*)XC.*')
        unit_kp = re.compile(r' k-points in units of 2pi/SCALE and weight:(.*)')
        ispin, efermi, final_distance = None, None, None
        getdi, getefer, getspin = 0, 0, 0
        
        with open(self.outcar, 'r') as f:
            for eachline in f:
                if unit_kp.search(eachline):
                    position = [[round(float(x), 8) for x in el.split()[0:3]] for el in islice(f, 0, self.nkpoints)]
                    distance = self._get_distance(position, scale=math.pi*2/nscale)
                    final_distance = [sum(distance[:i+1]) for i in range(len(distance))]
                    getdi = 1
                
                if efermi_parttern.search(eachline):
                    efermi = efermi_parttern.search(eachline)
                    efermi = float(efermi.groups()[0])
                    getefer = 1

                if ispin_parttern.search(eachline):
                    ispin = ispin_parttern.search(eachline)
                    ispin = False if int(ispin.groups()[0]) == 1 else True
                    getspin = 1
                    
                if getdi and getefer and getspin:
                    return ispin, efermi, final_distance
                
            raise ValueError("Can't find efermi or ispin or kpt_path!")


def run_band(tmpargs=None):
    m_description = "必须指定OUTCAR和PROCAR，根据OUTCAR中ISPIN参数自动判断是否存在自旋， 根据PROCAR画能带"
    usage = """
    示例：
        
        1. 查看帮助
            python vasp_band.py -h
        2. 画总能带
            python vasp_band.py -r True
        3. pband 帮助
            python vasp_band.py pband -h
        4. 指定1-10原子的s轨道
            python vasp_band.py pband -n 1,10 -o s
        5. 指定第8个原子的s至p轨道
            python vasp_band.py pband -n 8 -o sp
        6. 指定第1-20原子，每隔3个原子取一个，以及21-100的所有原子的p至d轨道
            python vasp_band.py pband -n 1,20,3;21,100 -o pd
        """
    
    from dancingcell.utility.auxbool_argparse import str2bool
    parser = argparse.ArgumentParser(description=m_description, usage=usage)
    parser.add_argument('-p', '--procar', type=str, default='PROCAR', help='PORCAR name Default:PROCAR')
    parser.add_argument('-o', '--outcar', type=str, default='OUTCAR', help='OUTCAR name Default:OUTCAR')
    parser.add_argument('-s', '--scale', type=float, default=1.0, help='Kpoint path scale factor.')
    parser.add_argument('-e', '--reduce_efermi', type=str2bool, default=True, help='Reduce efermi.')
    parser.add_argument('-ef', '--set_efermi', type=float, default=0, help='Reduce efermi.')
    parser.add_argument('-f', '--outputfn', type=str, default='band_data', help='OUTCAR name Default:OUTCAR')
    parser.add_argument('-r', '--run', type=str2bool, default=True, help='Run get bands.')

    sub_arg = parser.add_subparsers(dest='command', help='get contrib')
    pband_parser = sub_arg.add_parser('pband')
    pband_parser.add_argument('-n', '--number', type=str, default='', help='n,m: from n to m\n'
                                                                           'n,m,i: from n to m, intervel:i\n'
                                                                           'n,m,i;a,b,c: n,m,i and a,b,c\n')
    # choices=['s', 'p', 'd', 'sp', 'sd', 'pd', 't'],
    pband_parser.add_argument('-o', '--orbit', type=str, default='t',
                              help="Which orbit option: ['t', 's', 'p', 'px', 'py', 'pz', 'd', 'dxy', "
                                   "'dyz', 'dz2', 'dxz', 'x2-y2', 'sp', 'sd', 'pd']")
    pband_parser.add_argument('-p', '--peratom', type=str2bool, default=False,
                              help='Average contribute to each atom.')

    args, unparsed = parser.parse_known_args(tmpargs)
    bd = Bands(procar=args.procar, outcar=args.outcar, scale=args.scale)
    
    if args.set_efermi:
        bd.efermi = args.set_efermi
    
    if args.run and args.command != 'pband':
        bd.run(reduce_efermi=args.reduce_efermi, get_contrib=False, filename=args.outputfn)
    else:
        if args.command == 'pband':
            bd.run(reduce_efermi=args.reduce_efermi, number_string=args.number, orbit=args.orbit, peratom=args.peratom,
                   filename=args.outputfn, get_contrib=True)


if __name__ == '__main__':
    cmd = ''
    # cmd = '-h'.split()
    # cmd = '-r f'.split()
    # cmd = ['pband', '-n', '1; 2,10,2; 11, 108', '-o', 's, dz2, pd, x2-y2']
    run_band(cmd)
