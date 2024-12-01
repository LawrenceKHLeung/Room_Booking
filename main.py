import os
from prettytable import PrettyTable
from datetime import datetime, timedelta
from colorama import init, Fore, Style

# Initialize colorama
init()

# File paths
USERS_FILE = 'users.txt'
BOOKINGS_FILE = 'bookings.txt'

# ASCII Art for HKMU
def display_ascii_art():
    art = """
  _    _ _  ____  __ _    _ 
 | |  | | |/ /  \/  | |  | |
 | |__| | ' /| \  / | |  | |
 |  __  |  < | |\/| | |  | |
 | |  | | . \| |  | | |__| |
 |_|  |_|_|\_\_|  |_|\____/ 
                            
                            
    """
    print(art)
    print("HKMU Conference Room Booking (alpha)_by LEUNG Kim Hung 12895666")
    print("\n")
    print("Welcome to the Conference Room Booking System!")
    print("Instructions:")
    print("1. Login with your user ID and password.")
    print("2. View available time slots before booking.")
    print("3. Book, modify, or cancel your bookings as needed.")
    print("4. Follow the booking rules and enjoy your time in the conference room.")
    print("\n")

# Function to load users from file
def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            for line in file:
                user_id, password = line.strip().split(',')
                users[user_id] = password
    return users

# Function to load bookings from file
def load_bookings():
    bookings = []
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'r') as file:
            for line in file:
                bookings.append(line.strip().split(','))
    return bookings

# Function to save bookings to file
def save_bookings(bookings):
    with open(BOOKINGS_FILE, 'w') as file:
        for booking in bookings:
            file.write(','.join(booking) + '\n')

# Function to display bookings
def display_bookings(bookings):
    table = PrettyTable(['Index', 'Date', 'Time Slot', 'Booked By'])
    for index, booking in enumerate(bookings):
        table.add_row([index] + booking)
    print(table)

# Function to book the conference room
def book_room(user_id):
    display_availability()
    date = input("Enter date (YYYY-MM-DD): ")
    time_slot = input("Enter time slot (HH:00-HH:00): ")

    # Define allowed time slots
    allowed_time_slots = generate_time_slots()

    if time_slot not in allowed_time_slots:
        print("Invalid time slot. Allowed time slots are:")
        print(", ".join(allowed_time_slots))
        return

    bookings = load_bookings()
    
    # Check if the user has already booked 4 hours (2 sessions) for the given date
    daily_sessions = sum(1 for booking in bookings if booking[2] == user_id and booking[0] == date)
    if daily_sessions >= 2:
        print("You have already booked 4 hours (2 sessions) for this date.")
        return

    # Check if the user has already booked 8 hours (4 sessions) for the week
    week_start = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=datetime.strptime(date, "%Y-%m-%d").weekday())
    week_end = week_start + timedelta(days=6)
    weekly_sessions = sum(1 for booking in bookings if booking[2] == user_id and week_start.strftime("%Y-%m-%d") <= booking[0] <= week_end.strftime("%Y-%m-%d"))
    if weekly_sessions >= 4:
        print("You have already booked 8 hours (4 sessions) for this week.")
        return

    # Check if the time slot is already booked for the conference room
    for booking in bookings:
        if booking[0] == date and booking[1] == time_slot:
            print("This time slot is already booked for the conference room.")
            return

    bookings.append([date, time_slot, user_id])
    save_bookings(bookings)
    print("Conference room booked successfully!")

# Function to modify a booking
def modify_booking(user_id):
    bookings = load_bookings()
    user_bookings = [booking for booking in bookings if booking[2] == user_id]
    
    if not user_bookings:
        print("You have no bookings to modify.")
        return

    display_bookings(user_bookings)
    booking_index = int(input("Enter the index of the booking you want to modify: "))
    
    if booking_index < 0 or booking_index >= len(user_bookings):
        print("Invalid index.")
        return

    date = input("Enter new date (YYYY-MM-DD): ")
    time_slot = input("Enter new time slot (HH:00-HH:00): ")

    # Define allowed time slots
    allowed_time_slots = generate_time_slots()

    if time_slot not in allowed_time_slots:
        print("Invalid time slot. Allowed time slots are:")
        print(", ".join(allowed_time_slots))
        return

    # Check if the user has already booked 4 hours (2 sessions) for the given date
    daily_sessions = sum(1 for booking in bookings if booking[2] == user_id and booking[0] == date)
    if daily_sessions >= 2:
        print("You have already booked 4 hours (2 sessions) for this date.")
        return

    # Check if the user has already booked 8 hours (4 sessions) for the week
    week_start = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=datetime.strptime(date, "%Y-%m-%d").weekday())
    week_end = week_start + timedelta(days=6)
    weekly_sessions = sum(1 for booking in bookings if booking[2] == user_id and week_start.strftime("%Y-%m-%d") <= booking[0] <= week_end.strftime("%Y-%m-%d"))
    if weekly_sessions >= 4:
        print("You have already booked 8 hours (4 sessions) for this week.")
        return

    # Check if the time slot is already booked for the conference room
    for booking in bookings:
        if booking[0] == date and booking[1] == time_slot:
            print("This time slot is already booked for the conference room.")
            return

    bookings[bookings.index(user_bookings[booking_index])] = [date, time_slot, user_id]
    save_bookings(bookings)
    print("Booking modified successfully!")

# Function to cancel a booking
def cancel_booking(user_id):
    bookings = load_bookings()
    user_bookings = [booking for booking in bookings if booking[2] == user_id]
    
    if not user_bookings:
        print("You have no bookings to cancel.")
        return

    display_bookings(user_bookings)
    booking_index = int(input("Enter the index of the booking you want to cancel: "))
    
    if booking_index < 0 or booking_index >= len(user_bookings):
        print("Invalid index.")
        return

    bookings.remove(user_bookings[booking_index])
    save_bookings(bookings)
    print("Booking cancelled successfully!")

# Function to login
def login(users):
    user_id = input("Enter user ID: ")
    password = input("Enter password: ")

    if user_id in users and users[user_id] == password:
        print("Login successful!")
        return user_id
    else:
        print("Invalid credentials!")
        return None

# Function to generate time slots
def generate_time_slots():
    slots = []
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("21:00", "%H:%M")
    while start_time < end_time:
        end_time_slot = (start_time + timedelta(hours=2)).strftime("%H:%M")
        slots.append(f"{start_time.strftime('%H:%M')}-{end_time_slot}")
        start_time += timedelta(hours=2)
    return slots

# Function to generate dates for a week
def generate_week_dates():
    today = datetime.today()
    dates = [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
    return dates

# Function to display availability
def display_availability():
    dates = generate_week_dates()
    time_slots = generate_time_slots()
    bookings = load_bookings()

    table = PrettyTable(['Date/Time'] + dates)
    for slot in time_slots:
        row = [slot]
        for date in dates:
            booked = any(booking[0] == date and booking[1] == slot for booking in bookings)
            if booked:
                row.append(Fore.RED + "Booked" + Style.RESET_ALL)  # Highlight booked slots in red
            else:
                row.append("Available")
        table.add_row(row)
    print(table)

# Function to display booking rules
def display_rules():
    rules = """
    Rules for Booking the Conference Room:
    1. First Come, First Serve: The conference room is booked on a first come, first serve basis.
    2. Booking Limits: Each user can book a maximum of 4 hours (2 sessions) per day and 8 hours (4 sessions) per week.
    3. Booking Time: The conference room can be booked in 2-hour time slots from 9 AM to 9 PM.
    4. User Responsibility: Users are responsible for the room during their booked time slot.
    5. Cancellation: Please cancel your booking if you no longer need the room to allow others to use it.
    6. Cleanliness: Please keep the room clean and tidy for the next user.
    7. Personal Belongings: Do not leave personal belongings unattended in the room.
    8. Compliance: Users must comply with all facility rules and regulations.
    """
    print(rules)

# Main function
def main():
    display_ascii_art()
    users = load_users()
    print("Welcome to the Conference Room Booking System")

    while True:
        print("\n1. Login")
        print("2. View Bookings")
        print("3. View Availability")
        print("4. View Booking Rules")
        print("5. Modify Booking")
        print("6. Cancel Booking")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = login(users)
            if user_id:
                book_room(user_id)
        elif choice == '2':
            bookings = load_bookings()
            display_bookings(bookings)
        elif choice == '3':
            display_availability()
        elif choice == '4':
            display_rules()
        elif choice == '5':
            user_id = login(users)
            if user_id:
                modify_booking(user_id)
        elif choice == '6':
            user_id = login(users)
            if user_id:
                cancel_booking(user_id)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()