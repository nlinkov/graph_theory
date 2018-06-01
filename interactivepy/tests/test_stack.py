#test_stack.py

import unittest
from stack import Stack

#stack.testing = True

class Test_stack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_isEmpty(self):
        self.assertEqual(True, self.stack.isEmpty())
        self.assertEqual('Stack([])', self.stack.__repr__())
