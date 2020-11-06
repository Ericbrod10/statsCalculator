import unittest

from Calculator.Calculator import Calculator
from ParseInputs.ParseInputFiles import ParseInputFiles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.datafile = ParseInputFiles()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Addition.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_subtraction_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Subtraction.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_multiplication_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Multiplication.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_division_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Division.csv'
        file_data = self.datafile.parse(filepath)
        # Test divide by 0
        # self.assertEqual(self.calculator.divide(5, 0), 1)
        # Test CSV Data
        for row in file_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
        file_data.clear()

    def test_squared_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Square.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
        file_data.clear()

    def test_root_method_calculator(self):
        filepath = './Tests/testCSVs/Unit Test Square Root.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            self.assertEqual(round(self.calculator.root(row['Value 1']), 8), round(float(row['Result']), 8))
        file_data.clear()

    def test_mean_method_calculator(self):
        dataList = [2, 5, 7, 10]
        self.assertEqual(self.calculator.mean(dataList), 6)


if __name__ == '__main__':
    unittest.main()
