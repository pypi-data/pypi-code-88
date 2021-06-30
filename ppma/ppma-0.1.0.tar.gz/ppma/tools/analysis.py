import paddle
from paddle.io import DataLoader,Dataset
import time
from rich import print

__all__ = []

def param(model):
    total_params = sum(p.numel() for p in model.parameters())
    total_params = int(total_params)
    print('total params: {:,}'.format(total_params))




class test_set(Dataset):
    def __init__(self, data):
        super().__init__()
        self.data = data


    def __getitem__(self, idx):
        img = self.data[idx]               
        return img

    def __len__(self):
        return len(self.data)



def throughput(model, image_size=224):
    H = W = image_size
    data = paddle.randn([1000, 1, 3, H, W])
    test_loader = DataLoader(test_set(data),
	                        batch_size=1
	                        )
    
    num_data = len(data)
    num_warmup = 5
    total_time = 0

    model.eval()
    with paddle.no_grad():

        # warmup
        print("Warmup ...")
        input_tensor = paddle.randn([10, 1, 3, H, W])
        for i in input_tensor:
            model(i)
        print("Done!")

        for batch_id, batch_data in enumerate(test_loader):
            start = time.time()
            predicts = model(batch_data[0])
            end = time.time()
            total_time += end - start
            if (batch_id) % 100 == 0:
                infer_speed =  (batch_id + 1)/total_time
                print("[{: >3}/{:}]  infer_speed {:.1f} img/s ".format(batch_id, num_data, infer_speed))

    print("{{Infer speed {:.1f} img/s}}".format(num_data/total_time))