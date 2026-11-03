# PS No. 46: Movie Ticket Booking System
# Name: Devanshu Kumar Tandan
# ERP: RU-26-01783

FILE_NAME = "bookings.txt"
TICKET_PRICE = 200
ROWS = ["A", "B", "C"]
COLS = 5

# Initialize 2D list for seat map: 3 rows x 5 columns
# None represents an empty seat, customer name string represents a booked seat
seat_map = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]

# --- 1. Load existing bookings from bookings.txt at start ---
try:
    with open(FILE_NAME, "r") as f:
        for line in f:
            parts = line.strip().split(",", 1)
            if len(parts) == 2:
                s_code = parts[0].strip().upper()
                c_name = parts[1].strip()
                if len(s_code) == 2 and s_code[0] in ROWS and s_code[1] in ["1", "2", "3", "4", "5"]:
                    r_idx = ROWS.index(s_code[0])
                    c_idx = int(s_code[1]) - 1
                    seat_map[r_idx][c_idx] = c_name
except FileNotFoundError:
    pass

# --- 2. Main Application Loop ---
while True:
    print("\nSelect an Option:")
    print("1. Book")
    print("2. Cancel")
    print("3. Seat Map")
    print("4. Exit")
    choice = input("Enter choice (1-4): ").strip()

    # --- Option 1: Book ---
    if choice == "1":
        # Check immediately if theater is already full
        seats_left = sum(row.count(None) for row in seat_map)
        if seats_left == 0:
            print("Seats left: 0")
            print("Show is now housefull.")
            continue

        seat_input = input("Seat: ").strip()

        # Normalize input replacing commas, uppercase and lowercase 'and'
        cleaned = seat_input.replace(",", " ").replace("AND", " ").replace("and", " ")
        raw_tokens = [tok.strip().upper() for tok in cleaned.split() if tok.strip()]

        if not raw_tokens:
            continue

        valid = True
        parsed_seats = []
        for tok in raw_tokens:
            if len(tok) != 2 or tok[0] not in ROWS or tok[1] not in ["1", "2", "3", "4", "5"]:
                print("Invalid seat: " + tok + ". Rows are A to C and seat numbers are 1 to 5.")
                valid = False
                break

            r_idx = ROWS.index(tok[0])
            c_idx = int(tok[1]) - 1

            if seat_map[r_idx][c_idx] is not None:
                print("Seat " + tok + " is already booked.")
                valid = False
                break

            if any(s[0] == tok for s in parsed_seats):
                print("Seat " + tok + " was entered more than once.")
                valid = False
                break

            parsed_seats.append((tok, r_idx, c_idx))

        if valid:
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty. Booking cancelled.")
                continue

            for tok, r_idx, c_idx in parsed_seats:
                seat_map[r_idx][c_idx] = name

            # Save immediately to bookings.txt
            with open(FILE_NAME, "w") as f:
                for r in range(len(ROWS)):
                    for c in range(COLS):
                        if seat_map[r][c] is not None:
                            f.write(ROWS[r] + str(c + 1) + "," + seat_map[r][c] + "\n")

            total_amount = len(parsed_seats) * TICKET_PRICE
            if len(parsed_seats) == 1:
                print("Seat " + parsed_seats[0][0] + " booked for " + name + ". Amount: " + str(total_amount))
            else:
                seat_labels = ", ".join([s[0] for s in parsed_seats])
                print("Seats " + seat_labels + " booked for " + name + ". Amount: " + str(total_amount))

            # Recalculate remaining seats after booking
            seats_left = sum(row.count(None) for row in seat_map)
            if seats_left == 0:
                print("Seats left: 0")
                print("Show is now housefull.")
            elif seats_left == 1:
                for r in range(len(ROWS)):
                    for c in range(COLS):
                        if seat_map[r][c] is None:
                            print("Seats left: 1")
                            print("Only 1 seat left: " + ROWS[r] + str(c + 1))

    # --- Option 2: Cancel ---
    elif choice == "2":
        seat_input = input("Seat: ").strip().upper()
        if len(seat_input) != 2 or seat_input[0] not in ROWS or seat_input[1] not in ["1", "2", "3", "4", "5"]:
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            continue

        r_idx = ROWS.index(seat_input[0])
        c_idx = int(seat_input[1]) - 1

        if seat_map[r_idx][c_idx] is None:
            print("Seat " + seat_input + " is not booked.")
            continue

        seat_map[r_idx][c_idx] = None

        # Save immediately to bookings.txt
        with open(FILE_NAME, "w") as f:
            for r in range(len(ROWS)):
                for c in range(COLS):
                    if seat_map[r][c] is not None:
                        f.write(ROWS[r] + str(c + 1) + "," + seat_map[r][c] + "\n")

        print("Seat " + seat_input + " booking cancelled.")

    # --- Option 3: Seat Map ---
    elif choice == "3":
        for r_idx in range(len(ROWS)):
            row_symbols = []
            for c_idx in range(COLS):
                if seat_map[r_idx][c_idx] is not None:
                    row_symbols.append("X")
                else:
                    row_symbols.append("_")
            print("Row " + ROWS[r_idx] + ": " + " ".join(row_symbols))

        seats_left = sum(row.count(None) for row in seat_map)
        print("Seats left: " + str(seats_left))
        if seats_left == 0:
            print("Show is now housefull.")
        elif seats_left == 1:
            for r in range(len(ROWS)):
                for c in range(COLS):
                    if seat_map[r][c] is None:
                        print("Only 1 seat left: " + ROWS[r] + str(c + 1))

    # --- Option 4: Exit ---
    elif choice == "4":
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")