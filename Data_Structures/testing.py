from structure.linked_list import SLL
from tasks.students import *
from tasks.students2 import *
from toolbox.sort import insertion_sort
from toolbox.search import binary_search 
import numpy as np
from time import time

# def test_add_first():
#     sll = SLL()
#     for i in range(10):
#         sll.add_first(i)
#     for i in range(10):
#         assert sll[i] == i, "element %d not found" %i

# test_add_first()


# def division(x,y):
#   assert y!=0, "y cannot be zero"
#   print(x/y)

# try:
#   division(10,0)
# except AssertionError as msg:
#   print(msg)


# students test
# st = Students()
# n = st.create_node(StuNode, 400, "momo")
# print(n)

# # SLL test
# sll = SLL()
# sll.add_first(StuNode, 1, "momo")
# print(sll.tail.name)
# print(sll.tail)
# sll.add_first(StuNode, 2, "mamad")
# print(sll.head.name)
# print(sll.head)
# sll.add_after('stu_code', 3, StuNode, 3, "ali")
# target, prev = sll.search('name', 'ali')
# print(target.name)
# print(prev.name)

# insertion sort test
# A = [np.random.randint(1, 16) for i in range(16)]
# # print(insertion_sort(A))
# A = [0, 1, 2, 3, 4, 5]
# # A = np.random.rand(5)
# print(A)
# print("kk", binary_search(A, 0, len(A), 0))
