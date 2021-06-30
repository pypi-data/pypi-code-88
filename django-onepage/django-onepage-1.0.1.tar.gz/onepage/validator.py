
class BasicValidator:
    def __init__(self, *args, **kwargs):
        super(BasicValidator, self).__init__(*args, **kwargs)
        self.valid_request = True
        self.invalid_request = False

    def is_valid(self):
        return self.valid_request

    def is_invalid(self):
        return self.invalid_request
