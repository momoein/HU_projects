class SNode:
    def __init__(self):
        self.next = None

    def del_next(self):
        self.next = None


class DNode:
    def __init__(self):
        self.prev = None
        self.next = None
    
    def del_prev(self):
        self.prev = None
    def del_next(self):
        self.next = None
    def del_pointers(self):
        self.prev = None
        self.next = None


class SLLNode(SNode):
    def __init__(self, element):
        super().__init__(self, element)
        self.element = element


class DLLNode(DNode):
    def __init__(self, element):
        super().__init__(self, element)
        self.element = element


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
    
    def search(self, attrname, value):
        if self.is_empty():
            print("Error: list is empty")
            return
        target = self.head
        while target is not None and getattr(target, attrname) != value:
            target = target.next
        if target is None:
            print(f"not found node with {attrname} == {value}")
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

    def add_after(self, attrname, srch_value, NodeType, *parametr):
        node = self.create_node(NodeType, *parametr)
        target, _ = self.search(attrname, srch_value)
        if target is not None and target.next is not None:
            node.next = target.next
            target.next = node
            self.len += 1
        elif target is not None and target.next is None:
            target.next = node
            self.tail = node
            self.len += 1
        else:
            mtd_name = self.add_after.__name__
            print(f"{mtd_name}() not found node with {attrname} == {srch_value}")

    def del_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.len == 1:
                self.tail = self.head
            self.len -= 1

    def del_last(self):
        if self.is_empty():
            print(f"Error {self.del_last.__name__}: list is empty")
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
    
    def delete(self, attrname, srch_value):
        target, previous = self.search(attrname, srch_value)
        if target is None and previous is None:
            print(f"Error {self.delete.__name__}(): list is empty")
        elif target is None and previous is not None:
            print(f"Error {self.delete.__name__}(): {srch_value} not found")
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

    def search(self, attrname, value):
        if self.head is None:
            print("Error: list is empty")
            return (None, None)
        target = self.head
        previous = None
        while target is not None and getattr(target, attrname) != value:
            previous = target
            target = target.next
        if target is None:
            print(f"Error: not found {value}")
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
        temp = self.head
        self.head = self.head.next
        self.head.del_prev()
        temp.del_pointers()

    def del_last(self):
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.del_next()
        temp.del_pointers()

    def del_this(self, node):
        if node == self.head:
            self.del_last()
            self.len -= 1
        if node == self.tail:
            self.del_last()
            self.len -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.len -= 1