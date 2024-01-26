from tools.hash_table import DynamicHash
from tools.linked_list import SLL
from tools.tree import BST




class Consignment:
    def __init__(self) -> None:
        self.id = None
        self.weight = None
        self.subscription_code = None
        self.registration_date = None
        self.delivery_date = None
        self.cost = None
        self.group = None

    def __repr__(self) -> str:
        info = f"""Consignment:
            id: '{self.id}'
            weight: '{self.weight}'
            subscription_code: '{self.subscription_code}'
            registration_date: '{self.registration_date}'
            delivery_date: '{self.delivery_date}'
            cost: '{self.cost}'
            group: '{self.group}' """
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



class ConsignmentManager:
    def __init__(self) -> None:
        self.__table = DynamicHash()
        self.__costs = Costs()


    def add(self, data):
        node = self.create_consignment_node(data)
        if node.id not in self.__table:
            self.__table[node.id] = node
            self.__costs.add(id=node.id, cost=int(node.cost))
        else:
            print(f"tekrari: {node.id}")

    
    def search(self, id):
        item = self.__table[id]
        return item
    
    def get_costs_less_then(self, cost: int):
        for id in self.__costs.less_of(cost):
            # print(id)
            print(self.__table[id])

    
    def show_all(self):
        for key in self.__table:
            print(self.__table[key])


    def create_consignment_node(self, item_values):
        attr = ("id", 
                "weight", 
                "subscription_code", 
                "registration_date", 
                "delivery_date", 
                "cost", 
                "group",
                )
        node = Consignment()
        for i in range(len(attr)):
            setattr(node, attr[i], item_values[i])
        return node


    def consignments_csv(self):
        path = "data_structures\Final_Project\consignments.csv"
        with open(path, "+r")as f:
            for item in f:
                item = item.strip("\n")
                item = item.rsplit(',')
                yield item


    def insert_from_csv(self):
        for item in self.consignments_csv():
            self.add(item)
    ...





if __name__ == "__main__":
    c_manager = ConsignmentManager()
    c_manager.insert_from_csv()
    # c_manager.show_all()
    # print(c_manager.search("CDA1234"))
    # c_manager.get_costs_less_then(1750)
