import random     

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input("Guess number type between 1 to 10 :"))
        if guess < random_number:
            print("Sorry, guess again is too low")
        elif guess <random_number:
            print("Sorry, guess again is too high")
        
    print(f'Congrats your guessing number:{random_number}')
        
guess(10)       
