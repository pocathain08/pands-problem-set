#This program reads in a text ﬁle and outputs every second ine. 
#Theprogram should take the ﬁlename from an argument on the command line.
#Peadar O Cathain 26 Mar 2019
#Ref Section 7.2 in Python Tutorial

import sys

for arg in sys.argv[1:]:
    if arg == ("Moby Dick"):
        with open("Moby Dick.txt", "r") as f:
            for line in f.read().split("\n")[::2]:
                print(line)
                f.close()

    elif arg != ("Moby Dick"):
        print("That title is not available or should be entered in Quotation Marks.")
                
                

#This will print the second arguement from the Command line
#using sys.argv[1:] will print everything bar the filename (Soln-9.py)
#Ref: Python Tutorial 7.2

#if len(x) !=1:
#    print ("Please enter title as one word, seperate words with _")

#if x == ("Moby_Dick"):
#    with open("Moby Dick.txt", "r") as f: 
    #opens the file as f, if f is in same directory.

#Ref:https://stackoverflow.com/questions/47062493/how-can-i-get-python-to-read-every-nth-line-of-a-txt-file
 #       for line in f.read().split("\n")[::2]:
    #\n =go to a new line, [::2] every second line
            
            

#f = open('myfile.txt', 'r') , ../myfile.txt Can use abs or rel paths to access
#Tend to keep file in same location. Note w overwrites files. 

#s = f.read() #reads file

#f.close() #Closes the file




