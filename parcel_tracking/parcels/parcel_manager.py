from parcels.user_tracking import generate_tracking_id
from storage.file_handler import load_data, save_data
import utilities.validators as valid
from datetime import datetime
import time

def register_parcel():
    print("\n ========== Register New Parcel ==========\n")

    sender = valid.get_non_empty_input("Enter Sender Name                 : ").title()
    receiver = valid.get_non_empty_input("Enter Receiver Name               : ").title()
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
    time.sleep(0.5)
    print("Tracking ID       :", tracking_id)
    time.sleep(0.5)
    print("Sender name       :", sender)
    time.sleep(0.5)
    print("Receiver name     :", receiver)
    time.sleep(0.5)
    print("Destination place :", destination)
    time.sleep(0.5)
    print("Parcel Type       :", parcel_type)
    time.sleep(0.5)
    print("Parcel Weight     :", weight, "kg")
    time.sleep(0.5)
    print("Status            :  Registered")
    print("\n------------------------------------")
    time.sleep(1.5)

def search_parcel():
    print("\n========== Track Your Parcel ==========\n")
    tracking_id = input("Enter Your Tracking id : ").strip().upper()
    parcels = load_data()
    for parcel in parcels:
        if tracking_id == parcel["tracking_id"]:
            print("\nParcel Found !")
            print("....")
            time.sleep(0.75)
            print("\n========== PARCEL DETAILS ==========")
            time.sleep(0.5)
            print("Tracking ID       :", parcel["tracking_id"])
            time.sleep(0.5)
            print("Sender name       :", parcel["sender"])
            time.sleep(0.5)
            print("Receiver name     :", parcel["receiver"])
            time.sleep(0.5)
            print("Destination place :", parcel["destination"])
            time.sleep(0.5)
            print("Parcel Type       :", parcel["parcel_type"])
            time.sleep(0.5)
            print("Parcel Weight     :", parcel["weight"]," kg")
            time.sleep(0.5)
            print("Status            :", parcel["status"])
            time.sleep(0.5)
            print("Registered Time   :", parcel["history"][0]["timestamp"])
            print("====================================")
            time.sleep(1.5)
            return
    print("Parcel Not Found!.")
    print("Please check your tracking id.")
    time.sleep(0.5)

def update_status():
    print("\n========== Update Parcel Status ==========\n")

    tracking_id = input("Enter Tracking id : ").strip().upper()
    parcels = load_data()
    
    for parcel in parcels:
        if parcel["tracking_id"] == tracking_id:
            print("\nParcel Found!")
            print("Current Status : ",parcel["status"])
            time.sleep(0.75)
            print("\nAvailable Delivery Status:")
            print("1. Picked Up")
            time.sleep(0.5)
            print("2. In Transit")
            time.sleep(0.5)
            print("3. Out for Delivery")
            time.sleep(0.5)
            print("4. Delivered")
            time.sleep(0.5)
            print("5. Delivery Failed")
            time.sleep(1.5)

            choice = valid.get_menu_choice("\nSelect the choice within this options (1, 2, 3, 4, 5) : ",['1','2','3','4','5'])

            statuses = {
                "1": "Picked Up",
                "2": "In Transit",
                "3": "Out for Delivery",
                "4": "Delivered",
                "5": "Delivery Failed"
            }
            
            if parcel["status"] in ["Delivered","Delivered Failed"]:
                print("\nThis parcel has reached the final status!")
                time.sleep(2)
                return

            new_status = statuses[choice]
            old_status = parcel["status"]
            parcel["status"] = new_status

            history_record = {
                "status" : new_status,
                "timestamp" : datetime.now().strftime("%d-%m-%y %I:%M:%p")
            }
            parcel["history"].append(history_record)

            save_data(parcels)

            print("\nStatus Updated Successfully!")
            time.sleep(0.75)
            print("-----------------------------------")
            print("Tracking ID :", tracking_id)
            print("Old Status  :", old_status)
            print("New Status  :", new_status)
            print("-----------------------------------")
            time.sleep(2)
            return
    print("\nParcel Not Found")
    time.sleep(2)

def view_history():
    print("\n========== Parcel Delivery History ==========")

    tracking_id = input("Enter your Tracking id : ").strip().upper()
    parcels = load_data()

    for parcel in parcels:
        if parcel["tracking_id"] == tracking_id:
            print("\nParcel Found!")
            time.sleep(0.75)
            print("\nTracking ID     :", parcel["tracking_id"])
            time.sleep(0.5)
            print("Receiver Name     :", parcel["receiver"])
            time.sleep(0.5)
            print("Destination Place :", parcel["destination"])
            time.sleep(0.5)
            print("Current Status    :", parcel["status"])
            time.sleep(1.5)
            print("\n ========== Parcel Deliverable Status Timeline ==========")

            history = parcel.get("history",[])

            if not history:
                print("No deliverable history available!")
                time.sleep(1)

            else:
                for index,record in enumerate(history,start=1):
                    status = record.get("status","Unknown")
                    timestamp = record.get("timestamp","Timestamp Unavailabe")

                    print(f"\n{index}.{status}")
                    print("  Date & Time : ",timestamp)
                    time.sleep(2)
            print("\n=========================================")
            return
    print("\nParcel is not Found")
    print("Please check your tracking id.")
    time.sleep(1)

def view_all_parcels():
    print("\n========== All Registered Parcels ==========")

    parcels = load_data()
    if not parcels:
        print("\nNo parcel records found.")
        time.sleep(1)
        return
    
    print("\nTotal count of parcels : ",len(parcels))
    print("-"*40)
    time.sleep(2)

    for index,parcel in enumerate(parcels,start=1):
        print(f"\nParcel {index}")
        print("\n ========== Parcel Details ==========")
        time.sleep(0.75)
        print("Tracking Id       :", parcel.get("tracking_id", "N/A"))
        time.sleep(0.5)
        print("Sender name       :", parcel.get("sender", "N/A"))
        time.sleep(0.5)
        print("Receiver name     :", parcel.get("receiver", "N/A"))
        time.sleep(0.5)
        print("Destination place :", parcel.get("destination", "N/A"))
        time.sleep(0.5)
        print("Parcel type       :", parcel.get("parcel_type", "N/A"))
        time.sleep(0.5)
        print("Parcel weight     :", parcel.get("weight", "N/A"), "kg")
        time.sleep(0.5)
        print("Status            :", parcel.get("status", "N/A"))
        print('-'*40)
        time.sleep(2)
    print("End of the parcel lists")

def filter_parcel():
    print("\n============== Filter the Parcels ==============")
    print("""
    1.Filtered by delivery status.
    2.Filtered by destination point.
     """)
    time.sleep(0.75)
    choice = valid.get_menu_choice("\nSelect the choice (either 1 or 2) : ",['1','2'])
    filtered_parcel = []

    parcels = load_data()
    if not parcels:
        print("\nNo parcel record found.")
        time.sleep(1)
        return

    if choice == '1':
        
        print("\nAvailable Delivery Statuses")
        time.sleep(0.5)
        print("1. Registered")
        time.sleep(0.5)
        print("2. Picked Up")
        time.sleep(0.5)
        print("3. In Transit")
        time.sleep(0.5)
        print("4. Out for Delivery")
        time.sleep(0.5)
        print("5. Delivered")
        time.sleep(0.5)
        print("6. Delivery Failed")
        time.sleep(1.5)

        status_option = {
            "1" : "Registered",
            "2" : "Picked Up",
            "3" : "In Transit",
            "4" : "Out for Delivery",
            "5" : "Delivered",
            "6" : "Delivery Failed"
        }

        status_choice = valid.get_menu_choice("\nSelect the choice within this options (1, 2, 3, 4, 5, 6) : ",['1','2','3','4','5','6'])
        
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
        time.sleep(1)
        return

    print("\n =========== Filter Result =============")
    print("Matching Parcels : ",len(filtered_parcel))
    time.sleep(2)

    for index, parcel in enumerate(filtered_parcel,start=1):
        print("\nParcel ",index)
        print("-"*40)
        print("Tracking Id       :", parcel.get("tracking_id","N/A"))
        time.sleep(0.5)
        print("Receiver name     :", parcel.get("receiver","N/A"))
        time.sleep(0.5)
        print("Destination place :", parcel.get("destination","N/A"))
        time.sleep(0.5)
        print("Status            :", parcel.get("status","N/A"))
        time.sleep(2)

    print("="*40)
