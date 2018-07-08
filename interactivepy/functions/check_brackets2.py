#functions/check_brackets.py

from stack import Stack

def check_brackets(expression):
    if len(expression) == 0:
        return "No brackets found!"
    s = Stack()
    atleastone = 0
    for i in expression:
        if i == '(':
            atleastone = 1
	    s.push(i)
        elif i == ')':
            if s.size() > 0:
               s.pop()
            else:
               atleastone -= 1
        else:
            pass
    if s.size() == 0 and atleastone == 1:
        return "ok"
    elif s.size > 0:
        return "Left brackets more than Right brackets with: {}".format(s.size())
    elif s.size() == 0 and atleastone < 0:
        return "Right brackets more than Left brackets with: {}".format(-atleastone)
    else:
        return "problems!"
