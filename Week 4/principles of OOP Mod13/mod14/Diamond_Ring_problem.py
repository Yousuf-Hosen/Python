class A:
    def print_someting(self):
        print('Im on A')

class B(A):
     pass
class C(A):
     pass
class D(C,B):
     pass
ob1=A()
ob2=B()
ob3=C()
ob4=D()
ob1.print_someting()
ob2.print_someting()
ob3.print_someting()
ob4.print_someting()          

