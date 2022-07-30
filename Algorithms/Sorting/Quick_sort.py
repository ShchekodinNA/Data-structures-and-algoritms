numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def quick_sort(array):
    if len(array) <= 1:
        return array
    med_point = len(array) // 2
    array[med_point], array[-1] = array[-1], array[med_point]
    pivot = len(array)-1
    point = 0
    while point <= pivot:
        if array[point] > array[pivot]:
            array[pivot], array[pivot-1] = array[pivot-1], array[pivot]
            if pivot > 0 :
                array[pivot], array[point] = array[point], array[pivot]
            pivot -=1
        else:
            point += 1
    return quick_sort(array[:pivot]) + [array[pivot]] + quick_sort(array[pivot+1:])




print(quick_sort(numbers))
