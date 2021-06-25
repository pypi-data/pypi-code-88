class ServerTime:

    def __init__(self, time):
        self.iso = time.get('iso')
        self.epoch = int(time.get('epoch'))
