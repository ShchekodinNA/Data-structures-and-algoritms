class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    def get(self, index:int):
        return self.data[index] if index in self.data else None

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
    def pop(self):
        if self.length == 0:
            return None
        self.length -=1
        buffer = self.data[self.length]
        del self.data[self.length]
        return buffer

    def delete(self, index: int):
        if index >= self.length:
            return
        self.shiftDataLtR(index)
        self.length -=1
        del self.data[self.length]

    def shiftDataLtR(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
arr = Array()

arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)
arr.delete(2)
print(arr.data)