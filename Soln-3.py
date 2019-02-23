# This program prints numbers between 1000 and 10000 that are divisible by 6 but not 12


My_list = (list(range(1000, 10000)))

for i in (My_list):
    if i % 6 == 0 and i % 12 != 0:

        print (i)
    


