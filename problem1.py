#!python3
"""
###### Problem 1
Ask the user to enter in the width and height of a box.
This should be an integer value less than 10
Draw a box filled with "*" symbols that matches the
width and height.
You will need 2 nested loops to draw the contents of
1 row and the number of rows.

inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****

"""


h= input("Enter a number:")


h= int(h)


print(h*"*")

y= h-2
x= h-2
for i in range(0, x):
    print("*" + y*"*" + "*")

print(h*"*")