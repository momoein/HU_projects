from tools.hash_table import DynamicHash
from tools.linked_list import SLL
from tools.tree import BST
from tools.applied_functions import set_attrs
from tools.file_handler import LoadCSV


class Parcel:
    def __init__(self) -> None:
        self.id = None
        self.weight = None
        self.subscription_code = None
        self.registration_date = None
        self.delivery_date = None
        self.cost = None
        self.group = None

    def __repr__(self) -> str:
        info = f"""Parcel: 
        id: '{self.id}'
        weight: '{self.weight}'
        subscription_code: '{self.subscription_code}'
        registration_date: '{self.registration_date}'
        delivery_date: '{self.delivery_date}'
        cost: '{self.cost}'
        group: '{self.group}' 
        """
        return info




class Costs:
    def __init__(self) -> None:
        self.__bst = BST()


    def add(self, id: str, cost: int):
        sll = SLL()
        sll.insert(id)
        node_with_collision = self.__bst.insert(key=cost, data=sll, collision_handling=True)
        if node_with_collision:
            node_with_collision.insert(id)

    
    def less_of(self, cost):
        root = self.__bst.root
        costs = SLL()
        self.__get_lt(root, cost, costs)
        for id in costs:
            yield id
        

    def __get_lt(self, root, cost, sll):
        """insert in to the sll if node.key <= cost"""
        if root is None:
            return None
        else:
            self.__get_lt(root.left, cost, sll)
            #
            if root.key > cost:
                return None
            else:
                for item in root.data:
                    sll.insert(item)
            #
            self.__get_lt(root.right, cost, sll)


    def __search(self, key):
        return self.__bst.search(key)
    ...




class DeliveredParcels:
    """Delivered Parcel Manager"""
    def __init__(self) -> None:
        self.__table = DynamicHash()
        self.__costs = Costs()


    def insert_from_csv(self):
        path = "data_structures\\Final_Project\\data\\delivered_parcel.csv"
        file = LoadCSV(path)
        for item in file.lines():
            self.add(item)


    def add(self, data):
        consign = self.__get_consignment_node(data)
        # check id
        if consign.id not in self.__table:
            self.__table[consign.id] = consign
            self.__costs.add(id=consign.id, cost=int(consign.cost))
        else:
            print(f"Error: This id `{consign.id}` exist in table.")


    def __get_consignment_node(self, consign_data):
        attrs = ("id", 
                "weight", 
                "subscription_code", 
                "registration_date", 
                "delivery_date", 
                "cost", 
                "group",)
        consign = Parcel()
        set_attrs(consign, attrs, consign_data)
        return consign

    
    def search(self, id):
        if id in self.__table:
            item = self.__table[id]
            return item
    
    def show_costs_less_then(self, cost: int):
        print("-------------------------")
        print(f"All parcel less then {cost}\n")
        for id in self.__costs.less_of(cost):
            # print(id)
            print(self.__table[id])

    
    def show_all(self):
        for key in self.__table:
            print(self.__table[key])
    
    ...

