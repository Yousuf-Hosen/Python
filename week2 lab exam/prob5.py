result=[]
def create_list(x):
      global result
      key=x.keys()
      for index,words in enumerate(key):
         result.append(words)
         result.append(index+1)
      return result
x = { 'a' : 1, 'b' : 2, 'c': 3, 'd': 4}
output=create_list(x)
print(output)
