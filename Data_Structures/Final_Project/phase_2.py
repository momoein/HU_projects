from typing import Any, Iterable
from tools.hash_table import DynamicHash
from tools.linked_list import SLL
from tools.applied_functions import set_attrs
from file_handler import LoadCSV

import random


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
    



class Employees:

    def __init__(self) -> None:
        self.__table = DynamicHash()
        self.__nop = 0   #number of paik's
    

    def insert_paik_from_csv(self, file_path):
        file = LoadCSV(file_path)
        for line in file.lines():
            self.add_paik(line)


    def add_paik(self, paik_info: Iterable[str]):
        paik = self.__get_paik_node(paik_info)
        n_code = paik.national_code
        # checks the paik national code
        if n_code in self.__table:
            error = f"Error: This national code `{n_code}` exist in table."
            print(error)
            return None
        # Adding paik to the table
        self.__nop += 1
        paik.recruitment_id = str(self.__nop)
        self.__table[n_code] = paik


    def __get_paik_node(self, paik_info: Iterable[str]):
        attrs = ("name", 
                 "last_name", 
                 "national_code", 
                 "capacity", 
                 "status")
        paik = Paik()
        set_attrs(paik, attrs, paik_info)
        return paik


    def show_all_paikes(self):
        for key in self.__table:
            print(self.__table[key])

    ...





em = Employees()
path = "data_structures\\Final_Project\\data\\delivery_information.csv"
em.insert_paik_from_csv(path)
em.show_all_paikes()




def make_tests_paik(num=10):
    tf_path = "data_structures\\Final_Project\\data\\test.csv"
    tf = LoadCSV(tf_path)

    tf_filds = ["name","last_name","national_code","capacity","status"]
    rows = []
    chars = [chr(c) for c in range(97, 123)]

    for _ in range(num):
        row = []
        random.shuffle(chars)
        name = "".join(random.choices(population=chars, k=5))
        row.append(name)
        random.shuffle(chars)
        last_name = "".join(random.choices(population=chars, k=5))
        row.append(last_name)
        ncode = str(random.randint(1_000_000_000, 9_999_999_999))
        row.append(ncode)
        capa = str(random.randint(10, 99))
        row.append(capa)
        stat = random.choice(["A", "D"])
        row.append(stat)
        #
        rows.append(row)

    if tf.is_exist():
        tf.append(rows)
    else:
        tf.write(rows, tf_filds)
    

# make_tests_paik()