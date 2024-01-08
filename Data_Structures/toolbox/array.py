class Array:
    def __init__(self, size: int=0, obj=None):
        self.__array = [obj] * abs(size)
        self.__len = abs(size)
        
    def get(self):
        return self.__array 
    
    def __setitem__(self, index, data):
        if abs(index) < self.__len:
            self.__array[index] = data
        else:
            raise IndexError("Array assignment index out of range")

    def __getitem__(self, index):
        if abs(index) < self.__len:
            return self.__array[index]
        else:
            raise IndexError("Array index out of range")
    
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


class DynamicArray:
    def __init__(self, size: int=0, obj=None):
        self.__array = Array(size, obj)
        self.__size = abs(size)
        self.__dtype = obj
        self.__len = 0 # useful data

    def get(self):
        return self.__array 
    
    def __setitem__(self, index, data): 
        if index < 0:
            # hendle the negative indexing -> A[-1] = A[len + -1]
            index = self.__len + index
        #
        if self.__len > abs(index):
            self.__array[index] = data
        else:
            raise IndexError("DynamicArray index out of range")
        

    def __getitem__(self, index):
        if index < 0:
            # hendle the negative indexing -> A[-1] = A[len + -1]
            index = self.__len + index
        #
        if self.__len > abs(index):
            return self.__array[index]
        else:
            raise IndexError("DynamicArray index out of range")
    
    def __len__(self):
        return self.__len
    
    def size(self):
        return self.__size
    
    def extend(self): 
        if self.__size < 1:
            temp = Array(size=1, obj=self.__dtype)
        else:
            # temp = [self.__dtype] * (2*self.__len)
            temp = Array(size=2*self.__size, obj=self.__dtype)
        #
        for i in range(self.__len):
            temp[i] = self.__array[i]
        self.__array = temp
        self.__size = len(temp)
        temp = None
        del temp

    def append(self, x): 
        """Add an item to the end of the list"""
        if self.__len == self.__size:
            self.extend()
            self.__array[self.__len] = x
        else:
            self.__array[self.__len] = x
        #
        self.__len += 1
        return None

    def insert(self, i, x): 
        self[i] = x
        return None

    def remove(self, x): ...

    def pop(self): 
        if self.__len-1 >= 0:
            temp = self[-1]
            self[-1] = None
            self.__len -= 1
            return temp

    def clear(self): ...

    def count(x):
        """Return the number of times x appears in the list."""

    def reverse(self): 
        """Reverse the elements of the list in place."""

    def copy(self):
        """Return a shallow copy of the list."""

    def __repr__(self) -> str:
        return repr(self.__array)

    def __iter__(self):
        for i in range(self.__len):
            yield self.__array[i]

    def __contains__(self, x):
        for i in self:
            if i == x:
                return True
        return False



if __name__ == "__main__":
    arr = DynamicArray()
    # for i, v in enumerate(arr):
    #     arr[i] = i
    # arr[-4] = "test"
    t = arr
    print("len:", len(t))
    print("size:", t.size())
    # t.extend()
    # t.extend()
    # t[9] = 9
    t.append(99)
    # t.append(99)
    # t.append(99)
    print("pop", t.pop())
    # t.insert(-len(t), 55)
    print(t)
    print("len:", len(t))
    print("size:", t.size())
    # print(99 in t)
    

