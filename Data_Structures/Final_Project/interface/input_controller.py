from tools.array import Array


class InputController:
    
    @staticmethod
    def get_parcel_id():
        inp = input(">>> ").strip()
        while True:
            if len(inp) == 7 and inp[:3].isalpha() and inp[3:].isdigit():
                up = inp[:3].upper()
                inp = up + inp[3:]
                return inp
            inp = input("?!> ").strip()
    
    @staticmethod
    def get_integer():
        inp = input(">>> ").strip()
        while True:
            if inp.isdigit():
                return inp
            inp = input("?!> ").strip()

    @staticmethod
    def get_date():
        inp = input(">>> ").strip()
        while True:
            spl = inp.split("-")
            if len(spl) == 3 and all(map(lambda x: x.isdigit(), spl)):
                return inp
            inp = input("?!> ").strip()

    @staticmethod
    def get_group():
        grp = Array()
        grp.set(["F", "C", "O", "f", "c", "o"])
        #
        inp = input(">>> ").strip()
        while True:
            if len(inp) == 1 and inp in grp:
                return inp.upper()
            inp = input("?!> ").strip()

    @staticmethod
    def get_alpha():
        inp = input(">>> ").strip()
        while True:
            if inp.isalpha():
                return inp
            inp = input("?!> ").strip()

    @staticmethod
    def get_status():
        grp = Array()
        grp.set(["A", "D", "a", "d"])
        #
        inp = input(">>> ").strip()
        while True:
            if len(inp) == 1 and inp in grp:
                return inp.upper()
            inp = input("?!> ").strip()
...
