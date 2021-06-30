from robot304.parsing.model import Step, Variable
from robot304.parsing.settings import Setting

class KeywordRefactorHelper:
    """
    references:the reference objects
    old:the origin keyword name
    new:the new keyword name
    """
    def rename_keyword(self, references, old, new):
        for reference in references:
            reference.replace(old, new)
          
class VariableRefactorHelper:
    """
    references:the reference objects
    old:the origin variable name
    new:the new variable name
    """
    def rename_variable(self, references, old, new):
        for reference in references:
            reference.replace(old, new)