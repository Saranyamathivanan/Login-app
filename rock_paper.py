import random 

def play():

    userinput = input("What's your choice ? 'r' for rock , 'p' for paper , 's' for scissors:  ")
    ran_number = random.choice(['r','p','s'])

    if(userinput == ran_number):
        return "You are tie!"
    
    if is_win(userinput,ran_number):
        return "you win"
    
    return "you lost"

def is_win(player, opponent):
    
       if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r'):
          return True

print (play())
                            