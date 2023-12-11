import numpy as np


class MaxHeap:
    def __init__(self, size):
        self.A = np.zeros(size)
        self.useful = 0


    def parent(self, i):
        return i // 2
    
    def left_child(self, i):
        return 2*i
    
    def right_child(self, i):
        return 2*i
    
    def increase_key(self, i, key):
        if self.A[i] > key:
            print("Error: key smaller then the current key")
            return
        self.A[i] = key
        while i > 1 and self.A[i] > key:
            temp = self.A[self.parent(i)]
            self.A[self.parent(i)] = self.A[i]
            self.A[self.parent(i)] = temp
            i = self.parent(i)





print("--->" ,np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# A = np.zeros(10)
A = np.array([0, 3, 6, 1, 9, 7, 18, 9, 18, 5, 8])
print("run0", A)

def max_heapify(array, i):
    left = 2*i
    right = 2*i + 1
    bigchild = 0

    if left < len(array) and array[left] > array[i]:
        bigchild = left
    else:
        bigchild = i

    if right < len(array) and array[right] > array[i]:
        bigchild = right

    if i != bigchild:
        temp = array[i]
        array[i] = array[bigchild]
        array[bigchild] = temp
        max_heapify(array, bigchild)


max_heapify(A, 5)
print("run5", A)
max_heapify(A, 4)
print("run4", A)
max_heapify(A, 3)
print("run3", A)
max_heapify(A, 2)
print("run2", A)
max_heapify(A, 1)
print("run1", A)


# # def build_heap(array):
# #     n = len(array) - 1
# #     for i in range(n, n//2, -1):
# #         heapify(array, i)


