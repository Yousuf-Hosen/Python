a = ['oh', 'Emelia', 'to']
result_string=" "
def create_new_string(s):
    global result_string
    broken_words=s.split(" ")
    new_word=broken_words[0].split(",")
    new_word[0]=new_word[0].lower()
    broken_words[0]=new_word[0]
    for index,words in enumerate(broken_words):
        if words in a:
            for word in a:
                if broken_words[index]==word:
                    if index==11:
                        continue
                    else:
                     result_string+=broken_words[index+1]+" "

    f = open("output.txt", "a+")
    f.write(result_string)
    f.close()               
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
create_new_string(s)
f = open("output.txt", "r")
print(f.read())
