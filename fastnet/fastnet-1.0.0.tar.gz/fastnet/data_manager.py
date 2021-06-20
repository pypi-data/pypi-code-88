#This module contains classes that provides a high level interface for data loading.
import torch
import torch.utils.data as dm
import numpy as np
from fastnet.log import logger
import sklearn.model_selection as sms

def to_tensor(mat):
    '''Converts the passed numpy.array to a torch tensor'''
    return torch.tensor(mat, dtype = torch.float32)


def get_classes_input_data(data, classLabels = [+1, -1]):
    """Returns the input data corresponding to each class label.
       Parameters:
           - data: a (Input, Target) tuple where Input is the mixed input
                   data and Target their corresponding target.
           - classLabels: a list of class labels (default to [+1, -1])
       Returns: a tuple with the Input data for each class label in the same
                order as specified in classLabels.

       THIS WORKS FOR 2-CLASS CASE ONLY"""
    inData, targData = data
    targData = targData.flatten()
    return tuple([inData[targData == l,:] for l in classLabels])


def get_num_events_per_class(targList):
    """For a taget vector, tells how many events each class has.
    Returns a tuple with 2 lists ([labes], [counts]).The first provides each
    unique class label, and the second how many events each class has.

    THIS WORKS FOR 2-CLASS CASE ONLY"""
    labels, counts = np.unique(targList, return_counts = True)
    return labels, counts


def get_train_sampler(target):
    """
    Creates a weighted random sampler. The data sampler returned by this function
    will have the following features:
       - It will draw samples among classes with equal probability, regardless of number of events inbalances among classes.
       - Samples will be randomly selected.

    Input:
      - target: a [N x 1] numpy array containing all targets of all events of all classes.

    Return:
      - the weighted random sampler created after analysing the passed target vector.
    """
    #Getting the number of events per class.
    labels, counts = get_num_events_per_class(target)
    N = target.shape[0]
    logger.debug('Number of (unbalanced) events per target symbol {}: {}'.format(labels, counts))
    logger.debug('Total set size: {}'.format(N))

    largestClassSize = counts.max()
    weights = np.zeros(N)
    for label, numEv in zip(labels, counts):
        wVal = largestClassSize / numEv
        weights[target[:,0] == label] = wVal
        logger.debug('Weight for class {}: {}'.format(label, wVal))

    numSamples2Draw = int(largestClassSize * len(counts))
    logger.debug('Total available samples to retrieve at each epoch: {}'.format(numSamples2Draw))

    return dm.WeightedRandomSampler(weights, numSamples2Draw, replacement = True)



def get_datasets(dataList, test_size = 0.5):
    """
    Will get a list of class data and class labels and create proper training and testing
    sets.

    Input:
        dataList: list of tuples. Each tuple represents a class and should contain
                    the input data (a numpy array where each row is an event)
                    and label (a scalar) for a class. Example: [(X, +1), (Y,-1)].
        test_size: the percentual size [0,1] of the testing set.

    Output:
      - train: a (input, target) training tuple where input is a numpy array containing the input event where each event is a row.
               Target is a numpy array containing the target of each corresponding input (each target is a row).
      - test: a (input, target) testing tuple where input is a numpy array containing the input events where each event is a row.
               Target is a numpy array containing the target of each corresponding input (each target is a row).
    """

    inTrnList = []
    targTrnList = []
    inTstList = []
    targTstList = []

    classIdx = 1
    for input, label in dataList:
        nSamples = input.shape[0]

        #Creating a target vector using the scalar label passed.
        target = np.zeros([nSamples,1]) + label

        #Splitting the class data into training and testing sets.
        inTrn, inTst, targTrn, targTst = sms.train_test_split(input, target, test_size = test_size)
        logger.debug('Training / testing division for class {}: {}/{}'.format(classIdx, inTrn.shape[0], inTst.shape[0]))
        inTrnList.append(inTrn)
        targTrnList.append(targTrn)
        inTstList.append(inTst)
        targTstList.append(targTst)

        classIdx += 1

    #Concatenating everything to create a single dataset.
    inTrnList = np.concatenate(inTrnList)
    targTrnList = np.concatenate(targTrnList)
    inTstList = np.concatenate(inTstList)
    targTstList = np.concatenate(targTstList)

    #Creating the dataset (input x target) for the training / testing sets
    train = (inTrnList, targTrnList)
    test = (inTstList, targTstList)

    return train, test


def get_balanced_batched_loader(train, test, batch_size = 0):
    """
    Generates the train, test data loaders. The train dataloader will
    resolve any class number o samples inbalance by adjusting the samples
    drawing probability so the loader will draw samples from all classes with
    equal probability. In addition, the training loader will always ramdomly
    select samples. The test loader returned does NOT treat classes inbalances
    and always returns events in the same order.

    Input:
      - train: a (input, target) training tuple where input is a numpy array containing the input events where each event is a row.
               Target is a numpy array containing the target of each corresponding input (each target is a row).
      - test: a (input, target) testing tuple where input is a numpy array containing the input events where each event is a row.
               Target is a numpy array containing the target of each corresponding input (each target is a row).
      - batch_size: the training batch size to be used. Set it to 0 (zero) if you want to use the entire training set at each epoch. Defaults to zero.

    Returns:
      - trainDataLoader: the data loader for the trainign set already in torch.tensor format (ready to be used in the training).
      - testDataLoader: the data loader for the testing set already in torch.tensor format (ready to be used in the training).
    """

    #We will create a sampler that takes into considerantion
    #class inbalances regarding number of samples.
    trainSampler = get_train_sampler(train[1])

    if batch_size == 0: batch_size = trainSampler.num_samples
    logger.debug('Training batch size per epoch: {}'.format(batch_size))

    #Placing the data finally into a torch.tensor right before the training.
    train = dm.TensorDataset(to_tensor(train[0]), to_tensor(train[1]))
    test = dm.TensorDataset(to_tensor(test[0]), to_tensor(test[1]))

    trainDataLoader = dm.DataLoader(train, sampler = trainSampler, batch_size = batch_size)
    testDataLoader = dm.DataLoader(test, batch_size = len(test))
    logger.debug('Total testing events to be employed each epoch: {}'.format(len(test)))

    return trainDataLoader, testDataLoader



class CrossValidationManager:
    """
    This class manages cross-validation training by making sure
    data sets are split in training / test sets according to a cross validation
    object passed.
    """
    def __init__(self, crossValObj, dataList):
        """
        Input:
          - crossValObj: of the the many cross validation functions available in sklearn.model_selection.
                         the object passed will define how the training / testing sets will be drawn (Jack-knife, leave-one-out, etc.).
          - dataList:    list of tuples. Each tuple represents a class and should contain
                         the input data (a numpy array where each row is an event)
                         and label (a scalar) for a class. Example: [(X, +1), (Y,-1)].
        """
        inputList = []
        targetList = []
        classLabels = []
        for input, label in dataList:
            #Creating a target vector using the scalar label passed.
            inputList.append(input)
            targetList.append(np.zeros([input.shape[0],1]) + label)

        self.input = np.concatenate(inputList)
        self.target = np.concatenate(targetList)
        classLabels = self.target.flatten()
        self.Draws = [(trn, tst) for trn, tst in crossValObj.split(classLabels, classLabels)]


    def split(self, batch_size = 0, returnCounter = False):
        """
        Draw a new training / testing set to be used for the training.

        Input:
          - batch_size: the training batch size to be used. Set it to 0 (zero)
                        if you want to use the entire training set at each epoch. Defaults to zero.
          - returnCounter: if True, along with the training, testing sets, it will return also
                           the index of the set being draw (useful for control by the calling function).

        Return:
          A list where each element is a tuple of the format (k, train, test) if returnCounter = True
          or (train, test) if returnCounter = False, where:

            - k: is the index of the set being drawn
            - train: a (input, target) training tuple where input is a numpy array containing the input events where each event is a row.
                     Target is a numpy array containing the target of each corresponding input (each target is a row).
            - test: a (input, target) testing tuple where input is a numpy array containing the input events where each event is a row.
                    Target is a numpy array containing the target of each corresponding input (each target is a row).
        """
        ret = []
        for i, d in enumerate(self.Draws):
            v = []
            if returnCounter: v.append(i)
            trn, tst = d
            logger.debug('Deal "{}" - training indices: {}'.format(i, trn))
            logger.debug('Deal "{}" - testing indices: {}'.format(i, tst))
            v.append( (self.input[trn,:], self.target[trn,:]) )
            v.append( (self.input[tst,:], self.target[tst,:]) )
            ret.append(tuple(v))
        return ret
