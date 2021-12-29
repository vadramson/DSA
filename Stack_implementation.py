# Implementation of Stacks in python using Deque from collections

from collections import deque


#stack = deque()
#print(stack)
# print(dir(stack)) # see all the methods that are applicable to 

class Stack():
    def __init__(self):
        self.container = deque()
        
    def push(self, data):
        return self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
    
    def length(self):
        return len(self.container)
        
    def reverse_string(self, string):
        self.container.clear()
        self.container = string.split()
        return " ".join(self.container[::-1])


if __name__ == '__main__':
    s = Stack()
    print(f"Is Stack Empty?: {s.is_empty()}")
    s.push(5)
    s.push(3)
    s.push(6)
    print(f"The element popped from the Stack was {s.pop()} ")
    print(f"The length of Stack is {s.length()}" )
    print(f"Peek of Stack is {s.length()}" )
    print(s.reverse_string("Is the Stack Empty?"))
    
    
