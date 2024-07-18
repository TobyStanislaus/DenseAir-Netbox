import unittest
from netbox import collect_all_data
import json


class TestCircleArea(unittest.TestCase):
    def test_dict(self):
        url = "https://netbox-dev.da.int/api/dcim/devices/10/"
        token = "5ce339f64325ecfda8250344636943e24297cf62"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token '+token
            }
        self.assertEqual(collect_all_data(["id"], url, headers),
                         json.dumps({'id': 10}))
        self.assertEqual(collect_all_data(["display"], url, headers),
                         json.dumps({'display': "Kontron-2"}))
        self.assertEqual(collect_all_data(["tenant"], url, headers),
                         json.dumps({"tenant": None}))


if __name__ == "__main__":
    unittest.main()
