import random, time, re

class CheckMessage():
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

def dialogue():
    message = input()
    response_obj = CheckMessage(message)
    response = response_obj.check_message()
    print("BOT: {}".format(response))

while True:
    dialogue()
