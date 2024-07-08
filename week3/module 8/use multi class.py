class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
class Course:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
class Teacher:
    def __init__(self,name,course):
        self.name=name
        self.course=course
class  School:
    def __init__(self,name,teachers,courses,students):
        self.name=name
        self.teachers=teachers
        self.courses=courses
        self.students=students
    def get_students(self):
        for student in self.students:
            print([student.name,student.age,student.id])


school_name='Phitron high school'
ds_course=Course('data Structure','abdul')
teacher_1=Teacher('abdul',ds_course)
algo_course=Course('algorithm','rohim')
teacher_2=Teacher('rohim',algo_course)
dis_course=Course('Discreate','Anowar')
teacher_3=Teacher('Anowar',dis_course)
intro_com_course=Course('introduction of computing','khaleda')
teacher_4=Teacher('khaleda',algo_course)
student_1=Student('kobir',19,122)
student_2=Student('hasina',21,112)
student_3=Student('forhad',17,133)
student_4=Student('arfan',20,144)
teachers=[teacher_1,teacher_2,teacher_3,teacher_4]
courses=[ds_course,algo_course,dis_course,intro_com_course] 
students=[student_1,student_2,student_3,student_4]

my_school=School(school_name,teachers,courses,students)
print(my_school.students)
my_school.get_students()
