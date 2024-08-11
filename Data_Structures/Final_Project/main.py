from interface.interface import Interface
from phase_1 import Phase1
from phase_2 import Phase2
from phase_3 import Phase3



class Main:
    def __init__(self) -> None:
        self.phase_1 = Phase1()
        self.phase_2 = Phase2() 
        self.phase_3 = Phase3()



if __name__ == "__main__":
    main = Main()
    menu = Interface(main)
    menu.run()
