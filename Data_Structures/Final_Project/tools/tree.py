from tools.queue import Queue


# binary search tree 
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def clear(self):
        self.data = None
        self.left = None
        self.right = None



class BST:
    def __init__(self, insert_key=lambda x: x):
        self.root = None
        self.insert_key = insert_key

    def is_empty(self):
        return not self.root

    def __set_key(self, key): 
        if key is None:
            key = self.insert_key
        return key

    def insert(self, data, key=None):
        node = BSTNode(data)
        if self.is_empty():
            self.root = node
            return None
        #
        key = self.__set_key(key)
        temp = self.root
        while True:
            if key(data) > key(temp.data):
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = node
                    return
            if key(data) < key(temp.data):
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = node
                    return
            if key(data) == key(temp.data):
                return None



    
    def search(self, target, key=None, recursive=False):
        if recursive:
            search_function = self.__search_recursive
        else:
            search_function = self.__search_iterative
        key = self.__set_key(key)
        root = self.root
        node = search_function(root, target, key)
        return node.data
            


    def __search_recursive(self, node, target, key=None):
        if node is None:
            return None
        key = self.__set_key(key)
        if target == key(node.data):
            return node
        if target > key(node.data):
            return self._search_recursive(node.right, target, key)
        else:
            return self._search_recursive(node.left, target, key)


    def __search_iterative(self, node, target, key=None):
        if node is None:
            return
        key = self.__set_key(key)
        while node:
            if key(node.data) == target:
                return node
            if key(node.data) < target:
                node = node.right
            else:
                node = node.left


    def __parent_search(self, root, target, key=None):
        if root is None:
            raise Exception("Tree is empty")
        elif key(root.data) == target:
            raise Exception("root does have parent !!")
        #
        key = self.__set_key(key)
        papa = root
        while papa:
            if papa.left is not None and key(papa.left.data) == target:
                return (papa, "L")
            elif papa.right is not None and key(papa.right.data) == target:
                return (papa, "R")
            elif target > key(papa.data):
                papa = papa.right
            elif target < key(papa.data):
                papa = papa.left
        
        return (papa, None)
        
    
    def delete(self, target, key=None):
        if self.root is None:
            return None
        key = self.__set_key(key)
        #
        if key(self.root.data) == target:
            self.root = self.__succesor(self.root)
            return None
        #
        parent, pointer = self.__parent_search(self.root, target, key)
        if parent is None:
            return None
        if pointer == "L":
            parent.left = self.__succesor(parent.left)
        elif pointer == "R":
            parent.right = self.__succesor(parent.right)


    def __succesor(self, root):
        """return succesor subtree"""
        if root is None:
            return None
        if root.left and root.right:
            succesor = self.__two_child_succesor(root)
        else:
            succesor = self.__one_child_succesor(root)
        return succesor
    
        
    def __one_child_succesor(self, root):
        """return succesor of root if (num_children < 2)"""
        if root.left is None:
            succesor = root.right
        if root.right is None:
            succesor = root.left
        root.clear()
        root = None
        return succesor
    
    
    def __two_child_succesor(self, root):
        """return succesor of root if (num_children == 2)"""
        if root.left and root.right:
            left = root.left
            right = root.right
            root.clear()
            root = None
            if right.left:
                min, par = self.min(right)
                par.left = min.right
                succesor = min
                succesor.left = left
                succesor.right = right
            else:
                succesor = right
                succesor.left = left
            return succesor
    

    def min(self, root):
        """return (parent, root) with minimum value"""
        if root is None:
            return None
        parent = None
        while root.left is not None:
            parent = root
            root = root.left
        return (root, parent)


    def inorder(self, node, func=lambda x: print(x.data, end="  ")):
        if node is None:
            return
        else:
            self.inorder(node.left, func=func)
            func(node)
            self.inorder(node.right, func=func)
    

    def postorder(self, node, func=lambda x: print(x.data, end="  ")):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            func(node)
    

    def preorder(self, node, func=lambda x: print(x.data, end="  ")):
        if node is None:
            return
        else:
            func(node)
            self.preorder(node.left)
            self.preorder(node.right)
    

    def level_order(self, root, func=lambda x: print(x.data, end="  ")):
        if root is None:
            return None
        Q = Queue()
        Q.enqueue(root)
        while Q.len > 0:
            temp = Q.dequeue()
            func(temp)
            if temp.left is not None:
                Q.enqueue(temp.left)
            if temp.right is not None:
                Q.enqueue(temp.right)
        print()
    

    def height(self, node):
        if node is None:
            return -1
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        return max(l_height, r_height) + 1
    
