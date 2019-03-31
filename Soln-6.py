#This program takes a user input string and outputs 
#every second word. 
#Peadar O Cathain 12 Mar 2019

#Please enter a sentence: 
#The quick brown fox jumps over the lazy dog
 
s = (input("Please enter a sentence: "))

#https://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
ssplit = s.split()
#ssplit is a new variable that breaks the larger string, s,
# into smaller chunks.

#https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways
for i in range(len(ssplit)):
#i is the numerical assignment of the words in the sentence.
    
    if i % 2 != 1:
    #selects every second word by picking out the odd words    
        print (ssplit[i])
        #This prints the words with an index i, defined by the if loop above.
        

