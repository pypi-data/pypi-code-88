import os
base_dir = os.path.dirname(os.path.realpath(__file__))

def get_test_data(name='bus'):
    if name == 'bus':
        img_fp = os.path.join(base_dir, 'samples', 'bus.jpg')
    elif name == 'zidane':
        img_fp = os.path.join(base_dir, 'samples', 'zidane.jpg')
    return img_fp

def get_test_params():
    """
    name: {'yolov4', 'yolov4_tiny}
    """
    cfg_fp = os.path.join(base_dir, 'cfgs', 'yolov4_tiny', 'yolov4-tiny.cfg')
    weights_fp = os.path.join(base_dir, 'cfgs', 'yolov4_tiny', 'yolov4-tiny.weights')
    names_fp = os.path.join(base_dir, 'cfgs', 'yolov4_tiny', 'coco.names')
    return cfg_fp, names_fp, weights_fp

