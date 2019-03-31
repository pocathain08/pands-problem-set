# This program prints numbers between 1000 and 10000 that are 
#divisible by 6 but not 12
#Peadar O Cathain


My_list = (list(range(1000, 10000)))
#Defines a list that goes from 1000 to 10000.

for i in (My_list):
# i is all the numbers in this list.
    if i % 6 == 0 and i % 12 != 0:
        # i must be divisible by 6, i.e. no remainder left and
        # i must not be divisible by 12, i.e. a remainder is left.

        print (i)
        #This prints all of the re-defined 'i's that meet the if condition
    


