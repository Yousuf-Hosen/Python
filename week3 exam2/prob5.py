student_name=input()
mark=int(input())
student_id=int(input())
lines=[student_name,mark,student_id]
with open('info.txt','w') as f:
    f.write("students information")
    for line in lines:
        f.write(line)
        f.write(" ")


