'''
图像化展示孕橙的算法结果
该文件的主要功能是通过获取线上算法的结果进行一个展示，判断人工结果的差距
'''
import requests
from yuncheng_util_pkg.util import get_for_request
from yuncheng_util_pkg.util_file import *
import matplotlib.pyplot as plt
import cv2
import os
import copy
import json
def _show_value_change(result,savePath,save=False,groupsize=10):
    '''
    将value修改的结果进行展示，
    如果save为False，那就是单张展示，如果save为True，就按照groupsize，一张中展示多少张试纸结果
    :param result:
    :param savePath:
    :param save:
    :param groupsize:
    :return:
    '''
    def show_image(picpath,title1,title2,show=True):
        if picpath is None:
            print("error none:"+picpath)
        imdata = cv2.imread(picpath)
        plt.imshow(imdata[:,:,::-1])
        plt.title(title1+','+title2)
        plt.xlabel(os.path.basename(picpath))
        if show:
            plt.show()
    def save_pic(results,groupsize,savePath):
        grops = len(results)//groupsize
        if grops*groupsize < len(results):
            grops += 1
        for i in range(grops):
            plt.figure(figsize=(10,40))
            for index,k in enumerate(results[i*groupsize:(i+1)*groupsize]):
                plt.subplot(groupsize,1,index+1)
                show_image(k['path'],"al:{}".format(k['lhValue']),'manual:{}'.format(k['lhValueManual']),False)

            filename = os.path.join(savePath,"value-{}.jpg".format(i))
            plt.savefig(filename)
            plt.show()
    if save is False:
        [show_image(i['path'],"al:{}".format(i['lhValue']),'manual:{}'.format(i['lhValueManual'])) for i in result['data']]
        print(len(result['data']))
    else:
        save_pic(result['data'],groupsize,savePath)


def _show_line_change(results,savePath,save=False,groupsize=10):
    def make_line_label(imdata,cl,cr,tl,tr):
        imdata2 = copy.deepcopy(imdata)
        h, w, _ = imdata.shape
        if cl > 10:
            imdata2[h*3//4:,cl:cr,:] = (255,0,0)
        if tl > 10:
            imdata2[h * 3 // 4:, tl:tr, :] = (0, 0, 255)
        return imdata2
    def get_al_ct(info:str):
        info2 = json.loads(info)
        al_ct = {'cl':0,'cr':0,'tl':0,'tr':0}
        if info2['cl'] != '':
            al_ct['cl'] = float(info2['cl'])
        if info2['cr'] != '':
            al_ct['cr'] = float(info2['cr'])
        if info2['tl'] != '':
            al_ct['tl'] = float(info2['tl'])
        if info2['tr'] != '':
            al_ct['tr'] = float(info2['tr'])
        return al_ct
    def get_ma_ct(c,t):
        newc = float(c)
        newt = float(t)
        ma_ct = {'cl':newc-0.005,'cr':newc+0.005,'tl':newt-0.005,'tr':newt+0.005}
        return ma_ct
    def show_image(picpath,alct,manualct,show=True,sum=2,col=1,row=1):
        '''

        :param picpath:
        :param alct: {'cl':0.44,'cr':0.45,'tl':0.35,'tr':0.36}
        :param manualct: {'cl':0.44,'cr':0.45,'tl':0.35,'tr':0.36}
        :return:
        '''
        imdata = cv2.imread(picpath)
        h,w, _ = imdata.shape
        al_cl,al_cr,al_tl,al_tr = int(alct['cl']*w),int(alct['cr']*w),int(alct['tl']*w),int(alct['tr']*w)
        ma_cl, ma_cr, ma_tl, ma_tr = int(manualct['cl'] * w), int(manualct['cr'] * w), \
                                     int(manualct['tl'] * w), int(manualct['tr'] * w)
        imdata2 = make_line_label(imdata,al_cl,al_cr,al_tl,al_tr)
        imdata3 = make_line_label(imdata,ma_cl, ma_cr, ma_tl, ma_tr)
        plt.subplot(sum,col,row)
        plt.title("al")
        plt.imshow(imdata2[:,:,::-1])
        plt.subplot(sum,col,row+1)
        plt.title("manual")
        plt.imshow(imdata3[:, :, ::-1])
        plt.xlabel(os.path.basename(picpath))
        if show:
            plt.show()
    def save_pic(results,groupsize,savePath):
        grops = len(results)//groupsize
        if grops*groupsize < len(results):
            grops += 1
        for i in range(grops):
            plt.figure(figsize=(10,40))
            for index,k in enumerate(results[i*groupsize:(i+1)*groupsize]):
                # plt.subplot(groupsize,1,index+1)
                show_image(k['path'],k['alct'],k['mact'],False,groupsize*2,1,(index+1)*2)
            filename = os.path.join(savePath,"ct-{}.jpg".format(i))
            plt.savefig(filename)
            plt.show()
    # 由于result的数据不符合要求，需要重新设计
    adapters = []
    for i in results['data']:
        adapter = {"path":i['path'],'alct':get_al_ct(i['info']),'mact':get_ma_ct(i['cLoc'],i['tLoc'])}
        adapters.append(adapter)
    if save is False:
        for i in adapters:
            show_image(i['path'],i['alct'],i['mact'])
        return
    save_pic(adapters,groupsize,savePath)



def get_user_change(url,savePath,changeType=0,save=False,groupsize=10):
    '''
    获取统计程序关于value修改的记录的数据，并将这些图片进行保存，并批注
    :param url: 请求的地址
    :param savePath: 图片的保存地址
    :param changeType: 比较的类型， 0 ct，1，value
    :param save: 批注结果是否保存，如果为False，则进行单张图片的实时展示，如果为True，则根据下面的批数据，进行成批的保存
    :param groupsize: 每一张图片中保存张试纸图片。
    :return:
    '''
    result = get_for_request(url)
    if result == 'error':
        return result
    else:
        # 都会进行图片的下载
        for i in result['data']:
            picUrl = i['url']
            path = down_pic(picUrl, savePath)
            i['path'] = path
            if i.get("reverse",0) != 0:
                setPathRotateJust180(i['path'])

        if changeType == 0:
            _show_line_change(result, savePath, save, groupsize)
        elif changeType == 1:
            _show_value_change(result, savePath, save, groupsize)
        return result

