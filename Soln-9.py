#This program reads in a text ﬁle and outputs every second ine. 
#Theprogram should take the ﬁlename from an argument on the command line.
#Peadar O Cathain 26 Mar 2019
#Ref Section 7.2 in Python Tutorial

import sys

for arg in sys.argv[1:]:
    #This looks at all arguements in the command line after the file name
    if arg == ("Moby Dick"):
        #This assumes the unser wants to look at Moby Dick specifically
        #It then runs the program that outputs sever second line.
        with open("Moby Dick.txt", "r") as f:
            #Opens the file and reads it. The read file is abbreviated as f
            for line in f.read().split("\n")[::2]:
                #split("\n") splits the file into lines
                #[:: 2] looks at every second line. 
                #The print command outputs every second line
                print(line)
                f.close()

    elif arg != ("Moby Dick"):
        # Prints the b\m if title is not available.
        print("That title is not available or should be entered in Quotation Marks.")
                




