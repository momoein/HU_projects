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

def bubble_sort(array):
    for i in range(len(array)):
        j = 0
        while j+1 < len(array):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
            j += 1
    return array
