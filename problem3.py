#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
x= input("Enter a number:")
x= int(x)

 
def summation(x): 
    sum = 0
    j = 1
      
    for i in range(1, x + 1): 
        sum = sum + j 
        j = (j * 10) + 1
          
    return sum



y = summation(x)
y= str(y)
print("the sum of the series is" + ' ' + y) 