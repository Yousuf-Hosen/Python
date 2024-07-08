class Shopping:
    mall=' Jumuna Future park'
    hours=[]
    def __init__(self,customer):
        self.customer=customer
        self.items=[]
        self.total=0
    def openng_hour(cls,day):
        return cls.mall

    @staticmethod
    def multiply(x,y):
        return x*y
    def add_to_total(self,amount):
        self.total+=amount
    def add_to_cart(self,item,price,quantity):
        item_total=price*quantity
        self.total+=item_total
        self.items.append(item)



    def checkout(self):
        pass
my_shopping=Shopping('raton tana')
my_shopping.add_to_total(2300)
res=my_shopping.total
print(res)
