#functions/check_brackets.py

from stack import Stack

def check_brackets(expression):
    s1 = Stack()
    s2 = Stack()
    for i in expression:
        if i == '(':
	    s1.push(i)
        elif i == ')':
            s2.push(i)
        else:
            pass
    s1_size = s1.size()
    s2_size = s2.size()
    if s1_size == 0 and s2_size == 0:
        return "No brackets found!"
    elif s1_size == s2_size:
        return "ok"
    elif s1.size > s2.size():
        return "Left brackets more than Right brackets with: {}".format(s1.size() - s2.size())
    elif s1.size() < s2.size():
        return "Right brackets more than Left brackets with: {}".format(s2.size() - s1.size())
    else:
        return "problems!"
