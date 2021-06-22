import torch
import cv2
import numpy as np
from yolo_ens_dist.utilz.utils import plot_boxes_cv2, plot_boxes_cv2_uncertainty, load_class_names
from yolo_ens_dist.utilz.torch_utils import do_detect
from yolo_ens_dist.model.models import Yolo_Ensemble_Distillation


conf_thresh = 0.4
nms_thresh = 0.4
height = 416
width = 416
num_classes = 10
imgfile = 'data/images/kitti/kitti_example_2.png'
weightsfile = 'weights/clean/bdd/dist/Yolo_bdd_teachers_only_1.pth'
class_names_path = 'data/bdd.names'
box_uncertainties = True


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class_names = load_class_names(class_names_path)
model = Yolo_Ensemble_Distillation(yolov3conv137weight=None, n_classes=num_classes, inference=True, temp=1, vis=True)

pretrained_dict = torch.load(weightsfile, map_location=device)
model.load_state_dict(pretrained_dict)
if device.type == 'cuda':
    model.cuda()

img = cv2.imread(imgfile)
sized = cv2.resize(img, (width, height))
sized = cv2.cvtColor(sized, cv2.COLOR_BGR2RGB)
boxes = do_detect(model, sized, conf_thresh, nms_thresh, uncertainties=True)

if box_uncertainties:
    output_image = plot_boxes_cv2_uncertainty(img, boxes[0][0], class_names=class_names)
else:
    output_image = plot_boxes_cv2(img, boxes[0][0], class_names=class_names)

cv2.imshow("frame", output_image)
cv2.waitKey(0)

