class Multiplication:

    def __init__(self,matrix1,matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.result = []
        

    def ismultiplyable(self):
        """
        INPUT: No Input
        OUTPUT: ismultiplyable : bool

        DESC: Can matrices be multiplied?
        """
        if len(self.matrix1) == 0 or len(self.matrix2) == 0:
            return False
        else:
            return True
    
    def fill_result(self,col,row):
        """
        INPUT: col: int
               row: int
        OUTPUT: No Output

        DESC: Creates a col x row dimensional zero matrix.
        """
        self.result=[[0 for i in range(col)] for j in range(row)]

    def display_result(self):
        """
        DESC: Display result matrix
        """
        for r in self.result:
            print(r)

