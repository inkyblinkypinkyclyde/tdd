from re import template
import unittest

from src.template import *

class TestTemplate(unittest.TestCase):
    
    def test_can_return_string(self):
        self.assertEqual("string", return_complete("string"))