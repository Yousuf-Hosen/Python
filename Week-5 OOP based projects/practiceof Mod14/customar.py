import hashlib
class Customer:
    stored_password=" "
    def __init__(self,name,email,password,phone):
        self.name=name
        self.email=email
        self.password=password
        self.phone=phone
    
    def Create_account(email,password):
        encryted_password=hashlib.md5(password)
        print(f'create account for {email} {password}successfully ')


class Admin:
    

    
