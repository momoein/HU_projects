

class Array:
    def __init__(self, size: int=0, object=None):
        self.__array = [object] * abs(size)
        self.__len = abs(size)
        
    def get(self):
        return self.__array 
    
    def __setitem__(self, index, data):
        self.__array[index] = data

    def __getitem__(self, index):
        return self.__array[index]
    
    def __len__(self):
        return self.__len
    
    def __repr__(self) -> str:
        return repr(self.__array)
    
    def clear(self):
        self.__array = [None for i in range(self.__len)]

    def reverse(self):
        i = 0
        j = self.__len - 1
        while True:
            if i != j:
                self.__array[i], self.__array[j] = (
                    self.__array[j], self.__array[i]
                )
            if i > j:
                return
            i += 1
            j -= 1

    def __iter__(self):
        for i in self.__array:
            yield i

    def __contains__(self, key):
        for i in self.__array:
            if i == key:
                return True
        return False




class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def del_pointers(self):
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

    def __getitem__(self, index):
        for i, v in enumerate(self):
            if i == index:
                if v is not None:
                    return v
                else:
                    return None
  
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



class HashNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class OpenHashTable:
    """Closed Addressing: chaining"""
    def __init__(self, size: int=10) -> None:
        self.__table = Array(size)
        self.__table_size = size

    def __creat_sll(self, index):
        if self.__table[index] == None:
            self.__table[index] = SLL()
 
    def __setitem__(self, key, value):
        index = self.__hash_function(key)
        self.__creat_sll(index)
        sll = self.__table[index]
        sll.insert(HashNode(key, value))
    
    def __getitem__(self, key):
        index = self.__hash_function(key)
        if self.__table[index] is not None:
            sll = self.__table[index]
            for i in sll:
                if i.data is not None and i.data.key == key:
                    return i.data.value

    def __delitem__(self, key): 
        index = self.__hash_function(key)
        sll = self.__table[index]
        for i in sll:
            if i.data is not None and i.data.key == key:
                del sll[i]

    def __contains__(self, key):
        index = self.__hash_function(key)
        sll = self.__table[index]
        for i in sll:
            if i.data.key == key:
                return True
        return False

    def update(self, key, value):
        self.__setitem__(key, value)
    
    def __iter__(self):
        for item in self.__table:
            if item is not None:
                for node in item:
                    yield node.data.key

    def __missing__(self, key): ...

    def __hash_function(self, key):
        str_key = str(key)
        key = ord(str_key[0]) + ord(str_key[-1]) + ord(str_key[len(str_key)//2])
        return key % self.__table_size