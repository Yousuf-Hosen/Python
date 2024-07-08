class Phone:
    manufacture='china'
    def __init__(self,brand,price,colour):
        self.brand=brand # this is called instantenious attribute
        self.price=price
        self.colour=colour
my_phone=Phone(brand='samsung',price=15000,colour='blue')
print(my_phone.brand,my_phone.manufacture)
her_phone=Phone('oppo',12000,'black')
print(her_phone.brand,her_phone.colour)


        