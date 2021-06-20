from fastnet.log import logger
import fastnet.data_manager as dm
import fastnet.metrics as met
import numpy as np

def relevance(net, trn, val, mode = 'mse', cut = 0.):
    """r = relevance(net, trn, val, mode, cut)
    Performs relevance analysis.

    Inputs:
      - net: a regression/classification trained model. It must be an object that provides
             the model output by calling its __call__ method.
      - trn: the data used to train the model.
      - val: the dataset used to validate the model (as a (input, target) tuple where input and target are numpy.arrays).
      - mode [mse, sp]: tells whether to calculate the relevance using mse or sp (defaults to 'mse').
      - cut: cut is the cut threshold between classes (to be used only if mode = 'sp'). Defaults to 0.

    The function returns a numpy vector with the output goal (MSE or SP) deviation for each removed input.

    WARNING: THIS FUNCTION WORKS FOR 2 CLASSES CASE ONLY
    """

    assert mode in ('mse', 'sp'), 'Mode must be either "sp" or "mse"'

    #Getting the mean value of each input variable.
    mdata = trn.mean(axis=0)
    if mode == 'mse':
        logger.info('Doing relevance analysis by MSE.')
        return do_by_mse(mdata, net, val[0])
    else:
        logger.info('Doing relevance analysis by SP.')
        return do_by_sp(mdata, net, val, cut)


def do_by_mse(mdata, net, val):
    nDim = val.shape[1]
    ret = np.zeros(nDim)
    outRef = net(val)

    for i in range(nDIM):
        #Creating a copy of the validation set and replacing the i-th input
        #by its mean value.
        aux = val.copy()
        aux[;,i] = mdata[i]

        out = net(aux)

        ret[i] = ((outRef - out)**2).mean()

    return ret


def do_by_sp(mdata, net, val, cut):
    nDim = val.shape[1]
    ret = np.zeros(nDim)
    signal, noise = dm.get_classes_input_data(val)
    _,_, spRef ,_,_,_ = met.efficiency(net(signal), net(noise), cut)

    for i in range(nDIM):
        #Creating a copy of the validation set and replacing the i-th input
        #by its mean value.
        auxSignal = signal.copy()
        auxNoise = noise.copy()
        auxSignal[;,i] = mdata[i]
        auxNoise[;,i] = mdata[i]
        _,_, sp ,_,_,_ = met.efficiency(net(auxSignal), net(auxNoise), cut)
        ret[i] = spRef - sp
