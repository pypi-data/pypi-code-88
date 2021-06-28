import torch
from occamypy import Operator, VectorTorch


class Module(Operator):
    """
    Encapsulate a torch.nn.Module to a operator
    """
    def __init__(self, domain, range, module, device=None):
        if not isinstance(domain, VectorTorch):
            domain = VectorTorch(domain, device=device)
        if not isinstance(range, VectorTorch):
            range = VectorTorch(range, device=device)
        
        super(Module, self).__init__(domain, range)
        
        assert isinstance(module, torch.nn.Module), "module has to be of torch.nn.Module class"
        self.module = module.to(device)
        
    def forward(self, add, model, data):
        # todo allow different devices?
        self.checkDomainRange(model, data)
        if not add:
            data.zero()
        
        # compute module output
        data[:] += self.module(model.getNdArray())
        return
    
    def parameters(self):
        return self.module.parameters()
