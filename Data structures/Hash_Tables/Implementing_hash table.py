#implementation for understanding
class HshTbl:
    def __init__(self, size):
        self.data = [[]]*size

    def __hash(self, key) -> int:
        hsh = 0
        for i in range(len(key)):
            hsh = (hsh + ord(key[i]) * i) % len(self.data)
        return hsh

    def set(self, key, value) -> None:
        address = self.__hash(key)
        self.data[address] = self.data[address] + [[key, value]]
        return self.data


    def get(self, key):
        address = self.__hash(key)
        for i in range(len(self.data[address])):
            if self.data[address][i][0] == key:
                return self.data[address][i][1]
        return None

    def keys(self):
        ex_array = []
        for backet_pool in self.data:
            if backet_pool:
                for cur_backet in backet_pool:
                    ex_array.append(cur_backet[0])
        return ex_array



htbl = HshTbl(10)

htbl.set("some", 552)
htbl.set("value", 15)
htbl.set("test", "aboba")
htbl.set("planes", 2000)

print(htbl.keys())