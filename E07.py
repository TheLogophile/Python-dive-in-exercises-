# Write a program that displays the day of the week for today's date in the Solar Hijri (Persian) calendar.

import jdatetime
import locale

locale.setlocale(locale.LC_ALL, jdatetime.FA_LOCALE)
today = jdatetime.datetime.now().strftime("%A")
print(today)