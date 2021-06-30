from os import read
import cv2 as cv
import mtcnn
from matplotlib import pyplot as plt


def read_img(filename):
    return plt.imread(filename)


def save_img(filename, img):
    cv.imwrite(filename, img)


def save_img_colored(filename, img):
    cv.imwrite(filename, cv.cvtColor(img, cv.COLOR_RGB2BGR))


def show_img(image):
    cv.imshow('Image', image)
    cv.waitKey(0)


def detect_faces(image):
    if image is None:
        raise Exception('No image found.')

    model = mtcnn.mtcnn.MTCNN()
    return model.detect_faces(image)


def get_subject_bounds(face_info):
    return face_info['box']


# def correct_eye_bounds(top_left, bottom_right):
#     new_top_left = min(top_left[0], bottom_right[0]), min(
#         top_left[1], bottom_right[1])
#     new_bottom_right = max(top_left[0], bottom_right[0]), max(
#         top_left[1], bottom_right[1])
#     return new_top_left, new_bottom_right


def is_left_eye_higher(face_info):
    return face_info['keypoints']['left_eye'][1] < face_info['keypoints']['right_eye'][1]


def get_eye_bounds(face_info):
    # Average eye diameter is roughly 23 mm: Bekerman, Inessa & Gottlieb, Paul & Vaiman, Michael. (2014). Variations in Eyeball Diameters of the Healthy Adults. Journal of ophthalmology. 2014. 503645. 10.1155/2014/503645. \
    # Average face width is roughly 147.6 mm: DU LL, Wang LM, Zhuang Z. [Measurement and analysis of human head-face dimensions]. Zhonghua Lao Dong Wei Sheng Zhi Ye Bing Za Zhi. 2008 May;26(5):266-70. Chinese. PMID: 18727867.

    # Thus, the width of each eye should be roughly 16% of the face width
    # This function computes eye bounds by extending 16% of the face width upward and leftward from the left eye and the same downward and rightward from the right eye
    # The extension is used as 16% rather than 8% in either direction to allow cases where the innermost edge of the eye is detected as the eye
    extension = 0.16

    face_bounds = get_subject_bounds(face_info)
    _, _, face_width, _ = face_bounds

    left_higher = is_left_eye_higher(face_info)

    if left_higher:
        top_left = int(face_info['keypoints']['left_eye'][0] - (
            face_width * extension)), int(face_info['keypoints']['left_eye'][1] - (face_width * extension))
        bottom_right = int(face_info['keypoints']['right_eye'][0] + (
            face_width * extension)), int(face_info['keypoints']['right_eye'][1] + (face_width * extension))
    else:
        top_left = int(face_info['keypoints']['left_eye'][0] - (
            face_width * extension)), int(face_info['keypoints']['right_eye'][1] - (face_width * extension))
        bottom_right = int(face_info['keypoints']['right_eye'][0] + (
            face_width * extension)), int(face_info['keypoints']['left_eye'][1] + (face_width * extension))

    return (top_left, bottom_right)


def show_point(image, point):
    image = cv.circle(image, point, radius=10, color=(0, 0, 255), thickness=-1)
    show_img(image)


def show_rect(image, top_left, bottom_right):
    cv.rectangle(
        image, (top_left[0], top_left[1]), (bottom_right[0], bottom_right[1]), (0, 255, 0), 1)
    show_img(image)


def crop_subjects(image):
    faces_info = detect_faces(image)
    subjects = []
    for face in faces_info:
        bounds = get_subject_bounds(face)
        x, y, w, h = bounds
        sub = image[y:y+h, x:x+w]
        sub = cv.cvtColor(sub, cv.COLOR_BGR2RGB)
        subjects.append(sub)
    return subjects


# def show_bounding_boxes(image, bounding_boxes):
#     for box in bounding_boxes:
#         x, y, w, h = box['box']
#         cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
#     show_img(image)

def get_eye_frame_from_img(filename):
    img = read_img(filename)
    faces_info = detect_faces(img)
    for face in faces_info:
        yield get_eye_bounds(face)


def main():
    img = read_img('../resources/examples/fourfaces.jpg')
    subs = crop_subjects(img)
    for sub in subs:
        show_img(sub)


if __name__ == '__main__':
    main()
