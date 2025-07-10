# We start with a list of dictionaries.
# Each dictionary represents a driver and their information.
f1_drivers = [
    {"name": "Max Verstappen", "team": "Red Bull Racing", "number": 1},
    {"name": "Lewis Hamilton", "team": "Mercedes", "number": 44},
    {"name": "Charles Leclerc", "team": "Ferrari", "number": 16},
    {"name": "Fernando Alonso", "team": "Aston Martin", "number": 14}
]

def show_drivers():
    """Displays all drivers in the list."""
    if not f1_drivers:
        print("No drivers registered yet.")
        return

    print("\n--- Current F1 Drivers ---")
    for driver in f1_drivers:
        print(f"Name: {driver['name']}, Team: {driver['team']}, Number: {driver['number']}")
    print("----------------------------\n")

def add_driver():
    """Adds a new driver to the list."""
    print("\n--- Add New Driver ---")
    name = input("Enter the driver's name: ")
    team = input(f"Enter {name}'s team: ")
    # We use a loop to ensure the number is a valid integer
    while True:
        try:
            number = int(input(f"Enter {name}'s car number: "))
            break # Exits the loop if the number is valid
        except ValueError:
            print("Invalid input. Please enter an integer for the car number.")

    new_driver = {"name": name, "team": team, "number": number}
    f1_drivers.append(new_driver)
    print(f"Driver '{name}' added successfully!\n")

def search_driver():
    """Searches for a driver by name."""
    print("\n--- Search Driver ---")
    search_name = input("Enter the name of the driver you want to search for: ").strip().lower() # .strip() removes extra spaces and .lower() converts to lowercase

    found = False
    for driver in f1_drivers:
        if driver['name'].lower() == search_name: # Compares in lowercase for more flexible searching
            print(f"\nDriver Found:")
            print(f"Name: {driver['name']}, Team: {driver['team']}, Number: {driver['number']}")
            found = True
            break # Stops the search as soon as the driver is found
    
    if not found:
        print(f"Driver '{search_name}' not found.")
    print("-----------------------\n")


def main_menu():
    """Displays the main program menu and manages options."""
    while True:
        print("--- F1 Menu ---")
        print("1. View all drivers")
        print("2. Add new driver")
        print("3. Search driver by name")
        print("4. Exit")
        print("---------------")

        option = input("Choose an option: ")

        if option == '1':
            show_drivers()
        elif option == '2':
            add_driver()
        elif option == '3':
            search_driver()
        elif option == '4':
            print("Exiting the F1 program. See you!")
            break # Exits the loop and ends the program
        else:
            print("Invalid option. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main_menu()