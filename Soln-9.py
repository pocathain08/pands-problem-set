#This program reads in a text ﬁle and outputs every second ine. 
#Theprogram should take the ﬁlename from an argument on the command line.
#Peadar O Cathain 26 Mar 2019
#Ref Section 7.2 in Python Tutorial

f = open('myfile.txt', 'r') #opens file in same directory, ../myfile.txt Can use abs or rel paths to access
#Tend to keep file in same location. Note w overwrites files. \n =go to a new line

s = f.read() #reads file

f.close() #Closes the file




