import unittest

from ParseInputs.ParseInputFiles import ParseInputFiles


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.datafile = ParseInputFiles()

    def test_instantiate_parser(self):
        self.assertIsInstance(self.datafile, ParseInputFiles)

    def test_file_parser(self):
        filepath = './Tests/testCSVs/Unit Test Addition.csv'
        file_data = self.datafile.parse(filepath)
#       for row in file_data:
#           print(row)
        file_data.clear()

    def test_empty_list(self):
        # Non-empty list
        filepath = './Tests/testCSVs/Unit Test Addition.csv'
        # Empty list
        # filepath = './Tests/testCSVs/Unit Test Empty.csv'
        file_data = self.datafile.parse(filepath)
#        for row in file_data:
#            print(row)
        file_data.clear()


if __name__ == '__main__':
    unittest.main()
