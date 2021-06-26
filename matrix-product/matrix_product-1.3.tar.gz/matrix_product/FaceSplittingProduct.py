from .Multiplication import Multiplication

class FaceSplitting(Multiplication):
    """
    Wiki: https://en.wikipedia.org/wiki/Khatri%E2%80%93Rao_product
    """
    def __init__(self,matrix1,matrix2):
        Multiplication.__init__(self,matrix1,matrix2)
    
    def ismultiplyable(self):
        """
        INPUT: No Input
        OUTPUT: ismultiplyable : bool

        DESC: Matrices row must be the same size.
        """
        m = len(self.matrix1)
        p = len(self.matrix2)

        if Multiplication.ismultiplyable(self):
            if m == p:
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
            r = len(self.matrix2[0])

            Multiplication.fill_result(self,(n * r), m)

            colr = 0

            for i in range(n):

                for k in range(r):

                    for j in range(m):

                            self.result[j][colr] = self.matrix1[j][i] * self.matrix2[j][k]
                    colr += 1
        else:
            print("Matrices are not multiplyable!")