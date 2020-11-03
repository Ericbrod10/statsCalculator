import unittest

from ParseInputs.ParseInputFiles import ParseInputFiles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.datafile = ParseInputFiles()

    def test_instantiate_parser(self):
        self.assertIsInstance(self.datafile, ParseInputFiles)

    def test_file_parser(self):
        filepath = './src/testCSVs/Unit Test Addition.csv'
        file_data = self.datafile.parse(filepath)
        for row in file_data:
            print(row)
        file_data.clear()
