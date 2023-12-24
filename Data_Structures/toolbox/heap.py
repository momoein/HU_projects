
def parent(i):
    # (i-1) // k
    return (i-1) // 2

def left(i):
    return 2*i + 1

def right(i):
    # 2*i + k
    return 2*i + 2

def increase_key(array, i, key):
    p = parent(i)
    if key < array[p]:
        array[i] = key
    else:
        array[i] = array[p]
        array[p] = key
    
    while p > 1:
        increase_key(array, p, key)
        p = parent(p)


def max_heapify(array, i):
    l = left(i)
    r = right(i)

    if l < len(array) and array[l] > array[i]:
        big_child = l
    else:
        big_child = i
    
    if r < len(array) and array[r] > array[big_child]:
        big_child = r
    
    if big_child != i:
        # swap
        array[i], array[big_child] = array[big_child], array[i]
        max_heapify(array, big_child)
        
    
def build_heap(array):
    size = len(array)
    for i in range(size//2, -1, -1):
        max_heapify(array, i)


