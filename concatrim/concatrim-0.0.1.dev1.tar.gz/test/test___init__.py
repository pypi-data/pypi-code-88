import unittest
import concatrim

class test_mediapruner(unittest.TestCase):
    
    def setUp(self):
        self.pruner = concatrim.Pruner(1000)
        
    def test_is_overlapping(self):
        self.assertFalse(self.pruner.is_overlapping( (1,2), (3,4) ))
        self.assertFalse(self.pruner.is_overlapping( (3,4), (1,2) ))
        self.assertTrue(self.pruner.is_overlapping( (1,3), (2,4) ))
        self.assertTrue(self.pruner.is_overlapping( (1,4), (2,3) ))
    
    def test_add_spane(self):
        self.pruner.add_spans( [1,2] )
        self.assertEqual(1, len(self.pruner.span_starts))
        self.assertEqual(1, len(self.pruner.span_ends))
        self.pruner._empty_spans()
        self.pruner.add_spans( [1,2], [100, 200] )
        self.assertEqual(2, len(self.pruner.span_starts))
        self.assertEqual(2, len(self.pruner.span_ends))
        self.pruner._empty_spans()
        self.pruner.add_spans( [100,200], [10, 20] )
        self.assertEqual(2, len(self.pruner.span_starts))
        self.assertEqual(2, len(self.pruner.span_ends))
        self.pruner._empty_spans()
        with self.assertRaises(ValueError):
            self.pruner.add_spans([1,4], [0,10])
        self.pruner._empty_spans()
        self.pruner.add_spans([1,4], [0,10])
        
        

