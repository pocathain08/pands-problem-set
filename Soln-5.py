#python primes.py
x = int(input ("Please enter a positive integer: "))

LCD = (((x)//2)+2)

#LCD_range = list(range(0, LCD))

for i in (LCD):
    if x % i != 0:
        print ("this is a prime number" )


#print (LCD_range)