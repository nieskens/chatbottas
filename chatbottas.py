import checkmessage, random

def dialogue():
    message = input()
    check_obj = checkmessage.CheckMessage(message)
    check_result = check_obj.check_message()
    if check_result:
        print("BOT: {}".format(check_result))
    else:
        print("BOT: {}".format(random.choice(["Ok","Hmmm","That's interesting"]))) 

while True:
    dialogue()
