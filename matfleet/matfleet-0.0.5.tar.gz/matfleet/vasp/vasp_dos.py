#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2, 1, 2019"

from itertools import islice
import argparse
import numpy as np
try:
    from tqdm import trange
except ModuleNotFoundError:
    trange = range
    
"""
区分自旋和非自旋，可以获取指定原子，指定轨道的态密度（t, s, p, d）
"""


class DOS(object):
    def __init__(self, filename, efermi=None, fermi_zero=True, peratom=True, pri=True):
        """
        读取DOSCAR，并将数据分为 total dos data (tdos)和 particle dos data (pdos)
        :param filename: DOSCAR filename
        :param efermi: 自定义fermi能级的大小，如果不定义则从DOSCAR中读取
        :param fermi_zero: 是否将费米能级设置为0，即所有数据都减去费米能级，默认为True
        :param pri: 是否打印初始化信息
        """
        self.filename = filename
        self.fermi_zero = fermi_zero
        self.peratom = bool(peratom)

        f = open(self.filename)
        head = self.read_headlines(f)
        self.natoms = int(head[0][0])
        self.sys = head[4][0]
        self.nedos, read_efermi = int(head[-1][2]), float(head[-1][3])
        self.efermi = read_efermi if not efermi else efermi

        totdos = self.read_totaldos(f)
        self.spin = True if totdos.shape[-1] == 5 else False
        if self.peratom:
            totdos = self.set_stat_per_atom(totdos)

        self.dopdos = False
        pdos = self.read_pdos(f)

        self.totdos = totdos
        self.pdos = pdos
        self.display_info() if pri else None
        f.close()

    @staticmethod
    def make_spin(data):
        ind = np.arange(1, data.shape[-1], 1).astype(np.int32)
        spin1 = np.concatenate(([1], ind % 2 != 0)).astype(np.bool)
        spin2 = np.concatenate(([1], ind % 2 == 0)).astype(np.bool)
        return {'spin1': data[:, spin1],
                'spin2': data[:, spin2]}

    def display_info(self):
        print('Filename :   %s' % self.filename)
        print('System   :   %s' % self.sys)
        print('Natoms   :   %d' % self.natoms)
        print('Efermi   :   %.12f' % self.efermi)
        print('Nedos    :   %d' % self.nedos)
        print('Peratom   :   %s' % self.peratom)
        print('Spin     :   %s' % self.spin)
        print('Pdos     :   %s' % self.dopdos)

    @staticmethod
    def read_point_lines_to_list(f, num):
        return [x.strip().replace('\n', '').split() for x in islice(f, 0, num)]

    @staticmethod
    def read_point_lines_to_np(f, num):
        d = np.array([np.array(x.strip().replace('\n', '').split()).astype(np.float32) for x in islice(f, 0, num)])
        if num == 1:
            return d.flatten()
        else:
            return d

    def read_headlines(self, f):
        return self.read_point_lines_to_list(f, 6)

    def read_totaldos(self, f):
        data = self.read_point_lines_to_np(f, self.nedos)
        if self.fermi_zero:
            data = self.set_fermi_zero(data)
        return data

    def read_pdos(self, f):
        pdos = []
        for _ in trange(self.natoms):
            if len(f.readline()) > 0:
                pdos.append(self.read_point_lines_to_np(f, self.nedos))
            else:
                print("Don't have pdos data")
                return None

        if self.fermi_zero:
            pdos = self.set_fermi_zero(pdos)

        self.dopdos = True
        return np.array(pdos)

    def set_fermi_zero(self, data):
        data = np.array(data)
        assert (data.ndim >= 2) and (data.ndim <= 3)
        if data.ndim == 2:
            data[:, 0] = data[:, 0] - self.efermi
        else:
            data[:, :, 0] = data[:, :, 0] - self.efermi

        return data

    def set_stat_per_atom(self, data):
        data = np.array(data)
        if self.spin:
            data[:, 1:3] = data[:, 1:3] / self.natoms
        else:
            data[:, 1] = data[:, 1] / self.natoms
        return data

    @staticmethod
    def write_text(filename, data):
        with open(filename, 'w') as f:
            data = np.array(data, dtype=np.str)
            for i in range(data.shape[0]):
                f.write('\t'.join(data[i]) + '\n')

    @staticmethod
    def write_many_text(filename, data):
        assert len(data) >= 2
        for key, values in data.items():
            DOS.write_text(filename+'_%s' % key, values)

    @staticmethod
    def write_bin(filename, data):
        assert isinstance(data, dict)
        np.savez(filename, **data)

    def add_each_atom_data(self, index, pri=None):
        """
        是否计算每个原子的平均态密度
        :param index:
        :param pri:
        :return:
        """
        index = np.array(index, dtype=np.int32)
        index = index[index <= self.natoms]
        if pri:
            print('Add atoms: %s' % ' '.join(list((index+1).astype(np.str))))

        if self.dopdos:
            tmp = np.array([self.pdos[i, :, :] for i in index])
            if self.peratom:
                tmp = np.mean(tmp, axis=0)
            else:
                y = tmp[:, :, 1:]
                tmp = np.hstack((tmp[0, :, 0][:, np.newaxis], np.sum(y, axis=0)))
            return tmp
        else:
            print("Don't have pdos data")
            return np.array([])

    @staticmethod
    def get_input_number(number_string):
        return [x for x in range(int(number_string.split(',')[0])-1, int(number_string.split(',')[1]))]

    @staticmethod
    def checkdata(filename):
        f = np.load(filename)
        print('All data: %s' % '\t'.join([i for i in f.files]))

    def get_patom(self, atomlist, wri=True, write_filename='tmp_tpdos', pri=None):
        al = {keys+['_t', '_s', '_p', '_d'][i]: None for i, (keys, _) in enumerate(atomlist.items())}

        if self.dopdos:
            for keys, values in atomlist.items():
                if isinstance(values, list) or isinstance(values, tuple):
                    atom_list = (np.array(list(values)) - 1).tolist()
                elif isinstance(values, str):
                    atom_list = self.get_input_number(values)
                else:
                    raise TypeError

                tmpdata = self.add_each_atom_data(atom_list, pri=pri)

                if self.spin:
                    tt = self.make_spin(tmpdata)
                    ene = tt['spin1'][:, 0]
                    al[keys + '_t'] = np.vstack(
                        (ene, np.sum(tt['spin1'][:, 1:], axis=1), np.sum(tt['spin2'][:, 1:], axis=1))).T
                    al[keys + '_s'] = np.vstack((ene, tt['spin1'][:, 1], tt['spin2'][:, 1])).T
                    al[keys + '_p'] = np.vstack(
                        (ene, np.sum(tt['spin1'][:, 2: 5], axis=1), np.sum(tt['spin2'][:, 2: 5], axis=1))).T
                    al[keys + '_d'] = np.vstack(
                        (ene, np.sum(tt['spin1'][:, 5: 10], axis=1), np.sum(tt['spin2'][:, 5: 10], axis=1))).T
                else:
                    tt = tmpdata
                    ene = tt[:, 0]
                    al[keys+'_t'] = np.vstack((ene, np.sum(tt[:, 1:], axis=1))).T
                    al[keys+'_s'] = np.vstack((ene, tt[:, 1])).T
                    al[keys+'_p'] = np.vstack((ene, np.sum(tt[:, 2: 5], axis=1))).T
                    al[keys+'_d'] = np.vstack((ene, np.sum(tt[:, 5: 10], axis=1))).T

            if self.spin:
                # al['tdos'] = np.vstack((self.totdos[:, 0], self.totdos[:, 1], self.totdos[:, 3])).T
                al['tdos'] = self.totdos[:, :3]
            else:
                al['tdos'] = self.totdos[:, 0:2]

            if wri:
                assert write_filename
                self.write_bin(write_filename, al)
                self.checkdata(write_filename+'.npz')
        else:
            print('Please read pdos')
            exit()
        return al

    def get_orbit(self, orbit, atomlist=None, wri=True, write_filename=None, tp='bin'):
        atomlist = {'all': list(range(1, self.natoms+1))} if not isinstance(atomlist, dict) else atomlist
        al = self.get_patom(atomlist, wri=False, pri=False)
        orbit = [orbit] if isinstance(orbit, str) else orbit
        assert isinstance(orbit, list)
        al = {keys: values for i in orbit for keys, values in al.items() if i in keys}

        if wri:
            write_filename = '%s%s' % ('_'.join(orbit), self.filename) if not write_filename else write_filename
            self.write_bin(write_filename + '.npz', al) if tp == 'bin' else self.write_many_text(write_filename, al)
        print('Write file name: %s.npz' % write_filename) if tp == 'bin' else print(
            'Write file name: %s_*' % write_filename)
        print('Write data type: %s' % ', '.join(al.keys()))

    def __len__(self):
        return self.natoms

    def __getitem__(self, item):
        return self.make_spin(self.pdos[item]) if self.spin else self.pdos[item]


def run_dos(tmpargs=None):
    m_description = "区分自旋和非自旋，可以获取指定原子，指定轨道的态密度(t, s, p, d)"
    usage = """
示例：
    1. 画指定原子的贡献：2,108代表从第2原子到108原子全为Al:
    -a {'Zr':[1],'Al':'2,108'} -o ['t'] -p f -w y
    
    2. 画每个原子的每个轨道贡献:
    -a {'Zr':[1],'Al':'2,108'} -o ['s', 'p', 'd'] -p f -w y
    
    3. 画总dos:
    -p f -w y
    
    4. 画总dos，并将dos的值平均到每个原子:
    -p y -w y
    """
    
    from dancingcell.utility.auxbool_argparse import str2bool, str2list, str2dict
    parser = argparse.ArgumentParser(description=m_description, usage=usage)
    parser.add_argument('-f', '--filename', type=str, default='DOSCAR', help='DOSCAR name Default:DOSCAR')
    parser.add_argument('-e', '--efermi', type=float, help='efermi level')
    parser.add_argument('-o', '--orbit', type=str2list, default=['t'], help='which orbit you choose, [t, s, p, d]'
                                                                            ' Default: totaldos')
    parser.add_argument('-a', '--atomlist', type=str2dict, help="{'Zr': (1, 2), 'Al': '2 108'}'")
    parser.add_argument('-p', '--peratom', type=str2bool, default=True, help='DOS average to each atom, Default:True')
    parser.add_argument('-t', '--writetype', type=str, default='text', help='bin or text d:text')
    parser.add_argument('-w', '--iswrited', type=str2bool, default=False, help='Whether to write eightvalue file')
    
    args, unparsed = parser.parse_known_args(tmpargs)
    # at = {'Sb': (1, 2, 3), 'Te': '5 10', 'Ge': [12, 13, 43], 'C': '13 19'}
    # at = {'Zr': (1,), 'Al': '2 108'}
    dos = DOS(args.filename, efermi=args.efermi, peratom=args.peratom)
    dos.get_orbit(args.orbit, atomlist=args.atomlist, wri=args.iswrited, tp=args.writetype)


if __name__ == '__main__':
    # cmd = "-a {'Zr':[1],'Al':'2,108'} -o ['t'] -p f -w y".split()
    run_dos()
