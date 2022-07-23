arr1 = [0, 3, 4, 31]
arr2 = [4, 6, 30]


def merge_arrays(lst1: list, lst2: list) -> list:
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1

    st1, st2 = 0, 0
    result = []

    while len(lst1) > st1 and len(lst2) > st2:
        if lst1[st1] > lst2[st2]:
            result.append(lst2[st2])
            st2 += 1
        else:
            result.append(lst1[st1])
            st1 += 1

    while len(lst1) > st1:
        result.append(lst1[st1])
        st1 += 1
    while len(lst2) > st2:
        result.append(lst2[st2])
        st2 += 1

    return result


print(merge_arrays(arr1, arr2))
