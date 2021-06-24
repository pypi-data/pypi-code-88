import cv2 as cv
import pdf2txt.doc_analyzer.img as iu
from pdf2txt.utils import cluster_objects2
import numpy as np
import statistics

from pdf2txt.doc_analyzer.img import normalize_angle

KERNEL_SIZE = 3
# Aspect ration of 1.414:1 is preferred which is A4 paper's aspect ratio
# SCALE_RESOLUTION = (900, 1200)
# SCALE_RESOLUTION_INV = (1200, 900)

PIHLF = np.pi / 2
PI4TH = np.pi / 4

class ImageProcessor:
    def __init__(self, page, debug=False, remove_images=False, enhance=True):
        super().__init__()
        self.__img = page.page_image.copy()
        self.__original_img_size = self.__img.shape[:2]
#        self.__resized_img = self.__resize_img(self.__img)
        self.__debug = debug
        self.__enhance=enhance
        self.image_w=self.__img.shape[1]
        self.image_h=self.__img.shape[0]
        if remove_images:
            for im in page.images:
                cv.rectangle(self.__img, (int(im.left/page.pdf_width_scaler),int(im.top/page.pdf_height_scaler)), (int(im.right/page.pdf_width_scaler), int(im.bottom/page.pdf_height_scaler)), (255, 255, 255), -1)

    def preprocess(self):

 #       cv.rectangle(self.__img, (319, 526), ((892,691)),(255, 255, 0), 5)
 #       iu.show_and_wait("test",self.__img)
        self.__img_to_grayscale()


        self.__binarize_img()
#        self.test_hough()
        clusters=self.__detect_lines_to_keep()
        self.___remove_large_lines()
        self.__put_back_removed_lines(clusters)
        self.__smooth_img()
        return self.__img


    def test_hough(self):
        import cv2
        import numpy as np

        minLineLength = 100
        lines = cv2.HoughLinesP(image=self.__img, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]),
                                minLineLength=minLineLength, maxLineGap=80)

        a, b, c = lines.shape
        for i in range(a):
            cv2.line(self.__img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (255, 255, 255), 5,
                     cv2.LINE_AA)
            cv2.imwrite('houghlines5.jpg', self.__img)

        # Display the result.
        cv2.imshow('res', self.__img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __detect_dotted(self):

        imgLines = cv.HoughLinesP(self.__img, 15, np.pi / 180, 10, minLineLength=1000, maxLineGap=30)

        for i in range(len(imgLines)):
            for x1, y1, x2, y2 in imgLines[i]:
                cv.line(self.__img, (x1-2, y1), (x2+2, y2), (255, 255, 255), 3)

        if self.__debug:
            iu.show_and_wait('dotted line fixed Image', self.__img)

    # def __resize_img(self, img):
    #     if img.shape[0] > img.shape[1]:
    #         return cv.resize(img.copy(), SCALE_RESOLUTION, interpolation=cv.INTER_AREA)
    #     else:
    #         return cv.resize(img.copy(), SCALE_RESOLUTION_INV, interpolation=cv.INTER_AREA)

    def __img_to_grayscale(self):
        if len(self.__img.shape) == 3:
            self.__img = cv.cvtColor(self.__img, cv.COLOR_BGR2GRAY)
            if self.__debug:
                iu.show_and_wait('Grayscale Image', self.__img)

    def __enhance_img(self):
        self.__img = cv.adaptiveThreshold(self.__img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)

        if self.__debug:
            iu.show_and_wait('Enhanced Image', self.__img)



    def __smooth_img(self):
        self.__img = cv.blur(self.__img, (KERNEL_SIZE, KERNEL_SIZE))
        if self.__debug:
            iu.show_and_wait('Smoothed (Blurred) Image', self.__img)

    def __correct_skew(self):
        pts = cv.findNonZero(self.__img)
        ret = cv.minAreaRect(pts)

        (cx, cy), (w, h), ang = ret
        if w > h:
            w, h = h, w
            ang += 90

        m = cv.getRotationMatrix2D((cx, cy), ang, 1.0)
        self.__img = cv.warpAffine(
            self.__img, m, (self.__img.shape[1], self.__img.shape[0]))

    def __put_back_removed_lines(self, clusters):
        for cluster in clusters:
            for l in cluster:
                length = l[2] - l[0]
                if length > 20:
                    cv.line(self.__img, (l[0] + 5, l[1]), (l[2] - 5, l[3]), (255, 255, 255), 5, cv.LINE_AA)

        if self.__debug:
            iu.show_and_wait('Lines detection', self.__img)

    def __binarize_img(self):
        if self.__debug:
            iu.show_and_wait('Binarized Image', self.__img)
        self.__img = cv.adaptiveThreshold(self.__img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 3 , 2)

#        self.__img = Binarizer(self.__img).binarize()
        if self.__debug:
            iu.show_and_wait('Binarized Image', self.__img)

    def detect_lines(self, probabilistic=True):
        """
        Detect lines in input image using hough transform.
        Return detected lines as list with tuples:
        (rho, theta, normalized theta with 0 <= theta_norm < np.pi, DIRECTION_VERTICAL or DIRECTION_HORIZONTAL)
        """

        hough_rho_res = 1  # distance resolution in pixels of the Hough grid
        hough_theta_res = np.pi / 180  # angular resolution in radians of the Hough grid
        hough_votes_thresh = 15  # minimum number of votes (intersections in Hough grid cell)
        min_line_length = 100  # minimum number of pixels making up a line
        max_line_gap = 1  # maximum gap in pixels between connectable line segments



        if hough_votes_thresh is None:
            hough_votes_thresh=15

        if probabilistic:
            self.lines_hough = cv.HoughLinesP(self.__img, hough_rho_res, hough_theta_res, hough_votes_thresh,np.array([]),
                                min_line_length, max_line_gap)
        else:
            lines = cv.HoughLines(self.__img, hough_rho_res, hough_theta_res, hough_votes_thresh)
            if lines is None:
                lines = []
            self.lines_hough = self.__generate_hough_lines(lines)

#        else:
#


        if self.__debug and self.lines_hough is not None:
            img=np.zeros(self.__img.shape)
            for line in self.lines_hough:
                for x1, y1, x2, y2 in line:
                    if y1==y2:
                        cv.line(img,(x1,y1),(x2,y2),(255,0,0),2)

            iu.show_and_wait('Lines detection', img)

        return self.lines_hough


    def __detect_lines_to_keep(self):
        lines=self.detect_lines()
        if lines is not None:
            clusters = self.__cluster_lines(lines)


            return clusters

        return []


    def __cluster_lines(self, hough_lines):
        lines=[l[0] for l in hough_lines if l[0][2]-l[0][0]>1]
        line_clusers=cluster_objects2(lines, [0, 2], rel_tol=0.1 , min_cluster_size=3)

        line_clusers_returned=[]
        for cluster in line_clusers:
            cluster.sort(key=lambda x: x[1])
            heights=[c[1] for c in cluster]
            if len(heights)<=2:
                continue
            diffs=[t - s for s, t in zip(heights, heights[1:])]
            median_diff=statistics.median(diffs)
            to_keep=[i for i in range(0,len(diffs)) if diffs[i]<=median_diff+10]
            if len(to_keep)<=2:
                continue

            line_clusers_returned.append([cluster[i] for i in to_keep])

        return line_clusers_returned

    def __generate_hough_lines(self, lines):
        """
        From a list of lines in <lines> detected by cv2.HoughLines, create a list with a tuple per line
        containing:
        (rho, theta, normalized theta with 0 <= theta_norm < np.pi, DIRECTION_VERTICAL or DIRECTION_HORIZONTAL)
        """
        lines_hough = []
        for l in lines:
            rho, theta = l[0]  # they come like this from OpenCV's hough transform
            theta_norm = normalize_angle(theta)

            if abs(PIHLF - theta_norm) > PI4TH:  # vertical
                line_dir = 'vertical'
            else:
                line_dir = 'horizontal'

            lines_hough.append((rho, theta, theta_norm, line_dir))

        return lines_hough


    def ___remove_large_lines(self):

        kernel = np.ones((3, 5), np.uint8)
        self.__img= cv.dilate(self.__img,kernel, iterations=1)

        if self.__debug:
            iu.show_and_wait('dilated', self.__img)
        vertical_kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, int(self.image_h*0.15)))
        horizontal_kernel = cv.getStructuringElement(cv.MORPH_RECT, (int(self.image_w*0.5 ), 3))
        horizontal_mask = cv.morphologyEx(self.__img, cv.MORPH_OPEN, horizontal_kernel, iterations=1)

        vertical_mask = cv.morphologyEx(self.__img, cv.MORPH_OPEN, vertical_kernel, iterations=1)


        total_mask = cv.bitwise_or(horizontal_mask, vertical_mask)
        if self.__debug:
            iu.show_and_wait('mask', total_mask)

        self.__img[np.where(total_mask != 0)] = 0

        h, w = self.__img.shape[0:2]
        # erase the borders by adding a frame.
        #this removes some of the noise that remains on the borders
        cv.rectangle(self.__img, (0, 0), (w , h), (0, 0, 0), int(w*0.1))

        #add a while rectangle in the bottom.
        #it is sometimes very difficults to isolate footers.
        #we use this technique to be able to do a vertical split easily


        cv.rectangle(self.__img, (0, h - int(h*0.1)), (w, h), (0, 0, 0), -1)

#
        if self.__debug:
            iu.show_and_wait('Remove white lines', self.__img)
