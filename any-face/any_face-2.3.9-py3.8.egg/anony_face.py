import click
import sys
import itertools
import cv2.gapi
import mtcnn
import logging
import os
import cv2
import numpy as np
import re
from matplotlib import pyplot as plt
import threading
from time import time
# from app import flask_app
# from flask import request

@click.command()

@click.argument('file_path')
@click.option('--save_path', '-o')
def main(file_paths, save_path=None):
    face_anonymizer(file_paths)


logger = logging.Logger('app_logger', level=2)
# pool = multiprocessing.Pool(4)

def console_logger( anony_img, anony_fname):

    # f = open(img_dir+'/anony_img.png', 'wb')
    plt.imsave(fname=anony_fname, arr=anony_img)
    # f.write(anony_img)
    # f.close()
    logger.log(msg='Mission Completed! Check your image file in the directory.', level=1)
    return anony_img
    # flask app serialize image file and render on the view.

def bb_blur_pool(bb, img_file):
    nblocks = 3
    # img_gray = cv2.gapi.RGB2Gray(img_file)
    # for bb in face_bbs:
    # print(bb)
    ys = abs(bb['box'][0])
    ye = ys + abs(bb['box'][2])
    xs = abs(bb['box'][1])
    xe = xs + abs(bb['box'][3])
    px_x = int((xe - xs) / nblocks) - 1 if int((xe - xs) / nblocks) % 2 == 0 else int((xe - xs) / nblocks)
    px_y = int((ye - ys) / nblocks) - 1 if int((ye - ys) / nblocks) % 2 == 0 else int((ye - ys) / nblocks)
    img_file[xs:xe, ys:ye] = cv2.GaussianBlur(img_file[xs:xe, ys:ye], (33, 33), sigmaX=nblocks, sigmaY=nblocks)
    for i in range(1, nblocks + 1):
        img_file[xs:xs+(px_x*i), ys:ys+(px_y*i)] = cv2.GaussianBlur(img_file[xs:xs+(px_x*i), ys:ys+(px_y*i)], (px_x,px_y), sigmaX=0,
                                                                    sigmaY=0)

def fc_anonymizer(face_bbs, img_file, anony_fname):

    logging.log(msg='There are {0} faces found!'.format(len(face_bbs)), level=2)
    print('There are {0} faces found!'.format(len(face_bbs)))
    # if len(face_bbs):
    #     fc_fnd = True
    threads = []
    for bb in face_bbs:
        cthread = threading.Thread(target=bb_blur_pool, args=(bb, img_file))
        cthread.start()
        threads.append(cthread)

    for t in range(len(face_bbs)):
        threads[t].join()

    # cv2.rectangle(img_file, (xs,xe), (ys,ye), (0,0,0), -1)
        # np.zeros(shape=(xe-xs, ye-ys,3),  dtype=np.uint8)
        #
        # # img_file[xs:xe, ys:ye] *= np.random.randint(low=img_file[xs,ys], high=img_file[xs+1,ys+1],
        # #                                             size=(bb['box'][3], bb['box'][2], 3), dtype=np.uint8)
    # #     sum_ch = int(np.sum(cv2.mean(img_file[xs:xs + (px_x * i), ys:ys + (px_y * i)])))
    # #     img_file[xs:xs + (px_x * i), ys:ys + (px_y * i)] = np.random.random_integers(low=sum_ch,
    # #                                                                                     high=sum_ch + 1,
    # #                                                                                  size=(xs + (px_x * i) - xs,
    # #                                                                                        ys + (px_y * i) - ys,
    # #                                                                                        3))
    # else:
    #     fc_fnd = False
    console_logger(np.array(img_file, dtype=np.uint8), anony_fname)

# @flask_app.route('/run_mtcnn', methods = ['POST', 'GET'])
def face_anonymizer(img_n):
    # data = request.get_json()
    # print(data)
    # img_f = np.array(data, dtype=np.uint8)
    # img_n = '__'
    # dir = '/home/sisi/PycharmProjects/anony_face/app/'

    t_list = []
    start_t = time()  # beginning timestamp
    mtcnn_obj = mtcnn.MTCNN()
    # p = multiprocessing.()
    if type(img_n) is list:
        for f in img_n:
            t = threading.Thread()
            t.start()

            f = os.path.abspath(f)
            fext = str.split(f, '.')
            fsep = '/'  # default
            if str.lower(sys.platform) == 'linux':
                fsep = '/'
            elif str.lower(sys.platform) == 'windows':
                fsep = '\\'

            last_part = fext[0].split(fsep)[-1] + '_anony'
            path_parts = fext[0].split(fsep)
            path_parts[-1] = last_part

            anony_fname = fsep.join(path_parts) + '.' + fext[1]

            # anony_fname = img_f_loc.replace('.jpg', '_anony.jpg')
            img_f = np.array(plt.imread(f), dtype=np.uint8)

            face_bbs = mtcnn_obj.detect_faces(img_f)
            fc_fnd = len(face_bbs) > 0
            if not fc_fnd:
                logger.log(msg='Apologise. The image may not have humans’ faces.', level=1)
                print('Apologise. The image may not have humans’ faces.')
                return
                # flask app request response imp later
            else:
                print('Anonymized image will be saved to ', anony_fname)
                # f = open('/home/sisi/PycharmProjects/anony_face/resources/dataset/'), color='black'
                start_an = time()
                fc_anonymizer(face_bbs, img_f, anony_fname)
                print('Time taken to anonymize {0} face(s): {1} seconds.'.format(len(face_bbs), time() - start_an))

            t_list.append(t)

        for t in range(len(img_n)):
            t_list[t].join()
    else:
        img_n = os.path.abspath(img_n)
        fext = str.split(img_n, '.')
        fsep = '/' #default
        if str.lower(sys.platform) == 'linux':
            fsep = '/'
        elif str.lower(sys.platform) == 'windows':
            fsep = '\\'

        last_part = fext[0].split(fsep)[-1] + '_anony'
        path_parts = fext[0].split(fsep)
        path_parts[-1] = last_part

        anony_fname = fsep.join(path_parts) + '.' + fext[1]


        # anony_fname = img_f_loc.replace('.jpg', '_anony.jpg')
        img_f = np.array(plt.imread(img_n), dtype=np.uint8)

        face_bbs = mtcnn_obj.detect_faces(img_f)
        fc_fnd = len(face_bbs) > 0
        if not fc_fnd:
            logger.log(msg='Apologise. The image may not have humans’ faces.', level=1)
            print('Apologise. The image may not have humans’ faces.')
            return
            # flask app request response imp later
        else:
            print('Anonymized image will be saved to ', anony_fname)
            # f = open('/home/sisi/PycharmProjects/anony_face/resources/dataset/'), color='black'
            start_an = time()
            fc_anonymizer(face_bbs, img_f, anony_fname)
            print('Time taken to anonymize {0} face(s): {1} seconds.'.format(len(face_bbs), time() - start_an))

        print('Time taken to resolve this program instance: {0} seconds.'.format(time() - start_t))
        logger.log(msg='Time taken to resolve this program instance: {0} seconds.'.format(time() - start_t), level=1)

if __name__ == '__main__':
    face_anonymizer(['/home/sisi/PycharmProjects/anony_face/app/resources/dataset/arrested.jpg',
                     '/home/sisi/PycharmProjects/anony_face/app/resources/dataset/peds_in_rain.jpg'])