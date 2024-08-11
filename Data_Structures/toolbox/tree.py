import numpy as np
from toolbox.queue import Queue



class Tree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return not self.root
    
    def creat_node(self, node_type ,data):
        return node_type(data)
    
    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data, end="  ")
            self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
            
    def level_order(self, root):
        Q = Queue()
        Q.enqueue(root)
        while Q.len > 0:
            temp = Q.dequeue()
            print(temp.data, end="  ")
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)



class K_aryNode:
    def __init__(self, data, k):
        self.element = data
        self.child = np.empty(k)
        self.right_siblin = None
        self.parent = None

class BinaryTreeNode:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None



# binary search tree 
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return not self.root


    def insert(self, data):
        node = BSTNode(data)
        if self.is_empty():
            self.root = node
            return
        temp = self.root
        while temp.data != node.data:
            if node.data > temp.data:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = node
                    return
            if node.data < temp.data:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = node
                    return


    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.data, end="  ")
            self.inorder(node.right)


    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)


    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)


    def level_order(self, root):
        Q = Queue()
        Q.enqueue(root)
        while Q.len > 0:
            temp = Q.dequeue()
            print(temp.data, end="  ")
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)


    def height(self, node):
        if node is None:
            return -1
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return max(l_height, r_height) + 1


    def search(self, root, key, recursive=False):
        if recursive:
            return self._search_recursive(root, key)
        else:
            return self._search_iterative(root, key)


    def _search_recursive(self, node, key):
        if node is None:
            return
        if key == node.data:
            return node
        if key > node.data:
            return self._search_recursive(node.right, key)
        else:
            return self._search_recursive(node.left, key)


    def _search_iterative(self, node, key):
        if node is None:
            return
        while node:
            if node.data == key:
                return node
            if node.data < key:
                node = node.right
            else:
                node = node.left


    def parent_search(self, root, key):
        if root is None:
            raise Exception("Tree is empty")
        elif root.data == key:
            raise Exception("root does have parent !!")
        
        papa = root
        while papa:
            if papa.left is not None and papa.left.data == key:
                return (papa, "L")
            elif papa.right is not None and papa.right.data == key:
                return (papa, "R")
            elif key > papa.data:
                papa = papa.right
            elif key < papa.data:
                papa = papa.left

        return (papa, None)
            

    def min_node(self, root):
        if root is None:
            return
        parent = None
        while root.left is not None:
            parent = root
            root = root.left
        return (parent, root)
        
    
    def delete(self, root, key):
        if root.data == key:
            self._delete_root(root)
            return
        parent, pointer = self.parent_search(root, key)

        if parent is None:
            return 
        if pointer == "L":
            parent.left = self.succesor(parent.left)
        elif pointer == "R":
            parent.right = self.succesor(parent.right)
        

    def succesor(self, node):
        if node.left is not None and node.right is not None:
            p, right_min = self.min_node(node.right)
            node.data = right_min.data
            p.left = right_min.right
            return node
        
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left


    def _delete_root(self, root):
        p, nearest_big = self.min_node(root.right)
        root.data = nearest_big.data
        p.left = nearest_big.right
        


# AVL Tree
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0



class AVL(Tree):
    def __init__(self):
        self.root = None


    def insert(self, root, data):
        if self.is_empty():
            self.root = self.creat_node(AVLNode ,data)

        elif data > root.data:
            if root.right is None:
                root.right = self.creat_node(AVLNode ,data)
                root.height = self.live_height(root)
            else:
                self.insert(root.right, data)
                root.height = self.live_height(root)

        elif data < root.data:
            if root.left is None:
                root.left = self.creat_node(AVLNode ,data)
                root.height = self.live_height(root)
            else:
                self.insert(root.left, data)
                root.height = self.live_height(root)
        

    def height(self, root):
        if root is None:
            return -1
        LH = self.height(root.left)
        RH = self.height(root.right)
        return max(LH, RH) + 1

    def live_height(self, root):
        if root is not None:
            if root.left is None:
                LH = -1
            else:
                LH = root.left.height
            if root.right is None:
                RH = -1
            else:
                RH = root.right.height
            return max(LH, RH) + 1


    def get_balance_factor(self, root):
        if root is not None:
            return self.height(root.left) - self.height(root.right)


    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, f"h:{root.height}", end=" , ")
        self.inorder(root.right)
    

    def level_order(self, root):
        Q = Queue()
        Q.enqueue(root)
        while Q.len > 0:
            temp = Q.dequeue()
            print(temp.data, f"h:{temp.height}", end=" , ")
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)
    

    def insert2(self, root, data):
        if self.is_empty():
            self.root = self.creat_node(AVLNode ,data)
            return 
        
        if root is None:
            root = self.creat_node(AVLNode ,data)
            return root
        
        elif data > root.data:
            root.right = self.insert2(root.right, data)
            root.height = self.live_height(root)
            return root
        elif data < root.data:
            root.left = self.insert2(root.left, data)
            root.height = self.live_height(root)
            return root
