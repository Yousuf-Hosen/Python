class Item:
    def __init__(self,itemName,itemPrice) -> None:
        assert itemPrice>0 ,f"error in line 3 and the {itemPrice} is invalid"
        self.itemName=itemName
        self.itemPrice=itemPrice
class Person:
    def __init__(self,name,phone,age) -> None:
        assert age>=18,f"error in line 8 ,age {age} is invalid"
        #assert kaj ti korbo jodi condition true hoi
        assert len(phone)==11,f"error in line 10 invalid phone number"
        self.name=name
        self.phone=phone
        self.age=age
child=Person("akibba","01737298308",19)
print(child.name,child.phone,child.age)


        



# item1=Item("plate",-150)
# print(item1.itemName,item1.itemPrice)

