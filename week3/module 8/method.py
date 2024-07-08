"""  method are similar to function 
as if function takes some parameters an do some work and return result same 
method take parameters and gives result
 """

class Phone:
    brand='sumsung'
    colour='Blue'
    features=['camera','voice call','ai','hard body']
    def call(self):# self is the default arg of any methods
        print("ring ring ring")
    def send_sms(self,number,text):
        sms=f'send massage : {text} to -> {number}'
        return sms


my_phone=Phone()
my_phone.call() # Phone.call() takes 0 positional arguments but 1 was given 
sms=my_phone.send_sms('01725713538','i misses to miss you')
print(sms)

