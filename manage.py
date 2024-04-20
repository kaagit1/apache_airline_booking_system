import random
import string

# Function to generate a random booking reference
def generate_booking_reference():
    characters = string.ascii_letters + string.digits
    booking_ref = ''.join(random.choice(characters) for _ in range(8))
    return booking_ref

# Function to book a seat
def book_seat(seat_map, customer_data, row, col):
    # Prompt for customer details
    passport = input("Enter passport number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    # Generate booking reference
    booking_ref = generate_booking_reference()
    # Store booking reference and customer data
    customer_data[booking_ref] = {'passport': passport, 'first_name': first_name, 'last_name': last_name, 'row': row, 'col': col}
    seat_map[row][col] = booking_ref  # Use booking reference instead of 'R'
    print(f"Seat booked successfully! Your booking reference number is {booking_ref}.")
    return booking_ref

# Function to free a seat
def free_seat(seat_map, customer_data, row, col):
    # Prompt for customer details
    booking_ref = input("Enter booking reference number: ")
    if booking_ref in customer_data:
        if customer_data[booking_ref]['row'] == row and customer_data[booking_ref]['col'] == col:
            del customer_data[booking_ref]  # Remove booking reference from customer data
            seat_map[row][col] = 'F'
            print("Seat freed successfully!")
        else:
            print("Invalid booking reference for the provided seat.")
    else:
        print("Invalid booking reference.")

# Function to show booking state in a table format
def show_booking_state_table(seat_map):
    print("Seat Map:")
    print("   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ")
    for i, row in enumerate(seat_map):
        print(f"{i + 1:2d}", end="  ")
        for seat in row:
            print(seat, end=" ")
        print()

# Function to check booking details using booking reference
def check_booking_details(customer_data):
    booking_ref = input("Enter booking reference number: ")
    if booking_ref in customer_data:
        print("Booking Details:")
        print(f"Booking Reference: {booking_ref}")
        print(f"Passport Number: {customer_data[booking_ref]['passport']}")
        print(f"First Name: {customer_data[booking_ref]['first_name']}")
        print(f"Last Name: {customer_data[booking_ref]['last_name']}")
        print(f"Seat Row: {customer_data[booking_ref]['row']}")
        print(f"Seat Column: {customer_data[booking_ref]['col']}")
    else:
        print("Invalid booking reference.")

# Main function
def main():
    rows = 6
    cols = 20
    seat_map = [['F' for _ in range(cols)] for _ in range(rows)]
    customer_data = {}  # Dictionary to store customer data

    menu = {
        1: "Check availability of seat",
        2: "Book a seat",
        3: "Free a seat",
        4: "Show booking state",
        5: "Check booking details",
        6: "Exit program"
    }

    while True:
        print("\nMenu:")
        for key, value in menu.items():
            print(f"{key}. {value}")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            print("Seat available:", seat_map[row][col] == 'F')
        elif choice == 2:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            book_seat(seat_map, customer_data, row, col)
        elif choice == 3:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            free_seat(seat_map, customer_data, row, col)
        elif choice == 4:
            show_booking_state_table(seat_map)
        elif choice == 5:
            check_booking_details(customer_data)
        elif choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
