class Shopper:
    def __init__(self,name):
        self.name=name
        self.cart=[]
    def add_to_cart(self,item,price,quantity):
          self.cart.append({'item':item,'price':price,'quantity':quantity})
    def checkout(self,amount):
        price=0
        for item in self.cart:
            print(item)
            price=price+item['price']*item['quantity']
        print(price)
        if price>amount:
            return f'Please give me more money {price-amount}'
        elif price<amount:
            return f'here are your items and extra money->{amount-price}'
        else:
            return ' here is yours items'


shopping=Shopper('hadiya')
shopping.add_to_cart('shirt',400,4)
shopping.add_to_cart('pants',1100,5)
shopping.add_to_cart('shoes',1000,3)
reply=shopping.checkout(5000)
print(reply)


    