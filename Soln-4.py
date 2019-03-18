# python collatz 25 Feb 2019
#


x = int(input("Please enter a positive integer: "))

#New_list = []

while x > 1:
        #New_list = New_list + i
        #for i in range(1, x+1):
        if x % 2 == 0:
                print (x // 2)
                x = x//2

        elif x % 2 != 0:
                print ((3 * x) + 1)
                x = ((3 * x) + 1)
                


#n = input("Give me a number: ")
#while n != 1:
 #   n = collatz(int(n))
  #      New_list = (x//2)      

#elif x % 2 !=0:
 #        New_list = ((x*3)+1)

#Print: (New_list)
         
#Print (New_list)
                        
        #i= i-1



#def colz(n):    # write Collatz series up to n
 #   """Print a Collatz series up to n."""
  #  a, b = 0, 1
   # while a < n:
    #    print(a, end=' ')
     #   a, b = b, a+b
    #print()

#fib (2000)