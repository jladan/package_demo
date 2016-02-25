import unittest

import measure.norms as n

class TestNorms(unittest.TestCase):

    def test_l1_zero(self):
        self.assertEqual(n.l1([0,0,0,0,0]), 0)
    def test_l2_zero(self):
        self.assertEqual(n.l2([0,0,0,0,0]), 0)
    def test_sup_zero(self):
        self.assertEqual(n.sup([0,0,0,0,0]), 0)
    def test_manhattan_zero(self):
        self.assertEqual(n.manhattan([0,0,0,0,0]), 0)

    def test_failure(self):
        self.assertEqual(n.l1([1]),0)


if __name__ == '__main__':
    unittest.main()
