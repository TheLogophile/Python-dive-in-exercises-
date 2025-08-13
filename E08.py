# Write a program that calculates the user's age in the Solar Hijri (Persian) calendar based on their birth year.

from persiantools.jdatetime import JalaliDate

def age(user_birth_year):
    t_year = JalaliDate.today().year
    age = t_year - user_birth_year
    return age

print(age(1378))