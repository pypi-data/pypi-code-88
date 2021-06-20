#!/usr/bin/env python3

#Falta desenvolver:
#    1) Validação cruzada
#    2) Fazer a classe de treinamento trabalhar com classes (estilo seu cell array do matlab)

import os
import time
os.environ['FASTNET_LOG_LEVEL'] = 'ERROR'

import sys
import torch.nn
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import fastnet.train as fn
import fastnet.metrics as met
import fastnet.data_manager as dm


def plot_output(data, model, title):
    hist = []
    for i,c in enumerate(data):
        className = 'Class {}'.format(i+1)
        classOutData = model(c[0])
        hist.append(go.Histogram(x = classOutData, name = className, opacity=0.75))

    layout = go.Layout(title = title,
                        xaxis =  dict(title ='Neural Network Output'),
                        yaxis =  dict(title = 'Count'),
                        hovermode= 'closest')

    fig = go.Figure(data = hist, layout = layout)
    pyo.plot(fig, filename= '/tmp/' + title + '.html')


def plot_input(c1,c2):
    pc1 = go.Scatter(x = c1[:,0],
                      y = c1[:,1],
                      mode = 'markers',
                      name = 'Class 1')
    pc2 = go.Scatter(x = c2[:,0],
                      y = c2[:,1],
                      mode = 'markers',
                      name = 'Class 2')

    layout = go.Layout(title = "Patterns Original Distribution",
                        xaxis =  dict(title ='Var 1'),
                        yaxis =  dict(title = 'Var 2'),
                        hovermode= 'closest')

    fig = go.Figure(data = [pc1, pc2], layout = layout)
    pyo.plot(fig, filename='/tmp/input.html')



def plot_roc(det, fa, tit):
    det = np.atleast_2d(det)
    fa = np.atleast_2d(fa)
    pc1 = [go.Scatter(x = 100*fa[i,:],
                      y = 100*det[i,:],
                      mode = 'lines',
                      name = 'ROC') for i in range(det.shape[0])]
    layout = go.Layout(title = "ROC ({})".format(tit),
                        xaxis =  dict(title ='False Alarm'),
                        yaxis =  dict(title = 'Detection Efficiency'),
                        hovermode= 'closest')

    fig = go.Figure(data = pc1, layout = layout)
    pyo.plot(fig, filename= '/tmp/' + tit + '-ROC.html')


def plot_sp(spVec):
    sp = 100*spVec
    pc1 = [go.Scatter(x = [1],
                      y = [sp.mean()],
                      error_y = dict(type='data', array=[sp.std()], visible=True),
                      mode = 'lines+markers',
                      name = 'Max SP.')]
    layout = go.Layout(title = "Max SP Analysis",
                        xaxis =  dict(title ='Classifier'),
                        yaxis =  dict(title = 'SP (x100)'),
                        hovermode= 'closest')

    fig = go.Figure(data = pc1, layout = layout)
    pyo.plot(fig, filename= '/tmp/Max SP.html')



def plot_errors(trn, val):
    plot = []
    for i in range(trn.shape[0]):
        plot.append(go.Scatter(y = trn[i,:],
                                    mode = 'lines+markers',
                                    name = 'Training Error',
                                    line = dict(color = 'blue')))
        plot.append(go.Scatter(y = val[i,:],
                                    mode = 'lines+markers',
                                    name = 'Validation Error',
                                    line = dict(color = 'red')))

    layout = go.Layout(title = "Training Evolution",
                        xaxis =  dict(title ='Epoch'),
                        yaxis =  dict(title = 'MSE'),
                        hovermode= 'closest')

    fig = go.Figure(data = plot, layout = layout)
    pyo.plot(fig, filename='/tmp/Training Evolution.html')


def get_dataset(nData):
    #Generating data set.
    c1 = np.random.randn(nData, 2) + 3
    c2 = np.random.randn(nData, 2)
    plot_input(c1,c2)
    return [(c1, +1), (c2, -1)]



#Global level parameters
nData = 1000
batchSize = 0
hidNodes = 3
epochs = 100
evalFunc = 'sp'
nTrains = 2
saveData = True
nDeals = 5
numROC = 1000
testSize = 0.5
trfFunction = [torch.nn.Tanh, torch.nn.Tanh]

#Creating dataset.
data = get_dataset(nData)

#Resultados para a rede nao treinada.
net = fn.BinaryClassificationNetwork([2, hidNodes, 1], trfFunction, evalFunc = evalFunc)
outSignal = net(data[0][0])
outNoise = net(data[1][0])
det, fa, _, _, _, _, _ = met.roc(outSignal, outNoise, numPts = numROC, algo = 'matlab')
plot_output(data, net, 'Saída Antes do Treino')
plot_roc(det, fa, 'Antes do Treino')


ret = None
start = time.time()
if nDeals == 1:
    print('Using single-training')
    ret = fn.single_training(data, [hidNodes], trfFunction,
                                testSize = testSize, evalFunc = evalFunc,
                                nTrains = nTrains, batchSize = batchSize,
                                epochs = epochs, numROC = numROC)
else:
    print('Using cross-validation trainning')
    ret = fn.cross_validation_training(data, [hidNodes], trfFunction,
                                        testSize = testSize, evalFunc = evalFunc,
                                        nTrains = nTrains, batchSize = batchSize,
                                        epochs = epochs, numROC = numROC, nDeals = nDeals)

end = time.time()

print('Training elapsed time: {0:0.2f} seconds.'.format(end-start))

#Getting best network.
idx = ret.maxSP.argmax()
net = ret.net[idx]
tstDataAux = dm.get_classes_input_data(ret.tstData[idx])
tstData = [(tstDataAux[0], +1), (tstDataAux[1], -1)]


#Resultados pos treino
plot_output(tstData, net, 'Saída Após o Treino')
plot_roc(ret.det, ret.fa, 'Após o Treino')
plot_errors(ret.trnError, ret.tstError)
plot_sp(ret.maxSP)
