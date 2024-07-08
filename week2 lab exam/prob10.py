a = ['oh', 'Emelia', 'to']
result_string=" "
def create_new_string(s):
    global result_string
    broken_words=s.split(" ")
    new_word=broken_words[0].split(",")
    new_word[0]=new_word[0].lower()
    broken_words[0]=new_word[0]
    print(broken_words)
    for words in broken_words:
        if words in a:
            for word in a:
                if words==word:
                    index=broken_words.index(words)
                    print(index)
                    print(broken_words[index+1])

print(result_string)   


s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
create_new_string(s)