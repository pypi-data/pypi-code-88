# import os 
# import cv2
# import glob
# import random
# import darknet
# import numpy as np

# def load_images(images_path):
#     """
#     If image path is given, return it directly
#     For txt file, read it and return each line as image path
#     In other case, it's a folder, return a list with names of each
#     jpg, jpeg and png file
#     """
#     input_path_extension = images_path.split('.')[-1]
#     if input_path_extension in ['jpg', 'jpeg', 'png']:
#         return [images_path]
#     elif input_path_extension == "txt":
#         with open(images_path, "r") as f:
#             return f.read().splitlines()
#     else:
#         return glob.glob(
#             os.path.join(images_path, "*.jpg")) + \
#             glob.glob(os.path.join(images_path, "*.png")) + \
#             glob.glob(os.path.join(images_path, "*.jpeg"))

# def check_batch_shape(images, batch_size):
#     """
#         Image sizes should be the same width and height
#     """
#     shapes = [image.shape for image in images]
#     if len(set(shapes)) > 1:
#         raise ValueError("Images don't have same shape")
#     if len(shapes) > batch_size:
#         raise ValueError("Batch size higher than number of images")
#     return shapes[0]

# def prepare_batch(images, network, channels=3):
#     width = darknet.network_width(network)
#     height = darknet.network_height(network)

#     darknet_images = []
#     for image in images:
#         image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image_resized = cv2.resize(image_rgb, (width, height),
#                                    interpolation=cv2.INTER_LINEAR)
#         custom_image = image_resized.transpose(2, 0, 1)
#         darknet_images.append(custom_image)

#     batch_array = np.concatenate(darknet_images, axis=0)
#     batch_array = np.ascontiguousarray(batch_array.flat, dtype=np.float32)/255.0
#     darknet_images = batch_array.ctypes.data_as(darknet.POINTER(darknet.c_float))
#     return darknet.IMAGE(width, height, channels, darknet_images)

# def batch_detection(network, images, class_names, thresh=0.25, hier_thresh=.5, nms=.45, batch_size=4):
#     image_height, image_width, _ = check_batch_shape(images, batch_size)
#     darknet_images = prepare_batch(images, network)
#     batch_detections = darknet.network_predict_batch(network, darknet_images, batch_size, image_width,
#                                                      image_height, thresh, hier_thresh, None, 0, 0)
#     batch_predictions = []
#     for idx in range(batch_size):
#         num = batch_detections[idx].num
#         detections = batch_detections[idx].dets
#         if nms:
#             darknet.do_nms_obj(detections, num, len(class_names), nms)
#         predictions = darknet.remove_negatives(detections, class_names, num)
#         batch_predictions.append(predictions)
#     darknet.free_batch_detections(batch_detections, batch_size)
#     return batch_predictions

# if __name__ == "__main__":
#     args_batch_size = 3
#     args_base_dir = r'./cfgs/yolov4'
#     args_config_file = os.path.join(args_base_dir, r'road.cfg')
#     args_data_file = os.path.join(args_base_dir, r'road.data')
#     args_weights = os.path.join(args_base_dir, r'backup/road_best.weights')
#     # TODO get 3 images with same size
#     # args_image_names = load_images(r'./v4/yolo_img')[:100]
#     # images = [cv2.imread(image) for image in args_image_names]
#     # images = [i for i in images if i.shape == (480, 853, 3)][:3]

#     network, class_names, class_colors = darknet.load_network(
#         args_config_file,
#         args_data_file,
#         args_weights,
#         batch_size=args_batch_size
#     )

#     random.seed(3)  # deterministic bbox colors
#     detections = batch_detection(network, images, class_names, batch_size=args_batch_size)
#     print(images[0].shape)
#     print(len(detections))
#     print(detections)


#     cv2.imshow('Inference', images[0])
#     if cv2.waitKey() & 0xFF == ord('q'):
#         pass