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


class DynamicArray:
    def __init__(self, size: int, dtype: type=None):
        self.__array = Array(size, dtype)
        self.__len = abs(size)
        self.__dtype = dtype
        
    def get(self):
        return self.__array 
    
    def __setitem__(self, index, data):
        self.__array[index] = data

    def __getitem__(self, index):
        return self.__array[index]
    
    def __len__(self):
        return self.__len
    
    def extend(self, dtype: type=None):
        dtype = self.__dtype if dtype is None else dtype
        temp = [dtype] * (2*self.__len)
        for i in range(self.__len):
            temp[i] = self.__array[i]
        self.__array = temp
        temp = None
        del temp

    def __repr__(self) -> str:
        return repr(self.__array)


if __name__ == "__main__":
    # arr = DynamicArray(5, dtype=0)
    # arr.extend()
    # arr[1] = 9
    # for i, v in enumerate(arr):
    #     print(i, v)
    # a = Array(9, dtype=0)
    # print(a)
    # a.clear()
    # print(a)

    arr = Array(10, 0)
    # for i, v in enumerate(arr):
    #     arr[i] = i
    arr[4] = ""
    print(arr)
    arr.reverse()
    print(arr)
    

