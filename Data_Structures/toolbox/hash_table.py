from toolbox.array import Array
from toolbox.linked_list import SLL
import math


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
    


class DynamicHash:
    def __init__(self, size: int=0) -> None:
        self.__arr = Array(size)
        self.__size = size
        self.__useful = 0

    def __h1(self, key):
        """return int(m * (a*key % 1))"""
        a = (math.sqrt(5) - 1) / 2
        m = self.__size
        return int(m * (a*key % 1))
    
    def __h2(self, key, func=None):
        """return an odd number"""
        m = self.__size
        if func is None:
            func = lambda x: int(x % m)
        return 2 * func(key) + 1 
    
    def __get_key_as_integer(self, key): 
        k = 0
        for char in key:
            k += ord(char)
        return k

    def _hash(self, key, i):
        """double hashing
        return (h1 + i*h2) % m
        """
        key = self.__get_key_as_integer(key)
        h1 = self.__h1(key)
        h2 = self.__h2(key)
        m = self.__size
        return (h1 + i*h2) % m 

    def __is_ft(self):
        """return True if n/m >= FT
        FT: Full_Threshold = 0.75
        """
        n = self.__useful
        m = self.__size
        return n/m >= 0.75
    
    def __is_et(self):
        """return True if n/m <= EF
        ET: Empty_Threshold = 0.25
        """
        n = self.__useful
        m = self.__size
        return n/m <= 0.25

    def __is_deleted(self, index):
        """return True if table[i] == 'deleted' """
        return self.__arr[index] == "deleted" 

    def search(self, key): 
        m = self.__size
        arr = self.__arr
        index = ...
        #
        for i in range(m):
            index = self._hash(key, i)
            item = arr[index]
            if item and item != "deleted":
                if item.key == key:
                    return index
        #
        return None

    def insert(self, key, value): ...

    def update(self, key): ...

    def delete(self): ...

    def __setitem__(self, key, value): 
        m = self.__size
        arr = self.__arr
        index = ...
        for i in range(m):
            index = self._hash(key, i)
            if arr[index] == None or self.__is_deleted(index):
                arr[index] = HashNode(key, value)
                return None
        print(f"not found any place for key: {key}")
        # raise OverflowError("DynamicHash overflow")
    
    def __getitem__(self, key):
        index = self.search(key)
        if index:
            item = self.__arr[index]
            return item.value
        raise KeyError(key)

    def __delitem__(self, key): 
        
        ...

    # def __contains__(self, item): ...

    def __iter__(self): 
        for item in self.__arr:
            if item and item != "deleted":
                yield item.key

    # def __missing__(self, key): ...