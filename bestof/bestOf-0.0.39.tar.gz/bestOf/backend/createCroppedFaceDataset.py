import torch
from torch.utils.data import Dataset

# Custom dataset model for the data
class custom_dataset(Dataset):
    def __init__(self, all_x, all_y, transform, target_transform=None):
        self.all_x = all_x
        self.all_y = all_y
        self.transform = transform
        self.target_transform = target_transform
        
    def __len__(self):
        return len(self.all_x)
    
    def __getitem__(self, index):
        image = self.all_x[index]
        label = self.all_y[index]
        image = self.transform(image)
        
        if self.target_transform:
            label = self.target_transform(label)

        return image, label