import cv2
import mediapipe as mp
import time


class FaceDetector:
    def __init__(self, minDetectConfid=0.5):
        self.minDetectConfid = minDetectConfid

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(min_detection_confidence=self.minDetectConfid)

    def findFaces(self, img, imgRGB, draw=True):
        self.results = self.faceDetection.process(imgRGB)

        bboxes = []

        if self.results.detections:
            for i, detection in enumerate(self.results.detections):
                raw_bounds = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(raw_bounds.xmin * iw), int(raw_bounds.ymin * ih), int(raw_bounds.width * iw), int(
                    raw_bounds.height * ih),
                bboxes.append([bbox, detection.score])

                if draw:
                    # self.mpDraw.draw_detection(img, detection)
                    cv2.rectangle(img, bbox, (255, 0, 255), 2)
        return bboxes, img


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    p_time = 0

    while True:
        # Get video capture
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect face
        bboxes, img = detector.findFaces(img, imgRGB)

        # FPS
        c_time = time.time()
        fps = 1 / (c_time-p_time)
        p_time = c_time
        cv2.putText(img, f'FPS:{int(fps)}', (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Show image
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
