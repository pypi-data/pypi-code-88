import torch
from torchvision import transforms
from torch.autograd import Variable
import cv2 as cv

from bestOf.backend.classDefinitions import BlinkAndCropNet
import os
import site
sitePackageList = site.getsitepackages()
sitePackPath = ""

for i in sitePackageList:
    if "bestOf" in os.listdir(i):
        sitePackPath = os.path.join(i, "bestOf\\backend\\saved_models\\cropped_faces.pth")

sitePackPath = sitePackPath.replace("\\", "/")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BlinkAndCropNet()

model.load_state_dict(torch.load(sitePackPath, map_location=device))
model.eval()

transform = transforms.Compose(
    [transforms.ToTensor()])


def test(image):
    try:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = cv.resize(image, (80, 80), interpolation=cv.INTER_AREA)

        image_tensor = transform(image)
        image_tensor = image_tensor.unsqueeze(0)

        input_var = Variable(image_tensor)
        input_var = input_var.to(device)
        output = model(input_var)
        output = torch.round(output)

        return output.data.cpu().numpy()[0][0]

    except Exception as e:
        print(e)
        return 0


test(cv.imread('../resources/blinkset/blinkers/closed_eye_0059.jpg_face_2.jpg'))
