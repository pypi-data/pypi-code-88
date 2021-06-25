from Name import Name
import unittest

class NameTester(unittest.TestCase):
    def test_parse(self):
        A = Name.parse('Neil deGrasse Tyson')
        self.assertTrue(A.first == "NEIL")
        self.assertTrue(A.middle == "DEGRASSE")
        self.assertTrue(A.last == "TYSON")
        self.assertFalse(A.isDifficult())
        
    def test_equality(self):
        A = Name.parse('Neil deGrasse Tyson')
        B = Name('Neil','D','Tyson')
        C = Name('NEIL',None,'TYSON')
        D = Name('Neil','DEGRASSE','Tyson')
        E = Name('Bob',None,'Ross')
        
        self.assertTrue(A.equal_primary(B))
        self.assertTrue(C.equal_primary(B))
        
        self.assertTrue(A.equal_middle_full(D))
        self.assertFalse(B.equal_middle_full(A))
        self.assertTrue(B.equal_middle_initial(A))

        self.assertFalse(D.equal_middle_full(C))
        self.assertFalse(D.equal_middle_initial(C))

    def test_comparison(self):
        A = Name.parse('Neil deGrasse Tyson')
        B = Name('Neil','D','Tyson')
        C = Name('NEIL',None,'TYSON')
        D = Name('Neil','DEGRASSE','Tyson')
        
        self.assertEqual(A.compare(C), 3)
        self.assertEqual(C.compare(A), 2)

        self.assertEqual(A.compare(B), 1)
        self.assertEqual(B.compare(B), 1)

        self.assertEqual(D.compare(A), 0)
        self.assertEqual(A.compare(D), 0)

if __name__ == '__main__':
    unittest.main()
