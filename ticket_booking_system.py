class Star_Cinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for i in range(1, self._rows + 1):
            self._seats[i] = [['free'] * self._cols]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['free'] * self._cols for _ in range(self._rows)]

    def book_seats(self, id, seats_to_book, booking_name):
        if id not in self._seats:
            raise ValueError("Invalid show ID")
        for row, col in seats_to_book:
            if not (1 <= row <= self._rows and 1 <= col <= self._cols):
                raise ValueError("Invalid seat")
            if self._seats[id][row - 1][col - 1] == 'booked':
                raise ValueError("Seat already booked")
            self._seats[id][row - 1][col - 1] = 'booked'
        return booking_name

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError("Invalid show ID")
        return [[(i + 1, j + 1) for j, seat in enumerate(row) if seat == 'free'] for i, row in enumerate(self._seats[id])]

    def display_seats(self, id):
        for row in self._seats[id]:
            print(row)


cinema = Star_Cinema()

hall1 = Hall(7, 7, 1)
cinema.entry_hall(hall1)

hall1.entry_show(100, "KGF", "20/04/2024 10:00 AM")
hall1.entry_show(200, "AVATAR", "20/04/2024 4:00 PM")

while True:
    print("\n1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. Exit")
    option = input("\nENTER OPTION: ")

    if option == '1':
        print("SHOWS TODAY:")
        for show in hall1.view_show_list():
            print(f"MOVIE NAME: {show[1]} (SHOW ID: {show[0]}) TIME: {show[2]}")
    elif option == '2':
        show_id = int(input("ENTER SHOW ID: "))
        if show_id in [show[0] for show in hall1.view_show_list()]:
            print("Available Seats:")
            for row in hall1.view_available_seats(show_id):
                print(" ".join(f"Seat {seat}" for seat in row))
        else:
            print("Invalid show ID")
    elif option == '3':
        show_id = int(input("Show Id: "))
        if show_id in [show[0] for show in hall1.view_show_list()]:
            num_tickets = int(input("Number of Tickets?: "))
            booking_name = input("Enter Your Name: ")
            seats_to_book = []
            for _ in range(num_tickets):
                while True:
                    try:
                        row = int(input("Enter Seat Row: "))
                        col = int(input("Enter Seat Col: "))
                        if not (1 <= row <= hall1._rows and 1 <= col <= hall1._cols):
                            raise ValueError("Invalid seat")
                        if hall1._seats[show_id][row - 1][col - 1] == 'booked':
                            raise ValueError("Seat already booked")
                        seats_to_book.append((row, col))
                        break
                    except ValueError as e:
                        print(e)
            try:
                booking_name = hall1.book_seats(show_id, seats_to_book, booking_name)
                print(f"{num_tickets} seat(s) booked for show (ID: {show_id}) for {booking_name}")
                print("Updated Seats Matrix for Hall", hall1._hall_no)
                hall1.display_seats(show_id)
            except ValueError as e:
                print(e)
        else:
            print("Invalid show ID")
    elif option == '4':
        break
    else:
        print("Invalid option! Please select again.")
