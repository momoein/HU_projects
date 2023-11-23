import numpy as np

class stack:
  def __init__(self, size):
    self.size = size
    self.array = np.zeros(size)
    self.top = -1
  def pick(self):
    print('Top of stack:', self.array[self.top])
  def push(self, data):
    if self.top < self.size - 1:
      self.top += 1
      self.array[self.top] = data
    else:
      print("Error: stack is full")
  def pop(self):
    if self.top > -1:
      self.top -= 1
      self.array[self.top]