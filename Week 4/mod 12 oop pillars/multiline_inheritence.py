class Vehicle:
    def __init__(self,name,color,price,license):
        self.name=name
        self.color=color
        self.price=price
        self.license=license

    def start(self):
        print(f'{self.name} is started')
class Bus(Vehicle):
    def __init__(self,name,license,color,seat,price,ticket_price):
        self.seat=seat
        self.available_seat=seat
        self.ticket_price=ticket_price


    def sell_ticket(self,quantity,amount):
        self.quantity=quantity
        self.amount=amount
        self.available_seat=self.available_seat-quantity
        self.total_price=quantity*self.ticket_price
        if(self.available_seat>quantity):
            if(self.amount>self.ticket_price):
                print(f'You purchased your ticket {quantity} and backed amount {amount-self.total_price} ')
            else:
                print(f'you have not sufficient balance for purchased {self.quantity} you need {self.total_price-amount} taka more' )
        else:
            print(f'we have no more seat please contract the next bus counter please:...')
        

sky=Vehicle("Truck","blue",120000,"12ERF23TN")
bus=Bus("Sokal Sondha","ERC32TN","Green",40,12300000,120)

bus.sell_ticket(3,300)



