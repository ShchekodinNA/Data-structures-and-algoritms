numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(array):
    if len(array) == 1:
        return array

    len_half = len(array) // 2

    left = array[:len_half]
    right = array[len_half:]

    return merge(
        merge_sort(left),
        merge_sort(right)
    )


def merge(left, right):
    res = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    res += left[l:]
    res += right[r:]
    return res


answer = merge_sort(numbers)
print(answer)
