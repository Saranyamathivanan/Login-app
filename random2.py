import random

def g_number(x):
    r_number = random.randint(1, x)
    g_number =0
    while g_number != r_number:
        g_number =int(input("Enter your guessing number between 1 to 5:"))
        if g_number> r_number:
            print("Sorry your value is too high")
        elif g_number < r_number:
            print("sorry your valuer is too low")
    print(f"Congratlation your guessing number is correct{r_number}")
g_number(5)

