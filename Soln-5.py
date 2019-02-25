#python primes.py
x = int(input("Please enter a positive integer: "))

LCD = (((x)//2)+2)
LCD_range = list(range(2, LCD))

for i in (LCD_range):
        if x % i != 0:
                print ("This is a prime number" )

                break

                
        
#print (LCD_range)