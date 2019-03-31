#Write a program that outputs whether or not 
#today is a day that begins with the letter T
#Peadar O Cathain 30 Mar 2019

import datetime
 #Imports the daterime function from python library

if datetime.datetime.today().weekday() == (1, 3): 
# 1,3 refers to Tuesday and Thursday in Python.
    print("Yes - today begins with a T")
    # if condition is met, the a/m statement is printed.

else:
    print ("No - today does not begin with a T.")
     # if condition is not met, the a/m statement is printed.




