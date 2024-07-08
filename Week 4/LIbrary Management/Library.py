"""                 Library MAnagements System 

User part : Name,Reg_No,ROLL_No,Password,Department,
           List of [] borrowed books
           LIst of return Books

Library:  Books LIst dictionary {'Books Name':numbers of books}
          Register Dictionary{name: which books}
          method
          borrowed()
          returns()
          check available books()
          add_books
"""
class User:
    # allusers=[]
    def __init__(self,name,Roll_num,Reg_No,password):
        self.name=name
        self.Roll_num=Roll_num
        self.Reg_No=Reg_No
        self.password=password
        self.borrow_books=[]
        self.return_books=[]
        # self.allusers.append(self.name)
# arif=User('arif',173224,702,'jhuygryg4339')
# jarif=User('jarif',173744,898,'jhfuyguyfguy4667')

class Library:
    def __init__(self,book_lists) -> None:
        self.book_lists=book_lists


    def Borrow_books(self,book_name,user):
        for book in self.book_lists:
          if book ==book_name:
              if book_name in user.borrow_books:
                  print("Age boi ferot daw")
                  return 
              if self.book_lists[book]==0:
                  print("Boi library te sesh hoye gese")
                  return
              self.book_lists[book]-=1
              user.borrow_books.append(book_name)
              print("You have borrowed this books")
              return
        print("Books are not available in the library ")
    

    def return_books(self,bookname,user):
        belongs_book=False
        for book in self.book_lists:
            if book==bookname:
                belongs_book=True
                if book in user.borrow_books:     
                  self.book_lists[book]+=1
                  user.borrow_books.remove(bookname) 
                  user.return_books.append(bookname)
                  print("book returned successfully")
                  return
                else:
                   print("You don't Borrow a Book")
        if belongs_book==False:
            print("This book not belongs to our Library")

    def Donate_book(self,bookname,amount):
        for book in self.book_lists:
            if book==bookname:
                self.book_lists[book]+=amount
                print("Thanks for your Donating books")
                return
        self.book_lists[book_name]+=amount
        print("Thanks for your Donating books")
    
    def Check_availability(self):
        for book in self.book_lists:
            if self.book_lists[book]>0:
                print(book)

                  
library=Library({"English":3,"Math":5,"Bangla":7,"DSA":10})
        
allusers=[]
currentuser=None

while True:
    if currentuser==None:
        print("You are not logged in\n Please Log in or Craete Account (L/C)")
        option=input()
        if option=="L":
            roll=int(input("Give your Roll Number: "))
            reg=int(input("Enter Your registration number: "))
            password=input("Enter Your Password: ")
            match=False
            for user in allusers:
                if user.Roll_num==roll and user.Reg_No==reg and user.password==password:
                    currentuser=user
                    match=True
                    break
            if match==False:
                print("NO user found \n")
        else:
            name=input("Enter your name: ")
            roll=int(input("Give your Roll Number: "))
            reg=int(input("Enter Your registration number: "))
            password=input("Enter Your Password: ")
            user=User(name,roll,reg,password)
            currentuser=user
            allusers.append(user)
    else:
        print("OPTIONS")
        print("__________")
        print("Option->1: Borrow a book")
        print("Option->2: return the book")
        print("Option->3: Borrowed books List")
        print("Option->4: Returned Book List")
        print("Option->5: check availability ")
        print("Option->6: Donate books")
        print("Option->7: log_Out")
        x=int(input("Give option : "))
        if x==1:
            book_name=input("Book name please: ")
            library.Borrow_books(book_name,currentuser)
            print(user.borrow_books)
            print(library.book_lists)
        elif x==2:
            book_name=input("Book name please: ")
            library.return_books(book_name,currentuser)
            print(currentuser.return_books)
        elif x==3:
            print(currentuser.borrow_books)
        elif x==4:
            print(currentuser.return_books)
        elif x==5:
            library.Check_availability()
        elif x==6:
            book_name=input("Enter bookName: ")
            amount=int(input("Enter the books amount: "))
            library.Donate_book(book_name,amount)
            print(library.book_lists)
        elif x==7:
            currentuser=None
            print("\n\n\n")





        

  










      
    

