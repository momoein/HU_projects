import math

def parent(i):
    # (i-1) // k
    return (i-1) // 2

def left(i):
    return 2*i + 1

def right(i):
    # 2*i + k
    return 2*i + 2


def increase_key(array, i, key):
    if array[i] > key:
        print("Error: new key is smaller than the current key")
        return
    
    array[i] = key
    while i > 0:
        if array[i] > array[parent(i)]:
            # swap
            array[i], array[parent(i)] = array[parent(i)], array[i]
            i = parent(i)


def max_heapify(array, size, i):
    l = left(i)
    r = right(i)
    largest = i

    if l < size and array[l] > array[i]:
        largest = l
    
    if r < size and array[r] > array[largest]:
        largest = r
    
    if largest != i:
        # swap
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, size, largest)
        
    
def build_heap(array):
    size = len(array)
    for i in range(size//2, -1, -1):
        max_heapify(array, size, i)


class MaxHeap:
    def __init__(self, array=[]):
        self.array = array

    def insert(self, key):
        self.array.append(-math.inf)
        i = len(self.array) - 1
        increase_key(self.array, i, key)

    def delete(self):
        self.array[0] = self.array[-1]
        self.array.pop(-1)
        self.heapify(0)

    def build(self):
        build_heap(self.array)
    
    def heapify(self, i):
        max_heapify(self.array, len(self.array), i)

    def show(self):
        print(self.array)
