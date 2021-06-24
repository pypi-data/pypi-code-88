from tensorflow.keras import Model


class NN(Model):
    def __init__(self, name='nn', **kwargs):
        super(NN, self).__init__(name=name, **kwargs)
