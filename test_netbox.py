import unittest
from netbox import all_for_one
import ast

with open('testData.txt', 'r') as file:
    data = file.read()
data = ast.literal_eval(data)

with open('testResults.txt', 'r') as file:
    results = file.read()
results = ast.literal_eval(results)


class TestCircleArea(unittest.TestCase):
    def test_dict(self):

        self.assertEqual(all_for_one(data, '9'), results[0])
        self.assertEqual(all_for_one(data, 'Kontron'), results[1])
        self.assertEqual(all_for_one(data, ''), results[2])


if __name__ == "__main__":
    unittest.main()
