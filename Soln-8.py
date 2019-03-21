#This program returns today’s date and time
#Monday, January 10th 2019 at 1:15p 

import datetime

#https://stackoverflow.com/q/415511
x=(datetime.datetime.now().strftime('%A, %B, %d, %Y, %H:%M:'))
print (x)