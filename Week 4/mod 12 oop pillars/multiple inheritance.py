class School:
    def __init__(self,name):
        self.school_name=name
        print("School init called :")
class Grade:
    def __init__(self,grade_name):
        self.grade_name=grade_name
        print('Grade class init called')
class Sports:
    def __init__(self,sport_name):
        self.sport_name=sport_name
        print("sport class called")
        self.team=[]
    def add_player(self,player_name):
        self.team.append(player_name)

            
            
class Student(School,Grade,Sports):
    def __init__(self,name,grade_name,school_name):
        self.name=name
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)
        print('student init called')
ananto=Student("AT",'MBA','DU')
print(ananto.name)
print(ananto.grade_name)
print(ananto.school_name)
    


    