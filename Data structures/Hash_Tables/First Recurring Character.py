# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

# Bonus... What if we had this:
# [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2

t_undef = 'undefined'


def first_recurring_character(lst: list):   # O(n)
    htbl = {}
    for i in range(len(lst)):
        if lst[i] in htbl:
            return lst[i]
        htbl[lst[i]] = True
    return t_undef


print(first_recurring_character([2]))
