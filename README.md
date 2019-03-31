# pands-problem-set
This is the research from problem set 1, please see the following line for details of problem set 1 https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf.

Question 1: 
Asks to write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number. Soln 1. 

Soln:
For this soln, I referred to Pynative.com. Python looks at a list, taking the first number as zero. This will not affect the sum but will affect the number. This I why x is in the range 0 to x+1. This programme starts at 0 and using the inbuilt sum function add all of the numbers in the list.

Question 2: 
Asks to write a program that outputs whether or not today is a day that begins with the letter T. 

Soln:
This is a slight modification of a worked example done in class. It imports datetime from Python. Python indexes the days of the week starting with Monday as 0 (Ref: https://www.tutorialspoint.com/python/python_date_time.htm)
Initially it had two “if” statements for Tues and Thurs, however it was possible to combine these in a string to reduce the number of lines written. Within the “if” statement is a print statement that prints “”. 
If datetime.datetime.today().weekday() , doesn’t equal 1 or 3, it goes to an “else” statement that prints “”. 

Question 3: 
Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 

Soln:
The initial step here is to define “my_list “as a list in the range 1000 to 10000. 
It uses a for statement to look at all numbers in this list and if they are divisible by 6 and not divisible by 12 they are printed as a list.
Equally, for i in (list(range(1000, 10000))), could have been used rather than defining "my_List".

Question 4: 
This program asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
Soln:
The initial step in this program is to deal with incorrect inputs by the user. For this I referenced STACK  to get over a Value Error. I referenced https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff for this question. 
It was also necessary to ensure that the number was positive. In both cases using the “continue” and “break” command allowed the I wanted to run the program without defining the Col function using the while, if and ifel loop.

Question 5: 
Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

Soln:
Similar to previous questions, once the issue with incorrect inputs was overcome, the imputed number was divided by 2 and 2 added to the solution. This gives a number that is one above half of this number. This number entered was then divided by all numbers upto this figure. It there is a remainder upto just over half this figure, it is prime. 

Question 6: 
Write a program that takes a user input string and outputs every second word. 

Soln:
Split was used to split the sentence, i was then used to refer index the words. This was then used to print every second word using a for loop.

Ref: https://docs.python.org/3/tutorial/introduction.html#strings https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

Question 7: 
Write a program that that takes a positive floating point number as input and outputs
an approximation of its square root.

Soln:
This solution can be amended to ask the user to input an estimate, by adding the following: est =(input ("Please enter your estimate: ")). If this estimate is within the stated tolerance, if abs((est*est)-x) < y, will return (f"That is a good estimate, it is within {y} of the exact square root of {x}."). This is an f-string. This also breaks the elif loop.
If the est is not within the tolerance, the program runs using the calculation. 


Question 8: 
Write a program that outputs today’s date and time in the format ”Monday, January
10th 2019 at 1:15pm”.

Soln:
strftime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
If t is not provided, the current time as returned by localtime() is used. format must be a string. An exception ValueError is raised if any field in t is outside of the allowed range.
This solution was very much relaint on the following Ref:
https://www.tutorialspoint.com/python/time_strftime.htm.


Question 9: 
Write a program that reads in a text file and outputs every second line. The program
should take the filename from an argument on the command line.

Soln:
The intent for this program is to allow the used to enter a title as a Command line arguement. It the arguements match, the program is run automatically. If not, it asks the user to re-enter the title request.  

Question 10: 
Write a program Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].


Soln:
MATLAB is a case-sensitive language (that upper and lower case matters), so you must use upper-case "X" consistently, and "plot" is all lower case.
The "^" (raise to the power) operator is for square matrices. To computer a per-element raise to the power, use ".^" instead. However, ** worked better for power functions. 

Ref: https://se.mathworks.com/matlabcentral/answers/137854-how-can-i-plot-function-2-x


    