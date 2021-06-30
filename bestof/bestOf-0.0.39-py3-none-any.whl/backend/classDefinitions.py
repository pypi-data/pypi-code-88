import torch
import torch.nn as nn
import torch.nn.functional as fn


class BlinkAndCropNet(torch.nn.Module):
    def __init__(self):
        super(BlinkAndCropNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3)
        self.conv2 = nn.Conv2d(32, 32, 3)
        self.pool1 = nn.MaxPool2d(2)

        self.drop1 = nn.Dropout2d(0.25)

        self.conv3 = nn.Conv2d(32, 64, 3)
        self.pool2 = nn.MaxPool2d(2)

        self.drop2 = nn.Dropout2d(0.25)

        self.dense1 = nn.Linear(20736, 128)
        self.dense2 = nn.Linear(128, 64)
        self.dense3 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = fn.relu(self.conv2(fn.relu(self.conv1(x))))
        x = self.drop1(self.pool1(x))

        x = fn.relu(self.conv3(x))
        x = self.drop2(self.pool2(x))
        x = torch.flatten(x, 1)

        x = fn.relu(self.dense1(x))
        x = fn.relu(self.dense2(x))
        x = self.dense3(x)
        x = self.sigmoid(x)
        return x


class cropped_model(torch.nn.Module):
    def __init__(self):
        super(cropped_model, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3)
        self.conv2 = nn.Conv2d(32, 32, 3)
        self.pool1 = nn.MaxPool2d(2)

        self.drop1 = nn.Dropout2d(0.25)

        self.conv3 = nn.Conv2d(32, 64, 3)
        self.pool2 = nn.MaxPool2d(2)

        self.drop2 = nn.Dropout2d(0.25)

        self.dense1 = nn.Linear(20736, 128)
        self.dense2 = nn.Linear(128, 64)
        self.dense3 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = fn.relu(self.conv2(fn.relu(self.conv1(x))))
        x = self.drop1(self.pool1(x))

        x = fn.relu(self.conv3(x))
        x = self.drop2(self.pool2(x))
        x = torch.flatten(x, 1)

        x = fn.relu(self.dense1(x))
        x = fn.relu(self.dense2(x))
        x = self.dense3(x)
        x = self.sigmoid(x)
        return x


class custom_dataset(torch.utils.data.Dataset):
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
