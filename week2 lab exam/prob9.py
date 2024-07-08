result_string = " "
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
def  replace_word(s):

    global result_string
    broken_words=s.split(" ")
    # print(broken_words)
    for words in broken_words:
        if words in replace_with:
          for word in replace_with:
               if words==word:
                index=replace_with.index(word)
                result_string+=replace_with[index+1]+" "
        else:

           result_string+=words+" "
    print(result_string)

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
replace_word(s)
