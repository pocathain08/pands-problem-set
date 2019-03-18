# pands-problem-set
This is the research from problem set 1, please see the following line for details of problem set 1 https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf.

 Question 1: Asks to write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. 
 Soln 1. For this soln, I referred to Pynative.com. Python looks at a list, taking the first number as zero. This will not affect the sum but will affect the number. This I why x is in the range 0 to x+1. This programme starts at 0 and using the inbuilt sum function add all of the numbers in the list. 

 Question 2: Asks to write a program that outputs whether or not today is a day that begins with the letter T. This is a slight modification of a worked example done in class. It imports datetime from Python. It had 2 if statements and worked it the day was a 1 or a 3 but this required 2 if statements. I then tried with a string using 1 and 3. This is followed by an else statement. 

 Question 3: Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.  This defines my_list as a list in the range 1000 to 10000. It uses a for statement to look at all numbers in this list and if they are divisible by 6 and not divisible by 12 they are printed as a list.  

Question 4: This program asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even, divide it by two, but if it is odd, multiply it by three and add one.
I referenced https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff for this question. I wanted to run the program without defining the Col function using the while, if and ifelse loop. 

Question 6: Write a program that takes a user input string and outputs every second word.
References: 
https://docs.python.org/3/tutorial/introduction.html#strings
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
    