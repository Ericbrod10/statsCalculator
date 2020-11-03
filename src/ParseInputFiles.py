import csv
from pprint import pprint


# def ClassFactory(class_name, dictionary):
#     return type(class_name, (object,), dictionary)


class ParseInputFiles:
    data = []

    def __init__(self):
        pass

    def parse(self, filepath):
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                self.data.append(row)
                # print(row)
        return self.data

