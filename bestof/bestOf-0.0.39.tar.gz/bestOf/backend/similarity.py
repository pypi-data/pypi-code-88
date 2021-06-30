import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image
import cv2 as cv

# alt options are alexnet, vgg11, and densenet
model = models.resnet18(pretrained=True)
layer = model._modules.get('avgpool')
model.eval()

scaler = transforms.Resize((224, 224))
# expected normalization for pretrained pytorch networks
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
to_tensor = transforms.ToTensor()


def generate_feature_vector(image):
    image = Image.fromarray(image)
    transformed = Variable(normalize(to_tensor(scaler(image))).unsqueeze(0))
    embedding = torch.zeros(512)  # resnet18 uses 512 features

    def copy_layer_output(module, input, output):
        embedding.copy_(output.data.reshape(output.data.size(1)))

    # on the forward pass in the referenced layer, run the copy layer output function
    handle = layer.register_forward_hook(copy_layer_output)

    model(transformed)

    handle.remove()

    return embedding


def group(vectors, threshold=0.9):
    cos = nn.CosineSimilarity(dim=1, eps=1e-6)
    scores = []

    for i, u in enumerate(vectors):
        if i != len(vectors) - 1:
            scores.append([])

        for j, v in enumerate(vectors):
            if j > i:
                scores[i].append(cos(u.unsqueeze(0), v.unsqueeze(0)))
    print(scores)
    groups = []
    for i, row in enumerate(scores):
        for j, element in enumerate(row):
            j = j + i + 1
            if element >= threshold:
                found = False
                for k, group in enumerate(groups):
                    if i in group or j in group:
                        groups[k].add(i)
                        groups[k].add(j)
                        found = True
                if not found:
                    # print({i, j})
                    groups.append({i, j})
            else:
                found_i = False
                for k, group in enumerate(groups):
                    if i in group:
                        found_i = True
                if not found_i:
                    groups.append({i})
    found_last = False
    for k, group in enumerate(groups):
        if len(vectors) - 1 in group:
            found_last = True
    if not found_last:
        groups.append({len(vectors) - 1})
    # print(scores)
    # print(groups)
    return groups


# u = generate_feature_vector(cv.imread('../resources/examples/IMG_1663.jpg'))
# v = generate_feature_vector(cv.imread('../resources/examples/IMG_1665.jpg'))
# w = generate_feature_vector(cv.imread('../resources/examples/IMG_1667.jpg'))
# x = generate_feature_vector(cv.imread('../resources/examples/IMG_1668.jpg'))
# y = generate_feature_vector(cv.imread('../resources/examples/IMG_1669.jpg'))


# group([u, v, w, x, y])
