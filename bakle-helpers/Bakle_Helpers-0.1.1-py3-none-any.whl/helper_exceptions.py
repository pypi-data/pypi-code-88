class HelperExceptions:

    @staticmethod
    def raise_for_not_an_integer(data):
        raise TypeError(f'{data} is not an integer')

    @staticmethod
    def raise_for_not_a_string():
        raise TypeError('Some of the given args are not a string')