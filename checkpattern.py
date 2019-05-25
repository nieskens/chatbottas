import random, re

class CheckPattern(object):
    def __init__(self,message):
        self.userMessage = message
        self.patterns = {
            "I feel (.*)":["Why do you feel {}?", "You feel {}, why?","How long have you been feeling {}?"],
            "Do you remember (.*)":["Of course I remember {}","Yes, I do remember {}","Now that you mention it, I do remember {}"]
            
        }

    def checkPattern(self):
        for pattern in self.patterns:
            match = re.search(pattern.lower(), self.userMessage.lower())
            if match:
                answer = random.choice(self.patterns[pattern])
                return answer.format(match.group(1))