import random

def g_number(x):
   
    low = 1
    high = x
    correct = ""
    while correct != 'c':
        if low !=high:
               r_number = random.randint(low, high)
        else :
             r_number = low
        correct = input(f"Is {r_number} too high (h), too low (l), or correct(C)??")
        if correct == 'h':
            high = r_number - 1
        elif correct == 'l':
            low = r_number+1
          
   
    print("congrats user guess is correct!!")
  
g_number(10)     

    