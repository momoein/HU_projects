from tools.linked_list import SLL
from tools.tree import BST
from tools.hash_table import DynamicHash
from tools.applied_functions import get_next_day
from tools.file_handler import LoadCSV
from phase_1 import *
from interface.input_controller import InputController as inpc
from tools.array import Array
from phase_2 import *
from tools.calendar import Calendar



today = "2024-01-02"
delivered = DeliveredParcels()
deliveries = Deliveries()
posteds = SLL()
faileds = SLL()
send_q = SendQueue()
calendar = Calendar(origin=2020, num_years=10)



def main():
    global today
    while True:
        print("\n#  main")
        print("1) phase_1 ")
        print("2) phase_2 ") 
        print("3) phase_3 ") 
        print("4) next day")
        print("exit >> 00 \n")
        inp = input(">>> ").strip()
        if inp == "00":
            exit()
        elif inp == "1":
            phase_1()
        elif inp == "2":
            phase_2()
            pass
        elif inp == "3":
            phase_3()
        elif inp == "4":
            today = get_next_day(today)
            print(today)





def phase_1():
    delivered.insert_from_csv()
    while True:
        print("\n# deliverd parcels manage")
        print("1) show all ")
        print("2) show under cost ") 
        print("3) search parcel")
        print("4) add parcel")
        print("back >> 0")
        print("exit >> 00 \n")
        inp = input(">>> ").strip()
        if inp == "00":
            exit()
        elif inp == "0":
            return
        elif inp == "1":
            delivered.show_all()
        elif inp == "2":
            print("enter cost: ")
            inp = int(inpc.get_integer())
            delivered.show_costs_less_then(inp)
        elif inp == "3":
            print("enter parcel id:")
            inp = inpc.get_parcel_id()
            print(delivered.search(inp))
        elif inp == "4":
            arr = Array(7)
            print("enter parcel id:")
            arr[0] = inpc.get_parcel_id()
            print("enter weight:")
            arr[1] = inpc.get_integer()
            print("enter subscription code:")
            arr[2] = inpc.get_integer()
            print("enter registration date:")
            arr[3] = inpc.get_date()
            print("enter delivery date:")
            arr[4] = inpc.get_date()
            print("enter cost:")
            arr[5] = inpc.get_integer()
            print("enter group:")
            arr[6] = inpc.get_group()
            delivered.add(arr)




def phase_2():
    deliveries.insert_paik_from_csv()
    send_q.inser_from_csv()
    while True:
        print("\n# deliverd parcels manage")
        print("1) add delivery ")
        print("2) show deliveries ") 
        print("3) edit delivery info ")
        print("4) show parcel in send queue")
        print("5) show faileds parcels")
        print("6) allocation parcel")
        print("7) show posted")
        print("8) show posted parcel in special day")
        print("back >> 0")
        print("exit >> 00 \n")
        inp = input(">>> ").strip()
        if inp == "00":
            exit()
        elif inp == "0":
            return
        elif inp == "1":
            arr = Array(5)
            print("enter name:")
            arr[0] = inpc.get_alpha()
            print("enter last name:")
            arr[1] = inpc.get_alpha()
            print("enter national code:")
            arr[2] = inpc.get_integer()
            print("enter capacity:")
            arr[3] = inpc.get_integer()
            print("enter status:")
            arr[4] = inpc.get_status()
            deliveries.add_delivery(arr)
        elif inp == "2":
            deliveries.show_all_paikes()

        elif inp == "3":
            edit_delivery_info()

        elif inp == "4":
            send_q.show_parcels()

        elif inp == "5":
            for item in faileds:
                print(item)

        elif inp == "6":
            print("enter delivery id")
            d_id = inpc.get_integer()
            print("enter registration date")
            reg_date = inpc.get_date()
            #
            parcels = send_q.same_date(reg_date)
            delivery = deliveries.search_delivery(d_id)
            if delivery is None:
                print("not found delivery")
                return
            for item in parcels.iter():
                if delivery.is_free():
                    delivery.daycap += 1
                    if calendar[today] is None:
                        calendar[today] = DynamicHash()
                        calendar[today][d_id] = SLL()

                    parcel_id = item.data.id
                    calendar[today][d_id].append(parcel_id)
                    item.data.delivery_date = today
                    posteds.append(item.data)
                    parcels.delete(item)
                
            print(calendar[today])
            
            
        elif inp == "7":
            for item in posteds:
                print(item)
                
        elif inp == "8":
            print("enter date:")
            day = inpc.get_date()
            print("enter delivery id:")
            _id = inpc.get_integer()
            [print(i) for i in calendar[day][_id]]

            



def phase_3():
    max_ = 0
    for item in deliveries:
        num = int(item.capacity)
        if num > max_:
            print(item)
            max_ = num



def edit_delivery_info():
    print("Enter the delivery recruitment id:")
    id_ = inpc.get_integer()    
    delivery = main.search_delivery_by_id(id_)
    if delivery is None:
        print("!? not found delivery")
        return None
    #
    print("1) Edit name ")
    print("2) Edit last name ")
    print("3) Edit national code ")
    print("4) Edit capacity ")
    print("5) Edit status ")  
    print("back >> 0")
    print("exit >> 00 \n")
    while True:
        inp = input(">>> ").strip()
        if inp == "00":
            exit()
        if inp == "0":
            return
        
        # 1) Edit name 
        if inp == "1":
            print("Enter new name")
            name = inpc.get_alpha()
            deliveries.edit_delivery_info(id_, "name", name)

        # 2) Edit last name
        elif inp == "2":
            print("Enter new last name")
            last_name = inpc.get_alpha()
            deliveries.edit_delivery_info(id_, "last_name", last_name)

        # 3) Edit national code
        elif inp == "3":
            print("Enter new national code")
            national_code = inpc.get_alpha()
            deliveries.edit_delivery_info(id_, "national_code", national_code)

        # 4) Edit capacity
        elif inp == "4":
            print("Enter new capacity:")
            capacity = inpc.get_integer()
            deliveries.edit_delivery_info(id_, "capacity", capacity)

        # 5) Edit status
        elif inp == "5":
            print("choose between: 'D', 'A' ")
            status = inpc.get_status()
            deliveries.edit_delivery_info(id_, "status", status)


if __name__ == "__main__":
    main()
