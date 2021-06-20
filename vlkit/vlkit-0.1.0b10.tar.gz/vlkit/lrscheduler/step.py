import numpy as np
import math
from .base import Scheduler


class MultiStepScheduler(Scheduler):
    def __init__(self, epoch_size, epochs, milestones, gamma, base_lr,
            warmup_epochs=0, warmup_init_lr=0, **kwargs):

        super(MultiStepScheduler, self).__init__(epoch_size, epochs, warmup_epochs,
                warmup_init_lr, **kwargs)

        assert isinstance(gamma, (float, tuple, list))
        assert isinstance(milestones, (tuple, list))

        if isinstance(gamma, float):
            gamma = (gamma, ) * len(milestones)
        else:
            assert len(milestones) == len(gamma)

        self.base_lr = base_lr
        self.milestones = [epoch_size * i for i in milestones]
        self.gamma = gamma

        self.milestone_counter = 0

    def get_lr(self, iter):
        if self.warmup_iters > 0 and iter <= self.warmup_iters:
            lr = self.warmup_init_lr + (iter / self.warmup_iters) * (self.base_lr - self.warmup_init_lr)
        else:
            stage = np.digitize(iter, self.milestones)
            if stage == 0:
                lr = self.base_lr
            else:
                lr = self.base_lr * np.prod(self.gamma[:stage])
        return lr
