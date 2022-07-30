# Implement a function that reverses a string using iteration...and then recursion!
def reverse_string_iteration(line):
    resar = []
    for i in range(len(line)):
        resar.insert(0, line[i])
    return ''.join(resar)


def reverse_string_recursion(line):
    if len(line) < 2:
        return line
    return reverse_string_recursion(line[1::]) + line[0]

line_to_reverse =  'yoyo mastery'
print(reverse_string_iteration(line_to_reverse))
print(reverse_string_recursion(line_to_reverse))
# should return: 'yretsam oyoy'
