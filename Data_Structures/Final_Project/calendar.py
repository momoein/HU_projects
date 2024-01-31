from tools.array import Array




class Calendar:
    def __init__(self, origin=2000, num_years=100) -> None:
        self.origin = origin
        self.num_years = num_years
        self.__days = Array(size=(num_years*12*30))

    
    def scale(self, year):
        return year - self.origin
    

    def get_index(self, indices):
        y, m, d = indices
        indx = 30*(m-1) + d-1 # for one year
        indx = (indx*self.scale(y)) + indx
        return indx


    def int_format_date(self, key: str):
        D = key.split("-")
        y, m, d = int(D[0]), int(D[1]), int(D[2])
        return y, m, d


    def insert(self, indices, value):
        """indices = (yaer, month, day)
        yaer: `origin < y < orogin + num_years`
        month: `1 <= m <= 12`
        day: `0 <= d <= 12`"""
        #
        self.chack_indices(indices)
        indx = self.get_index(indices)
        self.__days[indx] = value


    def get(self, indices):
        """indices = (yaer, month, day)
        yaer: `origin < y < orogin + num_years`
        month: `1 <= m <= 12`
        day: `0 <= d <= 12`"""
        #
        self.chack_indices(indices=indices)
        indx = self.get_index(indices=indices)
        return self.__days[indx]


    def __setitem__(self, indices, value):
        self.insert(indices, value)


    def __getitem__(self, indices):
        return self.get(indices)
        

    def chack_indices(self, indices):
        y, m, d = indices
        scale = self.scale(y)
        if scale < 0 or self.num_years <= scale:
            lo, hi = self.origin, self.origin + self.num_years
            raise IndexError(f"year most be between {lo} to {hi}")
        if abs(m) > 12 or m == 0:
            raise IndexError(f"month most be between 1 to 12")
        if abs(d) > 30 or d == 0:
            raise IndexError(f"day most be between 1 to 30")
        return None
    

    def __iter__(self):
        for i in range((359*self.num_years) + 1):
            yield self.__days[i]

