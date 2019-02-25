# python collatz 25 Feb 2019
#


my_list = int(input("Please enter a positive integer: "))

for i in range(my_list):
    if i % 2 == 0:
        print (i//2)
