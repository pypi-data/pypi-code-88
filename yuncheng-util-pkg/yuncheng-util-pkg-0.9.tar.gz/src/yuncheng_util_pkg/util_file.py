import os
import requests
import base64
import cv2
import json
import matplotlib.pyplot as plt
def down_pic(url,savePath):
    '''
    把url相关的图片，下载到指定文件夹下
    :param url:  图片的地址
    :param savePath:  图片保存的文件夹路径
    :return: 文件的保存全路径
    '''
    name = os.path.basename(url)
    picPath = os.path.join(savePath,name)
    if os.path.exists(picPath):
        return picPath
    data = requests.get(url)
    if data.status_code != 200:
        return None
    with open(picPath,'wb') as f:
        f.write(data.content)
    return picPath

def read_pic_to_base64(path):
    '''
    将指定路径的文件读出base64编码的字符串
    :param path: 文件路径
    :return: base64字符串
    '''
    with open(path, 'rb') as f:
        data = f.read()
    imagedata = base64.b64encode(data).decode()
    return imagedata

def setRotateJust180(image,angle = 180):
    '''
    将图片按照指定的度数进行旋转
    1,找到矩形的中心点,
    2,找到需要旋转的角度
    3,然后绕着这个点进行旋转
    4,将得到的图返回
    :param image:
    :return:
    '''
    h, w = image.shape[:2]
    x1 = w // 2
    y1 = h // 2
    # 定义旋转矩阵
    M = cv2.getRotationMatrix2D((x1, y1), angle, 1.0)  # 12
    # 得到旋转后的图像
    rotated = cv2.warpAffine(image, M, (w, h))  # 13
    return rotated
def setPathRotateJust180(path,angle = 180):
    '''

    :param path:
    :return:
    '''
    image = cv2.imread(path)
    image = setRotateJust180(image,angle)
    cv2.imwrite(path,image)


def label_yc_line(imdata, result,title=""):
    '''
    将孕橙算法标记出的ct位置，指示在图片中
    :param imdata: 图片的cv::mat格式的信息
    :param result: 孕橙算法得到的结果
    :return:经过标记的mat
    '''
    h, w, _ = imdata.shape
    if result.get('reverse',0) == 1:
        imdata = setRotateJust180(imdata,180)
    if result.get('cLocation', 0) > 0.1:
        t1 = int(w * result['lhClineLeft'])
        t2 = int(w * result['lhClineRight'])
        imdata[h * 3 // 4:, t1:t2, :] = (255, 0, 0)
    if result.get('tLocation', 0) > 0.1:
        t1 = int(w * result['lhTlineLeft'])
        t2 = int(w * result['lhTlineRight'])
        imdata[h * 3 // 4:, t1:t2, :] = (0, 0, 255)
    show(imdata,title)
    return imdata

def show(imdata,title=""):
    plt.title(title)
    plt.imshow(imdata)
    plt.show()

def read_str(file):
    try:
        with open(file,'r') as f:
            data = f.read()
        return data
    except Exception as e:
        print(e)
        return ""

def read_json(file):
    data = read_str(file)
    try:
        result = json.loads(data)
        return result
    except Exception as e:
        print()
        return None

def write_str(file,data)->bool:
    try:
        with open(file, 'w') as f:
            f.write(data)
        return True
    except Exception as e:
        print(e)
        return False

def write_json(file,data)->bool:
    try:
        data = json.dumps(data)
        with open(file,'w') as f:
            f.write(data)
        return True
    except Exception as e:
        print(e)
        return False