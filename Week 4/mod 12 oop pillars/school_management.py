class School:
    # Constructor
    def __init__(self,name,location,principal=''):
        self.name=name
        self.location=location
        self.principal=principal
        self.grades=[]
    def add_grades(self,name,teacher):
            new_grades=Grades(name,teacher)
            self.grades.append(new_grades)
    def remove_grades(self,name):
         idx=0
         for i,grade in enumerate(self.grades):
              if grade.name==name:
                   idx=i
         del self.grades[idx]

              
class Grades:
    # Constructor
    def __init__(self,name,teacher):
        self.students=[]
        self.name=name
        self.teacher=teacher
    def __repr__(self) -> str:
         return f'{self.name} with teacher {self.teacher}'
    def __del__(self):
         print(f'Deleting {self.name} with teacher {self.teacher}')

oxford=School("Oxford kid academy","mirpur-12","abdul alim")
# print(oxford.principal)
oxford.add_grades("Class 3","Osman Goni")
oxford.add_grades("class 5","MD. Yousuf Hasnain")
oxford.add_grades("class 8","MD.Arafat hasan")

print(oxford.grades)
oxford.remove_grades("class 5")
print(oxford.grades)


