from tracking.tracking_manager import generate_tracking_id
from storage.file_handler import load_data, save_data
import utilities.validators as valid
from datetime import datetime

def register_parcel():
    print("\n ========== Register New Parcel ==========\n")

    sender = valid.get_non_empty_input("Enter Sender Name                 : ")
    receiver = valid.get_non_empty_input("Enter Receiver Name               : ")
    destination = valid.get_non_empty_input("Enter Destination city            : ")
    parcel_type = valid.get_non_empty_input("Enter type of the parcel          : ")
    weight = valid.get_positive_float("Enter weight of the parcel(in kg) : ")

    parcels = load_data()
    tracking_id = generate_tracking_id(parcels)

    parcel = {
        "tracking_id" : tracking_id,
        "sender" : sender,
        "receiver" : receiver,
        "destination" : destination,
        "parcel_type" : parcel_type,
        "weight" : weight,
        "status" : "Registered",
        "history" : [
            {
                "status" : "Resgistered",
                "timestamp" : datetime.now().strftime("%d-%m-%y %I:%M:%p")
            }
        ]
    }
    parcels.append(parcel)
    save_data(parcels)

    print("\n Parcel Registered Succussfully!")
    print("\n-----------------------------------")
    print("Tracking ID       :", tracking_id)
    print("Sender name       :", sender)
    print("Receiver name     :", receiver)
    print("Destination place :", destination)
    print("Parcel Type       :", parcel_type)
    print("Parcel Weight     :", weight, "kg")
    print("Status            :  Registered")
    print("\n------------------------------------")

def search_parcel():
    print("\n========== Track Your Parcel ==========\n")
    tracking_id = input("Enter Your Tracking id : ").strip().upper()
    parcels = load_data()
    for parcel in parcels:
        if tracking_id == parcel["tracking_id"]:
            print("\nParcel Found!")
            print("\n========== PARCEL DETAILS ==========")
            print("Tracking ID       :", parcel["tracking_id"])
            print("Sender name       :", parcel["sender"])
            print("Receiver name     :", parcel["receiver"])
            print("Destination place :", parcel["destination"])
            print("Parcel Type       :", parcel["parcel_type"])
            print("Parcel Weight     :", parcel["weight"]," kg")
            print("Status            :", parcel["status"])
            print("Registered Time   :", parcel["history"][0]["timestamp"])
            print("====================================")
            return
    print("Parcel Not Found!.")
    print("Please check your tracking id.")

def view_all_parcels():
    print("\n========== All Registered Parcels ==========")

    parcels = load_data()
    if not parcels:
        print("\nNo parcel records found.")
        return
    
    print("\nTotal count of parcels : ",len(parcels))
    print("-"*40)

    for index,parcel in enumerate(parcels,start=1):
        print(f"\nParcel {index}")
        print("\n ========== Parcel Details ==========")
        print("Tracking Id       :", parcel.get("tracking_id", "N/A"))
        print("Sender name       :", parcel.get("sender", "N/A"))
        print("Receiver name     :", parcel.get("receiver", "N/A"))
        print("Destination place :", parcel.get("destination", "N/A"))
        print("Parcel type       :", parcel.get("parcel_type", "N/A"))
        print("Parcel weight     :", parcel.get("weight", "N/A"), "kg")
        print("Status            :", parcel.get("status", "N/A"))
        print('-'*40)
    print("End of the parcel lists")

def filter_parcel():
    print("\n============== Filter the Parcels ==============")
    print("""
    1.Filtered by delivery status.
    2.Filtered by destination point.
     """)
    choice = valid.get_menu_choice("Select Your choice : ",['1','2'])
    filtered_parcel = []

    parcels = load_data()
    if not parcels:
        print("\nNo parcel record found.")
        return

    if choice == '1':
        print("\nAvailable Delivery Statuses")
        print("1. Registered")
        print("2. Picked Up")
        print("3. In Transit")
        print("4. Out for Delivery")
        print("5. Delivered")
        print("6. Delivery Failed")

        status_option = {
            "1" : "Registered",
            "2" : "Picked Up",
            "3" : "In Transit",
            "4" : "Out for Delivery",
            "5" : "Delivered",
            "6" : "Delivery Failed"
        }

        status_choice = valid.get_menu_choice("\nSelect option : ",['1','2','3','4','5','6'])
        
        selected_status = status_option[status_choice]
        for parcel in parcels:
            if parcel.get("status","").lower() == selected_status.lower():
                filtered_parcel.append(parcel)
        
    else:
        city = valid.get_non_empty_input("Enter destination city : ")

        for parcel in parcels:
            if parcel.get("destination","").lower() == city.lower():
                filtered_parcel.append(parcel)

    if not filtered_parcel:
        print("\nNo matching filtered parcel record found!")
        return

    print("\n =========== Filter Result =============")
    print("Matching Parcels : ",len(filtered_parcel))

    for index, parcel in enumerate(filtered_parcel,start=1):
        print("\nParcel ",index)
        print("-"*40)
        print("Tracking Id       :", parcel.get("tracking_id","N/A"))
        print("Receiver name     :", parcel.get("receiver","N/A"))
        print("Destination place :", parcel.get("destination","N/A"))
        print("Status            :", parcel.get("status","N/A"))

    print("="*40)
