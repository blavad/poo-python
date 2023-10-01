
import unittest
import random

from fifo import FIFO

class TestFIFO(unittest.TestCase):
    def test_00_empile(self):
        fifo00 = FIFO([1, 2, 3, 4, 5])
        fifo00.empile(6)
        target00 = FIFO([1, 2, 3, 4, 5, 6])
        self.assertEqual(str(fifo00), str(target00))

    def test_01_depile(self):
        fifo01 = FIFO([1, 2, 3, 4, 5])
        fifo01.depile()
        target01 = FIFO([2, 3, 4, 5])
        self.assertEqual(str(fifo01), str(target01))

    def test_02_depile_void(self):
        fifo02 = FIFO([])
        fifo02.depile()
        target02 = FIFO([])
        self.assertEqual(str(fifo02), str(target02))


if __name__ == "__main__":
    unittest.main()