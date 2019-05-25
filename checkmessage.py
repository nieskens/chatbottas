import random

class CheckMessage(object):
    def __init__(self,message):
        self.user_message = message.lower()
        self.messages = {
            "hi":["Hello, how are you?","Hey,you again!", "How have you been?","Goodday, what's up?"],
            "how are you?":["I'm good, thanks for asking!", "I'm fine, thanks!"]
        }

    def checkMessage(self):
        if self.user_message in self.messages:
            return random.choice(self.messages[self.user_message])
        else:
            return False