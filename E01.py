# Write a program that generates 100 random phone numbers.

import random

def numgen(_):
    prefix = ["90", "91", "92", "93", "94", "96", "10", "19", "11", "12", "13", "14", "15", "16", "17", "18", "30",
              "33", "35", "36", "37", "38", "39", "01", "02", "03", "05"]

    p = random.randint(0, len(prefix)-1)
    numberl = ["09", prefix[p]]
    for i in range(7):
        numberl.append(str(random.randint(0,9)))
    return ''.join(numberl)

numbers_list = list(map(numgen , range(100)))
print(numbers_list)

