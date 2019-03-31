#This program returns an approx square root of a positive
#ﬂoating point number.
#Peadar O Cathain

while True:
    try:
        x = float (input ("Please enter a positive number: "))

# If a non-integer is entered by the user
    except ValueError:
        print("That's not a positive number, please try again!")
        #Retruns to the start of the while loop
        continue
    
# Need to deal wth negative integers 
    if x < 1:
        print("That's not a positive number, please try again!")
        #Retrun to the start of the while True: loop
        continue
    #It the input is not an integer or negative
    else:
        #Exit the while True: loop and continue with the program
        break 
# Want to have the option of setting how close to the actual Sq Root the answer
#will be, i.e. within y of the actual tolerance.
y = float (input ("What is the tolerance +/-: ")) 

#This is a crude est is the estimate inputed for the root of x, it starts the calculations.
est = x//2 

if abs((est*est)-x) > y:
#Ref Lecture notes
#The while loop iterates and refines the inputed estimate until it is within 
#the tolerance set in y.
    while abs((est*est)-x)> y:
        est-=((est*est)-x)/(2*est)
#Use of an f string to print the answer. Indent the print to keep within the 
#elif loop in line 33.
    print (f"{est} is within {y} of the exact square root {x}.")