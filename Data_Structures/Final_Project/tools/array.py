


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
        """Reverse the elements of the list in place."""
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
