numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            buf = array.pop(i)
            for j in range(i - 1, -1, -1):
                if j == 0 or buf >= array[j - 1]:
                    array.insert(j, buf)
                    break


insertion_sort(numbers)
print(numbers)
