import unittest

from src.mushroom_scales import *

class TestTemplate(unittest.TestCase):

    set_one = {
        1: 10,
        2: 11,
        3: 14,
        4: 8,
        5: 10
    }

    def test_can_return_1_for_set_one(self):
        self.assertEqual([1], scales(self.set_one, 10))

    def test_can_return_15_for_set_one(self):
        self.assertEqual([1,5], scales(self.set_one, 20))
    
    def test_can_return_145_for_set_one(self):
        self.assertEqual([1,4,5], scales(self.set_one, 28))
