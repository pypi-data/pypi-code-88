import numpy as np
import math
from .base import Scheduler


class CosineScheduler(Scheduler):

    def __init__(self, epoch_size, epochs, max_lr, min_lr=0, warmup_epochs=0, warmup_init_lr=0,
            repeats=1, repeat_decay=0.1, last_epoch=-1, **kwargs):
        """
        epoch_size: number of iterations in a epoch (length of dataloader);
        epochs: total epochs;
        max_lr, min_lr: maximal and minimal learning rates;
        warmup_init_lr: initial learning rate in warmup (default: 0)
        repeat_decay: decay factor for repeating
        """
        super(CosineScheduler, self).__init__(epoch_size, epochs, warmup_epochs,
                warmup_init_lr, **kwargs)

        self.max_lr = max_lr
        self.min_lr = min_lr
        self.repeats = repeats
        self.repeat_decay = repeat_decay

        self.period = math.ceil((self.max_iters - self.warmup_iters) / self.repeats)
        assert self.last_epoch >= -1

    def get_lr(self, iter):
        if self.warmup_iters > 0 and iter <= self.warmup_iters:
            lr = self.warmup_init_lr + (iter / self.warmup_iters) * (self.max_lr - self.warmup_init_lr)
        else:
            repeat = (iter - self.warmup_iters - 1) // self.period
            step = (iter - self.warmup_iters - 1) % self.period
            base_lr = self.max_lr * (self.repeat_decay ** repeat)
            assert base_lr > self.min_lr
            lr = (base_lr - self.min_lr) * (1 + math.cos((step / self.period) * math.pi)) / 2 + self.min_lr
        return lr
