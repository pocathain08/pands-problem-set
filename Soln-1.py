# This program asks the user to input any positive integer and outputs 
#the sum of all numbers between one and that number.
#Peadar O Cathain

#Soln
#Need to overcome what happens if a letter is inputed
# Ref https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

while True:
    try:
        x = int (input ("Please enter a positive integer: "))

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
#Exit the while True: loop and continue with the program
        break
#source_pynative.com
#We must start at 0 or the first sum is 1+1
sum = 0
# No need to incl 0, but must add 1 to x as the first index is 0.
# EG for x = 5, range (1,x) is 1,2,3,4.
for i in range (1, x+1):
# sum function, adds all the numbers in the range 1 to x + 1.
# x+1 need to be used as python starts counting at 0
    sum = sum + i 
# prints the answer
print ("The sum of first", x, "numbers is: ", sum) 


    