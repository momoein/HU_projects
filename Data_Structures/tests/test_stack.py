import sys
sys.path.append("..") # package location --> root to package parent directory 
from package.stack import stack
import random

s = stack(8)
lis = [random.randint(0, 9) for i in range(10)]
print('random test data:', lis)
for item in lis:
  s.push(item)
s.pick()
s.pop()
s.pick()
print(s.array)