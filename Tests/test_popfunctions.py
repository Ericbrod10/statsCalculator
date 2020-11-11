import unittest
from Calculator.Calculator import Calculator
from ParseInputs.ParseInputFiles import ParseInputFiles


def convertDatatoList(data):
    ReturnList = []
    for i in data:
        ReturnList.append(float(i['Value']))
    return ReturnList


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.datafile = ParseInputFiles()
        self.ConfidenceLevel = 0.95
        self.ConfidenceZScore = 1.96
        self.TestProbability = 0.5
        self.PopulationPercentage = 41
        self.MarginOfError = 6
        # self.convert = convertDatatoList()

    def test_pop_sample_method_calculator(self):
        filepath = './Tests/testCSVs/TestStatData.csv'
        file_data = self.datafile.parse(filepath)
        file_data = convertDatatoList(file_data)
        self.assertEqual(len(self.calculator.randSample(file_data, 20)), 20)

    def test_ConfidenceInt(self):
        filepath = './Tests/testCSVs/TestStatData.csv'
        file_data = self.datafile.parse(filepath)
        file_data = convertDatatoList(file_data)
        self.assertEqual(self.calculator.ConfidenceInt(file_data, self.ConfidenceLevel),
                         (47.170905917537034, 50.78909408246296))

    def test_MarginOfError(self):
        filepath = './Tests/testCSVs/TestStatData.csv'
        file_data = self.datafile.parse(filepath)
        file_data = convertDatatoList(file_data)
        self.assertEqual(self.calculator.MarginOfError(file_data, self.ConfidenceZScore), 1.8082225352799999)

    def test_Cochran(self):
        filepath = './Tests/testCSVs/TestStatData.csv'
        file_data = self.datafile.parse(filepath)
        file_data = convertDatatoList(file_data)
        self.assertEqual(self.calculator.Cochran(file_data, self.ConfidenceLevel, self.ConfidenceZScore, self.TestProbability), 278)

    def test_UnknownStdPopSize(self):
        self.assertEqual(self.calculator.FindUnknownStdPopSampleSize(self.ConfidenceZScore, self.MarginOfError, self.PopulationPercentage), 1033)


if __name__ == '__main__':
    unittest.main()
