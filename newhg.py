import random

def guess_name():
    
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if user_guess.lower() == chosen_word[x]:
            blank_list[x] = user_guess.lower()
            correct_guess = True
        x+=1
    if correct_guess ==False:
        print(f"There is no {user_guess}, sorry.")
        update_display += 1
    x = 0

            
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
chosen_word =list(random.choice(word_list))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0
print(HANGMANPICS[update_display])
user_guess = input(f"Welcome to Hangman game!!!\n {blank}\n Make a guess? ")
guess_name()
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    user_guess = input("make to another guess? ")
    guess_name()
    print (HANGMANPICS[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print ("GAME OVER")

    