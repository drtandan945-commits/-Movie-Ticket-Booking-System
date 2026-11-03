# Name: Devanshu Kumar Tandan
# ERP:RU-26-01783

# Movie Ticket Booking System

A command-line movie ticket booking program written in Python. It lets you book or cancel seats, view the current seat map, and saves bookings between runs.

## Requirements

- Python 3

## Run the program

Open a terminal in this folder and run:

```powershell
python code.py
```

If your system uses the Python launcher, you can instead run:

```powershell
py code.py
```

## How to use

Choose an option from the menu:

1. **Book** — Enter one or more seat codes and a customer name. Multiple seats can be separated by spaces, commas, or `and` (for example, `A1 A2`, `A1,A2`, or `A1 and A2`).
2. **Cancel** — Enter the code of a booked seat to cancel it.
3. **Seat Map** — Display the seating layout and remaining seat count.
4. **Exit** — Close the program.

The theater has 15 seats: rows **A**, **B**, and **C**, with seats **1** through **5** in each row. A ticket costs **200**. The seat map displays `X` for a booked seat and `_` for an available seat.

## Booking data

Bookings are stored in `bookings.txt` in the same folder as the program. The file is loaded when the program starts and updated after each booking or cancellation. Each line contains a seat code and customer name, separated by a comma. Keep this file to preserve bookings between runs; if it is missing, the program starts with all seats available.
