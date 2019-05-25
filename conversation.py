import random, re

class Conversation(object):
    def __init__(self,message):
        self.userMessage = message
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

        # patterns to recognize in a user's statement and their responses
        self.patterns = {
            "I feel (.*)":["Why do you feel {}?", "You feel {}, why?","How long have you been feeling {}?"],
            "Do you remember (.*)":["Of course I remember {}","Yes, I do remember {}","Now that you mention it, I do remember {}"]
        }

    def checkPattern(self):
        for pattern in self.patterns:
            match = re.search(pattern.lower(), self.userMessage)
            if match:
                answer = random.choice(self.patterns[pattern])
                return answer.format(match.group(1))
            else:
                return False

    def checkMessage(self):
        # If user says hi, return with a greeting from the responses dictionary
        if self.userMessage in self.greetings:
            return random.choice(self.responses["greetings"])
        # Else, check for standard messages
        elif self.userMessage in self.messages:
            return random.choice(self.messages[self.userMessage])
        # Else, check for a pattern
        else:
            return self.checkPattern()
