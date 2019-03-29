#This program displays a plot of the functions x, x^2 and 2^x in the range [0,4].
#Peadar O Cathain 26 Mar 2019

#https://stackoverflow.com/questions/22476854/plotting-function-from-python
import numpy as np

import matplotlib.pyplot as plt

for x in range(5):
    a = x
    b = x**2
    c = 2**x

    #y = (a, b, c)

    #print (y)

plt.plot(x,b(x))

plt.show()

