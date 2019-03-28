# python collatz 25 Feb 2019
#

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
        break

Soln = list()

while x > 1:
        
    if x % 2 == 0:
        print (x // 2)

        #(x // 2) = Soln
        #x += (Soln)
                #
        x = x//2

    elif x % 2 != 0:
        print ((3 * x) + 1)
        #((3 * x) + 1) = (Soln)
                #
        x = ((3 * x) +1)

        #print (Soln)
                


