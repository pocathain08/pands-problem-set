#This program reads in a text ﬁle and outputs every second ine. 
#Theprogram should take the ﬁlename from an argument on the command line.
#Peadar O Cathain 26 Mar 2019
#Ref Section 7.2 in Python Tutorial



#Ref:https://stackoverflow.com/questions/47062493/how-can-i-get-python-to-read-every-nth-line-of-a-txt-file
with open("file.txt", "r") as f:
    for line in f.read().split("\n")[::2]:
        print(line)

f = open('myfile.txt', 'r') #opens file in same directory, ../myfile.txt Can use abs or rel paths to access
#Tend to keep file in same location. Note w overwrites files. \n =go to a new line

s = f.read() #reads file

f.close() #Closes the file




