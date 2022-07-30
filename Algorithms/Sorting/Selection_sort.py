numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(array):
    for i in range(len(array)):
        pointer = i
        for j in range(i, len(array)):
            if array[j] < array[pointer]:
                pointer = j
        array[i], array[pointer] = array[pointer], array[i]


selection_sort(numbers)
print(numbers)