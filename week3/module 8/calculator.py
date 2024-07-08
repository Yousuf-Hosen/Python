class Calculator:
    brand='Casio'
    model='Ms-991'
    def add(self,a,b):
        sum=a+b
        return sum
    def multiply(self,a,b):
        multiplication=a*b
        return multiplication
    def division(self,a,b):
        if a>b:
            div=a/b
        else:
            div=b/a
        return div
    def subtraction(self,a,b):
        sub=a-b
        return sub

       

my_cal=Calculator()
print(my_cal.brand)
print(my_cal.model)
jogfol=my_cal.add(100,200)
print(jogfol)
biyogfol=my_cal.subtraction(100,7000)
print(biyogfol)
gunfol=my_cal.multiply(299,988)
print(gunfol)
bagfol=my_cal.division(100,10000)
print(bagfol)

            
        
