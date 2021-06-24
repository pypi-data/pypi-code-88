from sierra import *

# def div(*args):
#     for arg in args:
#         b = ' ' + arg
#         with open('index.html', 'a') as f:
#             f.write(f'''{b}''')

# a = [[['coffee', 'get_tea'], ['tea', 'lol']]]
a = [[['coffee', 'tea'], ['black coffee', 'black tea']], [['sierra'], ['this', 'is', 'easy']]]

def def_lists(def_list, *args):
    """
    Creates a definition list from a list of lists
    Args:
    def_list(list, compulsory): Takes in a list of lists and creates a def list on it
    *args: To use global and event attributes, if required. Enter all of them within quotes, not comma-separated
    
    """
    with open('index.html', 'a+') as f:
        f.write(f'''\n<dl''')
    for arg in args:
            b = ' ' + arg
            with open('index.html', 'a') as f:
                f.write(f'''{b}''')
    open('index.html', 'a').write(">")
    for def_listings in def_list:
        for def_listing in def_listings[0]:
            open('index.html', 'a').write(f'''\n<dt>{def_listing}</dt>''')
        def_listings.remove(def_listings[0])
        for listings in def_listings:
            for listing in listings:
                open('index.html', 'a').write(f'''\n<dd>{listing}</dd>''')
    with open('index.html', 'a') as f:
        f.write("\n</dl>")

def_lists(a, "id='lol' class='lols'")
