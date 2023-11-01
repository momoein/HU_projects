import numpy as np

class queue:
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