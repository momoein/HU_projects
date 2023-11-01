class SLLNode:
    def __init__(self, element):
        self.element = element
        self.next = None


class DLLNode(SLLNode):
    def __init__(self, element):
        super().__init__(element)
        self.prev = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    def is_empty(self):
        return self.head is None
    def size(self):
        return self.len
    def first(self):
        if not self.is_empty():
            return self.head
    def show_all(self):
        node = self.head
        print("list elements:", "{", sep="\n")
        while node:
            print("  ", node.element)
            node = node.next
        print("}")
        print(node)
    
    def search(self, element):
        if self.head is None:
            print("Error: list is empty")
            return
        temp = self.head
        while temp.element != element and temp is not None:
            temp = temp.next
        if temp is None:
            print("Error: not found element")
            return
        else:
            return temp


class SLL(LL):
    def add_first(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1

    def del_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.len == 1:
                self.tail = self.head
            self.len -= 1

    def add_last(self, data):
        self.tail.next = SLLNode(data)
        self.tail = self.tail.next
        self.len += 1

    def del_last(self):
        temp = self.head
        while temp.next:
            if not temp.next.next:
                temp.next = None
                self.tail = temp
                self.len -= 1
            else:
                temp = temp.next

    def add_after(self, element, data):
        node = SLLNode(data)
        temp = self.head
        while temp.next:
            if temp.element == element:
                node.next = temp.next
                temp.next = node
                self.len += 1
                if temp == self.tail:
                    self.tail = temp.next
            temp = temp.next
    
    def del_after(self, element):
        temp = self.head
        while temp.next:
            if temp.element == element:
                temp.next = temp.next.next
                self.len -= 1
            if not temp.next:
                self.tail = temp
            temp = temp.next
    
    def __getitem__(self,item):
        n = self.head
        while n is not None and item>0:
            n = n.next
            item -= 1
        if item == 0 and n:
            return n.element
        raise IndexError("index out of range")
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.element
            node = node.next
    