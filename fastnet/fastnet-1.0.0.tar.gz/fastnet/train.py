import torch
import torch.nn
import torch.optim
import numpy as np
import copy
import collections
import math
from fastnet.log import logger
import fastnet.data_manager as dm
import fastnet.utils as ut
import fastnet.metrics as met
from sklearn.model_selection import StratifiedShuffleSplit


class SPLoss(torch.nn.modules.loss._Loss):
    """Implements SP loss function according to PyTorch requirements for loss functions"""

    def __init__(self, num_roc_pts = 200, signal_label = 1., noise_label = -1.):
        """
        - num_roc_pts: scalar definign how many points to be used when evaluating the ROC. Defaults to 200.
        - signal_label: a scalar defining the label to be used for the signal class. Defaults to +1.
        - noise_label: a scalar defining the label to be used for the noise class. Defaults to -1.
        """
        super(SPLoss, self).__init__()
        self.num_roc_pts = num_roc_pts
        self.signal_label = signal_label
        self.noise_label = noise_label

    def forward(self, output, target):
        """
        Computes the SP loss based on the output x target arrays passed.
        Returns the maximum SP found for the generated ROC.
        WORKS ONLY FOR BINARY CLASSIFICATION NETWORKS.
        """
        cutVec = np.linspace(self.noise_label, self.signal_label, self.num_roc_pts)
        signal = output[target == self.signal_label]
        noise = output[target == self.noise_label]
        nSignal = float(len(signal))
        nNoise = float(len(noise))
        maxSP = -torch.ones(1, dtype = torch.float32)
        efics = torch.zeros(2, dtype = torch.float32)
        for cut in cutVec:
            efics[0] = torch.sum(signal >= cut, dtype = torch.float32) / nSignal #Detection efficiency
            efics[1] = torch.sum(noise < cut, dtype = torch.float32) / nNoise # 1 - false alarm
            sp = torch.sqrt( efics.prod().sqrt() * efics.mean() )
            maxSP = torch.max(maxSP, sp)
        return maxSP


class BinaryClassificationNetwork:
    """Class to implement the training of a binary classifier."""

    def __init__(self, numNodes, trfFunc, evalFunc = 'mse'):
        """
        - numNodes: a list of scalars defining the number of nodes in each layer (including the input layer).
        - trfFunc: a list of torch.nn available transfer functions for all hidden layer and the output layer.
        - evalFunc: a string defining the desired evaluation function. Values can be 'mse' or 'sp'. Defaults to 'mse'.
        """
        assert evalFunc in ['mse', 'sp'], 'Invalid evaluation function for validation step.'
        assert (len(numNodes)-1) == len(trfFunc), 'numNodes and trFunc vectors length do not make sense! trFunc must have 1 element less than numNodes.'
        topology = []
        for i, func in enumerate(trfFunc):
            topology.append(torch.nn.Linear(numNodes[i], numNodes[i+1]))
            topology.append(func())
        self.model = torch.nn.Sequential(*tuple(topology))
        self.loss_fn_trn = torch.nn.MSELoss(reduction='mean')
        if evalFunc == 'mse':
            self.loss_fn_val = torch.nn.MSELoss(reduction='mean')
            logger.info('Stop criteria: MSE')
            self.evalFix = 1.
        elif evalFunc == 'sp':
            self.loss_fn_val = SPLoss()
            logger.info('Stop criteria: SP')
            self.evalFix = -1.
        self.optimizer = torch.optim.Rprop(self.model.parameters())
        self.bestModel = copy.deepcopy(self.model)


    def initWeights(self, m):
        """Initializes the network weights."""
        if type(m) == torch.nn.Linear:
            torch.nn.init.kaiming_uniform_(m.weight, a = math.sqrt(5))
            if m.bias is not None:
                fan_in, _ = torch.nn.init._calculate_fan_in_and_fan_out(m.weight)
                bound = 1 / math.sqrt(fan_in)
                torch.nn.init.uniform_(m.bias, -bound, bound)


    def train(self, trnData):
        """Trains the neural network for just one epoch."""
        avg = 0.
        N = 0.
        for input, target in trnData:
            self.model.train()
            out = self.model(input)
            loss = self.loss_fn_trn(out, target)
            avg += loss.item()
            N += 1
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
        return avg / N


    def validate(self, val):
        """Validates the neural network for just one epoch."""
        self.model.eval()
        with torch.no_grad():
            #We assume here that the val set is not batched so we call
            #the next function of the data loader iterator so we can get
            #the full size of the valdiation set.
            inVal, targVal = next(val.__iter__())
            return self.loss_fn_val(self.model(inVal), targVal).item()


    def initializeAndTrain(self, train, val, epochs):
        """
        Forces a new weights initialization and then performs the training.
        This is useful when doing multiple weights initialization to dodge local minimum.
        """
        trnError = []
        valError = []
        minError = 10000000000
        self.model.apply(self.initWeights)
        bestModel = None
        for e in range(epochs):
            trnError.append(self.train(train))
            valE = self.validate(val)
            valError.append(valE)
            valE *= self.evalFix
            if valE < minError:
                bestModel = copy.deepcopy(self.model)
                minError = valE
                logger.debug('Best net found in epoch {}: {}'.format(e, self.evalFix*valE))
        return np.array(trnError), np.array(valError), minError, bestModel


    def fit(self, train, val, epochs = 100, numInitializations = 10, batch_size = 0):
        """
        Fit the neural network using the training data passed.

        Input:
          - train: a (input, target) training tuple where input is a list where each
                   element is a numpy array containing the input events of the i-th class where each event is a row.
                   Target is a numpy array containing the target of each corresponding input (each target is a row).
          - test: a (input, target) testing tuple where input is a list where each
                  element is a numpy array containing the input events of the i-th class where each event is a row.
                  Target is a numpy array containing the target of each corresponding input (each target is a row).
          - epochs: for how many epochs to train the model (save the best is employed,
                    so do not fear setting a large value if desired). Defaults to 100.
          - numInitializations: how many times re-initialize the network and re-train it.
                    Useful to dodge local minimus. If > 1, then just the network
                    with the best result for the testing set is returned. Defaults to 10.
          - batch_size: the training batch size to be used. Set it to 0 (zero)
                        if you want to use the entire training set at each epoch. Defaults to zero.
        """
        #Creating the torch.tensors datasets for handling the network data feeding.
        train, val = dm.get_balanced_batched_loader(train, val, batch_size)
        gbMinError = gbTrnError = gbValError = 10000000000
        self.bestModel = copy.deepcopy(self.model)
        for i in range(numInitializations):
            trnError, valError, minError, bestModel = self.initializeAndTrain(train, val, epochs)
            logger.debug('Min error for initialization was {}'.format(minError))
            if minError < gbMinError:
                self.bestModel = bestModel
                gbTrnError = trnError
                gbValError = valError
                gbMinError = minError
        logger.debug('Best network min error = {}'.format(gbMinError))
        return gbTrnError, gbValError


    def propagate(self, vec):
        """
        Feedforward the input vector (numpy or torch tensor where each event is a row)
        through the network (trained or not).

        Returns a flattened [0 x N] numpy vector with the output obtained for each provided input.
        """
        return self.bestModel(vec)

    def __call__(self, vec):
        """
        Feedforward the input vector (numpy or torch tensor where each event is a row)
        through the network (trained or not).

        Returns a flattened [0 x N] numpy vector with the output obtained for each provided input.
        """
        if type(vec) is np.ndarray:
            logger.debug('Converting numpy matrix to torch.Tensor before propagating iot through the network.')
            vec = dm.to_tensor(vec)
        ret = self.bestModel(vec)
        return ret.detach().numpy().flatten()


def create_results_structure(nDeals, epochs, numROC):
    """
    Creates a structure to hold the network results

    Input:
      - nDeals: how many cross-validation deals to consider.
      - epochs: number of training epochs.
      - numROC: number of points to consider when generating the ROC.

    Returns a ObjectView object with the following attributes:
      - net: list for storing BinaryClassificationNetwork trained objects for each deal.
      - trnError: [nDeals, epochs] numpy.zeros matrix for storing training evolution errors.
      - tstError: [nDeals, epochs] numpy.zeros matrix for storing testing evolution scores.
      - det: [nDeals, numROC] numpy.zeros matrix for storing detection efficiency for each deal.
      - fa: [nDeals, numROC] numpy.zeros matrix for storing false alarme probability for each deal.
      - maxSP: [0, nDeals] numpy.zeros vector to store the maximum SP obtained for each deal.
      - thres: [0, nDeals] numpy.zeros vector to store the threshold where the maximum SP was obtained for each deal.
      - trnData: a list to hold the training data used for each deal.
      - tstData: a list to hold the testing data used for each deal.
    """
    ret = ut.ObjectView()
    ret.net = []
    ret.trnError = np.zeros([nDeals, epochs])
    ret.tstError = np.zeros([nDeals, epochs])
    ret.det = np.zeros([nDeals, numROC])
    ret.fa = np.zeros([nDeals, numROC])
    ret.maxSP = np.zeros(nDeals)
    ret.thres = np.zeros(nDeals)
    ret.trnData = []
    ret.tstData = []
    return ret


def save_results(ret, idx, trnError, tstError, net, trainData, tstData):
    """
    Saves the training results into the structure created by create_results_structure.

    Inputs:
      - ret: an ObjectView structure created by create_results_structure.
      - idx: the index of the training (deal) being performed.
      - trnError: [0, epochs] vector with the network training evolution errors.
      - tstError: [0, epochs] vector with the network testing evolution errors.
      - net: a BinaryClassificationNetwork trained objects.
      - trnData: training data used for the deal.
      - tstData: testing data used for the deal.

    Returns ret with its corresponding attributes populated for the idx-th deal.
    """

    numROC = ret.det.shape[1]
    inTst, targTst = tstData
    targTst = targTst.flatten()
    inSignal, inNoise = dm.get_classes_input_data(tstData)
    outSignal = net(inSignal)
    outNoise = net(inNoise)
    ret.det[idx,:], ret.fa[idx,:], spVec, _, _, _, thres = met.roc(outSignal, outNoise, numPts = numROC, algo = 'matlab')
    ret.net.append(net)
    ret.trnError[idx,:] = trnError
    ret.tstError[idx,:] = tstError
    ret.maxSP[idx] = spVec.max()
    ret.thres[idx] = thres[spVec.argmax()]
    ret.trnData.append(trainData)
    ret.tstData.append(tstData)
    return ret


def single_training(data, hiddenNodes, trfFunction, testSize = 0.5, evalFunc = 'sp', nTrains = 10, batchSize = 0, epochs = 100, numROC = 200):
    """
    single_training(data, hiddenNodes, trfFunction, testSize = 0.5, evalFunc = 'sp',
                    nTrains = 10, batchSize = 0, epochs = 100, numROC = 200)

    Performs a single training.

    Inputs:
      - data: list of tuples. Each tuple represents a class and should contain
              the input data (a numpy array where each row is an event)
              and label (a scalar) for a class. Example: [(X, +1), (Y,-1)].
      - hiddenNodes: a list stating how many nodes to be used in each hidden layer
                    (do not specify nodes for the input and output layers).
      - trfFunction: a list of torch.nn available transfer functions for all hidden layers and the output layer.
      - testSize: the percentual size [0,1] of the testing set. Defaults to 0.5.
      - evalFunc: the evalutiaon function to use ('mse' or 'sp'). Defaults to 'sp'.
      - nTrains: how many weights initialization to perform. Defaults to 10.
      - batchSize: epochs batch size. Defaults to zero (use all available data).
      - epochs: number of training epochs. Defaults to 100.
      - numROC: ROC size, when evaluating performance. Defaults to 200.

     Returns a populated ObjectView object created by create_results_structure.
    """

    train, test = dm.get_datasets(data, test_size = testSize)
    numNodes = [train[0].shape[1]] + hiddenNodes + [train[1].shape[1]]
    net = BinaryClassificationNetwork(numNodes, trfFunction, evalFunc = evalFunc)
    trnError, tstError = net.fit(train, test, epochs, numInitializations = nTrains, batch_size = batchSize)
    ret = create_results_structure(1, epochs, numROC)
    return save_results(ret, 0, trnError, tstError, net, train, test)


def cross_validation_training(data, hiddenNodes, trfFunction, testSize = 0.5, evalFunc = 'sp', nTrains = 10, batchSize = 0, epochs = 100, numROC = 200, nDeals = 20):
    """
    cross_validation_training(data, hiddenNodes, trfFunction, testSize = 0.5, evalFunc = 'sp',
                                nTrains = 10, batchSize = 0, epochs = 100, numROC = 200, nDeals = 20)

    Performs a cross-validation training.

    Inputs:
      - data: list of tuples. Each tuple represents a class and should contain
              the input data (a numpy array where each row is an event)
              and label (a scalar) for a class. Example: [(X, +1), (Y,-1)].
      - hiddenNodes: a list stating how many nodes to be used in each hidden layer
                    (do not specify nodes for the input and output layers).
      - trfFunction: a list of torch.nn available transfer functions for all hidden layers and the output layer.
      - testSize: the percentual size [0,1] of the testing set. Defaults to 0.5.
      - evalFunc: the evalutiaon function to use ('mse' or 'sp'). Defaults to 'sp'.
      - nTrains: how many weights initialization to perform. Defaults to 10.
      - batchSize: epochs batch size. Defaults to zero (use all available data).
      - epochs: number of training epochs. Defaults to 100.
      - numROC: ROC size, when evaluating performance. Defaults to 200.
      - nDeals: how many cross-validation deals to execute. Defaults to 20.

     Returns a populated ObjectView object created by create_results_structure
     including the results for all deals.
    """

    skf = StratifiedShuffleSplit(n_splits = nDeals, test_size = testSize)
    cvm = dm.CrossValidationManager(skf, data)
    ret = create_results_structure(nDeals, epochs, numROC)
    for i, train, test in cvm.split(returnCounter = True):
        numNodes = [train[0].shape[1]] + hiddenNodes + [train[1].shape[1]]
        net = BinaryClassificationNetwork(numNodes, trfFunction, evalFunc = evalFunc)
        trnError, tstError = net.fit(train, test, epochs, numInitializations = nTrains, batch_size = batchSize)
        ret = save_results(ret, i, trnError, tstError, net, train, test)
    return ret
