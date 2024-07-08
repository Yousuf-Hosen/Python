"""
make -> chatbot
steps
1.input/ listen
2. process / decide
3. output / talkback 
 """
greet_word=['hi','hello','yo']
by_word=['bye','next','tata']
funny_word=['pakboy','morgirDim','nightprincess']
bad_word=['halarput','chuodury','nanir bari','dog','girgit']
def listen():
    return input("Say something ")
def decide(command):
    # print(command)
    command=command.lower()
    broken_words=command.split(" ")
    for word in broken_words:
        if word in greet_word:
            talkback("HI MAN")
            break
        elif word in by_word:
            talkback("bye bye tata ")
            break
        elif word in bad_word:
            talkback("you are a bad man, behave yourself!")
            break
        elif word in funny_word:
            talkback("you are a funny man, please mstop your mouth!")
            break
    
def talkback(response):
    print(response) 
while True:
    command=listen()
    decide(command)

