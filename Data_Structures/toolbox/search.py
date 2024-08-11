def binary_search(array, left, rigth, key):
    m = (left + rigth) // 2
    if m >= 0 and m < len(array):
        if key == array[m]:
            return m
        if key > array[m]:
            return binary_search(array, m+1, rigth, key)
        else:
            return binary_search(array, left, m-1, key)