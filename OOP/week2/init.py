class Phone:
    manufacture="China"
    color="black"  #class attributes
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def send_sms(self,number,text):
        sms= f" sending {text} to {number}"
        return sms
    
my_phone=Phone("samsumg",1200)
print(my_phone.color)
        
        