#MIT 6_0001 Intro to Computer Science Fall 2016 
#Problem Set 0
#Assignment:
#Write a program that does the following in order:
#1. Asks the user to enter a number “x” 
#2. Asks the user to enter a number “y”
#3. Prints out number “x”, raised to the power “y”. 
#4. Prints out the log (base 2) of “x”.
#
#solution by Alex Murshak - 2/14/2018

import numpy as np

X = int(input('Please enter a number "x"'))
Y = int(input('Please enter a number "y"'))


print(X**(Y))
print(np.log2(X))
