import torch
from torchvision import transforms
import pathlib
import skimage.io



class DictDataset(torch.utils.data.Dataset):
    
    def __init__(self, root, metadata, transform=None):
        self.root = pathlib.Path(root).expanduser()
        self.metadata = metadata
        self.transform = transform

    def load_image(self, file_name):
        return skimage.io.imread(self.root / file_name)

    def load_data(self, idx):
        raise NotImplementedError()
    
    def load_target_dict(self, idx):
        raise NotImplementedError()

    def __getitem__(self, idx):
        data = self.load_data(idx)
        
        if self.transform:
            data = self.transform(data)
        else:
            data = transforms.ToTensor()(data)
        
        return {"data": data, **self.load_target_dict(idx)}        
        
    def __len__(self):
        return len(self.metadata)


class EnzodeCreationsDataset(DictDataset):

    def load_data(self, idx):
        file_name = f"{self.metadata.iloc[idx]['creation_id']}.png"
        return self.load_image(file_name)
    
    def load_target_dict(self, idx):
        record = self.metadata.iloc[idx].to_dict()
        
        return {col: torch.tensor(record[col]).float() 
                for col in ['clicks', 'validated', 'left', 'right', 'CR', 'creation_id', 'CR_relative', 'CR_by_group']
               }