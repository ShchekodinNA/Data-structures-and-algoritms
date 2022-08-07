def memoization_adding_50():
    cache = {}

    def intfunc(n):  # Closures
        if n in cache:
            return cache[n]
        else:
            cache[n] = 50 + n
            print("long time")
            return cache[n]

    return intfunc


memoized = memoization_adding_50()

memoized(5)

print(memoized(5))
print(memoized(10))
print(memoized(5))
print(memoized(5))
print(memoized(15))
print(memoized(10))
print(memoized(5))
