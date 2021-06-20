#   coding: utf-8
#   This file is part of potentialmind.

#   potentialmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/10/22"

import img2pdf
from argparse import ArgumentParser
from matfleet.untilities.get_nowonlyfile import abs_file, get_now_allfiles


def run(filedir, wfn, direction=True):
    if direction:
        a4_papersize = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    else:
        a4_papersize = (img2pdf.mm_to_pt(430), img2pdf.mm_to_pt(210))

    a4_layout = img2pdf.get_layout_fun(a4_papersize)
    now_path = abs_file(filedir)
    all_files = get_now_allfiles(now_path, suffix=['.jpg'])

    with open(wfn, 'wb') as f:
        f.write(img2pdf.convert(all_files, layout_fun=a4_layout))


def pictures2pdf():
    m_description = 'test'
    parser = ArgumentParser(description=m_description)
    parser.add_argument("-r", "--read_filedir", type=str, help="read file dir")
    parser.add_argument("-w", "--write_fn", type=str, help="write filename")
    parser.add_argument("-d", "--direction", type=bool, default=False, help="default: horizen, true: verti")
    
    args = parser.parse_args()
    run(args.read_filedir, args.write_fn, direction=args.direction)


if __name__ == '__main__':
    filedirs = ''
    wfn = ''
    run(filedirs, wfn)
