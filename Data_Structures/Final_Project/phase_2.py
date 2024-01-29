from typing import Any, Iterable
from tools.hash_table import DynamicHash
from tools.linked_list import SLL
from tools.applied_functions import set_attrs
from file_handler import LoadCSV
from tools.array import DynamicArray



class Paik:

    def __init__(self) -> None:
        self.recruitment_id = None
        self.name = None
        self.last_name = None
        self.national_code = None
        self.capacity = None
        self.status = None
    

    def __repr__(self) -> str:
        info = f"""Paik: {{
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
        self.__table = DynamicHash()
        self.__nop = 0   #number of paik's
        self.__deliveries = DynamicArray()
    

    def insert_paik_from_csv(self, file_path):
        file = LoadCSV(file_path)
        for line in file.lines():
            self.add_paik(line)


    def add_paik(self, paik_info: Iterable[str]):
        paik = self.__make_paik_node(paik_info)
        n_code = paik.national_code
        # checks the paik national code
        if n_code in self.__table:
            error = f"Error: This national code `{n_code}` exist in table."
            print(error)
            return None
        # Adding paik to the table
        self.__nop += 1
        paik.recruitment_id = str(self.__nop)
        self.__deliveries.append(paik)
        self.__table[n_code] = paik


    def __make_paik_node(self, paik_info: Iterable[str]):
        attrs = ("name", 
                 "last_name", 
                 "national_code", 
                 "capacity", 
                 "status")
        paik = Paik()
        set_attrs(paik, attrs, paik_info)
        return paik


    def show_all_paikes(self):
        for delivery in self.__deliveries:
            print(delivery)


    def get_paik_by_id(self, id):
        return self.__deliveries[int(id)-1]
    

    def edit_paik_info(self, id, keyword, value):
        if keyword == "recruitment_id":
            error = "`recruitment id` has not changeable"
            print(error)
            return None
        paik = self.get_paik_by_id(id)
        setattr(paik, keyword, value)
        #
        print(paik)
        print(f"The '{keyword}' change to:", getattr(paik, keyword))
    ...




class NotDeliveredParcel:
    def __init__(self) -> None:
        self.parcel_id = None
        self.weight = None
        self.subscription_code = None
        self.registration_date = None
        self.cost = None
        self.group = None

    def __repr__(self) -> str:
        info = f"""not delivered parcel:
            id: '{self.id}'
            weight: '{self.weight}'
            subscription_code: '{self.subscription_code}'
            registration_date: '{self.registration_date}'
            cost: '{self.cost}'
            group: '{self.group}' """
        return info


class SendQueue:

    def __init__(self) -> None:
        self.__days = DynamicHash()

    def insert_from_csv(self, path):
        file = LoadCSV(path)
        for line in file.lines():
            self.add(line)

    def add(self, parcel_info):
        parcel = self.__make_parcel_node(parcel_info)
        ...
        

    def __make_parcel_node(self, parcel_info: Iterable[str]):
        attrs = ("id", 
                "weight", 
                "subscription_code", 
                "registration_date", 
                "cost", 
                "group",)
        parcel = NotDeliveredParcel()
        set_attrs(parcel, attrs, parcel_info)
        return parcel

    
    
class Day:
    def __init__(self) -> None:
        self.waiting = DynamicHash()
        self.Posted = SLL()
        self.failed = SLL()

    # def add(self, percel_node):
    #     ...

class Days:
    def __init__(self) -> None:
        self.__table = DynamicHash()

    
    


from datetime import date



def get_date(date_: str):
    D = date_.split("-")
    y, m, d = int(D[0]), int(D[1]), int(D[2])
    return date(y, m, d)

def days_difference(d1, d2):
    delta = d2 - d1
    return delta.days

start = get_date("2024-01-05")
end = get_date("2024-01-07")

res = days_difference(end, start)
print(res)





# em = Deliveries()
# path = "data_structures\\Final_Project\\data\\delivery_information.csv"
# em.insert_paik_from_csv(path)
# em.show_all_paikes()
# print(em.get_paik_by_id(10))
# em.edit_paik_info(10, "capacity", "85")


