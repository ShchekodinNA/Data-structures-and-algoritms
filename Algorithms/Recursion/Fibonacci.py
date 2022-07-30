

def fibonacci_recursive(val):
    if val < 2:
        return val
    return fibonacci_recursive(val-1) + fibonacci_iterative(val-2)


def fibonacci_iterative(val):
    if val <= 0:
        return 0
    first = 1
    second = 0
    for i in range(val-1):
        buf = first
        first = first + second
        second = buf
    return first


fib = 5
print(fibonacci_iterative(fib))
print(fibonacci_recursive(fib))