# recursive
def find_factorial_recursive(value):
    if value <= 2:
        return value
    res = find_factorial_iterative(value - 1) * value
    return res


# Iterative
def find_factorial_iterative(value):
    res = 1
    for i in range(2, value + 1):
        res *= i
    return res


for_find = 1
print(find_factorial_iterative(for_find))
print(find_factorial_recursive(for_find))
