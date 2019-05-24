import random

class CheckMessage(object):
    def __init__(self,message):
        self.user_message = message
        self.messages = {
            "Hi":["Hello, how are you?","Hey,you again!", "How have you been?","Goodday, what's up?"],
            "How are you?":["I'm good, thanks for asking!", "I'm fine, thanks!"]
            }

    def check_message(self):
        if self.user_message in self.messages:
            return random.choice(self.messages[self.user_message])
        else:
            return False