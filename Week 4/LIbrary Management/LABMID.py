class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls._hall_list.append(hall)
            print(f"Hall {hall._hall_no}  added to the hall_list.")
        else:
            print("Invalid input. Please provide an object of the Hall class.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}  # Initially empty
        self._show_list = []  # Initially empty

        # Allocate seats using a 2D list, initially all seats are free
        self._allocate_seats()

        # Add the Hall object to the hall_list using inheritance
        Star_Cinema.entry_hall(self)

    def _allocate_seats(self):
        # Create a 2D list to represent the seats, initially all seats are free
        self._seats = {self._hall_no: [["Free" for _ in range(self._cols)] for _ in range(self._rows)]}

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        print(f"Show {show_id} ({movie_name} at {time}) has been added to the show_list.")

    def book_seats(self, show_id, seat_list):
        for show in self._show_list:
            if show[0] == show_id:
                for row, col in seat_list:
                    if 0 <= row < self._rows and 0 <= col < self._cols:
                        if self._seats[self._hall_no][row][col] == "Free":
                            self._seats[self._hall_no][row][col] = "Booked"
                            print(f"Seat ({row}, {col}) for show {show_id} has been booked.")
                        else:
                            print(f"Seat ({row}, {col}) for show {show_id} is already booked.")
                    else:
                        print(f"Invalid seat ({row}, {col}) for show {show_id}. Seat does not exist.")
                return
        print(f"Show {show_id} does not exist in the show_list.")

    def view_show_list(self):
        if not self._show_list:
            print("No shows currently running in this hall.")
        else:
            print(f"Shows running in Hall {self._hall_no}:")
            for show in self._show_list:
                print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        for show in self._show_list:
            if show[0] == show_id:
                print(f"Available seats for show {show_id}:")
                for row in range(self._rows):
                    for col in range(self._cols):
                        if self._seats[self._hall_no][row][col] == "Free":
                            print(f"Seat ({row}, {col})")
                return
        print(f"Show {show_id} does not exist in the show_list.")

# Counter class
class Counter:
    def __init__(self):
        self._current_hall = None  # Currently selected hall

    def select_hall(self, hall_no):
        for hall in Star_Cinema._hall_list:
            if hall._hall_no == hall_no:
                self._current_hall = hall
                print(f"Counter selected for Hall_no {hall_no}")
                return
        print(f"Hall {hall_no} does not exist in the hall_list.")

    def view_all_shows(self):
        if self._current_hall:
            self._current_hall.view_show_list()
        else:
            print("Please select a hall first using 'select_hall()'.")

    def view_available_seats(self, show_id):
        if self._current_hall:
            self._current_hall.view_available_seats(show_id)
        else:
            print("Please select a hall first using 'select_hall()'.")

    def book_tickets(self, show_id, seat_list):
        if self._current_hall:
            self._current_hall.book_seats(show_id, seat_list)
        else:
            print("Please select a hall first using 'select_hall()'.")

hall=Hall(5,5,1)
cinema=Star_Cinema()
hall.entry_show("A1","3 Idiots","4.30 AM")
hall.entry_show("A2","Pathan","6.30 AM")
hall.book_seats("A1",[(1,2),(2,3),(3,3),(6,6)])
hall.view_available_seats("A1")
counter=Counter()
counter.select_hall(1)
counter.book_tickets("A2",[(1,1),(2,2),(3,3)])
counter.view_all_shows()
counter.view_available_seats("A1")
