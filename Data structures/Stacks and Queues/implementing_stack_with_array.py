class Stack:
    def __init__(self):
        self.data = []

    def peek(self):                     # see top element
        if self.is_empty():
           return None
        return self.data[-1]

    def push(self, value):                     # add node to a top
        self.data.append(value)

    def pop(self):                      # remove from a top
        if self.is_empty():
            return None
        return self.data.pop()

    def is_empty(self) -> bool:                 # check if stack is empty
        if not self.data:
            return True
        return False


stk = Stack()

print(stk.is_empty())
stk.push("21")
stk.push("24")
print(stk.is_empty())
print(stk.peek())
print(stk.pop())
print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.is_empty())

