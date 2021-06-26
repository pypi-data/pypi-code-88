'''Data Handler Functions for Colour-GAN.'''
import os
import cv2
import pickle
import random
import tarfile
import urllib.request
import numpy as np
from torch.utils.data import DataLoader, Dataset
from colourgan.logger import log

class Cifar10(Dataset):
    def __init__(self,
                 data_dir,
                 mirror=False,
                 random_seed=None):
        self.imgs_paths = [os.path.join(data_dir,f) for f in os.listdir(data_dir)]
        if random_seed is not None:
            self.imgs_paths.sort()
            random.Random(random_seed).shuffle(self.imgs_paths)
        self.mirror = mirror

    def __len__(self):
        return len(self.imgs_paths)

    def __getitem__(self, id):
        img_path = self.imgs_paths[id]
        img_bgr = cv2.imread(img_path)

        # just a random Transformation for better training
        if self.mirror:
            if random.random() > 0.5:
                img_bgr = img_bgr[:, ::-1, :]

        img_bgr = img_bgr.astype(np.float32) / 255.0
        # transform to LAB
        img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
        img_lab[:, :, 0] = img_lab[:, :, 0] / 50 - 1
        img_lab[:, :, 1] = img_lab[:, :, 1] / 127
        img_lab[:, :, 2] = img_lab[:, :, 2] / 127
        img_lab = img_lab.transpose((2, 0, 1))

        return img_lab

class Cifar10Dataset:
    '''Class for Dwonloading and Processing Cifar 10 Dataset.'''
    def __init__(self,
                 dataset_path='cifar10',
                 batch_size=8,
                 num_workers=4):
        self.batch_size = batch_size
        self.dataset_path = dataset_path

        self.download_cifar10()
        datasets = self.process_and_split_cifar10()
        train_data = Cifar10(datasets['train'])
        test_data = Cifar10(datasets['test'])

        data_loaders = {
            'train': DataLoader(train_data,batch_size=self.batch_size, shuffle=True,
                                num_workers=num_workers),
            'test': DataLoader(test_data, batch_size=self.batch_size, shuffle=False,
                               num_workers=num_workers)
        }
        self.data_loaders = data_loaders

    def get_dataloaders(self):
        return self.data_loaders

    def download_cifar10(self):
        '''Method for Downloading CIFAR10 dataset.'''
        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)
            log(f'{self.dataset_path} Directory Created' , 'data.py/Cifar10Dataset')
            log('Downloading Cifar 10', 'data.py/Cifar10Dataset')
            urllib.request.urlretrieve('https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',
                                       os.path.join(self.dataset_path, 'cifar-10-python.tar.gz'))

            log('Unzipping Dataset', 'data.py/Cifar10Dataset')
            tar = tarfile.open(os.path.join(self.dataset_path, 'cifar-10-python.tar.gz'), 'r:gz')
            tar.extractall(path=self.dataset_path)
            tar.close()
        else:
            log('Downloaded Dataset Found', 'data.py/Cifar10Dataset')
        return



    def process_and_split_cifar10(self):
        '''Extracting, Processing and Splitting Cifar10 Dataset.'''
        data_batches = {}
        data_batches['train'] = [
            os.path.join(self.dataset_path,'cifar-10-batches-py',f) for f in [
                'data_batch_1' , 'data_batch_2' , 'data_batch_3' , 'data_batch_4' , 'data_batch_5'
            ]
        ]
        data_batches['test'] = [os.path.join(self.dataset_path,'cifar-10-batches-py','test_batch')]
        data_dir = {}
        # Directories for Train and Test Split
        data_dir['train'] = os.path.join(self.dataset_path,'cifar-10-images','train')
        data_dir['test'] = os.path.join(self.dataset_path, 'cifar-10-images', 'test')

        for task in ['train' , 'test']:
            if not os.path.exists(data_dir[task]):
                os.makedirs(data_dir[task])
                log(f'{data_dir[task]} Directory Created', 'data.py/Cifar10Dataset')
                log(f'Extracting {task} Dataset', 'data.py/Cifar10Dataset')
                for batch_path in data_batches[task]:
                    with open(batch_path,'rb') as f:
                        batch = pickle.load(f, encoding='bytes')
                    if task == 'train':
                        print(len(batch[b'filenames']))
                    for image_name,image_vector in zip(batch[b'filenames'],batch[b'data']):
                        r, g, b = image_vector[0:1024], image_vector[1024:2048], image_vector[2048:]
                        r, g, b = np.reshape(r, (32, -1)), np.reshape(g, (32, -1)), np.reshape(b, (32, -1))
                        img = np.stack((b, g, r), axis=2)

                        save_path = os.path.join(data_dir[task],image_name.decode('utf-8'))
                        cv2.imwrite(save_path,img)
            else:
                log(f'{task} Split Found', 'data.py/Cifar10Dataset')
        return data_dir

# if __name__ == '__main__':
#     # for testing
#     dataloaders = Cifar10Dataset('cifar10').get_dataloaders()
#     print(len(dataloaders['test']))




