#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import os
#调用示例
#list1 = get_filelist("D:\Tony\接收文件\吴鹏\src\src", [])
#    for i in list1:
#        print(i)
def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist

def readwrite_file(infiledir,outfiledir,code):
    infile = open(infiledir, "r")  # 打开文件
    outfile = open(outfiledir, "w")  # 内容输出
    for line in infile:  # 按行读文件，可避免文件过大，内存消耗
        outfile.write(line.replace('    ', '    '))  # first is old ,second is new
    infile.close()  # 文件关闭
    outfile.close()

def test():
    list1 = get_filelist("D:\\Tony\\接收文件\\吴鹏\\src\\src", [])
    print(len(list1))
    for i in list1:
        print(i)

def t():
    print("aa")

