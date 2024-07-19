import unittest
# from netbox import iterate_devices
import ast


with open('testData.txt', 'r') as file:
    data = file.read()
data = ast.literal_eval(data)

with open('testResults.txt', 'r') as file:
    results = file.read()
results = ast.literal_eval(results)


def build_url(api, filter_string):
    return api + '?manufacturer=' + filter_string.lower()


class TestCircleArea(unittest.TestCase):
    def test_dict(self):
        self.assertEqual()
        self.assertEqual('', results[1])
        self.assertEqual('', results[2])

    def test_url_capital(self):
        api = 'https://netbox-dev.da.int/api/dcim/devices/'
        filter_string = 'Kontron'
        url = build_url(api, filter_string)
        self.assertEqual(url, 'https://netbox-dev.da.int/api/dcim/devices/?manufacturer=kontron')


if __name__ == "__main__":
    unittest.main()
