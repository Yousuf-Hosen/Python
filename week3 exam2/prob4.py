import re

def new_string(values):
    parts = re.split(r"(\d+)", values)
    parts_map = {parts[i]:int(parts[i+1]) for i in range(0, len(parts)-1, 2)}

    result=''.join([c*parts_map[c] for c in sorted(parts_map.keys(),key=str.lower)])
    return result
values="x3b4U5i2"
output=new_string(values)
print(output)



    

        
    
