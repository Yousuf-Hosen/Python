
# for i in range(0,len(pal)):
#     for j in range(len(pal),0):
#         if pal[i] != pal[j]:
#             check=True
#         else:
#             continue

pal=input("Enter your string ")
check=False

i=0
j=len(pal)-1
while i<j:
    if(pal[i] != pal[j]):
        check=True
        break
    i+=1
    j-=1
if check==True:
    print("NOT palindrome")
else:
    print("palindrome")

            

    
