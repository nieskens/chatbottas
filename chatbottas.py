import checkmessage, checkpattern, random, re

def dialogue():
    userMessage = input()
    messageObj = checkmessage.CheckMessage(userMessage)
    messageResult = messageObj.checkMessage()
    patternObj = checkpattern.CheckPattern(userMessage)
    patternResult = patternObj.checkPattern()
    if messageResult:
        print("BOT: {}".format(messageResult))
    elif patternResult:
        print("BOT: {}".format(patternResult))
    else:
        print("BOT: {}".format(random.choice(["Ok","Hmmm","That's interesting"]))) 

while True:
    dialogue()
