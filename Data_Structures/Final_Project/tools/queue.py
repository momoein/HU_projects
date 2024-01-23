class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def is_empty(self):
        return self.len == 0
    
    def __len__(self):
        return self.len

    def enqueue(self, data):
        node = QNode(data)
        if self.front is None:
            self.front = node
            self.rear = node
            self.len += 1
        else:
            self.rear.next = node
            self.rear = self.rear.next
            self.len += 1
    
    def dequeue(self):
        if self.front is not None:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.len -= 1
            return temp.data
