from .Multiplication import Multiplication

class Hadamard(Multiplication):
    """
    Wiki: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
    """
    def __init__(self,matrix1,matrix2):
        Multiplication.__init__(self,matrix1,matrix2)
    
    def ismultiplyable(self):
        """
        INPUT: No Input
        OUTPUT: ismultiplyable : bool

        DESC: Matrices must be the same size.
        """
        m = len(self.matrix1)
        n = len(self.matrix1[0])
        p = len(self.matrix2)
        r = len(self.matrix2[0])

        if Multiplication.ismultiplyable(self):
            if m == p and n == r:
                return True
        else:
            return False
        
    
    def multiply(self):
        """
        DESC: For matrices of different dimensions (m × n and p × q, where m ≠ p or n ≠ q), 
              the Hadamard product is undefined.
        """
        if self.ismultiplyable():
            m = len(self.matrix1)
            n = len(self.matrix1[0])

            Multiplication.fill_result(self,n, m)

            for i in range(0, m): 
         
                for k in range(0, n):
                    self.result[i][k] = self.matrix1[i][k] * self.matrix2[i][k]
        else:
            print("Matrices are not multiplyable!")