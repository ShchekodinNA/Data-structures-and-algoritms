class Node:
    def __init__(self, value):
        self.value =value
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):                     # see top element
        if self.is_empty():
           return None
        return self.top.value

    def push(self, value):                     # add node to a top
        if self.length == 0:
            self.top = Node(value)
            self.bottom = self.top
            self.length += 1
            return
        self.top.next = Node(value)
        self.top.next.prev = self.top
        self.top = self.top.next
        self.length += 1

    def pop(self):                      # remove from a top
        if self.is_empty():
            return None
        res = self.top
        self.top = self.top.prev
        self.length -= 1
        if stk.length == 0:
            self.bottom = None

    def is_empty(self) -> bool:                 # check if stack is empty
        if self.length < 1:
            return True
        return False


stk = Stack()
print(stk.is_empty())
print(stk.top, stk.bottom)
stk.push(12)
print(stk.top, stk.bottom)
stk.pop()
print(stk.top, stk.bottom)
