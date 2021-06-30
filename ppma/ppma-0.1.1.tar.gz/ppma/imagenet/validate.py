import paddle
import paddle.vision.transforms as T
from paddle.io import Dataset, DataLoader

import numpy as np
import time
from PIL import Image

__all__ = []

class ILSVRC2012_val(Dataset):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.transforms = T.Compose([T.Resize(256),
                                     T.CenterCrop(224),
                                     T.ToTensor(),
                                     T.Normalize(mean=[0.485, 0.456, 0.406],
                                                 std =[0.229, 0.224, 0.225])
                                     ])

    def __getitem__(self, idx):
        # 处理图像
        img_path = self.data[idx][0]                # 得到某样本的路径
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = self.transforms(img)                  # 数据预处理

        # 处理标签
        label = self.data[idx][1]                   # 得到某样本的标签
        label = np.array([label], dtype="int64")    # 把标签数据类型转成int64
        return img, label

    def __len__(self):
        # 返回每个Epoch中图片数量
        return len(self.data)

        

def val(model, path):

	data_list = []
	with open(path + '/' + "val.txt") as f:
	    for line in f:
	        a,b = line.strip("\n").split(" ")
	        data_list.append([path + '/' + a, int(b)])

	val_loader = DataLoader(ILSVRC2012_val(data_list),
	                        batch_size=128
	                        )


	m = paddle.metric.Accuracy(topk=(1,5))
	model.eval()

	with paddle.no_grad():

	    end = time.time()
	    for i, (images, target) in enumerate(val_loader):
	        
	        output = model(images)

	        m.update(m.compute(output, target))
	        acc1, acc5 = m.accumulate()

	        batch_time = time.time() - end
	        
	        if i % 40 == 0:
	            print("[{: >3}/{:}]  top1_acc {:.3f}  top5_acc {:.3f}  time {:.3f}s".format(i, len(val_loader), acc1, acc5, batch_time))

	        end = time.time()

	print("top1_acc {:.3f}  top5_acc {:.3f}".format(m.accumulate()[0], m.accumulate()[1]))













