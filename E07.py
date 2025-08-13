# Write a program that displays the day of the week for today's date in the Solar Hijri (Persian) calendar.

from persiantools.jdatetime import JalaliDate

today_index = JalaliDate.today().weekday()
print(today_index)
week_days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
print(week_days[today_index])