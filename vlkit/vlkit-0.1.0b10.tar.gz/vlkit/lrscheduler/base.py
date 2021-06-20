import numpy as np


class Scheduler(object):
    def __init__(self, epoch_size, epochs, warmup_epochs, warmup_init_lr,
            noice_std=0, last_epoch=-1):

        self.max_iters = epoch_size * epochs
        self.warmup_iters = epoch_size * warmup_epochs
        self.warmup_init_lr = warmup_init_lr
        # the a random value with std=noice_std will be added to the lr
        self.noice_std = noice_std

        self.last_epoch = last_epoch
        assert self.last_epoch >= -1

        self.iter = (self.last_epoch+1) * epoch_size

    def step(self):
        self.iter += 1
        lr = self.get_lr(self.iter)
        if self.noice_std > 0:
            lr = max(lr + np.random.normal(scale=self.noice_std * lr), 0)
        return lr

    def get_lr():
        raise NotImplementedError
