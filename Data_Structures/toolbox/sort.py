def insertion_sort(array):
    n = len(array)
    key = array[1]
    for k in range(1, n):
        i = k
        key = array[i]
        while i > 0 and key < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = key
    return array