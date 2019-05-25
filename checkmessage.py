import random

class CheckMessage(object):
    def __init__(self,message):
        self.user_message = message
        # greetings to be recognized
        self.greetings = ["hi","hello","goodday","what's up","sup","yo","hi there","hey there","hey","greetings earthling","greetings"]
        # a collection of responses to a recognized greeting
        self.responses = {
            "greetings":["Hello, how are you?","Hey,you again!", "Hi, how have you been?","Goodday, what's up?"]
        }
        # a collection of standard sentences and a number of responses to choose from
        self.messages = {
            "how are you":["I'm good, thanks for asking!", "I'm fine, thanks!"]
        }
        # the responses that the chatbot has given (to prevent repetition of responses)
        self.responsesGiven = []

    def checkMessage(self):
        # If user says hi, return with a greeting from the responses dictionary
        if self.user_message in self.greetings:
            return random.choice(self.responses["greetings"])
        # Else, check for 
        elif self.user_message in self.messages:
            return random.choice(self.messages[self.user_message])
        else:
            return False