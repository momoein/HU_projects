from structure.queue import queue
import random

lis = [random.randint(0, 9) for i in range(10)]
print('random test data:', lis)
Q = queue(10)
for item in lis:
  Q.enqueue(item)

print('front element:', Q.front_element())
print('is full:', Q.is_full(), '& size:', Q.size())
print('dequeue:', Q.dequeue())
print('front element:', Q.front_element())
print('is full:', Q.is_full(), '& size:', Q.size())