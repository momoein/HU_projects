import numpy as np

class Kary_Node:
    def __init__(self, data, k):
        self.element = data
        self.child = np.empty(k)
        self.right_siblin = None
        self.parent = None

class Binary_Tree_Node:
    def __init__(self, data):
        self.element = data
        self.parent = None
        self.l_child = None
        self.r_child = None

class Binary_Tree:
    def __init__(self):
        self.root = None

