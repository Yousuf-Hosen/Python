class Shop:
    cart=[]
    def __init__(self,buyer):
        self.buyer=buyer
    def add_to_cart(self,item):
        self.cart.append(item)
shopper_1=Shop('meraj khan')
shopper_1.add_to_cart('T-shirt')
print(shopper_1.cart)
shopper_2=Shop('hiddi')
shopper_2.add_to_cart('lungi')
print(shopper_2.cart)

