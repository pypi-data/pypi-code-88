from .Multiplication import Multiplication

class Kronecker(Multiplication):
    """
    Wiki: https://en.wikipedia.org/wiki/Kronecker_product
    """
    def __init__(self,matrix1,matrix2):
        Multiplication.__init__(self,matrix1,matrix2)
    
    def multiply(self):
        """
        DESC: If A is an m × n matrix and B is a p × q matrix, 
              then the Kronecker product A ⊗ B is the pm × qn block matrix.
        """
        if Multiplication.ismultiplyable(self):
            m = len(self.matrix1)
            n = len(self.matrix1[0])
            p = len(self.matrix2)
            r = len(self.matrix2[0])

            Multiplication.fill_result(self,(m * p), (n * r))

            col = 0
            row = 0

            for i in range(0, m):
            
                for k in range(0, p):
        
                    for j in range(0, n):
        
                        for l in range(0, r):
        
                            self.result[col][row] = self.matrix1[i][j] * self.matrix2[k][l]
                            row += 1
                    row = 0    
                    col += 1
        else:
            print("Matrices are not multiplyable!")
                
