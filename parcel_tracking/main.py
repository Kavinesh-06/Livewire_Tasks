from parcels.parcel_manager import (
    register_parcel,
    search_parcel,
    update_status,
    view_history,
    view_all_parcels,
    filter_parcel
    )
import time
from utilities.validators import get_menu_choice,get_non_empty_input
import parcels.user_tracking as user
import sys

def Admin():
    while True:
        print("\n")
        print('='*50)
        print("         Parcel Tracking Management System (ADMIN)")
        print('='*50)
        time.sleep(1)

        print("1. Register New Parcel")
        time.sleep(0.5)
        print("2. Track / Search Parcel")
        time.sleep(0.5)
        print("3. Update Delivery Status")
        time.sleep(0.5)
        print("4. View Delivery History")
        time.sleep(0.5)
        print("5. View All Parcels")
        time.sleep(0.5)
        print("6. Filter Parcels")
        time.sleep(0.5)
        print("7. Exit")
        time.sleep(0.5)
        print('='*50)
        time.sleep(1)
        choice = get_menu_choice("Select the choice within this options (1, 2, 3, 4, 5, 6, 7) : ",['1','2','3','4','5','6','7'])
        print('='*50)

        if choice == '1':
            register_parcel()

        elif choice == '2':
            search_parcel()

        elif choice == '3':
            update_status()

        elif choice == '4':
            view_history()

        elif choice == '5':
            view_all_parcels()
                
        elif choice == '6':
            filter_parcel()

        elif choice == '7':
            print("\nThanking you for using Parcel Tracking System!.")
            time.sleep(0.5)
            print("This Application will be closed !.......")
            time.sleep(1)
            sys.exit(0)

def main():

    print("\n")
    print('='*50)
    print("         Parcel Tracking Management System")
    print('='*50)
    time.sleep(1)

    print('\n')
    print(f"{'-'*20} Login {'-'*20}")
    print("\n1. Users")
    time.sleep(0.5)
    print("2. Admin")
    time.sleep(0.5)
    print("3. Exit")
    time.sleep(0.5)

    select = get_menu_choice("Select the choice within(1, 2, 3) : ",['1','2','3'])

    if select == '1':
        while True:
            print("\n")
            print('='*50)
            print("         Parcel Tracking Management System (USERS)")
            print('='*50)
            time.sleep(1)

            print("1. Register New Parcel")
            time.sleep(0.5)
            print("2. Track / Search Parcel")
            time.sleep(0.5)
            print("3. Exit")

            print('='*50)
            point = get_menu_choice("Select the choice within this options (1, 2, 3) : ",['1','2','3'])
            print('='*50)

            if point == '1':
                user.register_parcel()
            elif point == '2':
                user.search_parcel()
            else:
                print("\nThanking you for using Parcel Tracking System!.")
                time.sleep(0.5)
                print("This Application will be closing !.......")
                time.sleep(0.5)
                sys.exit(0)

    elif select == '2':

        print("Admin Id : PTMS01 and password : 1234")
        count = 0
        while count < 3:
            admin = get_non_empty_input("Enter Admin Id (PTMSXX) : ")
            password = get_non_empty_input("Enter password : ")
            if admin == "PTMS01" and password == "1234":
                print("Login successful!")
                time.sleep(0.5)
                Admin()
                break

            count += 1
            print(f"Invalid credentials. Attempts remaining: {3 - count}")
            time.sleep(0.5)

        if count == 3:
            print("Maximum attempts reached.")
            time.sleep(0.5)
            sys.exit(0)
    else:
        print("\nThanking you for using Parcel Tracking System!.")
        time.sleep(0.5)
        print("This Application will be closing !.......")
        time.sleep(0.5)
        sys.exit(0)

if __name__ == "__main__":
    main()