test = ["A", "B", 'C', 'D']
# 4*4 = 16 "Shelves" of data in RAM



test.append("E") # O(1)

test.pop()
test.pop() #O(1)


test.insert(0,"X") #O(N)



test.insert(3,"F") #O(N)



print(test)
