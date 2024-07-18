import unittest
from netbox import all_for_one
import json
import ast

with open('testData.txt', 'r') as file:
    content = file.read()


data = ast.literal_eval(content)
all_for_one(data)


class TestCircleArea(unittest.TestCase):
    def test_dict(self):
        self.assertEqual()
        '''
        self.assertEqual(collect_all_data(["display"], url, headers),
                         json.dumps({'display': "Kontron-2"}))
        self.assertEqual(collect_all_data(["tenant"], url, headers),
                         json.dumps({"tenant": None}))'''


if __name__ == "__main__":
    unittest.main()
