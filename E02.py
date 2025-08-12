# Write a program that generates a one-time password (OTP) with a 60-second validity period.


import time
import random


def passgen():
    psw = ''.join(str(num) for num in (random.choices(range(10), k=8)))
    return psw


passgen()
ct = 0
timeout = 60
while True:
    if time.time() > ct + timeout:
        f = 0
        p = (passgen())
        print(p)
        ct = time.time()
    password = str(input("Enter password: "))
    if time.time() - ct < timeout:
        if password == p:
            print("Done!")
            break
        else:
            print("Incorrect password")
            f += 1
            if f == 3:
                print("Try again later")
                break
    else:
        print("Your time is up. The code has expired. Here is your new code: ")
