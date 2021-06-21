import torch
import logging


class EarlyStop():

    def __init__(self, checkpoint, epoch=10, delta=0, min=True):
        self.min = min
        self.epoch = epoch
        self.delta = delta
        self.checkpoint = checkpoint

        self.counter = 0
        self.best_score = None
        self.early_stop = False

    def __call__(self, metric, model):
        logging.debug("Enter EarlyStop __call__ routine")
        score = - metric if self.min is True else metric

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(model)
        elif abs(score - self.best_score) <= self.delta:
            self.counter += 1
            if self.counter >= self.epoch:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(model)
            self.counter = 0
        logging.debug("Exit EarlyStop __call__ routine")

    def save_checkpoint(self, model):
        logging.debug("Enter EarlyStop save_checkpoint routine")
        torch.save(model.state_dict(), self.checkpoint)
        logging.debug("Exit EarlyStop save_checkpoint routine")
