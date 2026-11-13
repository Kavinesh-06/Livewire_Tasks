from parcels.parcel_manager import (
    register_parcel,
    search_parcel,
    view_all_parcels,
    filter_parcel
    )

from tracking.tracking_manager import (
    update_status,
    view_history
)

from utilities.validators import get_menu_choice

def display_menu():

    print("\n")
    print('='*50)
    print("         Parcel Tracking Management System")
    print('='*50)

    print("1. Register New Parcel")
    print("2. Track / Search Parcel")
    print("3. Update Delivery Status")
    print("4. View Delivery History")
    print("5. View All Parcels")
    print("6. Filter Parcels")
    print("7. Exit")
    print('='*50)

def main():

    while True:
        display_menu()
        choice = get_menu_choice("Enter Your Choice : ",['1','2','3','4','5','6','7'])
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
            print("Application closed succussfully.......")
            break

if __name__ == "__main__":
    main()