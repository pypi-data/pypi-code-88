from torch.optim import (Adadelta, Adagrad, Adam, AdamW,
                         SparseAdam, Adamax, ASGD, LBFGS,
                         RMSprop, Rprop, SGD)
import logging

optimizer_map = {
    'adadelta': Adadelta,
    'adagrad': Adagrad,
    'adam': Adam,
    'adamw': AdamW,
    'sparseadam': SparseAdam,
    'adamax': Adamax,
    'asgd': ASGD,
    'lbfgs': LBFGS,
    'rmsprop': RMSprop,
    'rprop': Rprop,
    'sgd': SGD
}


def get_optimizer(key, args, model):
    """Creates and returns a optimizer based on optimizer type and arguments.

    Parameters
    ----------
    key : string
        type of optimizer instance
    args : dict
        dictionary of optimizer parameters.
    model : torch.nn.Module
        model to train or validate.

    Returns
    -------
    torch.optim
        optimizer instance.

    """
    logging.debug("Enter get_optimizer routine")
    optimizer = optimizer_map[key]
    args['params'] = model.parameters()
    logging.debug("Exit get_optimizer routine")
    return optimizer(**args)
