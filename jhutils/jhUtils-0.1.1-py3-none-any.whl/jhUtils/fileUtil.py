import os
import random
import shutil


def select_image_from_imageDir(imageDir, aimDir, num, isRandom):
    '''
    select image from imageDir to a aimImageDir
    :param imageDir: source image dir
    :param aimDir: aim image dir with selected image
    :param num: selected image number
    :return: success?
    '''
    print("{} select {} to {}".format(os.path.basename(imageDir), num, os.path.basename(aimDir)))
    if os.path.exists(imageDir)==False:
        raise ("imageDir error!")
    if os.path.exists(aimDir):
        while(True):
            inputStr = input(aimDir + ' exist! Is rebuild? Y/N')
            if inputStr=="Y":
                shutil.rmtree(aimDir)
                os.makedirs(aimDir)
                break
            if inputStr=="N":
                break
    else:
        os.makedirs(aimDir)
    imageList = os.listdir(imageDir)
    if isRandom:
        random.shuffle(imageList)
    for imageName in imageList[:min(num, len(imageList))]:
        shutil.copy(os.path.join(imageDir, imageName), os.path.join(aimDir, imageName))
    print("success {} images".format(min(num, len(imageList))))

if __name__ == '__main__':
    select_image_from_imageDir("/Users/a1/Documents/resource/CCPD2020/ccpd_green/test",
                               "/Users/a1/Documents/resource/CCPD2020/ccpd_green/test_local",
                               200,True)
