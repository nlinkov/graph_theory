##!/usr/bin/env python3
  
'''

Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
pop() removes the top item from the stack. It needs no parameters and returns the item.
The stack is modified.
peek() returns the top item from the stack but does not remove it. It needs no parameters.
The stack is not modified.
isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
size() returns the number of items on the stack. It needs no parameters and returns an integer.

Stack Operation	    Stack Contents	     Return Value
s.isEmpty()	        []	                 True
s.push(4)	        [4]
s.push('dog')	    [4,'dog']
s.peek()	        [4,'dog']	         'dog'
s.push(True)	    [4,'dog',True]
s.size()	        [4,'dog',True]	     3
s.isEmpty()	        [4,'dog',True]	     False
s.push(8.4)	        [4,'dog',True,8.4]
s.pop()	            [4,'dog',True]	     8.4
s.pop()	            [4,'dog']	         True
s.size()	        [4,'dog']	         2

'''


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.__getitem__(len(self.stack) - 1)

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

    @property
    def get(self):
        return self.stack

    def __repr__(self):
        return 'Stack({})'.format(self.stack)

    def __getitem__(self, pos):
        return self.stack.__getitem__(pos)

    def __setitem__(self, pos, val):
        return self.stack.__setitem__(pos, val)
