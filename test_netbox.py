import unittest
from netbox import build_url


class TestCircleArea(unittest.TestCase):
    def test_url_capital(self):
        api = 'https://netbox-dev.da.int/api/dcim/devices/'
        filter_string = 'Kontron'
        url = build_url(api, filter_string)
        self.assertEqual(url, 'https://netbox-dev.da.int/api/dcim/devices/?manufacturer=kontron')


if __name__ == "__main__":
    unittest.main()
