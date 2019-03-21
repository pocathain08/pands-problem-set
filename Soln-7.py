#This program returns an approx square root of a positive
#ﬂoating point number. 

x = float (input ("Please enter a positive number: "))
if x < 0:
    print ("This is not a positive number, please try again")

y = float (input ("What is the tolerance +/-: "))    

est = float (input ("Please enter your estimate: "))

while abs((est*est)-x)> y:
    est-=((est*est)-x)/(2*est)

print (f"{est} is within {y} of the exact square root {x}.")