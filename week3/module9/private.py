class user:
    def __init__(self,name,password,phone):
        self.name=name
        self.__password=password
        self.__phone=phone
    def __get_password(self):
        print(self.__password)
    def user_login(self,name,password):
        if(name==self.name and password==self.__password):
            return True
        return False
          
ryan=user('ryan dal','uygrfuhbah','87763467823187187')
# print(ryan.__phone)
# print(ryan.__password)
# ryan.__get_password()
res=ryan.user_login('ryan dal','uygrfujnhhbah')
print(res)