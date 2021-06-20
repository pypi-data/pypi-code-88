import torch
import numpy as np
from os.path import join, isfile
from collections import defaultdict
from torchvision.datasets.folder import pil_loader

class FileListDataset(torch.utils.data.Dataset):

    def __init__(self, filelist, root=None, transform=None, target2indice=False):

        assert isfile(filelist)
        self.root = root
        self.transform = transform

        self.items = [i.strip().split(" ") for i in open(filelist).readlines()]
        if root is not None:
            self.items = [[join(root, i[0]), i[1:]] for i in self.items]

        self.num_classes = np.unique(np.array([int(i[1]) for i in self.items])).size if len(self.items[0]) > 1 else -1

        if target2indice:
            assert self.num_classes > 0
            self.target2indice = defaultdict(list)
            for idx, i in enumerate(self.items):
                target = int(i[1])
                self.target2indice[target].append(idx)
        else:
            self.target2indice = None

    def __getitem__(self, index):

        if len(self.items[index]) >= 2:
            fpath, target = self.items[index]
            target = int(target)
        else:
            fpath, = self.items[index]
            target = -1

        assert isfile(fpath), fpath
        im = pil_loader(fpath)

        if self.transform is not None:
            im = self.transform(im)

        return {"image": im, "target": target, "path": fpath}

    def __len__(self):
        return len(self.items)


class KFoldFileListDataset(FileListDataset):

    def __init__(self, filelist, root=None, transform=None, fold=0, num_folds=10, train=True, target2indice=False):
        super(KFoldFileListDataset, self).__init__(filelist, root, transform, target2indice)

        self.all_items = [i.strip().split(" ") for i in open(filelist).readlines()]
        if root is not None:
            self.all_items = [[join(root, i[0]), i[1:]] for i in self.all_items]

        fold_size = len(self.all_items) // num_folds

        test_mask = np.zeros((len(self.all_items),), dtype=bool)
        test_mask[fold * fold_size:(fold + 1) * fold_size] = True
        test_mask = test_mask.tolist()

        self.test_items = [i for idx, i in enumerate(self.all_items) if test_mask[indx] == True]
        self.train_items = [i for idx, i in enumerate(self.all_items) if test_mask[indx] == False]

        if train:
            self.items = self.train_items
        else:
            self.items = self.test_items

        self.num_classes = np.unique(np.array([int(i[1]) for i in self.items])).size if len(self.items[0]) > 1 else -1

        if target2indice:
            assert self.num_classes > 0
            self.target2indice = defaultdict(list)
            for idx, i in enumerate(self.items):
                target = int(i[1])
                self.target2indice[target].append(idx)
        else:
            self.target2indice = None
