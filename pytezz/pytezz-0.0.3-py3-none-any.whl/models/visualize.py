import matplotlib.pyplot as plt
import numpy as np


def plot_learning_rate(history):
  learning_rate=[x['lrs'] for x in history ]
  learning_rate=np.concatenate(learning_rate)
  plt.ylabel("learning_Rate")
  plt.xlabel("Images")
  plt.title("learning_Rate with Respect No of Images")
  plt.plot(learning_rate)
  
  plt.show()


def plot_metric(history,metric='accuracy'):
  accuracy=[x['Val_'+metric] for x in history]
  plt.title("accuracy")
  plt.xlabel("Epoch Number")
  plt.ylabel("Accuracy")

  plt.plot(accuracy,'-go')
  plt.show()

def plot_result(history):
  train_loss=[x['Train_loss'] for x in history]
  valid_loss=[x['Val_loss'] for x in history]

  plt.ylabel("Loss")
  plt.xlabel("Epoch Number")
  plt.title("Loss with respect to Epoch")

  plt.plot(train_loss,'-rx')
  plt.plot(valid_loss,'-bx')
  plt.legend(['Training_Loss','Validation_loss'])
  

  plt.show()
