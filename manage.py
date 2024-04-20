# Function to check seat availability
def check_availability(seat_map, row, col):
    # Check if the seat is available
    if seat_map[row][col] == 'F':
        return True
    else:
        return False

# Function to book a seat
def book_seat(seat_map, row, col):
    # Book the seat if available
    if check_availability(seat_map, row, col):
        seat_map[row][col] = 'R'
        print("Seat booked successfully!")
    else:
        print("Seat is already booked.")

# Function to free a seat
def free_seat(seat_map, row, col):
    # Free the seat if booked
    if seat_map[row][col] == 'R':
        seat_map[row][col] = 'F'
        print("Seat freed successfully!")
    else:
        print("Seat is already free.")

# Function to show booking state
def show_booking_state(seat_map):
    print("Seat Map:")
    for i, row in enumerate(seat_map):
        for seat in row:
            print(seat, end=" ")
        print()

# Function to show booking state in a table format
def show_booking_state_table(seat_map):
    print("Seat Map:")
    print("   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ")
    for i, row in enumerate(seat_map):
        print(f"{i + 1:2d}", end="  ")
        for seat in row:
            print(seat, end=" ")
        print()

# Main function
def main():
    # Initialize seat map
    rows = 6
    cols = 20
    seat_map = [['F' for _ in range(cols)] for _ in range(rows)]

    # Menu options
    menu = {
        1: "Check availability of seat",
        2: "Book a seat",
        3: "Free a seat",
        4: "Show booking state",
        5: "Exit program"
    }

    while True:
        # Display menu
        print("\nMenu:")
        for key, value in menu.items():
            print(f"{key}. {value}")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            print("Seat available:", check_availability(seat_map, row, col))
        elif choice == 2:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            book_seat(seat_map, row, col)
        elif choice == 3:
            row = int(input("Enter row number: ")) - 1
            col = int(input("Enter column number: ")) - 1
            free_seat(seat_map, row, col)
        elif choice == 4:
            show_booking_state_table(seat_map)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
