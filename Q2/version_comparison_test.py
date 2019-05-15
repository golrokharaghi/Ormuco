import unittest
from version_comparison import version_comparison

class test_VersionComparison(unittest.TestCase):

    def test_version_greater(self):
        result = version_comparison('1.2', '1.1.2')
        self.assertEqual(result, '1.2 is greater than 1.1.2')

    def test_version_less(self):
        result = version_comparison('1,2', '1.2.1')
        self.assertEqual(result, '1,2 is less than 1.2.1')

    def test_version_equal(self):
        result = version_comparison('1-2', '1-2')
        self.assertEqual(result, '1-2 is equal to 1-2')

    def test_version_alphabet(self):
        result = version_comparison('a.b.a', 'a.c')
        self.assertEqual(result, 'a.b.a is less than a.c')

if __name__ == '__main__':
    unittest.main()
