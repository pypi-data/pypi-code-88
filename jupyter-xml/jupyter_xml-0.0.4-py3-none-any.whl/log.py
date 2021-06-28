from IPython.display import display

class JupyterLogger:

    def __init__(self):
        self.verbose = False

    def set_verbose(self, verbose=True):
        self.verbose = verbose

    def print(self, msg, verbose=False):
        self.out(msg, verbose, True)

    def out(self, msg, verbose=False, _print=False):
        if verbose and not self.verbose:
            return
        else:
            if _print:
                print(msg)
            else:
                display(msg)
