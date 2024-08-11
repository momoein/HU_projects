import interface.cli as cli
from interface.menu import Menu1, Menu2, Menu3



class Interface:
    def __init__(self, main: object) -> None:
        self.__phase1_menu = Menu1(main.phase_1)
        self.__phase2_menu = Menu2(main.phase_2)
        self.__phase3_menu = Menu3(main.phase_3)
        self.__date_menu = None


    def run(self):
        while True:
            print(cli.main_panel)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return
            elif inp == "1":
                self.__phase1_menu.run()
            elif inp == "2":
                self.__phase2_menu.run()
            elif inp == "3":
                self.__phase3_menu.run()
            # elif inp == "4":
            #     self.__date_menu.run()