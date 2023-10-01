
import unittest
import random

from lifo import LIFO

class TestLIFO(unittest.TestCase):
    def test_00_empile(self):
        lifo00 = LIFO([1, 2, 3, 4, 5])
        lifo00.empile(6)
        target00 = LIFO([1, 2, 3, 4, 5, 6])
        self.assertEqual(str(lifo00), str(target00))

    def test_01_depile(self):
        lifo01 = LIFO([1, 2, 3, 4, 5])
        lifo01.depile()
        target01 = LIFO([1, 2, 3, 4])
        self.assertEqual(str(lifo01), str(target01))

    def test_02_depile_void(self):
        lifo02 = LIFO([])
        lifo02.depile()
        target02 = LIFO([])
        self.assertEqual(str(lifo02), str(target02))


if __name__ == "__main__":
    unittest.main()