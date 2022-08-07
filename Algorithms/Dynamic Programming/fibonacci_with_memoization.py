import time
calculations = 0


def fibonacci(val:int):
    global calculations
    calculations += 1
    if val < 2:
        return val
    return fibonacci(val-1) + fibonacci(val-2)


def fibonacci_with_memoization(val:int):
    cache = {}
    def internal_fib(val:int):
        global calculations
        calculations += 1
        if val not in cache:
            if val < 2:
                return val
            cache[val] = internal_fib(val-1) + internal_fib(val-2)
        return cache[val]

    return internal_fib(val)

seek_value = 35

start = time.time()
print(fibonacci(seek_value))
result = time.time() - start
print(f"{result} sec without dynamic programming")
print(calculations)

calculations = 0
start = time.time()
print(fibonacci_with_memoization(seek_value))
result = time.time() - start
print(f"{result} sec with dynamic programming")
print(calculations)

