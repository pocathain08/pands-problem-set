#This program asks the user to input a positive integer and tells the user 
#whether or not the number is a prime.
#Peadar O Cathain

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
    #It the input is not an integer or negative
    else:
        #Exit the while True: loop and continue with the program
        break

y = (((x)//2)+2)
#y is a number that is 1 above x divided by 2, therefore the remainder when 
#x is divided by range (2, y) must be less than y, so there is no need to
#divide x by any number greater that y to see if it is prime

for i in range(2, y):
#As outlined this range is all the numbers from 2 to one above half of x
        if x % i == 0:
        #The remainder when x is divided by the range (2, y) is zero, so 
        # x is divisable by i, therefore it is not prime. (note y > 1)
                print (x,"is not a prime number" )
                #Exit the for i in range(2,y) loop and the program
                break
#Ref: Python tutorial 4.4
#What to do if x is not divisable by i in range (2,y)       
else: 
        print (x, "is a prime number" )


                
 