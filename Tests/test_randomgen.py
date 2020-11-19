import unittest

from RandomGen.RandomRange import randDec
from RandomGen.RandomRange import randInt
from RandomGen.RandomList import randDecList
from RandomGen.RandomList import randIntList
from RandomGen.SelectRandom import selectRand
from RandomGen.RandomRange_wSeed import randIntwSeed
from RandomGen.RandomRange_wSeed import randDecwSeed
from RandomGen.SelectRandom_wSeed import selectRand_wSeed
from RandomGen.RandomNumber import RandomNumb

class MyTestCase(unittest.TestCase):

    def test_randomNumber_generator(self):
        num = RandomNumb()
        self.assertIs(type(num), int)

    def test_randomInt_generator(self):
        num = randInt(0, 100)
        self.assertIs(type(num), int)
        # print(num)

    def test_randomDec_generator(self):
        num = randDec(0, 100)
        self.assertIs(type(num), float)
        # print(num)

    def test_randomInt_wSeed_generator(self):
        num = randIntwSeed(0, 100, 50)
        self.assertEqual(num, 63)
        # print(num)

    def test_randomInt_wSeed_generator(self):
        num = randDecwSeed(0, 100, 50)
        self.assertEqual(num, 49.75365687586023)
        # print(num)

    def test_randomIntList_generator(self):
        datalist = randIntList(5, 0, 100)
        self.assertIs(type(datalist[1]), int)
        # print(datalist)
        datalist.clear()

    def test_randomDecList_generator(self):
        datalist = randDecList(5, 0, 100)
        self.assertIs(type(datalist[1]), float)
        # print(datalist)
        datalist.clear()

    def test_selectRandom_generator(self):
        datalist = randIntList(5, 0, 100)
        # Select random element
        singlerandom = selectRand(datalist)
        self.assertIs(type(singlerandom), int)
        # Select N random elements
        randomlist = selectRand(datalist, 2)
        self.assertIs(type(randomlist), list)
        datalist.clear()

    def test_selectRandom_generator(self):
        datalist = randIntList(5, 0, 100)
        # Select random element
        singlerandom = selectRand(datalist)
        self.assertIs(type(singlerandom), int)
        # Select N random elements
        randomlist = selectRand(datalist, 2)
        self.assertIs(type(randomlist), list)
        datalist.clear()

    def test_selectRandom_wSeed_generator(self):
        datalist = [10, 20, 30, 40, 50, 60, 70, 25, 15, 30, 45, 70, 60, 80, 21]
        randomele = selectRand_wSeed(datalist, 1, 25)
        randomlist = selectRand_wSeed(datalist, 5, 25)
        self.assertEqual(randomele, 70)
        self.assertEqual(randomlist, [60, 80, 60, 40, 80])
        datalist.clear()


if __name__ == '__main__':
    unittest.main()
