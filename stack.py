"""
Stack Data Structure
A
B
C
D
E
"""
#A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
#In stack, a new element is added at one end and an element is removed from that end only. 
#The insert and delete operations are often called push and pop



class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items()
a = Stack()
a.push("G")
a.push("I")
a.push("T")
a.push("H")
a.push("U")
a.push("B")
