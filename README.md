# Conference Room Booking System

This is a simple conference room booking system implemented in Python. The system allows users to book, modify, and cancel bookings for a conference room. It also displays available time slots and enforces booking rules.

## Features

- User authentication
- Book conference room in 2-hour time slots from 9 AM to 9 PM
- Modify and cancel bookings
- View available time slots
- Enforce booking rules (maximum 4 hours per day and 8 hours per week)

## Prerequisites

- Python 3.x
- `prettytable` library
- `colorama` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/LawrenceKHLeung/Room_Booking.git
   cd Room_Booking
   ```

2. Install the required libraries:
   ```sh
   pip install prettytable colorama
   ```

## Usage

1. Run the main script:
   ```sh
   python main.py
   ```

2. Follow the on-screen instructions to login, book, modify, or cancel bookings.

## Testing

### Test Cases

#### Test Case 1: User Login

1. **Description**: Test user login with valid and invalid credentials.
2. **Steps**:
   - Run the script.
   - Choose the "Login" option.
   - Enter a valid user ID and password.
   - Verify that the login is successful.
   - Choose the "Login" option again.
   - Enter an invalid user ID or password.
   - Verify that the login fails.

#### Test Case 2: View Availability

1. **Description**: Test viewing available time slots.
2. **Steps**:
   - Run the script.
   - Choose the "View Availability" option.
   - Verify that the available time slots for the current week are displayed correctly.

#### Test Case 3: Book Conference Room

1. **Description**: Test booking the conference room.
2. **Steps**:
   - Run the script.
   - Login with a valid user ID and password.
   - Choose the "Book Conference Room" option.
   - Enter a valid date and time slot.
   - Verify that the booking is successful.
   - Choose the "View Bookings" option.
   - Verify that the new booking is listed.

#### Test Case 4: Modify Booking

1. **Description**: Test modifying an existing booking.
2. **Steps**:
   - Run the script.
   - Login with a valid user ID and password.
   - Choose the "Modify Booking" option.
   - Enter the index of an existing booking.
   - Enter a new valid date and time slot.
   - Verify that the booking is modified successfully.
   - Choose the "View Bookings" option.
   - Verify that the modified booking is listed.

#### Test Case 5: Cancel Booking

1. **Description**: Test canceling an existing booking.
2. **Steps**:
   - Run the script.
   - Login with a valid user ID and password.
   - Choose the "Cancel Booking" option.
   - Enter the index of an existing booking.
   - Verify that the booking is canceled successfully.
   - Choose the "View Bookings" option.
   - Verify that the canceled booking is no longer listed.

#### Test Case 6: Enforce Booking Rules

1. **Description**: Test enforcing booking rules (maximum 4 hours per day and 8 hours per week).
2. **Steps**:
   - Run the script.
   - Login with a valid user ID and password.
   - Choose the "Book Conference Room" option.
   - Attempt to book more than 4 hours (2 sessions) for a single day.
   - Verify that the system prevents the booking.
   - Attempt to book more than 8 hours (4 sessions) for a single week.
   - Verify that the system prevents the booking.

