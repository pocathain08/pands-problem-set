#This program returns today’s date and time
#Monday, January 10th 2019 at 1:15pm
#Peadar O Cathain 

import datetime

day = (datetime.datetime.now().strftime(' %d'))
#To get the ordinal numbers for the date.
#Ord numbers to added using an f string
if day == (1, 11, 31):
    Ord = "st"
if day == (2, 22):
    Ord = "nd"
if day == (3, 23):
    Ord = "rd"
else:
    Ord = "th"

#https://stackoverflow.com/q/415511
#https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-with-datetime-strptime
x=(datetime.datetime.now().strftime(f'%A, %B %d{Ord} %Y, at %I:%M %p'))
#Account for 1st, 2nd, 3rd, etc using an f string

print (x)


