def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))


#x = int(input("Please enter a positive integer: "))

#y = (((x)//2)+2)
#LCD_range = list(range(2, LCD))

#for i in range(2, y):
       # if x % i == 0:
               # print (x,"is not a prime number" )

               # break
# Python tutorial 4.4       
#else: 
       # print (x, "is a prime number" )
