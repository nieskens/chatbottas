import random, re

class Conversation(object):
    def __init__(self):
        # greetings to be recognized
        self.greetings = ["hi","hello","goodday","what's up","sup","yo","hi there","hey there","hey","greetings earthling","greetings"]
        self.goodbye = ["goodbye","bye","bye bye","so long","take care","salut","see ya","see you","see ya later","see you later","ttyl","talk to you later","we'll talk later","i gotta go","i gotta go now","i have to go","have to go now"]

        # a collection of responses to a recognized greeting
        self.responses = {
            "greetings":["Hello, how are you?","Hey,you again!", "Hi, how have you been?","Goodday, what's up?"],
            "goodbye":["Bye!","Goodbye!","See you later","Talk to you later","I was nice to talk to you, bye!","I'm looking forward to our next chat. :)"]
        }
        # a collection of standard sentences and a number of responses to choose from
        self.messages = {
            "how are you":["I'm good, thanks for asking!", "I'm fine, thanks!"]
        }
        
        # patterns to recognize in a user's statement and their responses
        self.patterns = {
            "I feel (.*)":["Why do you feel {}?", "You feel {}, why?","How long have you been feeling {}?"],
            "Do you remember (.*)":["Of course I remember {}","Yes, I do remember {}","Now that you mention it, I do remember {}"]
        }

        # the responses that the chatbot has given (to prevent repetition of responses)
        self.responsesGiven = []

    def startOver():
        self.responsesGiven = []

    def addResponse(self,response):
        self.responsesGiven.append(response)

    def checkPattern(self,message):
        for pattern in self.patterns:
            match = re.search(pattern.lower(), message)
            if match:
                response = random.choice(self.patterns[pattern])
                answer = response.format(match.group(1))
                self.addResponse(answer)
                return answer
            else:
                return False

    def checkMessage(self,message):
        # If user says hi, return with a greeting from the responses dictionary
        if message in self.greetings:
            answer = random.choice(self.responses["greetings"])
            self.addResponse(answer)
            return answer
        # If user says bye, return with a goodbye from the responses dictionary
        elif message in self.goodbye:
            answer = random.choice(self.responses["goodbye"])
            self.addResponse(answer)
            return answer
        # Else, check for standard messages
        elif message in self.messages:
            answer = random.choice(self.messages[message])
            self.addResponse(answer)
            return answer
        # Else, check for a pattern
        else:
            return self.checkPattern(message)
