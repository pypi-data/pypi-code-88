class Message:
    def __init__(self, delivery, sender="", receiver=""):
        self._delivery = delivery
        self._sender = sender
        self._receiver = receiver

    @property
    def delivery(self):
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        self._delivery = delivery

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver
