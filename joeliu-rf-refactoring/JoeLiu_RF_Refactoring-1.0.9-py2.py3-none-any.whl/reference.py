"""
This class is used to represent reference.
"""
class Reference:
    """
    reference: the reference data.
    present_method: a func obj which used to present the reference.
    replace_method: a func obj which used to modify the reference.
    """
    def __init__(self, reference, present_method, replace_method):
        self.reference = reference
        self.present_method = present_method
        self.replace_method = replace_method
    """
    This func is used to present the reference.
    return: the value after calling the present method.
    """
    def get_present_value(self):
        return self.present_method(self.reference)
    """
    This func is used to modify the reference.
    old: the string need to be modified.
    new: the string would replace.
    """
    def replace(self, old, new):
        self.replace_method(self.reference, old, new)