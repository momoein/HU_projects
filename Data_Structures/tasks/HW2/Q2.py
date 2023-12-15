class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class Tree:
    def __init__(self):
        self.root = None

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
            print(node.data, end="  ")
            self.preorder(node.left)
            self.preorder(node.right)



def construct_bt(pre, ino, root):
    if len(ino) != len(pre):
        print('Error ino and pre is not match')
        return 
    
    if len(ino) == 0:
        return
    
    l_ino, l_pre, r_ino, r_pre = split_tree(pre, ino)

    root = BTNode(pre[0])
    root.left = construct_bt(l_pre, l_ino, root.left)
    root.right = construct_bt(r_pre, r_ino, root.right)

    return root



def split_tree(pre, ino):
    l_ino, l_pre, r_ino, r_pre = None, None, None, None
    iri = None # in-order root index

    for i in range(len(ino)):
        if ino[i] == pre[0]:
            iri = ino[i-1]
            l_ino = ino[:i]
            r_ino = ino[i+1:]
            break

    for i in range(len(pre)):
        if iri == pre[i]:
            r_pre = pre[i+1:]
            l_pre = pre[1:i+1]
            break

    return (l_ino, l_pre, r_ino, r_pre)
    
    


if __name__ == '__main__':   
    pre = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
    ino = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]

    t = Tree()
    t.root = construct_bt(pre, ino, t.root)
    
    t.preorder(t.root)
    print()
    t.inorder(t.root)