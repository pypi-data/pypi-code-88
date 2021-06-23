from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2
import os
import fitz
import random
import shutil
from pdfminer.pdfpage import PDFPage
from PyPDF2 import PdfFileWriter, PdfFileReader


def round32(x): return (x + 16) & ~31


def check_each_image(image, debug=False):
    orig = image.copy()
    (H, W) = image.shape[:2]
    # set the new width and height and then determine the ratio in change
    # for both the width and height
    (newH, newW) = (320, 320)  # (round32(H), round32(W))
    rW = W / float(newW)
    rH = H / float(newH)
    # resize the image and grab the new image dimensions
    image = cv2.resize(image, (newW, newH))
    (H, W) = image.shape[:2]
    layerNames = [
        "feature_fusion/Conv_7/Sigmoid",
        "feature_fusion/concat_3"]
    # load the pre-trained EAST text detector
    print("[INFO] loading EAST text detector...")
    net = cv2.dnn.readNet("frozen_east_text_detection.pb")
    # construct a blob from the image and then perform a forward pass of
    # the model to obtain the two output layer sets
    blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
                                 (123.68, 116.78, 103.94), swapRB=True, crop=False)
    start = time.time()
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)
    end = time.time()
    # show timing information on text prediction
    print("[INFO] text detection took {:.6f} seconds".format(end - start))
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []
    # loop over the number of rows
    for y in range(0, numRows):
        # extract the scores (probabilities), followed by the geometrical
        # data used to derive potential bounding box coordinates that
        # surround text
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]
        # loop over the number of columns
        for x in range(0, numCols):
            # if our score does not have sufficient probability, ignore it
            if scoresData[x] < 0.5:
                continue
            # compute the offset factor as our resulting feature maps will
            # be 4x smaller than the input image
            (offsetX, offsetY) = (x * 4.0, y * 4.0)
            # extract the rotation angle for the prediction and then
            # compute the sin and cosine
            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)
            # use the geometry volume to derive the width and height of
            # the bounding box
            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]
            # compute both the starting and ending (x, y)-coordinates for
            # the text prediction bounding box
            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)
            # add the bounding box coordinates and probability score to
            # our respective lists
            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])
    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    boxes = non_max_suppression(np.array(rects), probs=confidences)
    # loop over the bounding boxes
    grayImage = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayImage, 100, 200)
    (thresh, blackAndWhiteImage) = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
    n_of_white_pix = 0
    n_of_black_pix = 0

    for (startX, startY, endX, endY) in boxes:
        # scale the bounding box coordinates based on the respective
        # ratios
        startX = int(startX * rW)
        startY = int(startY * rH)
        endX = int(endX * rW)
        endY = int(endY * rH)
        # draw the bounding box on the image
        cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
        n_of_white_pix = n_of_white_pix + np.sum(blackAndWhiteImage[startX:endX][startY:endY] == 255)
        n_of_black_pix = n_of_black_pix + np.sum(blackAndWhiteImage[startX:endX][startY:endY] == 0)
    pr = n_of_white_pix / n_of_black_pix
    if debug == True:
        # show the output image
        cv2.imshow("Text Detection", orig)
        cv2.imwrite("Text Detection.png", orig)
        cv2.waitKey(0)
    if n_of_black_pix == 0:
        return (-1)

    return (pr)


def pix2np(pix):
    im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    im = np.ascontiguousarray(im[..., [2, 1, 0]])  # rgb to bgr
    return im


def find_image_pixel_ratio(stream, filetype, th, debug=False):
    images = []
    doc = fitz.open(stream, filetype)  # open document
    for page in doc:
        pix = page.get_pixmap()
        im = pix2np(pix)
        images.append(im)

    # print(images[0])
    pixel_ratio = []
    estimated_characters = []
    flag = []
    document = fitz.open(stream, filetype)

    for i in range(len(images)):
        grayImage = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grayImage, 100, 200)
        (thresh, blackAndWhiteImage) = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)
        n_of_white_pix = np.sum(blackAndWhiteImage == 255)
        n_of_black_pix = np.sum(blackAndWhiteImage == 0)
        pr = n_of_white_pix / n_of_black_pix

        if debug == True:
            cv2.imshow('bw image', edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print(pr)
        ec = pr * 18000

        estimated_characters.append(ec)
        pixel_ratio.append(pr)

        print(document[i])
        text = document[i].getText()
        print(len(text), ec)

        if len(text) > ec:
            flag.append(0)
            print(0)
        elif (len(text) < (th * ec)):
            new_pr = check_each_image(images[i])
            print("newpr is :", new_pr, new_pr * 4000)
            if (len(text) < th * new_pr * 4000) or (new_pr == -1):
                flag.append(1)
                print(1)
                return (1)
            else:
                flag.append(0)
                print(0)

        else:
            flag.append(0)
            print(0)

    return (0)


def create_pdf_data(stream, filetype, file_name):
    # try:
    #     os.mkdir(rootdir + "/trash")
    # except:
    #     print("exists")
    #
    # for subdir, dirs, files in os.walk(rootdir):
    #     for file in files:
    #         path = os.path.join(subdir, file)
    #         if file.endswith(".pdf"):
    images = []
    document = fitz.open(stream, filetype)
    for page in document:
        pix = page.get_pixmap()
        im = pix2np(pix)
        images.append(im)
    page = fitz.Document()

    for i in range(len(images)):
        if i % random.randint(1, len(images) - 1) == 0:
            img_rect = document.loadPage(i).MediaBox
            cv2.imwrite('/tmp/' + "/trash/img.png", images[i])
            page.insertPage(pno=i)
            page[i].insertImage(img_rect, filename='/tmp/' + "/trash/img.png")

        else:
            page.insertPDF(document, from_page=i, to_page=i, start_at=i - 1)
    page.save('/tmp/' + "/created_" + file_name)


def get_pdf_searchable_pages(fname):
    searchable_pages = []
    non_searchable_pages = []
    page_num = 0
    with open(fname, 'rb') as infile:

        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                searchable_pages.append(page_num)
            else:
                non_searchable_pages.append(page_num)
    if page_num > 0:
        if len(searchable_pages) == 0:
            return (1)
        elif len(non_searchable_pages) == 0:
            return (0)
        else:
            return (1)
    else:
        print(f"Not a valid document")


def dir_ocr_req_or_not(stream, filetype, file_name, create_data=False):
    # try:
    #     os.mkdir(rootdir + "/output")
    # except:
    #     print("../output Directory already exists")
    # try:
    #     os.mkdir(rootdir + "/output/ocr_not_required")
    # except:
    #     print("../output/ocr_not_required Directory already exists")
    # try:
    #     os.mkdir(rootdir + "/output/ocr_required")
    # except:
    #     print("../output/ocr_required Directory already exists")
    #
    # output_dir_path = rootdir + "/output"
    # output_non_ocr_dir_path = rootdir + "/output/ocr_not_required"
    # output_ocr_dir_path = rootdir + "/output/ocr_required"
    #
    # if create_data == True:
    #     created_data_dir = rootdir + "/created_data"
    #     try:
    #         os.mkdir(created_data_dir)
    #     except:
    #         print("../created_data_dir Directory already exists")
    #     create_pdf_data(rootdir, created_data_dir, file_name)
    #
    # for subdir, dirs, files in os.walk(rootdir):
    #     if "/output" not in subdir:
    #         print(subdir)
    #         for file in files:
    #             if file.endswith(".pdf"):
    #                 path = os.path.join(subdir, file)
    ocr_flag = find_image_pixel_ratio(stream, filetype, 0.5)
    # print(path)
    #
    # OCR_req_flag = get_pdf_searchable_pages(path)
    #
    # if ocr_flag == 1:
    #     shutil.copy(path, rootdir + "/output/ocr_required")
    #     print("file - ocr required")
    #
    # else:
    #     shutil.copy(path, rootdir + "/output/ocr_not_required")
    #     print("file - ocr not required")


def Pdf_ocr_req(stream, filetype, create_data=False):
    ocr_flag = find_image_pixel_ratio(stream, filetype, 0.5)
    # OCR_req_flag = get_pdf_searchable_pages(path)
    print("pixel ratio", ocr_flag)
    if ocr_flag == 1:
        return (True)
    else:
        return (False)
