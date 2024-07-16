import unittest
from netbox import run


class TestCircleArea(unittest.TestCase):
    def test_dict(self):
        self.assertEqual(run('id'),10)
        self.assertEqual(run("display"),'Kontron-2')
        self.assertEqual(run("tenant"),None)
    
unittest.main()