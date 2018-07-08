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
    def test_the_stack(self):
        self.assertEqual(None, self.stack.push(4))
        self.assertEqual('Stack([4])', self.stack.__repr__())
        self.assertEqual(None, self.stack.push('dog'))
        self.assertEqual("Stack([4, 'dog'])", self.stack.__repr__())
        self.assertEqual('dog', self.stack.peek())
        self.assertEqual("Stack([4, 'dog'])", self.stack.__repr__())
        self.assertEqual(None, self.stack.push(True))
        self.assertEqual("Stack([4, 'dog', True])", self.stack.__repr__())
        self.assertEqual(3, self.stack.size())
        self.assertEqual("Stack([4, 'dog', True])", self.stack.__repr__())
        self.assertEqual(False, self.stack.isEmpty())
        self.assertEqual("Stack([4, 'dog', True])", self.stack.__repr__())
        self.assertEqual(None, self.stack.push(8.4))
        self.assertEqual("Stack([4, 'dog', True, 8.4])", self.stack.__repr__())
        self.assertEqual(8.4, self.stack.pop())
        self.assertEqual("Stack([4, 'dog', True])", self.stack.__repr__())
        self.assertEqual(True, self.stack.pop())
        self.assertEqual("Stack([4, 'dog'])", self.stack.__repr__())
