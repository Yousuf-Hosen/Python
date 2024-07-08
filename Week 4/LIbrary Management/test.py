class Hall:
    def __init__(self, rows, cols, hall_no):
        # Initialize instance attributes
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        # Create a 2D list to represent seat availability, initially all free
        self.seat_matrix = [['Free' for _ in range(cols)] for _ in range(rows)]

        # Create a key in the seats attribute with the hall_id mapping to the 2D list
        self.seats[hall_no] = self.seat_matrix

    def entry_show(self, id, movie_name, time):
        # Create a tuple with show information
        show_info = (id, movie_name, time)

        # Append the show_info tuple to the show_list
        self.show_list.append(show_info)

    def book_seats(self, show_id, seats_to_book):
        # Find the show with the specified ID in the show_list
        show = None
        for s in self.show_list:
            if s[0] == show_id:
                show = s
                break

        if show is None:
            print(f"Show with ID {show_id} not found.")
            return

        # Get the seat matrix for this show
        seat_matrix = self.seats[self.hall_no]

        # Book the specified seats if they are available
        for row, col in seats_to_book:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if seat_matrix[row][col] == 'Free':
                    seat_matrix[row][col] = 'Booked'
                    print(f"Seat ({row}, {col}) for show {show_id} has been booked.")
                else:
                    print(f"Seat ({row}, {col}) for show {show_id} is already booked.")
            else:
                print(f"Invalid seat ({row}, {col}). Seat does not exist in this hall.")

# Example usage:

# Creating an instance of Hall
hall = Hall(10, 10, 1)

# Adding a show to the hall
hall.entry_show(1, "Movie A", "3:00 PM")

# Booking seats for the show
hall.book_seats(1, [(0, 0), (0, 1), (1, 1), (10, 10)])  # Attempt to book valid and invalid seats

# Checking the seat_matrix after booking
print(hall.seats[1])
