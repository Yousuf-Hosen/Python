a=input("enter your first strings: ")
b=input("enter your second strings: ")
count=0
for i in range(0,len(b)):
    if a[i] !=b[i]:
        count+=1
if count>1:
        print("False")
else:
     print("True")

