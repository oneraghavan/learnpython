import unittest
from Accumulator import Accumulator

__author__ = 'admin'


class TestAccumulator(unittest.TestCase):

    def test_should_create_accumualtor(self):
        my_acc = Accumulator(4)
        summer = my_acc.getSum()
        summer.next()
        summer.send(4)
        summer.send(6)

if __name__ == '__main__':
    unittest.main()
