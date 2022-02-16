def selection_sort(array):
    for i in range(len(array) - 1):
        min_number_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_number_index]:
                min_number_index = j
        array[i], array[min_number_index] = array[min_number_index], array[i]

    return array
