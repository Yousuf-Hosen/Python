class Star_Cinema:
    def __init__(self) -> None:
        self._hall_list=[]
    def entry_hall(self,Hall_obj):
        self._hall_list.append(Hall_obj)

class Hall:
    def __init__(self,rows,cols,hall_no):
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        # allocates seats using 2D list 
        self.allocate_seats()

    
    def allocate_seats(self):
        self._seats = {self._hall_no: [["Free" for _ in range(self._cols)] for _ in range(self._rows)]}

    def entry_show(self,show_id,movie_name,time):
        show_infos=(show_id,movie_name,time)
        self._show_list.append(show_infos)
        print(f"Show {show_id} ({movie_name} at {time}) has been added to the show_list.")

          # Create a 2D list to represent seat availability, initially all free
    
    def book_seats(self,show_id,seat_to_booked):
        for show in self._show_list:
            if show[0]==show_id:
                for row,col in seat_to_booked:
                    if 0<=row<self._rows and 0<=col<self._cols:
                        if self._seats[self._hall_no][row][col]=="Free":
                            self._seats[self._hall_no][row][col]="Booked"
                            print(f"seats ({row} {col}) has been booked for show_id {show_id}")
                        
                        else:
                             print(f"seats ({row} {col}) Already booked for show_id {show_id}")
                    else:
                        print(f"Invalid seat ({row}, {col}) for show {show_id}. Seat does not exist.")

    
            else:
                print(f'show id {show_id} does not match or exist')                                                                                      

    def view_show_list(self):
        if not self._show_list:
            print("No shows currently running in this hall.")
        else:
            print(f'show running in the hall no {self._hall_no}')
            for show in self._show_list:
                print(f'show ID: {show[0]} Movie: {show[1] } show_time: {show[2]}')

    
    def view_available_seats(self,show_id):
        for show in self._show_list:
            if show[0]==show_id:
                print(f'Avaiable seats for show ID:{show_id}')
                for row in range(self._rows):
                    for col in range(self._cols):
                        if self._seats[self._hall_no][row][col]=="Free":
                            print(f'seats ({row}, {col}) is Available')
                return
        print(f'Show_ID {show_id} Does not match')


class Counter(Hall):
    def __init__(self):
        self._current_hall=None # currently no hall are selected
    
    def Select_hall(self,hall_no):
        for hall in Star_Cinema._hall_list:
            if hall==hall_no:
                self._current_hall=hall
                print(f"Hall is selected {hall_no}")
                return
        print(f"hall no {hall_no} does not matched")
    
    def view_all_show(self):
        if self._current_hall:
            self._current_hall.view_show_list()
        else:
            print("no show is Running ")
    
    def show_available_seats(self,show_id):
        if self._current_hall:
            self._current_hall.view_available_seats(show_id)
        else:
            print("Please select a hall first by hall_select() ")
    
    def booked_tickets(self,show_id,book_to_seats):
        if self._current_hall:
            self._current_hall.book_seats(show_id,book_to_seats)
        else:
            print("please select a hall first by using hall_select() function")

hall1=Hall(10,10,1)
cinema=Star_Cinema()
cinema.entry_hall(hall1)
print(cinema._hall_list)
hall1.entry_show(1,'Zailar','5.30 AM')
hall1.entry_show(1,"3 Idiots","8.30 PM")
counter=Counter()
counter.Select_hall(1)
counter.booked_tickets(1,[(1,1),(1,3),(3,4),(5,4),(1,3)])
counter.show_available_seats(1)
counter.view_all_show()





