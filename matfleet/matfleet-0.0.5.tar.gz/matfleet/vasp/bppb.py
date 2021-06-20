#!/usr/bin/python -u 
#encoding=utf-8
import os
import re
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import pickle
from optparse import OptionParser
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
__author__ = "Guanjie Wang"
__email__ = "wangguanjie@buaa.edu.cn"
__date__ = "Mar. 21, 2018"

def _get_procar():
    filename = 'PROCAR'
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("Can't find PROCAR")
        exit()
    lines = f.readlines()
    f.close()
    return lines

def _remove_path(path):
    if os.path.exists(path):
        os.remove(path)
        print('{0} ******* This file path exists, removed'.format(path))

def _write(filename,content):
    f = open(filename,'a')
    for i in content:
        f.write(i+'\n')
    f.close()

def _get_input_number(number_string):
    '''
    :return: 返回输入指定开始和结尾原子的列表
    '''
    return  [x for x in range(int(number_string.split(',')[0]),int(number_string.split(',')[1])+1 )]

#TODO：
#将倒空间K点转换成实空间K点路径，这样就不用读取OUTCAR了
def _get_kpoint_path(kpoint):
    '''
    对OUTCAR中kpoint的路径进行处理，PROCARE中记录的是倒空间K点的路径，因此必须从OUTCAR中读取
    返回k路径的列表，和每个路径K点个数
    '''
    efermi_command = 'grep E-fermi OUTCAR'
    try:
        f = open('OUTCAR','r')
        efermi = float(os.popen(efermi_command).read().split()[2])
    except FileNotFoundError:
        print("Don't find OUTCAR")
        exit()
    content = f.readlines()
    f.close()
    for dd in content:
        a = re.findall(r' k-points in units of 2pi/SCALE and weight: SYSTEM(.*)', dd)
        if len(a) > 0:
            number_kpoint = len(a[0].replace(' ','').split('-'))-1
            gogal_line = content.index(dd) +1
            break

    position = [[round(float(x), 8) for x in content[m].split()[0:3]] for m in range(gogal_line,gogal_line+kpoint)]
    distance =[(math.pi * 2 / Scale * math.sqrt(
            (position[i][0] - position[i - 1][0]) ** 2 + (position[i][1] - position[i - 1][1]) ** 2 + (
            position[i][2] - position[i - 1][2]) ** 2)) for i in range(1, len(position))]

    final_distance = [0]
    a = 0
    for i in distance:
        a += i
        final_distance.append(round(a,5))
    return final_distance,int(len(final_distance)/number_kpoint),efermi

def _get_all_number(kpoint,bands,ions):
    '''返回每个k点对应的所有能到的行号'''
    kpoint_number = __get_kpoint_line_number(kpoint,bands,ions)
    kpoint = kpoint_number.keys()
    all_line = {}
    for b in kpoint:
        nn = __get_bands_line_number(kpoint_number[b],bands,ions)
        all_line[b] = nn
    return all_line

def _get_band(all_line_number,efermi,lines):
    E_fermi = float(input('Please input E-fermi, now E-fermi of OUTCAR was {0} ：'.format(efermi)))
    energy_and_kpoint = {}
    for i in all_line_number.keys():
        band_e = {}
        band_line_number = list(all_line_number[i].values())
        for m in range(len(band_line_number)):
            band_e[m+1] = __get_band_energy(lines[band_line_number[m]-1],E_fermi)
        energy_and_kpoint[i] = band_e
    return energy_and_kpoint

def _get_contributes(all_line_number,ions,set_number,lines):
    '''
    very slow , be patient
    '''
    kpoint_band_contribute = {}
    for i,j in all_line_number.items():
        print('now kpoints was: {0} '.format(i))
        band_contribute = {}
        total_band_contribute = {}
        for m,h in j.items():
            space = h + 3
            atom_contribute = __get_matrix(space,ions,lines)
            element_contribte = [0] * 9
            for n in set_number:
                for x in range(len(atom_contribute[n])):
                    element_contribte[x] += atom_contribute[n][x]
            band_contribute[m] = element_contribte
            total_element_contribte = 0
            for xx in element_contribte:
                total_element_contribte += xx
            total_element_contribte = round(total_element_contribte,8)
            total_band_contribute[m] = total_element_contribte
        kpoint_band_contribute[i] = total_band_contribute
    return kpoint_band_contribute

def __get_matrix(first_atom_line_number,ions,lines,choose='total'):
    '''
    输入第一个原子位置，返回所有原子及对应的内容
    修改choose部分可以修改最终写出的结果，total写指定元素总的贡献值，spd分别代表不同轨道的贡献值
    '''
    alter = {'total':'1:10','s':'1:2','p':'2:5','d':'5:-2'}
    alter_index = [int(x) for x in alter[choose].split(':')]
    tmp = {}
    for x in range(first_atom_line_number-1,first_atom_line_number+ions-1):   # if delete -1, it will be string type which include 'tot' value
        i = [round(float(mm),8) for mm in lines[x].split()]
        atom = i[alter_index[0]:alter_index[1]]
        tmp[int(i[0])] = atom
    return tmp

def __get_band_energy(band_content,E_fermi):
    return round(float(band_content.split()[4])-E_fermi,8)

def __get_kpoint_line_number(kpoint,bands,ions):
    '''
    根据PROCAR格式自己制定规则，返回所有kpoint所在行的行号
    '''
    space = (ions + 4) * bands + bands + 3
    kpoint_number = {}
    for i in range(kpoint):
        line = 4 + space * i
        kpoint_number[i+1] = line
    return kpoint_number

def __get_bands_line_number(kpoint_number,bands,ions):
    '''
    根据PROCAR格式自己制定规则，返回所有band所在行的行号
    '''
    space = ions+5
    bands_number = {}
    for i in range(bands):
        line = kpoint_number +2 + space * i
        bands_number[i+1] = line
    return bands_number

#run

def get_content(numberstring,lines):
    a1 = time.time()
    c = lines[1].split()
    kpoint = int(c[3])
    bands = int(c[7])
    ions = int(c[11])
    print('Total Kpoints was {0},  Total Bands was {1},  Total atom was {2}'.format(kpoint, bands, ions))

    set_number = _get_input_number(number_string)
    print('You choose atom was {0}'.format(set_number))


    kpoint_path,number_kpoint,efermi = _get_kpoint_path(kpoint)

    all_line_number = _get_all_number(kpoint, bands, ions)
    band_energy = _get_band(all_line_number,efermi,lines)
    contributes = _get_contributes(all_line_number,ions,set_number,lines)
    a3 = time.time()
    print('Using time was:',a3-a1,'s')
    return kpoint_path,band_energy,contributes,number_kpoint

def reorder(gogalfilename,kpoint_path,band_energy,contributes):
    '''将获得的所有结果按照数据可以处理的形式排序，返回用来画图的列表，调用该函数会默认写输出文件，文件名为gogalfilename'''
    total_data = []
    for i,j in band_energy[1].items(): #i represent the number of bands
        content = []
        plt_content = []
        for m,n in contributes.items(): # m represent the number of k-points
            subplt_content = []
            each_line='{0:.8f}    {1:.8f}    {2:.8f}'.format(kpoint_path[m-1],band_energy[m][i],contributes[m][i])
            subplt_content.append(round(kpoint_path[m-1],8))
            subplt_content.append(round(band_energy[m][i],8))
            subplt_content.append(round(contributes[m][i],8))
            plt_content.append(subplt_content)
            content.append(each_line)
        content.append('')
        total_data.append(plt_content)
        _write(gogalfilename,content)
    return total_data

def plt_band(content,kpoint_path,luminance=200,ymin=-0.5,ymax=1):
    linewidth = 2
    x1 = np.array(content)
    print('total bands was {0}'.format(len(x1)))
    a1 = x1[0,:, 0]
    plt.xlim(0, a1[-1])
    plt.ylim(ymin,ymax)
    plt.plot(a1, [0] * len(a1), '--', color='black')
    if len(a1) % kpoint_path == 0:
        total_k = int(len(a1) / kpoint_path)
    else:
        print('do not devise')
        exit()
    print('total kpoint was {0}'.format(total_k))
    kkk = []
    for i in range(1, total_k + 1):
        kkk.append(a1[kpoint_path * i - 1])
    for m in kkk:
        plt.plot([m] * 200, [y for y in range(-100, 100)], '--',color='black')

    for mmin in range(len(x1)):
        if x1[mmin][:,1].min() >= ymin:
            m1 = mmin
            # print('min was {0}'.format(m1))
            break
    for mmax in range(m1, len(x1)):
        if x1[mmax][:,1].max() >= ymax:
            m2 = mmax
            # print('max was {0}'.format(m2))
            break
    # for m in range(len(x1)):
    for m in range(m1, m2):
        b1 = x1[m][:, 1]
        b2 = x1[m][:, 2]
        plt.plot(a1, b1, color='black',linewidth=linewidth)
        plt.scatter(a1,b1,color='red',s=b2*luminance)
    # plt.plot([0] * 80, [x for x in range(80)], '--', color='lightcoral', linewidth=linewidth)
    fffsize = 15
    plt.ylabel('BANDS',fontsize = fffsize+2)
    plt.yticks(fontsize=fffsize)
    plt.xticks([])

    #write kpoint path text
    kpoint_name = ['F', 'Q', 'Z', 'G']
    kpt_y = ymin - 0.09
    for kname  in range(len(kkk)):
        # plt.text(kkk[kname]-0.005,kpt_y,kpoint_name[kname])
    # plt.text(0-0.005,kpt_y,'G')
        try:
            plt.text(kkk[kname] - 0.009, kpt_y, kpoint_name[kname],fontsize=fffsize)
        except KeyError:
            print("adjust kpoint_name, it's too little")
    plt.text(0 - 0.009, kpt_y, 'G',fontsize=fffsize)

    # plt.legend(loc='upper right', bbox_to_anchor=(0.95, 0.92), fancybox=True, ncol=3,fontsize=15)  # ncol 控制有几列，bbox控制位置

    plt.show()

def main():
    if continues == 1:
        lines = _get_procar()
        _remove_path(os.path.join(os.getcwd(),gogalfilename))
        _remove_path(os.path.join(os.getcwd(),pick_name))

        kpoint_path, band_energy, contributes, number_kpoint = get_content(number_string,lines)
        plt_content = reorder(gogalfilename,kpoint_path,band_energy,contributes)

        #save data
        fw = open(pick_name,'wb')
        pickle.dump(number_kpoint,fw)
        pickle.dump(plt_content, fw)
        plt_band(plt_content,number_kpoint,luminance)
        fw.close()
    else:

        fr = open(pick_name,'rb')
        number_kpoint = pickle.load(fr)
        plt_content = pickle.load(fr)
        fr.close()

        plt_band(plt_content,number_kpoint,luminance)


if __name__ == "__main__":
    usage = '''%prog -n arg1 [option] [arg]
        eg:%prog -c 1 -n 85,92 200
        -c 1 : from initial to deal data(if want to continue don't use -c)
        -n 85,92: from atom 85 to atom 92
        200: continbute luminance was 200
        '''
    parse = OptionParser(usage)
    parse.add_option('-c', '--continue', action='store_true', dest='con',
                     help='''if you have tmp file, can use this parameter''')
    parse.add_option('-n', '--number', action='store', help='''n m from n atom to m atom''')
    parse.add_option('-s', '--scale', action='store',default=1.0,
                     help='''scale factor (you can read from POSCAR, default was 1.0) ''')

    (option, args) = parse.parse_args('-h'.split())
    if option.con:
        continues = 1
    else:
        continues = 2
        print('read data from tmp.*')
    try:
        luminance = int(args[0])
    except IndexError:
        luminance = 200

    if option.scale:
        Scale = float(option.scale)

    if continues == 1 and option.number:
        number_string = option.number
        gogalfilename = 'bands-' + number_string.replace(' ','-')
        pick_name = 'tmp' + number_string
        print('you choose atom was {0} to {1}'.format([x for x in number_string.split(',')][0],[x for x in number_string.split(',')][1]))
    elif continues == 2 and not option.number:
        number_string = [x.replace('tmp','') for x in  os.listdir(os.getcwd()) if len(re.findall('tmp(.*)',x)) > 0][0]
        pick_name = 'tmp' + number_string
        print('you choose atom was {0} to {1}'.format([x for x in number_string.split(',')][0],[x for x in number_string.split(',')][1]))
    elif continues == 2 and option.number:
        number_string = option.number
        pick_name = 'tmp' + number_string
        print('you choose atom was {0} to {1}'.format([x for x in number_string.split(',')][0],[x for x in number_string.split(',')][1]))
    else:
        print('Please use -n assign which atom number or use -h to see help')
        exit()

    main()
