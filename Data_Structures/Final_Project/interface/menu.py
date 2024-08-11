import interface.cli as cli
from interface.input_controller import InputController as ic
from tools.array import Array




class Menu1:
    def __init__(self, phase1: object) -> None:
        self.__phase1_main = phase1 # phase one class


    def run(self):
        while True:
            print(cli.phase1_panel)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return

            # add delivered parcel
            if inp == "1":
                info = self.get_delivered_parcel_info()
                self.__phase1_main.add_consingment(info)

            # search delivered parcel
            elif inp == "2":
                id = input("enter id: ")
                parcel = self.__phase1_main.search_delivered_parcel(id)
                print(parcel)

            # show all under cost 
            elif inp == "3":
                cost = input("enter a cost: ")
                self.__phase1_main.show_all_under_cost(int(cost))

            # show all delivered parcel
            elif inp == "4":
                self.__phase1_main.show_all_delivered_parcel()

            # insert from csv
            elif inp == "5":
                self.__phase1_main.insert_from_csv()


    def get_delivered_parcel_info(self): 
        info = Array(7)
        print("Enter delivered parcel info")
        print("parcel id:")
        info[0] = ic.get_parcel_id()
        print("weight:")
        info[1] = ic.get_integer()
        print("subscription_code: ")
        info[2] = ic.get_integer()
        print("registration_date: ")
        info[3] = ic.get_date()
        print("delivery_date: ")
        info[4] = ic.get_date()
        print("cost: ")
        info[5] = ic.get_integer()
        print("group: ")
        info[6] = ic.get_group()
        return info
    




class Menu2:
    def __init__(self, phase2: object) -> None:
        self.__phase2 = phase2 # phase one class


    def run(self):
        while True:
            print(cli.phase2_panel)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return
            
            # 1) Add delivery agent 
            if inp == "1":
                info = self.__get_delivery_info()
                self.__phase2.add_delivery(info)

            # 2) Edit delivery agent info 
            elif inp == "2":
                self.__edit_delivery_info()

            # 3) Allocation of parcel 
            elif inp == "3":
                self.__phase2.allocate_parcel()

            # 4) Show all delivery agent 
            elif inp == "4":
                self.__phase2

            # 5) K best delivery agent 
            elif inp == "5":
                self.__phase2

            # 6) Find by agent name 
            elif inp == "6":
                self.__phase2

            # 7) Show waiting queue 
            elif inp == "7":
                self.__phase2

            # 8) Show all parcel 
            elif inp == "8":
                self.__phase2

            # 9) Show all delivered parcel
            elif inp == "9":
                self.__phase2

            # 10) Show all not delivered parcel 
            elif inp == "10":
                self.__phase2

            # 11) show by day   
            elif inp == "11":
                self.__phase2
        
    
    def __edit_delivery_info(self):
        print("Enter the delivery recruitment id:", end=" ")
        id_ = ic.get_integer()    
        delivery = self.__phase2.search_delivery_by_id(id_)
        if delivery is None:
            print("!? not found delivery")
            return None
        #
        print(cli.phase2_edit_delivery_info_panel.format(delivery))  
        while True:
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return
            
            # 1) Edit name 
            if inp == "1":
                print("Enter new name")
                name = ic.get_alpha()
                self.__phase2.edit_delivery_info(id_, "name", name)

            # 2) Edit last name
            elif inp == "2":
                print("Enter new last name")
                last_name = ic.get_alpha()
                self.__phase2.edit_delivery_info(id_, "last_name", last_name)

            # 3) Edit national code
            elif inp == "3":
                print("Enter new national code")
                national_code = ic.get_alpha()
                self.__phase2.edit_delivery_info(id_, "national_code", national_code)

            # 4) Edit capacity
            elif inp == "4":
                print("Enter new capacity:")
                capacity = ic.get_integer()
                self.__phase2.edit_delivery_info(id_, "capacity", capacity)

            # 5) Edit status
            elif inp == "5":
                print("choose between: 'D', 'A' ")
                status = ic.get_status()
                self.__phase2.edit_delivery_info(id_, "status", status)
        

    def __get_delivery_info(self):
        info = Array(5)
        print("Enter delivery info")
        print("name: ")
        info[0] = ic.get_alpha()
        print("last_name:")
        info[1] = ic.get_alpha()
        print("national_code: ")
        info[2] = ic.get_integer()
        print("capacity: ")
        info[3] = ic.get_integer()
        print("status: ")
        info[4] = ic.get_status()
        return info




class Menu3:
    def __init__(self, phase3: object) -> None:
        self.__phase1_main = phase3

    def run(self):
        while True:
            print(cli.phase3_panel)
            inp = input(">>> ").strip()
            if inp == "00":
                exit()
            if inp == "0":
                return

