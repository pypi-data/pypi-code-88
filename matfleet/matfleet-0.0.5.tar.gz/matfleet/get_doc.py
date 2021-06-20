#   coding:utf-8
#   This file is part of potentialmind.
#
#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = " 09/04/2019"

import os

dir_order = ['tools', 'core', 'utilities', 'utility', 'vasp']

final_file = os.path.join(os.path.dirname(__file__), 'source.code.txt')
final_file = open(final_file, 'w', encoding="UTF8")


def deal_one_dir(dir_path):
    rm_line_index = [1, 2, 3, 4, 5, 7, 8, 9]
    rp = [os.path.join(dir_path, i) for i in os.listdir(dir_path) if (i.endswith('.py') or 'POSCAR' in i  or 'cif' in i or 'xyz' in i or 'xsf' in i or 'envirment' in i)]
    for i in rp:
        with open(i, 'r', encoding='UTF8') as f:
            lines = f.readlines()
            if len(lines) > 11:
                try:
                    for r in reversed(rm_line_index):
                        lines.pop(r)
                except:
                    pass
                
                final_file.write(''.join(lines))
                final_file.write('\n')


if __name__ == '__main__':
    deal_one_dir(os.path.dirname(__file__))

    for m in dir_order:
        _ = os.path.join(os.path.dirname(__file__), m)
        deal_one_dir(_)

