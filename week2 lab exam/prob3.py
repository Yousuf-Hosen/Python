import pyjokes
def listen():
    return input("Say something ")
def decide(command):
    if  command=="Y" or command=="y" or command=="YES" or command=="yes" or command=="Yes":
       talkback(pyjokes.get_joke())
    else:
          talkback("You are enter wrong key")
def talkback(response):
    print(response) 
while True:
    command=listen()
    decide(command)
