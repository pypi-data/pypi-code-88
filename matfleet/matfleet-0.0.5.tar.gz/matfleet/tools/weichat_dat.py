# -*- coding: utf-8 -*-
# 微信.dat文件转jpg文件

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/03/03 10:46:00'

import os
from tqdm import trange


def imageDecode(f,fn):
    dat_read = open(f, "rb")
    out=fn
    png_write = open(out, "wb")
    for now in dat_read:
        for nowByte in now:
            newByte = nowByte ^ 0x24
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()
 

def findFile(f):
    fsinfo = os.listdir(f)
    for n in trange(len(fsinfo)):
        fn = fsinfo[n]
        temp_path = os.path.join(f, fn)
        if (not os.path.isdir(temp_path)) and (fn.endswith('.dat')):
            final_fp = os.path.join(f, fn.replace('.dat', '.jpg'))
            # print('%s convert to %s' % (temp_path, final_fp))
            imageDecode(temp_path, final_fp)
        else:
            pass
        
        
def run_many_dir():
    nowpt = os.path.dirname(__file__)
    for i in os.listdir(nowpt):
        pp = os.path.join(nowpt, i)
        if os.path.isdir(pp):
            os.chdir(pp)
            print('-'*50 + i + '-'*50)
            findFile('.')
            os.chdir(nowpt)


if __name__ == '__main__':
    # findFile('.')
    run_many_dir()
