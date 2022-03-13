""" Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line. */

Input : nums bt 2000 and 3200
Output: print list of numbers that fulfill criteria

2111,2415,2421



#Define array to store result
result = []

for x in range(2000,3201):
    if x % 7 == 0 and x%5 !=0:
        result.append(x)

print(*result,sep=",")
print(len(result))
"""

"""
### Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

num = input("Enter num:")
num = int(num) #typecasting because python will save as string as default
temp = 1
fact = 1

for x in range(1,num+1,1):
    temp = fact
    fact = x * temp

print("result:",fact)

"""
"""
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that 
 (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


kamus = {}
for i in range(1,9,1):
    kamus[i] = i*i

print(kamus.items())

"""

"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


# list vs tuple

mylist = []

while True:
    word = input ("Enter value:")
    if word == 'q':
        break
    mylist.append(word)

print(mylist)
# Convert to tuple
print(tuple(mylist))

"""

"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.



class test(object):
    
    def __init__(self):
        self.x = ""

    def getString (self):
        self.x = input("Enter input:")

    def toUpper(self):
        x = self.x.upper()
        print(x)

obj = test()
obj.getString()
obj.toUpper()
"""
"""
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

import math 
c = 50
h = 30
d=100
q = math.sqrt((2*c*d)/h)
print(int(q))


# To use sqrt
import math 

# Declare list to store inputs
numlist = []

# Fx to get user inputs
def getinput():

    while True:
        num = input("Enter num:")  
        if (num == 'q'):
            break
        numlist.append(num)

# Fx to calculate
def calc (d):
    c = 50
    h = 30
    return int(math.sqrt((2*c*d)/h))

def main():
    getinput()    
    for x in range(len(numlist)):
        temp = int(numlist[x])
        q = calc (temp)
        print("Output "+ str(x) +": " + str(q))

if __name__ == "__main__":
    main()
"""
"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
implement list