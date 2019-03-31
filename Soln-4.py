# This program asks the user to input any positive integer and 
#outputs the successive values of the following calculation. 
#At each step calculate the next value by taking the current value 
#and, if it is even, divide it by two, but if it is odd, multiply 
#it by three and add one. 
#Peadar O Cathain 25 Feb 2019


#Ref https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while True:
    #If x is not a integer, it will return a valueError, this will bring it back to the try loop
    try:
        x = int (input ("Please enter a positive integer: "))
        # Ask the used to enter an integer

# If a non-integer is entered by the user
    except ValueError:
        print("That's not a positive integer, please try again!")
        #Retruns to the start of the while loop
        continue
    
# Need to deal wth negative integers 
    if x < 1:
        print("That's not a positive integer, please try again!")
        #Retrun to the start of the while True: loop
        continue
    
    else:
        break
        #Breaks out of the loop and goes to the next line of the program.

Soln = list()
#Creates an empty list. 
#This will be used for the calculated values of x
while x > 1:
# The following loops will continue running until x > 1.
# Once x in the program reached 2, it will be divided by two, 
#this will return one and the while condition will not be true. 
    Soln.append(x)
    # Starts the list
        
    if x % 2 == 0:
    # for x even. (x mod 2  doen't leave a remainder)
        x = x//2
        # The next value of x

    elif x % 2 != 0:
     # for x odd. (x mod 2 leaves a remainder)
        x = ((3 * x) +1)
        # The next value of x
Soln.append(x)
# Itterates through the answere and puts them into a list called Soln

print (Soln)
                


