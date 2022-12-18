"""
18.	The following functions are necessary to handle the stack: 
push(), pop() and empty(). Below is a simple implementation of 
the stack using a Python list. Note the definition of the listed functions. 
What action do these functions perform? Copy and paste the 
program code below into a module named stack.py.


19.	Write a program, in which, import the module stack.py. Then do the following:
a.	Display stack
b.	Put the number 2 on the stack
c.	Put the number 14 on the stack
d.	Put the number 9 on the stack
e.	Display stack
f.	Get element from stack
g.	Display stack
h.	Put the number 31 on the stack
i.	Put the number 6 on the stack
j.	Display stack
k.	Get two elements from stack
l.	Display stack

"""

import stack 

stack.push(2)

stack.push(14)

stack.push(9)

stack.display()

stack.pop()

stack.display()

stack.push(31)

stack.push(6)

stack.display()

stack.pop()
stack.pop()

stack.display()
