class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):                 # show first
        if self.is_empty():
            return None
        return self.first.value

    def enqueue(self, value):       # add value on top
        if self.is_empty():
            self.first = Node(value)
            self.last = self.first
        else:
            self.last.next = Node(value)
            self.last = self.last.next
        self.length += 1

    def dequeue(self):              # pop value from bottom
        if self.is_empty():
            return
        res = self.first.value
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return res

    def is_empty(self):
        if self.length == 0:
            return True
        return False
qu = Queue()

qu.enqueue("21")
qu.enqueue("32")
print(qu.dequeue())
print(qu.peek())

qu.enqueue("43")
qu.enqueue("54")
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.is_empty())

a = 1
