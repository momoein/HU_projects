class SLLNode:
    def __init__(self, element):
        self.element = element
        self.next = None



class DLLNode:
    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None



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
        
    def create_node(self, NodeType, *parametr):
        return NodeType(*parametr)

    def show_all(self):
        node = self.head
        print("list elements:", "{", sep="\n")
        while node:
            print("  ", node.element)
            node = node.next
        print("}")
    
    def search(self, element):
        if self.is_empty():
            print("Error: list is empty")
            return
        target = self.head
        while target is not None and target.element != element:
            target = target.next
        if target is None:
            print("Error: not found element")
            return
        else:
            return target
        
    def traverse(self):
        if self.is_empty():
            return
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next



class SLL(LL):
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

    def add_after(self, element, data):
        node = SLLNode(data)
        target, _ = self.search(element)
        if target is not None and target.next is not None:
            node.next = target.next
            target.next = node
            self.len += 1
        elif target is not None and target.next is None:
            target.next = node
            self.tail = node
            self.len += 1
        else:
            print(f"Error: not found element {element}")

    def del_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.len == 1:
                self.tail = self.head
            self.len -= 1

    def del_last(self):
        if self.is_empty():
            print(f"Error {__name__}: list is empty")
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.len -= 1
            return
        temp = self.head
        while temp and temp.next is not None:
            if not temp.next.next:
                temp.next = None
                self.tail = temp
                self.len -= 1
            else:
                temp = temp.next
    
    def delete(self, element):
        target, previous = self.search(element)
        if target is None and previous is None:
            print(f"Error: list {__name__} is empty")
        elif target is None and previous is not None:
            print(f"Error: element {element} not found")
        elif target is not None and previous is None:
            self.head = target.next
            target.next = None
            if target is self.tail:
                self.tail = None
            self.len -= 1
        else:
            previous.next = target.next
            target.next = None
            self.len -= 1

    def search(self, element):
        if self.head is None:
            print("Error: list is empty")
            return (None, None)
        target = self.head
        previous = None
        while target is not None and target.element != element:
            previous = target
            target = target.next
        if target is None:
            print("Error: not found element")
            return (target, previous)
        else:
            return (target, previous)

    def __getitem__(self, item):
        n = self.head
        while n is not None and item > 0:
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
    


class DLL(LL):
    def add_first(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.len += 1
    
    def add_last(self, data):
        node = DLLNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.len += 1

    def del_first(self):
        pass

    def del_last(self):
        pass

    def del_this(self, node):
        if node == self.head:
            del_first()
            self.len -= 1
        if node == self.tail:
            del_last()
            self.len -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.len -= 1