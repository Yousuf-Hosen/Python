def reverse_string(s):
    word=s.split(" ")
    new_word=[i[::-1]for i in word]
    final_word=" ".join(new_word)
    return final_word
s=input("Enter an sentence : ")
output=reverse_string(s)
print(output)