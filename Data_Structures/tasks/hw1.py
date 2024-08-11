import numpy as np

# Question 1
class SLLNode:
    def __init__(self, element):
        self.element = element
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.len
        
    def create_node(self, NodeType, *parametr):
        return NodeType(*parametr)

    def add_first(self, NodeType, *parametr):
        node = self.create_node(NodeType, *parametr)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1

    def add_last(self, NodeType, *parametr):
        node = self.create_node(NodeType, *parametr)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.len += 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.len += 1


def question_1():
    sll = SLL()
    sll.add_last(SLLNode, 1)
    sll.add_last(SLLNode, 2)
    sll.add_last(SLLNode, 3)
    sll.add_last(SLLNode, 4)
    sll.add_last(SLLNode, 5)
    sll.add_last(SLLNode, 6)

    # create loop in linked list
    sll.tail.next = sll.head.next.next.next
    print(sll.tail.next.element)
    
    def is_have_loop(head):
        slow = head
        fast = head
        while True:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return False
            if slow == fast:
                return True
            
    print(is_have_loop(sll.head))

# test question 
question_1()

# Question 10
def solve8queens(board, col=0):
    if col == 8:
        print('The solution:')
        print(board)
        return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve8queens(board, col+1):
                return True
            board[i][col] = 0
    return False

def is_safe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

# test Question 2
def question_2():
    board = np.zeros((8, 8), dtype=int)
    solve8queens(board)

question_2()