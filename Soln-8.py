#This program returns today’s date and time
#Monday, January 10th 2019 at 1:15p 

import datetime

day = (datetime.datetime.now().strftime(' %d'))
if day == 1:
    Ord = "st"
if day == 2:
    Ord = "nd"
if day == 3:
    Ord = "rd"
else:
    Ord = "th"

#https://stackoverflow.com/q/415511
#https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-with-datetime-strptime
x=(datetime.datetime.now().strftime(f'%A, %B %d{Ord} %Y, at %I:%M %p'))
#Account for 1st, 2nd, 3rd, etc using an f string

print (x)


