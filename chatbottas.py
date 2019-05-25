import conversation, random, re

def stripPunctuation(message):
    if message.endswith(('!','?')):
        message = message[0:-1]
        return message
    else:
        return message

conv = conversation.Conversation()

def dialogue():
    global conv
    # take user's message from input, make lowercase and strip punctuation
    userMessage = input()
    userMessage = userMessage.lower()
    userMessage = stripPunctuation(userMessage)
    
    # create a new conversation unless the message is "start over"
    # create objects to check for standard messages and patterns
    if userMessage == "start over":
        conv = conv.startOver()
    botResponse = conv.checkMessage(userMessage)

    # respond according to results
    if botResponse:
        print("BOT: {}".format(botResponse))
    else:
        print("BOT: {}".format(random.choice(["Ok","Hmmm","That's interesting"]))) 
        print("***")
        print("Answers given so far: ", conv.responsesGiven)

while True:
    dialogue()
