from tools.hash_table import DynamicHash
# from toolbox.array import DynamicArray



class Consignment:
    def __init__(self) -> None:
        self.id = None
        self.weight = None
        self.subscription_code = None
        self.registration_date = None
        self.delivery_date = None
        self.cost = None
        self.group = None
        

class Phase1:
    def __init__(self) -> None:
        self.__table = DynamicHash()

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
        path = "data_structures\consignments.csv"
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
    
    def search(self, id):
        item = self.__table[id]
        return item
    
    def show_all(self):
        for key in self.__table:
            print(key, ":", self.__table[key])
    


f1 = Phase1()
f1.insert_from_csv()
f1.show_all()
print(f1.search("ABC1234").weight)

