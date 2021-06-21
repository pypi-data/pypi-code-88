'''This is the “nester.py" module, and it provides one function called
list_fun() which prints lists that may or may not include nested lists.'''

def list_fun(data):
    '''
    This function takes a positional argument called "data", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line.
    '''
    for list_item in data:
        if isinstance(list_item, list):
            list_fun(list_item)
        else:
            print(list_item)
