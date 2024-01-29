from interface.cli import *
from sys import exit
from tools.array import Array

from phase_1 import DeliveredPM




class Menu:
    def __init__(self) -> None:
        self.__delivered_pm = DeliveredPM()

    def phase1(self):

        while True:
            print(phase1_cli)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            elif inp == "0":
                return
            
            elif inp == "1":
                info = self.get_delivered_parcel_info()
                self.__delivered_pm.add(info)

            elif inp == "2":
                id = input("enter id: ")
                parcel = self.__delivered_pm.search(id)
                print(parcel)

            elif inp == "3":
                cost = input("enter a cost: ")
                self.__delivered_pm.show_costs_less_then(int(cost))

            elif inp == "4":
                self.__delivered_pm.show_all()

            elif inp == "5":
                path = "data_structures\\Final_Project\\data\\delivered_parcel.csv"
                self.__delivered_pm.insert_from_csv(path)
            
    # for phase 1
    def get_delivered_parcel_info(self): 
        info = Array(7)
        print("Enter delivered parcel info")
        info[0] = input("id: ")
        info[1] = input("weight: ")
        info[2] = input("subscription_code: ")
        info[3] = input("registration_date: ")
        info[4] = input("delivery_date: ")
        info[5] = input("cost: ")
        info[6] = input("group: ")
        return info




    def phase2(self):
        while True:
            print(phase2_cli)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return
            

    def phase3(self):
        return None
    ...




if __name__ == "__main__":
    menu = Menu()
    while True:
        print(main_cli)
        inp = input(">>> ").strip()
        if inp == "00":
            break
        elif inp == "1":
            menu.phase1()
        elif inp == "2":
            menu.phase2()
        elif inp == "3":
            menu.phase3()
