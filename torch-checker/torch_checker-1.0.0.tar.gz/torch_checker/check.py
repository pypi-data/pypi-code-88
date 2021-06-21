import torch
from torch import nn
import numpy as np
from torch.optim import Optimizer
from functools import reduce

class TensorChecker:
    """
    检查每层网络的输入和输出的梯度是否正常
    """

    def __init__(self,prefix="",check=True):
        self.check=check
        self.prefix=prefix

    def __call__(self, module:nn.Module, tensor_in, tensor_out):
        if(not self.check):
            return

        print("################")
        print(module.name)
        print(f"{self.prefix}_in:")
        for e in tensor_in:
            print(e.shape)
        print("----------------")
        print(f"{self.prefix}_out:")
        for e in tensor_in:
            print(e.shape)
        # print("----------------")
        # print(f"{module.__class__}_param:")
        # for a,e in module.named_parameters():
        #     print(a,e.shape)
        print("################")

    def set_state(self,check):
        self.check=check
        return self

    def get_state(self):
        return self.check


class ModuleWrapper(nn.Module):
    def __init__(self, model: nn.Module, backward_hook: TensorChecker = None,
                 forward_hook: TensorChecker = None):
        """

        :param model:要做检查的module
        :param backward_hook:state为真的情况下，在反向传播时触发
        :param forward_hook:state为真的情况下，在正向传播时触发
        """
        super(ModuleWrapper,self).__init__()
        self.model=model
        self.check=True
        self.hook1 = backward_hook.set_state(self.check) if backward_hook is not None else None
        self.hook2 = forward_hook.set_state(self.check) if forward_hook is not None else None
        for a, e in model.named_modules():
            e.name = a

        if(backward_hook is not None):
            for a, e in model.named_children():
                e.register_full_backward_hook(backward_hook)
        if(forward_hook is not None):
            for a, e in model.named_children():
                e.register_forward_hook(forward_hook)

    def forward(self,*args,**kwargs):
        return self.model(*args,**kwargs)

    def param_check(self):
        print("model check:")
        for a, e in self.model.named_children():
            print("check", a)
            res=dict()
            # weights=[]
            # res=[]
            for param in e.parameters():
                n=param.ndim
                if(n not in res):
                    res[n]=dict(weights=[],stats=[])
                res[n]["weights"].append(reduce(lambda x,y:x*y,param.shape))
                res[n]["stats"].append(self.stat(param.detach().numpy()))

            for n,ans in res.items():
                a = np.stack(ans["stats"])
                w = ans["weights"]
                print(n,"dim: ",np.average(a, axis=0, weights=w))

        # res=[]
        # for a,e in self.model.named_children():
        #     print("check",a)
        #     sub_res=[]
        #     for param in e.parameters():
        #         #TODO
        #         sub_res.append(1)
        #     res.append(sub_res)
        # return res

    def stat(self,param:np.ndarray):
        #return dict(mean=np.mean(param),median=np.median(param),max=np.max(param),min=np.min(param),std=np.std(param))
        return np.mean(param), np.median(param), np.max(param), np.min(param),np.std(param)

# class Net(nn.Module):
#     def __init__(self,):
#         super(Net,self).__init__()
#         self.moda=nn.Linear(100,200)
#         self.modb = nn.Linear(200, 300)
#         self.modc = nn.Linear(300, 400)
#
#     def forward(self,x):
#         x=self.moda(x)
#         x = self.modb(x)
#         x = self.modc(x)
#         return x.sum()
#
#
# if __name__ == '__main__':
#     net=Net()
#
#     net=ModuleWrapper(net,forward_hook=TensorChecker("feat"),backward_hook=TensorChecker("feat"))
#     x=torch.ones(10,100,requires_grad=True)
#     z=net(x)
#     z.backward()
#
#     net.param_check()