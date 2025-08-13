# Write a program that displays only the day and month of today's date in the Solar Hijri (Persian) calendar.

from persiantools.jdatetime import JalaliDate

today = JalaliDate.today()
print(f"{today.month}/{today.day}")