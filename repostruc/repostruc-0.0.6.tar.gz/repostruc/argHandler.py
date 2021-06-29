from repostruc.__init__ import __version__ as version
from docopt import docopt
from pathlib import Path
import sys

sys.dont_write_bytecode = True

class GetArgumentParser:
   
    """
    Argument Parser class for repostruc:
    
    @functions
    __init__     => Initializes docopt
    getArguments => Returns docopt
    
    """

    def __init__(self):
        """
        Initializes Usage of arguments for Docopt

        """
        doc = """repostruc.

                Usage:
                    repostruc 
                    repostruc (-c | --clip)
                    repostruc [-r | --readme] (-f | --file) [<filepath>]
                    repostruc (-h | --help)
                    repostruc (-v | --version)
                
                Options:
                    -r --readme   Add to readme file.
                    -c --clip     Copy to clipboard.
                    --version     Show version.

                """
        self.doc = doc
        self.version = version
        self.name = "repostruc"

    def getArguments(self):
        """
        Initializes Docopt.

        @return
        Docopt object for Argument Parsing 
        """
        return docopt(self.doc, version=f'{self.name}_{self.version}')


if __name__ == '__main__':
    argparse = GetArgumentParser()
    arguments = argparse.getArguments()
    print(arguments)
