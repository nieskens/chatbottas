import conversation, random, re

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
    conv = conversation.Conversation(userMessage)
    botResponse = conv.checkMessage()

    # respond according to results
    if botResponse:
        print("BOT: {}".format(botResponse))
    else:
        print("BOT: {}".format(random.choice(["Ok","Hmmm","That's interesting"]))) 

while True:
    dialogue()
