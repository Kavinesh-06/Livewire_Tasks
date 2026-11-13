from storage.file_handler import load_data, save_data
import utilities.validators as valid
from datetime import datetime

def generate_tracking_id(parcels):
    if not parcels:
        return "PKG1001"
    ids = []
    for parcel in parcels:
        tracking_id = parcel["tracking_id"]
        number = int(tracking_id[3:])
        ids.append(number)
    next_number = max(ids) + 1
    return f"PKG{next_number}"

def update_status():
    print("\n========== Update Parcel Status ==========\n")

    tracking_id = input("Enter Tracking id : ").strip().upper()
    parcels = load_data()
    
    for parcel in parcels:
        if parcel["tracking_id"] == tracking_id:
            print("\nParcel Found!")
            print("Current Status : ",parcel["status"])
            print("\nAvailable Delivery Status:")
            print("1. Picked Up")
            print("2. In Transit")
            print("3. Out for Delivery")
            print("4. Delivered")
            print("5. Delivery Failed")

            choice = valid.get_menu_choice("Select from the status option : ",['1','2','3','4','5'])

            statuses = {
                "1": "Picked Up",
                "2": "In Transit",
                "3": "Out for Delivery",
                "4": "Delivered",
                "5": "Delivery Failed"
            }
            
            if parcel["status"] in ["Delivered","Delivered Failed"]:
                print("\nThis parcel has reached the final status!")
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
            print("-----------------------------------")
            print("Tracking ID :", tracking_id)
            print("Old Status  :", old_status)
            print("New Status  :", new_status)
            print("-----------------------------------")
            return
    print("\nParcel Not Found")

def view_history():
    print("\n========== Parcel Delivery History ==========")

    tracking_id = input("Enter your Tracking id : ").strip().upper()
    parcels = load_data()

    for parcel in parcels:
        if parcel["tracking_id"] == tracking_id:
            print("\nParcel Found!")
            print("\nTracking ID     :", parcel["tracking_id"])
            print("Receiver Name     :", parcel["receiver"])
            print("Destination Place :", parcel["destination"])
            print("Current Status    :", parcel["status"])

            print("\n ========== Parcel Deliverable Status Timeline ==========")

            history = parcel.get("history",[])

            if not history:
                print("No deliverable history available!")

            else:
                for index,record in enumerate(history,start=1):
                    status = record.get("status","Unknown")
                    timestamp = record.get("timestamp","Timestamp Unavailabe")

                    print(f"\n{index}.{status}")
                    print("  Date & Time : ",timestamp)
            print("\n=========================================")
            return
    print("\nParcel is not Found")
    print("Please check your tracking id.")
    