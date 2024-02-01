from typing import Any, Iterable
from tools.hash_table import DynamicHash
from tools.linked_list import SLL
from tools.applied_functions import set_attrs
from tools.file_handler import LoadCSV
from tools.array import DynamicArray, Array
from phase_1 import Parcel



class Delivery:

    def __init__(self) -> None:
        self.recruitment_id = None
        self.name = None
        self.last_name = None
        self.national_code = None
        self.capacity = None
        self.status = None
        self.daycap = 0 # capacity in day
    
    def is_free(self):
        if self.daycap < int(self.capacity):
            return True
        return False

    def __repr__(self) -> str:
        info = f"""Delivery: {{
        recruitment_id: '{self.recruitment_id}'
        name: '{self.name}'
        last_name: '{self.last_name}'
        national_code: '{self.national_code}'
        capacity: '{self.capacity}'
        status: '{self.status}' 
        }}"""
        return info




class Deliveries:

    def __init__(self) -> None:
        self.__national_code = DynamicHash()
        self.__nop = 0   #number of paik's
        self.__deliveries = DynamicArray()
        # self.__capacity = DynamicArray()

    

    def insert_paik_from_csv(self):
        path = "data_structures\\Final_Project\\data\\delivery_information.csv"
        file = LoadCSV(path)
        for line in file.lines():
            self.add_delivery(line)


    def add_delivery(self, paik_info: Iterable[str]):
        paik = self.__make_paik_node(paik_info)
        n_code = paik.national_code
        # checks the paik national code
        if n_code in self.__national_code:
            error = f"Error: This national code `{n_code}` exist in table."
            print(error)
            return None
        
        # Adding paik to the table
        self.__nop += 1
        paik.recruitment_id = str(self.__nop)
        self.__deliveries.append(paik)
        # self.__capacity.append("0")
        self.__national_code[n_code] = paik.recruitment_id


    def __make_paik_node(self, paik_info: Iterable[str]):
        attrs = ("name", 
                 "last_name", 
                 "national_code", 
                 "capacity", 
                 "status")
        paik = Delivery()
        set_attrs(paik, attrs, paik_info)
        return paik


    def show_all_paikes(self):
        for delivery in self.__deliveries:
            print(delivery)


    def get_paik_by_id(self, id):
        return self.__deliveries[int(id)-1]
    

    def edit_delivery_info(self, id, keyword, value: str):
        if keyword == "recruitment_id":
            print("`recruitment id` has not changeable")
            return None
        #
        if keyword == "national_code":
            if value in self.__national_code:
                print(f"this national code: '{value}' not unique")
                return None
            self.__national_code.delete(key=value)
            self.__national_code.insert(key=value, value=id)
        #  
        paik = self.get_paik_by_id(id)
        setattr(paik, keyword, value)
        print(paik)
        print(f"The '{keyword}' change to:", getattr(paik, keyword))


    def is_delivery(self, id):
        if int(id)-1 < len(self.__deliveries):
            return True
        else:
            return False
        
    def search_delivery(self, id):
        if self.is_delivery(id):
            return self.get_paik_by_id(id)
        
    def is_free(self, id):
        deliver = self.__deliveries[int(id)]
        cap = deliver.capacity
        daycap = deliver.daycap
        if daycap < int(cap):
            return True
        return False

    def __iter__(self):
        for delivery in self.__deliveries:
            yield delivery
    ...




class Day:
    def __init__(self) -> None:
        self.waiting = DynamicHash()
        self.posted = SLL()

    def add_to_waiting(self, parcel_node):
        if parcel_node is None:
            return None
        if parcel_node.group == "F":
            if "F" in self.waiting:
                self.waiting["F"].append(parcel_node)
                return None
            self.waiting["F"] = SLL()
            self.waiting["F"].append(parcel_node)
        #
        if parcel_node.group == "C":
            if "C" in self.waiting:
                self.waiting["C"].append(parcel_node)
                return None
            self.waiting["C"] = SLL()
            self.waiting["C"].append(parcel_node)
        #
        if parcel_node.group == "O":
            if "O" in self.waiting:
                self.waiting["O"].append(parcel_node)
                return None
            self.waiting["O"] = SLL()
            self.waiting["O"].append(parcel_node)


    def add_to_posted(self, delivery_node, parcel_node):
        info = Array(size=2)
        info[0] = delivery_node.recruitment_id
        info[1] = parcel_node.id
        self.posted.append(info)

    def show_all_in_waiting(self):
        if self.waiting is None:
            return None
        for item in self.waiting["F"]:
            # print(item)
            yield item
        for item in self.waiting["C"]:
            # print(item)
            yield item
        for item in self.waiting["O"]:
            # print(item)
            yield item

    def  show_all_in_posted(self):
        for item in self.posted:
            # print(item)
            yield item
        



class SendQueue:
    def __init__(self) -> None:
        self._table = DynamicHash()

    def add_parcel(self, parcel_info):
        parcel = self.creat_parcel_node(parcel_info)
        reg_date = parcel.registration_date

        if reg_date not in self._table:
            sll = SLL()
            sll.append(parcel)
            self._table[reg_date] = sll
        self._table[reg_date].append(parcel)
        

    def show_parcels(self):
        for key in self._table:
            for item in self._table[key]:
                print(item)


    def inser_from_csv(self):
        path = "data_structures\\Final_Project\\data\\not_delivered_parcel.csv"
        file = LoadCSV(path)
        for item in file.lines():
            self.add_parcel(item)
    
    def creat_parcel_node(self, paik_info: Iterable[str]):
        attrs = ("id", 
                "weight", 
                "subscription_code", 
                "registration_date", 
                "cost", 
                "group",)
        parcel = Parcel()
        set_attrs(parcel, attrs, paik_info)
        return parcel

    def search_parcel(self, key):
        if key in self._table:
            for item in self._table[key]:
                print(item)

    def same_date(self, date):
        if date in self._table:
            return self._table[date]
                

    
        


    






# em = Deliveries()
# path = "data_structures\\Final_Project\\data\\delivery_information.csv"
# em.insert_paik_from_csv(path)
# # em.show_all_paikes()
# # print(em.get_paik_by_id(13))
# # em.edit_paik_info(10, "capacity", "85")

# print(em.search_paik(13))
