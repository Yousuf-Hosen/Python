import re
def replace_comma_with_space(text):
   mystring = re.sub(",", " ", text)
   return mystring

s="I,have,been,practising,python,since,the,course,started"
output=replace_comma_with_space(s)
print(output)

