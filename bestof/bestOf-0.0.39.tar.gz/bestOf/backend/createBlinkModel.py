import math
import cv2 as cv
import numpy as np
import os
import torch
import torchvision
from torchvision import transforms
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as fn
from torch.utils.data import DataLoader, Dataset, random_split
from bestOf.backend.createCroppedFaceDataset import custom_dataset


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


def load_dataset(img_height, img_width):
    print("Loading images into dataset...")

    # Loads all images from lfw and lfw_cut with opencv and stores it in all_x,
    # stores all labels in all_y
    nonblinkpath = "../resources/blinkset/nonblinkers"
    blinkpath = "../resources/blinkset/blinkers"

    all_x = []
    all_y = []
    img_count = 0
    # Load all images from lfw with label in all_x and all_y
    # for folder in os.listdir(nonblinkpath):
    #folder_path = os.path.join(nonblinkpath, folder)

    for img in os.listdir(nonblinkpath):
        image = cv.imread(os.path.join(nonblinkpath, img))

        if image.shape[0] < img_height or image.shape[1] < img_width:
            continue

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = cv.resize(image, (img_height, img_width),
                          interpolation=cv.INTER_AREA)
        img_count += 1
        all_x.append(image)
        all_y.append(0.0)

    # for folder in os.listdir(blinkpath):
        #folder_path = os.path.join(blinkpath, folder)

    for img in os.listdir(blinkpath):
        image = cv.imread(os.path.join(blinkpath, img))

        if image.shape[0] < img_height or image.shape[1] < img_width:
            continue

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = cv.resize(image, (img_height, img_width),
                          interpolation=cv.INTER_AREA)
        img_count += 1
        all_x.append(image)
        all_y.append(1.0)

    # Convert to np array to change to tensor
    all_x = np.asarray(all_x)
    all_y = np.asarray(all_y)
    print("Finished loading all images! Loaded " + str(img_count) + " images!\n")
    return all_x, all_y


def train(all_x, all_y, split, device):
    # Define basic variables and parameters
    learning_rate = 0.00005
    batch_size = 64
    epoch = 11
    model_path = "./saved_models/blinkingFaces.pth"

    # Create all of the dataloaders and models, then train it with train_loader
    transform = transforms.Compose(
        [transforms.ToTensor()])

    full_dataset = custom_dataset(all_x, all_y, transform)
    train_len = math.floor(len(all_x) * split)
    val_len = len(all_x) - train_len
    train_dataset, val_dataset = random_split(
        full_dataset, [train_len, val_len])

    print(str(train_dataset.__len__))

    train_loader = DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    model = BlinkAndCropNet().to(device)
    criteria = nn.BCELoss()
    opt = optim.Adam(model.parameters(), learning_rate)

    n_total_steps = len(train_loader)

    if torch.cuda.is_available():
        print("Starting the training using the GPU")
    else:
        print("Starting the training using the CPU, this'll take a while")

    for epoch_num in range(epoch):
        for i, (images, labels) in enumerate(train_loader):
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criteria(outputs[:, 0], labels.float())

            opt.zero_grad()
            loss.backward()
            opt.step()

            if (i + 1) % 20 == 0:
                print(
                    f"Epoch: [{epoch_num+1}/{epoch}], Step: [{i+1}/{n_total_steps}], Loss: {loss.item():.4f}")
    print("Successfully finished training!\n")
    torch.save(model.state_dict(), model_path)

    return model, val_loader


def validation(model, val_loader, device):
    # Validate the model
    print("Validating model...")

    model.eval()
    with torch.no_grad():
        correct = 0
        samples = 0
        acc = 0.0

        with torch.no_grad():
            for images, labels in val_loader:
                images = images.to(device=device)
                labels = labels.to(device=device)

                scores = model(images)
                scores = torch.round(scores)
                scores = scores[:, 0]

                correct += (scores == labels).sum()
                samples += scores.size(0)

            acc = (correct / samples) * 100
            print("Accuracy: " + str(acc) + "\n")


if __name__ == "__main__":
    img_height = 80
    img_width = 80
    train_val_split = 0.75
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    all_x, all_y = load_dataset(img_height, img_width)
    model, val_loader = train(all_x, all_y, train_val_split, device)
    validation(model, val_loader, device)
    print("Done with creating the face cropped detection model!")
