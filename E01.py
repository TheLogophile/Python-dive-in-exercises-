# Write a program that generates 100 random phone numbers.

import random

def numgen(_):
    prefix = ["90", "91", "92", "93", "94", "96", "10", "19", "11", "12", "13", "14", "15", "16", "17", "18", "30",
              "33", "35", "36", "37", "38", "39", "01", "02", "03", "05"]
    numberl = ["09", random.choice(prefix)]
    numberl.append(''.join(map(str,random.choices(range(0,9),k=7))))
    return ''.join(numberl)

numbers_list = list(map(numgen , range(100)))
print(numbers_list)

