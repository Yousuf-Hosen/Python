class School:
    def __init__(self,name) -> None:
        self.school_name=name
    def say_hello(self):
        print(f"hello i am {self.school_name}")
    
    def __repr__(self) -> str:
        return f" School {self.school_name} "
class Teacher:
    def __init__(self,name) -> None:
        self.teacher_name=name
    
    def say_hello(self):
        print(f"hello i am {self.teacher_name}")
    
    def __repr__(self) -> str:
        return f" Teacher {self.teacher_name} "
class Student(Teacher,School):
    def __init__(self,name,school_name,teacher_name) -> None:
        # School.__init__(self,school_name)  #1 no process
        # Teacher.__init__(self,teacher_name)
        super().__init__(teacher_name)
        super().__init__(school_name)
     
        
        # super().__init__(teacher_name)

        self.student_name=name
    def __repr__(self) -> str:
        return f" Students {self.student_name} "
      

student=Student("rakib","Mr.Mazharul","Trust school")
student.say_hello()
        