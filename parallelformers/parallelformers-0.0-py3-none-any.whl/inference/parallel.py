from typing import Any

import torch
import torch.distributed as dist
from deepspeed import init_distributed
from torch import nn


class ParallelModule(nn.Module):

    def __init__(self, gpu_from, gpu_to):
        super().__init__()
        init_distributed()

        self.local_rank = gpu_from
        self.world_size = gpu_to - gpu_from + 1
        torch.cuda.set_device(self.local_rank)

        ranks = [_ for _ in range(self.world_size)]
        self.mp_group = dist.new_group(ranks)

        self.module.to(torch.cuda.current_device())
        for p in self.module.parameters():
            if torch.is_tensor(p):
                if not p.is_contiguous():
                    p = p.contiguous()
                dist.broadcast(p, 0)

    def forward(self, x):
        pass
