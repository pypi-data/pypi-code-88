# -*- coding: UTF-8 -*-
"""
导入依赖包
图像格式转换
旋转图片
增加图片亮度
腐蚀处理
膨胀处理
边缘检测
颜色提取
过滤连通域
霍夫变换
均值滤波、高斯滤波、中值滤波
检测轮廓
绘制轮廓
寻找最大轮廓，并显示该轮廓所在的最小矩形区域
用轮廓面积过滤轮廓
用轮廓最小外接矩形长宽比过滤轮廓
SSIM:主要用来评估相同内容图片缩略图质量，图片内容不同不适用,SSIM取值范围[0, 1]，值越大，表示图像失真越小。
"""

from PIL import ImageEnhance, Image
import cv2
import numpy as np
from scipy.signal import convolve2d


def image_type_trans_opencv_image(image):
    """
    opencv和Image打开格式的图片互相转换

    :param image:
    :return:
    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        return image
    else:
        image = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
        return image


def image_type_transform(
        image,
        image_type='',
        transfor_image_type='',
        threshold=100,
        maxval=255,
        method=cv2.THRESH_BINARY):
    """
    图像格式转换：支持RGB转灰度图、BGR图、二值化图或者BGR图转RGB图、灰度图、二值化图

    :param image:需要转换的图片，支持RGB和BGR格式图片
    :param image_type:需要转换的图片格式，支持'RGB'和'BGR'
    :param transfor_image_type:要转换的格式类型，支持'RGB'/'BGR'/'GRAY':转灰度图/'BINARY':转二值化图/'HSV'
    :param threshold: 阈值，转二值化图时需要根据情况重新设置！！！！
    :param maxval: 最大值
    :param method: 二值化转变方法，可选如下参数：
    cv2.THRESH_BINARY 大于阈值的部分被置为255，小于部分被置为0
    cv2.THRESH_BINARY_INV 大于阈值部分被置为0，小于部分被置为255
    cv2.THRESH_TRUNC 大于阈值部分被置为threshold，小于部分保持原样
    cv2.THRESH_TOZERO 小于阈值部分被置为0，大于部分保持不变
    cv2.THRESH_TOZERO_INV 大于阈值部分被置为0，小于部分保持不变
    cv2.THRESH_OTSU，并且把阈值threshold设为0，算法会找到最优阈值，并作为第一个返回值ret返回。
    :return:返回转换后的transfor_image_type设置类型图
    """
    if image_type == 'RGB':
        if transfor_image_type == 'BGR':
            image_bgr = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
            return image_bgr
        elif transfor_image_type == 'HSV':
            image_bgr = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
            image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
            return image_hsv
        elif transfor_image_type == 'GRAY':
            image_bgr = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
            image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
            return image_gray
        elif transfor_image_type == 'BINARY':
            image_bgr = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
            image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
            _, image_binary = cv2.threshold(
                image_gray, threshold, maxval, method)
            return image_binary
        else:
            return image
    elif image_type == 'BGR':
        if transfor_image_type == 'RGB':
            image_RGB = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            return image_RGB
        elif transfor_image_type == 'GRAY':
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return image_gray
        elif transfor_image_type == 'HSV':
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            return image_hsv
        elif transfor_image_type == 'BINARY':
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, image_binary = cv2.threshold(
                image_gray, threshold, maxval, method)
            return image_binary
        else:
            return image
    else:
        return image


def rotate_angle(image, angle):
    """
    旋转图片

    :param image: 需要opencv打开格式的numpy.ndarray格式图片！！！！
    :param angle: 旋转角度
    :return: 旋转之后的numpy.ndarray格式图片
    """
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, -angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


def image_lightup(image, brightness):
    """
    增加图片亮度

    :param image: PIL中Image打开格式图片
    :param brightness: 增加的亮度值
    :return: 增加亮度后的图片
    """
    enh_bri = ImageEnhance.Brightness(image)
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened


def image_erosion(image, kernel=3, iteration=3):
    """
    腐蚀处理

    :param image: 需要腐蚀的图片
    :param kernel: 核步长数，值为奇数,参数越大，效果越明显,默认值3
    :param iteration: 腐蚀次数，参数越大，效果越明显，默认值3
    :return: 腐蚀后的图
    """
    kernel = np.ones((kernel, kernel), np.uint8)
    after_erosion = cv2.erode(image, kernel, iterations=iteration)
    return after_erosion


def image_dilate(image, kernel=3, iteration=3):
    """
    膨胀处理

    :param image:  需要膨胀的图
    :param kernel: 核步长数，值为奇数,参数越大，效果越明显，默认值3
    :param iteration: 膨胀次数，值越大，效果越明显，默认值3
    :return:膨胀后的图
    """
    kernel = np.ones((kernel, kernel), np.uint8)
    after_dilate = cv2.dilate(image, kernel, iterations=iteration)
    return after_dilate


def edge_detection(image, threshold1=50, threshold2=150, aperturesize=3):
    """
    边缘检测
    threshold1、threshold2需要根据情况重新设置

    :param image: 转换后的灰度图
    :param threshold1: 小阈值，用来控制边缘连接，如果一个像素的梯度小于下限阈值，则被抛弃。需要根据情况重新设置！！！
    :param threshold2: 大阈值，用来控制强边缘的初始分割即如果一个像素的梯度大与上限值则被认为是边缘像素。
    如果该点的梯度在两者之间则当这个点与高于上限值的像素点连接时我们才保留，否则删除。需要根据情况重新设置！！！
    :param aperturesize: sobel算子的大小，默认设置为3.
    :return: 检测后的边缘二值化图
    """
    edges = cv2.Canny(image, threshold1, threshold2, apertureSize=aperturesize)
    return edges


def hsv_extract(
    image_hsv, lower_color=[
        100, 200, 60], upper_color=[
            124, 255, 255]):
    """
    颜色提取,lower_color、upper_color分别是hsv格式颜色上下限阈值
    提取lower_color和upper_color之间的值

    :param image_hsv: 转换到hsv颜色空间的图片
    :param lower_color: 下阈值，需要根据情况重新设置！！！！！
    :param upper_color: 上阈值，需要根据情况重新设置！！！！！
    :return: 提取之后的图
    """
    lower_color = np.array(lower_color)
    upper_color = np.array(upper_color)
    after_extract = cv2.inRange(image_hsv, lower_color, upper_color)
    return after_extract


def remove_outliers(mask, area):
    """
    过滤小的连通区域，area是阈值
    面积小于area的连通域会被过滤掉

    :param mask: 二值化图像
    :param area: 阈值
    :return: 过滤后的二值化图
    """
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(
        mask)
    result = mask
    for istat in stats[1:]:  # 0是默认的图片大小，所以从1开始
        if istat[4] < area:  # 如果面积小于area，被认为是干扰，剔除
            result = cv2.rectangle(mask, tuple(istat[0:2]), tuple(
                istat[0:2] + istat[2:4]), 0, thickness=-1)  # 画矩阵，厚度是-1，会填充矩形
    return result


def hough_lines(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=20,
        lines=20,
        minLineLength=20,
        maxLineGap=50):
    """
    霍夫变换

    :param edges: 边缘检测后的二值图
    :param rho: 表示极坐标中ρ，以像素值为单位的分辨率，这里一般使用 1 像素
    :param theta: 表示极坐标中θ,以弧度为单位的分辨率，这里使用 np.pi/180度
    :param threshold: 表示确定一条直线至少需要多少个曲线相交
    :param lines: 表示存储检测到的直线，也就是直线的两个端点坐标
    :param minLineLength: 表示能组成一条直线的最少点，也就是直线的长度，小于该长度就抛弃
    :param maxLineGap：同一方向上两条线段判定为一条线段的最大允许间隔（断裂），超过了设定值，则把两条线段当成一条线段，
    值越大，允许线段上的断裂越大，越有可能检出潜在的直线段
    :return:
    """
    lines = cv2.HoughLinesP(
        edges,
        rho,
        theta,
        threshold,
        lines,
        minLineLength,
        maxLineGap)
    return lines


def filtering_function(image, mode='', ksize=3):
    """
    均值滤波。高斯滤波，中值滤波

    :param image: 需要处理的图片
    :param mode: 使用的过滤器，支持’mean‘/'Guassian'/'median'
    :param ksize: 卷积核大小
    :return: 处理后的图
    """
    if mode == 'mean':  # 均值滤波
        image = cv2.blur(image, (ksize, ksize))
    elif mode == 'Guassian':  # 高斯滤波
        image = cv2.GaussianBlur(image, (ksize, ksize), 0)
    elif mode == 'median':  # 中值滤波
        image = cv2.medianBlur(image, ksize)
    else:
        image = image
    return image


def contour_detection(
        image,
        search_mode=cv2.RETR_TREE,
        approximate_method=cv2.CHAIN_APPROX_SIMPLE):
    """
    检测轮廓

    :param image: 二值化图
    :param search_mode: 表示轮廓的检索模式，有四种：
    cv2.RETR_EXTERNAL表示只检测外轮廓
    cv2.RETR_LIST检测的轮廓不建立等级关系
    cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。
    如果内孔内还有一个连通物体，这个物体的边界也在顶层。
    cv2.RETR_TREE建立一个等级树结构的轮廓。
    :param approximate_method: 表示轮廓的近似办法:
    cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
    cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标
    cv2.CHAIN_APPROX_TC89_L1使用teh-Chinl chain 近似算法
    CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
    :return:contours表示轮廓本身，是个list，list中的每个元素表示一个轮廓，用numpy中的ndarray表示
    hierachy表示轮廓的属性，元素个数和轮廓个数相同，每个轮廓contours[i]对应4个hierarchy元素
    hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。
    """
    contours, hierachy = cv2.findContours(
        image, search_mode, approximate_method)
    return contours, hierachy


def draw_contour(image, contour, colors=(0, 0, 255)):
    """
    在原图上绘制全部轮廓

    :param image: 需要绘制检测轮廓的图片
    :param contour: 检测到的轮廓
    :param cplors: 绘制的颜色，默认红色
    :return: 在原图上绘制过轮廓的图
    """
    image = image.copy()
    image = cv2.drawContours(image, contour, -1, colors, 1)
    return image


def max_area_contours(image, contours, colors=(0, 0, 255)):
    """
    寻找最大轮廓，并用指定颜色显示该轮廓所在的最小矩形区域，默认红色

    :param image: 需要绘制检测轮廓的图片
    :param contours: 检测到的轮廓
    :return: 绘制了最大轮廓的最小外接斜矩形的图片
    """
    area = []
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
        max_idx = np.argmax(np.array(area))
        rect = cv2.minAreaRect(contours[max_idx])
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, colors, 3)
    return image


def filter_contours_area(contours, area_threshold):
    """
    过滤面积较小的轮廓,返回面积满足要求大小的轮廓

    :param contours: 检测到的图片的轮廓
    :param area_threshold: 轮廓面积的阈值
    :return: 满足面积大小的轮廓列表
    """
    contours_list = []
    for i in range(len(contours)):
        contours_area = cv2.contourArea(contours[i])
        if contours_area > area_threshold:
            contours_list.append(contours[i])
    return contours_list


def filter_contours_ratio(contours, ratio_threshold):
    """
    根据轮廓最小外接矩形长宽比筛选轮廓
    返回轮廓最小外接矩形长边/短边比值大于ratio_threshold的轮廓列表

    :param contours: 检测到的轮廓
    :param ratio_threshold: 设置的比值阈值
    :return: 返回满足比值调价的轮廓列表
    """
    contours_list = []
    for i in range(len(contours)):
        rect = cv2.minAreaRect(contours[i])
        (width, height) = rect[1]
        if width / height > ratio_threshold or width / height < 1 / ratio_threshold:
            contours_list.append(contours[i])
    return contours_list


def matlab_style_gauss2D(shape=(3, 3), sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]
    h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


def filter2(x, kernel, mode='same'):
    return convolve2d(x, np.rot90(kernel, 2), mode=mode)


def compute_ssim(im1, im2, k1=0.01, k2=0.03, win_size=11, L=255,sigma=1.5):
    """
    计算两张图的相似度

    :param im1: 灰度图
    :param im2: 灰度图
    :param k1: 远小于1的常数
    :param k2: 远小于1的常数
    :param win_size: 卷积核大小
    :param L: 图像灰度级数，八位为255
    :param sigma: 常数系数
    :return: [0, 1]之间的一个数，值越大，表示图像失真越小
    """
    im1 = np.array(im1)
    im2 = np.array(im2)
    if not im1.shape == im2.shape:
        raise ValueError("Input Imagees must have the same dimensions")
    if len(im1.shape) > 2:
        raise ValueError("Please input the images with 1 channel")

    C1 = (k1 * L) ** 2
    C2 = (k2 * L) ** 2
    window = matlab_style_gauss2D(shape=(win_size, win_size), sigma=sigma)
    window = window / np.sum(np.sum(window))

    if im1.dtype == np.uint8:
        im1 = np.double(im1)
    if im2.dtype == np.uint8:
        im2 = np.double(im2)

    mu1 = filter2(im1, window, 'valid')
    mu2 = filter2(im2, window, 'valid')
    mu1_sq = mu1 * mu1
    mu2_sq = mu2 * mu2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = filter2(im1 * im1, window, 'valid') - mu1_sq
    sigma2_sq = filter2(im2 * im2, window, 'valid') - mu2_sq
    sigmal2 = filter2(im1 * im2, window, 'valid') - mu1_mu2
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigmal2 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    return np.mean(np.mean(ssim_map))




