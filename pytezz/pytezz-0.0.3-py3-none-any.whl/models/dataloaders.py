import torch
import cv2
import numpy as np
import torchvision
class PlainDataSet:
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        data = self.data[idx]
        targets = self.targets[idx]
        X= torch.tensor(data)
        Y=torch.tensor(targets),
        return {
            "X_in": X,
            "Y_out": Y,
        }

class Image_Classification_DataSet:
    def __init__(self,image_paths,targets,augmentations=None,grayscale=False):
    
        self.image_paths = image_paths
        self.targets = targets
        self.augmentations = augmentations
        self.grayscale = grayscale

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, item):
        targets = self.targets[item]
        if self.grayscale is False:
            image = cv2.imread(self.image_paths[item])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            image = cv2.imread(self.image_paths[item], cv2.IMREAD_GRAYSCALE)
        if self.augmentations is not None:
            augmented = self.augmentations(image=image)
            image = augmented["image"]
        Tensor_image = torch.tensor(np.transpose(image, (2, 0, 1)).astype(np.float32))
        if self.grayscale:
            image_tensor = image_tensor.unsqueeze(0)
        return {"image": image_tensor,"targets": torch.tensor(targets)}


def get_default_device():
    if torch.cuda.is_available():
        return torch.device('cuda')
    else:
        return torch.device('cpu')
    
def to_device(data, device):
    if isinstance(data, (list,tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)

class DeviceDataLoader():
    def __init__(self, dl, device):
        self.dl = dl
        self.device = device
        
    def __iter__(self):
    
        for b in self.dl: 
            yield to_device(b, self.device)

    def __len__(self):
        
        return len(self.dl)



