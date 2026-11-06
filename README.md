# Movie Ticket Booking System

A simple Python command-line application for booking movie tickets in a small theater layout.

## Author
- Devanshu Kumar Tandan
- ERP: RU-26-01783

## Project Overview
This project allows users to:
- Book available seats
- Cancel existing bookings
- View the current seat map
- Exit the application

The system supports 3 rows (A, B, C) and 5 seats per row, for a total of 15 seats. Each ticket costs 200.

## Features
- Validates seat input
- Prevents double-booking the same seat
- Allows multiple seat selections in one booking
- Supports input such as `A1`, `B3`, `A1 A2`, `A1,B2`, and `A1 and B2`
- Saves bookings to `bookings.txt`
- Loads existing bookings automatically on startup
- Displays the remaining seat count and house-full status
- Shows the final amount based on the number of tickets booked

## File Structure
- `one.py` — main application logic
- `bookings.txt` — stores booked seats and customer names
- `README.md` — project documentation

## How to Run
Open a terminal in the project folder and run:

```bash
python one.py
```

If your system uses the Python launcher, you can also use:

```bash
py one.py
```

## Menu Options
1. Book
   - Enter one or more seat codes such as `A1`, `B3`, or `A1 A2`
   - You can separate multiple seats with spaces, commas, or the word `and`
   - Enter the customer name to complete the booking
   - The total booking amount is calculated automatically

2. Cancel
   - Enter a seat code such as `C2` to remove a booking

3. Seat Map
   - Displays the current seat layout
   - `X` marks a booked seat and `_` marks an available seat
   - Shows how many seats remain

4. Exit
   - Ends the program

## Booking Data Format
The program stores bookings in `bookings.txt` as:

```text
A1,John Doe
B2,Jane Smith
```

Each line uses the format:

```text
SEATCODE,NAME
```

## Notes
- If `bookings.txt` is missing, the program starts with all seats available.
- Invalid seat entries and duplicate bookings are rejected.
- The application is designed for small-scale theater booking and uses a simple text file for data storage.
