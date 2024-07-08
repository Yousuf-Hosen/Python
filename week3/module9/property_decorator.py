class User:
    def __init__(self,f_name,L_name):
        self.first=f_name
        self.last=L_name
        self.email=f'{self.first}{self.last}@user.com'
    @property
    def full_name(self):
        return f'{self.first} {self.last}'
    # for set anything then the getter er definition and setter er defination name same dite hobe
    @full_name.setter
    def full_name(self,value):
        # self.first=value.split(' ')[0]
        # self.last=value.split(' ')[1]
        first,last=value.split(' ')
        self.first=first
        self.last=last
        self.email=f'{self.first}.{self.last}User@gmail.com'


    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last

    @property
    def get_email(self):
        return self.email

mark =User('mark','zuku')
print(mark.first) # trhis call as a attribute
print(mark.last)
print(mark.email)
# print(mark.get_email) # for this output we call this by a method
print(mark.full_name)
print(mark.get_email) # this is call as a property or attribute

mark.full_name = 'Yousuf hasan'
print(mark.full_name)
print(mark.get_email)
# del mark.full_name
print(mark.first)
print(mark.last)
print(mark.get_email)


