#This program displays a plot of the functions x, x^2 and 2^x in the range [0,4].
#Peadar O Cathain 26 Mar 2019

#https://stackoverflow.com/questions/22476854/plotting-function-from-python
import numpy as np

import matplotlib.pyplot as plt

import matplotlib.patches as mpatch

X = np.arange(0.,4., 0.001)
# defines the np arrange specified, in this e.g. 0 to 5 in interval of 0.001)
A = X
B = X**2
C = 2**X
#Defines the functions, for reuse if necessery

#Add legend, Ref: https://matplotlib.org/users/legend_guide.html
legend = mpatch.Patch(color='black', label='Red:x=y, Blue:x^2, Green: x=2^x')
plt.legend(handles=[legend])

plt.plot(X, A, 'r', X, B, 'b', X, C, 'g')
#I could also have used the actual functions, i.e. plt.plot(X, X, 'r', X, X**2, 'b', X, 2**X, 'g' )

plt.show()
# To get a graphic of the Plot

