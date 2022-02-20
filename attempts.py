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

"""

