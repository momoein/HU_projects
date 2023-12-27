from toolbox.heap import max_heapify, build_heap
from random import randint

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

def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    # split array
    m = n // 2
    L = array[:m]
    R = array[m:]
    # sort and merge
    L_sorted = merge_sort(L)
    R_sorted = merge_sort(R)
    return merge(L_sorted, R_sorted)


def merge(L, R):
    n, m = len(L), len(R)
    i, j = 0, 0
    array = [None for i in range(n+m)]
    for k in range(0, n+m):
        # handle the last index
        if i == n:
            i_value = R[j] + 1
        else:
            i_value = L[i]
        if j == m:
            j_value = L[i] + 1
        else:
            j_value = R[j]
        # comparison two the least element of arrays
        if i_value <= j_value:
            array[k] = i_value
            i += 1
        if i_value > j_value:
            array[k] = j_value
            j += 1
    return array


def heap_sort(array, k=None):
    size = len(array) - 1
    if k is None:
        k = size

    build_heap(array)
    while size > 0 and k > 0:
        array[0], array[size] = array[size], array[0]
        max_heapify(array, size, 0)
        size -= 1
        k -= 1
    return array



def count_sort(array, max):
    a, m = array, max
    c = [0 for i in range(m+1)] 
    b = [0 for i in range(len(array) + 1)]

    for i in range(len(a)):
        c[a[i]] += 1
    
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for i in range(len(a)-1, -1, -1):
        b[c[a[i]]] = a[i]
        c[a[i]] -= 1

    return b[1:]



def radix_sort(array, digits):
    d = digits
    for i in range(1, d+1):
        array = count_sort_by_digit(array, 9, i)
    return array


def count_sort_by_digit(array, max, digit):
    a, m = array, max
    c = [0 for i in range(m+1)] 
    b = [0 for i in range(len(array) + 1)]
    
    for i in range(len(a)):
        c[which_digit(a[i], digit)] += 1
    
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for i in range(len(a)-1, -1, -1):
        b[c[which_digit(a[i], digit)]] = a[i]
        c[which_digit(a[i], digit)] -= 1

    return b[1:]


def which_digit(integer, digit):
    base =  10 ** (digit)
    integer %= base
    base /= 10
    return int(integer // base)



def partition(array, low, high):
    # randomized partition
    i = randint(low, high)
    array[i], array[high] = array[high], array[i]
    
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)