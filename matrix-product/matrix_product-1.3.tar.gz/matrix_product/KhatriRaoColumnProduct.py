from .Multiplication import Multiplication

class KhatriRaoColumn(Multiplication):
    """
    Wiki: https://en.wikipedia.org/wiki/Khatri%E2%80%93Rao_product
    """
    def __init__(self,matrix1,matrix2):
        Multiplication.__init__(self,matrix1,matrix2)
    
    def ismultiplyable(self):
        """
        INPUT: No Input
        OUTPUT: ismultiplyable : bool

        DESC: Matrices column must be the same size.
        """
        n = len(self.matrix1[0])
        r = len(self.matrix2[0])

        if Multiplication.ismultiplyable(self):
            if n == r:
                return True
        else:
            return False
        
    
    def multiply(self):
        """
        DESC: This type of operation is based on row-by-row Kronecker products of two matrices.
        """
        if self.ismultiplyable():
            m = len(self.matrix1)
            n = len(self.matrix1[0])
            p = len(self.matrix2)

            Multiplication.fill_result(self,n, (m * p))

            rowr = 0

            for i in range(m):

                for k in range(p):

                    for j in range(n):

                            self.result[rowr][j] = self.matrix1[i][j] * self.matrix2[k][j]
                    rowr += 1
        else:
            print("Matrices are not multiplyable!")