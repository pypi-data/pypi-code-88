import cv2 as cv
import numpy as np
import math



def show_rects_and_wait(rects, image, title="", color=(255, 0, 0)):

    for graph in rects:
        cv.rectangle(image, (int(graph.left), int(graph.top)), (int(graph.right), int(graph.bottom)), color,4)
    show_and_wait(title, image)


def show_and_wait(title, img):
    cv.namedWindow(title, cv.WINDOW_KEEPRATIO)
    cv.imshow(title, img)
    if cv.waitKey(0):  # & 0xff == 27:
        cv.destroyAllWindows()


def draw_contours_then_show_and_wait(title, img, ccs_and_colors_list):
    img = img.copy()
    if ccs_and_colors_list:
        for ccs_and_color in ccs_and_colors_list:
            if ccs_and_color[0]:
                cv.drawContours(img, [cc.get_contour() for cc in ccs_and_color[0]], -1, ccs_and_color[1], 2)
    show_and_wait(title, img)


def draw_rects_then_show_and_wait(title, img, ccs_and_colors_list):
    img = img.copy()
    if ccs_and_colors_list:
        color = ccs_and_colors_list[0][1]
        for rect in ccs_and_colors_list[0][0]:
            #            cv.rectangle(img, (384, 0), (510, 128), (255, 255, 255), 3)

            cv.rectangle(img, (int(rect.get_rect()[0]), int(rect.get_rect()[1])),
                         (int(rect.get_rect()[2]), int(rect.get_rect()[3])), (255, 255, 255), 2)
    show_and_wait(title, img)


def read_img(path):
    return cv.imread(path, cv.IMREAD_UNCHANGED)


def calculate_area(bbox):
    return bbox[2] * bbox[3]


def write_img(path, img):
    cv.imwrite(path, img)


def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0
    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


def normalize_angle(theta):
    """Normalize an angle theta to theta_norm so that: 0 <= theta_norm < 2 * np.pi"""
    twopi = 2 * np.pi

    if theta >= twopi:
        m = math.floor(theta / twopi)
        if theta / twopi - m > 0.99999:  # account for rounding errors
            m += 1
        theta_norm = theta - m * twopi
    elif theta < 0:
        m = math.ceil(theta / twopi)
        if theta / twopi - m < -0.99999:  # account for rounding errors
            m -= 1
        theta_norm = abs(theta - m * twopi)
    else:
        theta_norm = theta

    return theta_norm