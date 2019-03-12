#Write a program that outputs whether or not 
#today is a day that begins with the letter T

import datetime

#for i in (1,3)

if datetime.datetime.today().weekday() == i for i in (1,3):
    print("Yes - today begins with a T")

#if datetime.datetime.today().weekday() == 3:
 #   print("Yes - today begins with a T")

else:
    print ("No - today does not begin with a T.")




