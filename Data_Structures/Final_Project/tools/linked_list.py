class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None



class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__len = 0

    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.__len
    
    def __add_first(self, data):
        node = SLLNode(data)
        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node
        self.__len += 1

    def append(self, data) -> None:
        """Add an item to the end of the list"""
        node = SLLNode(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.__len += 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.__len += 1

    def insert(self, data, node=None) -> None:
        """Insert an item after a given node.
        The seconde argument is the element before which to insert,
        so a.insert(x, n) inserts at the front of the list.
        """
        new_node = SLLNode(data)
        if node is None:
            self.__add_first(data)
            return
        temp = node.next
        node.next = new_node
        new_node.next = temp

    def __del_first(self):
        if not self.is_empty():
            self.head = self.head.next
            if self.__len == 1:
                self.tail = self.head
            self.__len -= 1
        
    def remove(self, node: object=None) -> None:
        """
        Remove the first item from the SLL whose value is equal to x (target)
        and if data = None remove first value of SLL.
        """
        if node is None:
            self.__del_first()
            return 
        # previous node of target
        prev = self.search(node, key=lambda x: x.next if x.next is not None else None)
        if prev.next is self.tail:
            self.pop()
            return
        if prev:
            target_ = prev.next 
            prev.next = target_.next
            target_.data = None
            target_.next = None
            del target_
            self.__len -= 1
        else:
            raise  ValueError("SLL.remove(x): x not in SLL")

    def pop(self) -> object | None:
        """Remove and returns the last item in the list."""
        if self.is_empty():
            return None
        #
        res = self.tail.data
        #
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.__len -= 1
            return res
        #
        temp = self.head
        while temp and temp.next is not None:
            if not temp.next.next:
                temp.next = None
                self.tail = temp
                self.__len -= 1
                return res
            else:
                temp = temp.next
    
    def __delitem__(self, node): 
        if node is self.head:
            self.__del_first()
            return None
        if node is self.tail:
            self.pop()
            return None
        for i in self:
            if i.next is node:
                temp = node.next
                i.next = temp
                node.data = None
                node.next = None
                del node
                self.__len -= 1
                return None

    def search(self, target, key=lambda x: x.data): 
        for i in self:
            if key(i) == target:
                return i
            
    def clear(self):
        while self.head:
            self.__del_first()

    def __getitem__(self, index):
        for i, v in enumerate(self):
            if i == index:
                if v is not None:
                    return v
                else:
                    return None
  
    def iter(self, as_data=False):
        node = self.head
        while node:
            if as_data:
                yield node.data
            else:
                yield node
            node = node.next

    def __iter__(self):
        # node = self.head
        # while node:
        #     yield node
        #     node = node.next
        return self.iter(as_data=True)