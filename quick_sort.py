def partition(array, start, end):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(array, start, end):
    if start < end:
        p = partition(array, start, end)

        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)
