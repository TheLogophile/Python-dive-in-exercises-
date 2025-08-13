# Write a program that converts the Gregorian date of Christmas to the Solar Hijri (Persian) calendar.

from persiantools.jdatetime import JalaliDate

print(JalaliDate.to_jalali(2026,1,1))