import random 

command_1 = ["hello", "hey", 'wake up',"you there", ' help me', 'Hello', "Hey"]
reply_1 = ["Hello sir", "hey", "Welcome back Sir!", "Hope your day was good!", "Hope you missed me?","How are you?","Hey there!"]

command_2 = ["bye", "good bye", "sleep"]
reply_2 = ["ok sir1", "See you later!", "Bye sir!"]

def ChatterBot(Text):
    for word in Text.split():
        if word in command_1:
            return random.choice(reply_1) + "."
        
        if word in command_2:
            return random.choice(reply_2) + "."

