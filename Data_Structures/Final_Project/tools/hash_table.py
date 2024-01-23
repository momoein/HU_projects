from tools.array import Array
from tools.linked_list import SLL
import math


class HashNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class DynamicHash:
    def __init__(self) -> None:
        self.__arr = Array()
        self.__size = 0
        self.__useful = 0
    ...

    def __h1(self, key):
        """return int(m * (a*key % 1))"""
        a = (math.sqrt(5) - 1) / 2
        m = self.__size
        return int(m * (a*key % 1))
    
    def __h2(self, key):
        """return an odd number"""
        m = self.__size
        return 2 * int(key % m) + 1 
    
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

    def __expand(self): 
        m = self.__size
        if m == 0:
            self.__arr = Array(1)
            self.__size = 1
            return None
        #
        if self.__is_ft():
            sll = SLL()
            for i in range(m):
                item = self.__arr[i]
                if item and item != "deleted":
                    sll.append(item)
            #
            m *= 2
            self.__arr = Array(m)
            self.__size = m
            self.__useful = 0
            for node in sll:
                key = node.data.key
                value = node.data.value
                self[key] = value
            # print("len", len(sll), "size", len(self.__arr))
            sll.clear()
    ...
 
    def __compress(self): 
        m = self.__size
        if m == 0:
            return None
        #
        if self.__is_et():
            sll = SLL()
            for i in range(m):
                item = self.__arr[i]
                if item and item != "deleted":
                    sll.append(item)
            #
            m //= 2
            self.__arr = Array(m)
            self.__size = m
            self.__useful = 0
            for node in sll:
                key = node.data.key
                value = node.data.value
                self[key] = value
            # print("len", len(sll), "size", len(self.__arr))
            sll.clear()
    ...

    def __search(self, key): 
        """return index of the key if find it"""
        m = self.__size
        arr = self.__arr
        index = 0
        #
        for i in range(m):
            index = self._hash(key, i)
            item = arr[index]
            if item and item != "deleted":
                if item.key == key:
                    return index
        return None
    ...

    def insert(self, key, value): 
        self.__expand()
        m = self.__size
        arr = self.__arr
        index = 0
        #
        for i in range(m):
            index = self._hash(key, i)
            if arr[index] == None or arr[index] == "deleted":
                arr[index] = HashNode(key, value)
                self.__useful += 1
                return None
        # print(f"not found any place for key: {key}")
        raise OverflowError("DynamicHash overflow")
    ...

    def update(self, key, value): 
        index = self.__search(key)
        if index is not None:
            item = self.__arr[index]
            item.value = value
    ...

    def delete(self, key): 
        self.__compress()
        index = self.__search(key)
        if index is not None:
            self.__arr[index] = "deleted"
            self.__useful -= 1
    ...

    def get(self, key):
        index = self.__search(key)
        if index is not None:
            item = self.__arr[index]
            return item.value
        raise KeyError(key)
    ...

    def clear(self):
        for i in self:
            self.delete(i)
        self.__init__()
    ...

    def __setitem__(self, key, value): 
        self.insert(key=key, value=value)
    ...
    
    def __getitem__(self, key):
        return self.get(key)
    ...

    def __delitem__(self, key): 
        self.delete(key)
    ...

    def __contains__(self, key): 
        index = self.__search(key)
        if index is not None:
            return True
        else:
            return False
    ...

    def __iter__(self): 
        for item in self.__arr:
            if item and item != "deleted":
                yield item.key
    ...

    def __len__(self):
        return self.__useful

    # def __missing__(self, key): ...
