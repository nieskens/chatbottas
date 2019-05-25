import checkmessage, checkpattern, random, re

def stripPunctuation(message):
    if message.endswith(('!','?')):
        message = message[0:-1]
        return message
    else:
        return message

def dialogue():
    # take user's message from input, make lowercase and strip punctuation
    userMessage = input()
    userMessage = userMessage.lower()
    userMessage = stripPunctuation(userMessage)
    
    # create objects to check for standard messages and patterns
    messageObj = checkmessage.CheckMessage(userMessage)
    messageResult = messageObj.checkMessage()
    patternObj = checkpattern.CheckPattern(userMessage)
    patternResult = patternObj.checkPattern()

    # respond according to results
    if messageResult:
        print("BOT: {}".format(messageResult))
    elif patternResult:
        print("BOT: {}".format(patternResult))
    else:
        print("BOT: {}".format(random.choice(["Ok","Hmmm","That's interesting"]))) 

while True:
    dialogue()
