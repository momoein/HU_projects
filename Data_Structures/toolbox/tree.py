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
        papa = root
        while papa is not None:
            if papa.data == key:
                return None
            if papa.data < key:
                papa = papa.right
            elif papa.data > key:
                papa = papa.left
            elif papa.left.data == key or papa.right.data == key:
                return papa

    def min_node(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node
        
    # def delete(self, node):
    #     if node is None:
    #         return "tree is empty"
    #     if node.left is None:
    #         node.data = node.right.data if node.right is not None else None
    #         return self.delete(node.right)
    #     if node.right is None:
    #         node.data = node.left.data if node.left is not None else None
    #         return self.delete(node.left)
    #     if node.left is not None and node.right is not None:
    #         right_smallest = self.min_node(node.right)
    #         node.data = right_smallest.data
    #         return self.delete(right_smallest)


    def _delete(self, parent, child):
        if child.left is not None:
            child = child.left
            return self._delete(parent.right)

    
    # def delete(self, root, key):
    #     parent = self.parent_search(root, key)
    #     if parent is None:
    #         return 
    #     child = self.find_child(parent , key)
    #     count = self.child_count(child)
    #     if count == 0:
    #         child = None
    #     if count == 1:
    #         ...
        


        
    
    def find_child(self, node, key):
        if node.left.data == key:
            return node.left
        elif node.right.data == key:
            return node.right
        else:
            return None
    
    def child_count(self, node):
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count


    
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
                root.height += 1
            else:
                self.insert(root.right, data)
                root.height += 1

        elif data < root.data:
            if root.left is None:
                root.left = self.creat_node(AVLNode ,data)
                root.height += 1
            else:
                self.insert(root.left, data)
                root.height += 1


    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, f"h:{root.height}", end=" , ")
        self.inorder(root.right)
    

    