def shell_sort(array):
    array_len = len(array)
    interval = array_len // 2

    while interval > 0:
        for i in range(interval, array_len):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

    return array
