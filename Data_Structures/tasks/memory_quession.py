import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rigth = None

node = Node(10)
data = node.data
node2 = node

node_id = id(node)
data_id = id(data)
print(f"--> node_id: {hex(node_id).upper()}")
print(f"--> data_id: {hex(data_id).upper()}")

del(node)
del(data)
try:
    print(node)
except Exception as err:
    print(f"Error: {err}")

print(ctypes.cast(node_id, ctypes.py_object).value)
print(ctypes.cast(data_id, ctypes.py_object).value)