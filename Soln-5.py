#python primes.py
x = int(input("Please enter a positive integer: "))

y = (((x)//2)+2)
#LCD_range = list(range(2, LCD))

for i in range(2, y):
        if x % i == 0:
                print (x,"is not a prime number" )

                break
# Python tutorial 4.4       
else: 
        print (x, "is a prime number" )


                
 