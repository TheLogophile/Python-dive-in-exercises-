# Write a program that generates a one-time password (OTP) with a 60-second validity period.


import time
import random

def passgen():
    digits = [str(random.randint(0,9)) for i in range(7)]
    print(''.join(digits))
    c_time = time.time()
    return ''.join(digits) , c_time

command = input("Press c to create a password: ")
if command == "c":
      p,t = passgen()
else:
    print("Invalid input")
password = str(input("Enter password: "))
if time.time()-t < 60:
    if password == p:
        print("Done!")
    else:
        print("Incorrect password")
else:
    print("Your time is up. The code has expired.")



