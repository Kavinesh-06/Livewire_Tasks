def get_non_empty_input(text):
    while True:
        value = input(text).strip()
        if value:
            return value
        print("Input value cannot be empty. Please try again!.")

def get_positive_float(text):
    while True:
        try:
            value = float(input(text))
            if value > 0:
                return value
            print("weight must be greater than zero!.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_menu_choice(text,valid_choice):
    while True:
        choice = input(text).strip()
        if choice in valid_choice:
            return choice
        print("Invalid choice. Please select valid option.")