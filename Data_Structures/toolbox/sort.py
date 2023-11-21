
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


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in  range(i, n):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    return array

# def merge_sort(array): # it have bug
#     n = len(array)
#     if n == 1:
#         return array
#     m = n // 2
#     L = array[:m]
#     R = array[m:]

#     merge_sort(L)
#     merge_sort(R)
#     merge(L, R)

# def merge(L, R):
#     n, m = len(L), len(R)
#     i, j = 0, 0
#     array = [None for i in range(n+m)]
#     for k in range(0, n+m):
#         if i == n:
#             i_value = R[j] + 1
#         else:
#             i_value = L[i]
#         if j == m:
#             j_value = L[i] + 1
#         else:
#             j_value = R[j]

#         if i_value <= j_value:
#             array[k] = i_value
#             i += 1
#         if i_value > j_value:
#             array[k] = j_value
#             j += 1
#     return array