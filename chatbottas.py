import checkmessage

def dialogue():
    message = input()
    response_obj = checkmessage.CheckMessage(message)
    response = response_obj.check_message()
    print("BOT: {}".format(response))

while True:
    dialogue()
