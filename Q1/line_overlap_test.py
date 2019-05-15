import unittest
from line_overlap import line_overlap

class TestLineOverlap (unittest.TestCase):

    def test_positive_overlap(self):
        result = line_overlap((1,5), (2,6))
        self.assertEqual(result, 'The lines (1, 5) and (2, 6) overlap.')


    def test_negative_overlap(self):
        result = line_overlap((-1,-5), (-2,-6))
        self.assertEqual(result, 'The lines (-1, -5) and (-2, -6) overlap.')


    def test_positive_nooverlap(self):
        result = line_overlap((1,5), (6,8))
        self.assertEqual(result, 'The lines (1, 5) and (6, 8) don\'t overlap.')


    def test_negative_nooverlap(self):
        result = line_overlap((-1,-5), (-6,-8))
        self.assertEqual(result, 'The lines (-1, -5) and (-6, -8) don\'t overlap.')


    def test_negpos_overlap(self):
        result = line_overlap((-2,5), (-1,-8))
        self.assertEqual(result, 'The lines (-2, 5) and (-1, -8) overlap.')


    def test_unordered_coordinates_overlap(self):
        result = line_overlap((5,-2), (6,1))
        self.assertEqual(result, 'The lines (5, -2) and (6, 1) overlap.')


    def test_same_coordinates_overlap(self):
        result = line_overlap((1,3), (1,6))
        self.assertEqual(result, 'The lines (1, 3) and (1, 6) overlap.')

if __name__ == '__main__':
    unittest.main()
