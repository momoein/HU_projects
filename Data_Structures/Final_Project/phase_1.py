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
        info = f"""
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
        for i in costs:
            id = i.data
            yield id
        

    def __get_lt(self, root, cost, sll):
        """insert in to the sll if node.key <= cost"""
        if root is None:
            return 
        else:
            self.__get_lt(root.left, cost, sll)
            #
            if root.key <= cost:
                for node in root.data:
                    sll.insert(node.data)
            #
            if root.right and root.right.key <= cost:
                self.__get_lt(root.right, cost, sll)

    def __search(self, key):
        return self.__bst.search(key)

class Phase1:
    def __init__(self) -> None:
        self.__table = DynamicHash()
        self.__costs = Costs()

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
            
    
    def add(self, data):
        node = self.create_consignment_node(data)
        if node.id not in self.__table:
            self.__table[node.id] = node
            self.__costs.add(id=node.id, cost=int(node.cost))

    
    def search(self, id):
        item = self.__table[id]
        return item
    
    def cost_search(self, cost: int):
        for id in self.__costs.less_of(cost):
            print(id)
            # print(repr(self.__table[id]))

    
    def show_all(self):
        for key in self.__table:
            print(key, ":", self.__table[key])
    






f1 = Phase1()
f1.insert_from_csv()
# f1.show_all()
# print(f1.search("ABC1234").weight)

f1.cost_search(10000000)

