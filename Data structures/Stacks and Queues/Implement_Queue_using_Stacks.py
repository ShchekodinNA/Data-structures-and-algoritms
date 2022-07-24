class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.sec_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.main_stack)):
            self.sec_stack.append(self.main_stack.pop())
        res = self.sec_stack.pop()

        for i in range(len(self.sec_stack)):
            self.main_stack.append(self.sec_stack.pop())

        return res

    def peek(self) -> int:
        for i in range(len(self.main_stack)):
            self.sec_stack.append(self.main_stack.pop())
        res = self.sec_stack[-1]

        for i in range(len(self.sec_stack)):
            self.main_stack.append(self.sec_stack.pop())

        return res

    def empty(self) -> bool:
        return True if len(self.main_stack) == 0 else False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
