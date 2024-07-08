""" 
reference the value print korte hole repr function use korbo

 """

class Item:
    # class attributes
    all=[]
    def __init__(self,itemName,itemPrice) -> None:
        assert itemPrice>0 ,f"error in line 3 and the {itemPrice} is invalid"
        self.__itemName=itemName
        self.__itemPrice=itemPrice #instans attributes
        self.all.append(self)
    def __repr__(self) -> str:
        return f"Item {self.itemName} {self.itemPrice}"
    
item1=Item("Bowl",200)
item2=Item("plate",150)
# item1.discount=20 #not private
# item2.offer="50%" # dynamic attributes created 
# print(Item.all) #print class attributes

# print(item2.__dict__)
item1._Item__discount=20
# item2.offer="50%"

print(item1.all)
print(item1.__dict__) 
# print(item1.__discount)
item1._Item__itemName="Bowl broken"
# print(item1._Item__itemName)
print(item1.__dict__) 

