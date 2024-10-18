
import random
print("Password Generator")
print("===================")

def number_password(num):
   
    if number == 0:
        print("Please Enter the integer value")
    else:
        number_password

def pass_length(pass_len):
    
    if passLen == 0:
        print("Please Enter the integer value")
    else: 
        pass_length
   
number= int(input("number of password?"))
number_password(number)
passLen=int(input("password length?"))       
pass_length(passLen)

chars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+0123456789|ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("\n here the password length: ")  
for pwd in range(number):
    password =''
    for c in range(passLen):
        password += random.choice(chars)
    print(password)       
     
      






