#This program returns today’s date and time
#Monday, January 10th 2019 at 1:15p 

import datetime

#print (dt.now().strftime('%Y-%m-%d %H:%M:%S'))
#datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

#print(now)
#datetime.datetime.now()
#datetime.datetime(2015, 2, 17, 23, 43, 49, 94252)
print(datetime.datetime.now().strftime('%A-%B-%d-%Y %H:%M:%S'))