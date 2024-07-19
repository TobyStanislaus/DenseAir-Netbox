import unittest
from netbox import iterate_devices
import ast
import json

with open('testData.txt', 'r') as file:
    data = file.read()
data = ast.literal_eval(data)

with open('testResults.txt', 'r') as file:
    results = file.read()
results = ast.literal_eval(results)


class TestCircleArea(unittest.TestCase):
    def test_dict(self):
        self.assertEqual(iterate_devices(data, '9'),
                         results[0])
        self.assertEqual(iterate_devices(data, 'Kontron'),
                         results[1])
        self.assertEqual(iterate_devices(data, ''),
                         results[2])


if __name__ == "__main__":
    unittest.main()
