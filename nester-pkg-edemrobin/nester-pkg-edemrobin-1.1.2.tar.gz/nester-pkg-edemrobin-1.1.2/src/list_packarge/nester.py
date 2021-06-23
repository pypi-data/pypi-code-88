import sys
'''This is the “nester.py" module, and it provides one function called
list_fun() which prints lists that may or may not include nested lists.'''


def list_fun(data, indent=False, level=0, fh=sys.stdout):
    '''
    This function takes a positional argument called "data", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line.
    level have been added to the function to make it possible to neatly format the code,
    An optional parameter has been added to the function called "indent".By default indent is set to False
    '''
    for list_item in data:
        if isinstance(list_item, list):
            list_fun(list_item, indent, level + 1,fh)
        else:
            if indent:
                for new_tab in range(level):
                    print('\t', end='',file=fh)
            print(list_item,file=fh)
