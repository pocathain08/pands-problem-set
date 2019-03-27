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
#will be.
y = float (input ("What is the tolerance +/-: "))    
#The est is the estimate inputed for the root of x.
est = float (input ("Please enter your estimate: "))

if abs((est*est)-x) < y:
    print (f"That is a good estimate, it is within {y} of the exact square root of {x}.")
    #If the est is within y of root x, the program should break using the elif loop
elif abs((est*est)-x) > y:
#Ref Lecture notes
#The while loop iterates and refines the inputed estimate until it is within 
#the tolerance set in y.
    while abs((est*est)-x)> y:
        est-=((est*est)-x)/(2*est)
#Use of an f string to print the answer. Indent the print to keep within the 
#elif loop in line 33.
    print (f"{est} is within {y} of the exact square root {x}.")