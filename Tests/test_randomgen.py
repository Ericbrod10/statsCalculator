import unittest

from RandomGen.RandomRange import randInt
from RandomGen.RandomRange import randDec


class MyTestCase(unittest.TestCase):

    def test_randomInt_generator(self):
        num = randInt(0, 100)
        self.assertIs(type(num), int)
        # print(num)

    def test_randomDec_generator(self):
        num = randDec(0, 100)
        self.assertIs(type(num), float)
        # print(num)


if __name__ == '__main__':
    unittest.main()
