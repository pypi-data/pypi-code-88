#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/09/24"

import numpy as np
import pandas as pd


def read_csv(fn):
    assert fn.endswith('.csv')
    df = pd.read_csv(fn)
    head = df.keys().values
    cont = df.values
    cont = np.vstack((head, cont))
    
    print("Table shape: %s" % str(cont.shape))
    return cont.astype(np.str)


def _clean_str(st):
    # if st.startswith('nan'):
    #     st = '-'
    return st.replace('\\', '\\\\').replace('_', '\_').replace('\n', '')


def deal_tex_table(cont, add_caption='', add_label='', ver_style=0, hor_style=3, posi='l'):
    cont = np.array(cont)
    tmple ="""
\\begin{table}
    \centering
    \caption{%s}
    \label{%s}
    \\resizebox{\\textwidth}{!}{
    \\begin{tabular}{%s}
    \hline
    %s
    \hline
    %s
    \hline
    \end{tabular}
    }
\\end{table}
    """
    if hor_style == 3:
        stuff = '\\\\ \n'
    else:
        stuff = '\\\\ \hline \n'
        
    _tt = [posi] * cont.shape[-1]
    type_info = '|'.join(_tt) if ver_style else ''.join(_tt)
    head_info = _clean_str(' & '.join(cont[0, :].tolist())) + stuff
    content_info = [_clean_str(' & '.join(i.tolist())) + stuff for i in cont[1:, :]]
    
    tmple_info = tmple % (add_caption, add_label, type_info, head_info, ''.join(content_info))
    print(tmple_info)
    return tmple_info


def write_text(fn, cont):
    assert isinstance(cont, str)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(cont)


def run(read_fn, write_fn, caption, label):
    cont = read_csv(read_fn)
    cc = deal_tex_table(cont, add_caption=caption, add_label=label)
    write_text(write_fn, cc)
    
if __name__ == '__main__':
    run('1.csv', '111', '高通量工作流及数据库', 'ht')
    run('2.csv', '222', '机器学习软件国内外研究进展', 'allmlsoftware')
    run('3.csv', '333', '常用的机器学习研究方法', 'allmlmethods')
    run('4.csv', '444', '材料数据库国内外研究进展', 'allmdb')

