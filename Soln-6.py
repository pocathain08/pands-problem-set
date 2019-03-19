#This program takes a user input string and outputs 
#every second word. 12 Mar 2019

#Please enter a sentence: 
#The quick brown fox jumps over the lazy dog
 
s = (input("Please enter a sentence: "))



#https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
ssplit = s.split()
#print (ssplit)
#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
#i is the numerical assignment of the words in the sentence.
for i in range(len(ssplit)):
#select every second word by picking out the odd words
    if i % 2 == 1:
        
        
        #print(x)
        l = (ssplit[i])

        print (l)
        #print (ssplit[i])
    #if i %2 != 1:
     #   print (i)

# Python tutorial 3.1.2 Strings
#(var1 = 'Hello World!'
#var2 = "Python Programming"

#print ("var1[0]: ", var1[0])
#print ("var2[1:5]: ", var2[1:5]))

#
