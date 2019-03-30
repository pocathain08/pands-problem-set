#This program reads in a text ﬁle and outputs every second ine. 
#Theprogram should take the ﬁlename from an argument on the command line.
#Peadar O Cathain 26 Mar 2019
#Ref Section 7.2 in Python Tutorial

import sys

x = (sys.argv[1:])
print (x)
if len(x) !=1:
    print ("Please enter title as one word")

if x == ("Moby_Dick"):
    #with open("Moby Dick.txt", "r") as f:
    
    print("Title;", sys.argv[1:])
#This will print the second arguement from the Command line
#using sys.argv[1:] will print everything bar the filename (Soln-9.py)
#Ref: Python Tutorial 7.2
#with open("Moby Dick.txt", "r") as f: #opens file in same directory

#Ref:https://stackoverflow.com/questions/47062493/how-can-i-get-python-to-read-every-nth-line-of-a-txt-file
    #for line in f.read().split("\n")[::2]:
    #\n =go to a new line, [::2] every second line
        #print(line)

#f = open('myfile.txt', 'r') , ../myfile.txt Can use abs or rel paths to access
#Tend to keep file in same location. Note w overwrites files. 

#s = f.read() #reads file

#f.close() #Closes the file




