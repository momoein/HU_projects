from toolbox.array import Array
from toolbox.linked_list import SLL



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

    
    def __iter__(self):
        for item in self.__table:
            if item is not None:
                for node in item:
                    yield node

    def __missing__(self, key): ...

    def __hash_function(self, key):
        return key % self.__table_size