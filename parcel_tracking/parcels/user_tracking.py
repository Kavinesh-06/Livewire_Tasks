from storage.file_handler import load_data, save_data
import utilities.validators as valid
from datetime import datetime
import time

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

    time.sleep(0.75)
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
    tracking_id = input("Enter Your Tracking id : ").upper()
    sender_name = input("Enter parcel sender name : ").title()
    parcels = load_data()
    for parcel in parcels:
        if tracking_id == parcel["tracking_id"].upper() and sender_name == parcel["sender"].title():
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