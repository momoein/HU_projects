class Array:
    def __init__(self, size: int, dtype: type=None):
        self.__array = [dtype] * abs(size)
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
    
    def __repr__(self) -> str:
        return repr(self.__array)
    
    def clear(self):
        self.__array = [None for i in range(self.__len)]



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
    arr = DynamicArray(5, dtype=0)
    arr.extend()
    arr[1] = 9
    for i, v in enumerate(arr):
        print(i, v)
    a = Array(9, dtype=0)
    print(a)
    a.clear()
    print(a)
    