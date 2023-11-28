import numpy as np

class QueueArray:
    def __init__(self, capacity):
        self.array = np.zeros(capacity + 1)
        self.max = self.array.size
        self.front = 0
        self.rear = 0
    def is_empty(self):
        return self.front == self.rear
    def is_full(self):
        return (self.rear + 1) % self.max == self.front
    def size(self):
        return (self.max + self.rear - self.front) % self.max
    def front_element(self):
        return self.array[self.front]
    def enqueue(self, data):
        if self.is_full():
            print('Error: the Queue is full')
        else:
            self.array[self.rear] = data
            self.rear += 1
    def dequeue(self):
        if self.is_empty():
            print('Error: the Queue is empty')
        else:
            self.front += 1
            return self.array[self.front - 1]



class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def del_next(self):
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def is_empty(self):
        return self.len == 0
    
    def size(self):
        return self.len

    def enqueue(self, data):
        node = QNode(data)
        if self.front is None:
            self.front = node
            self.rear = node
            self.len += 1
        else:
            self.rear.next = node
            self.rear = self.rear.next
            self.len += 1
    
    def dequeue(self):
        if self.front is not None:
            temp = self.front
            self.front = self.front.next
            temp.del_next()
            self.len -= 1
            return temp.data
