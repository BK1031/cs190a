"""
For this problem, write a program that determines if a supplied seven-digit telephone number
should be routed to the directory information operator, that is, the prefix number is 555.

Input:
The single line of input contains a single integer n (1000000 < n < 9999999), which is a telephone number.

Output:
Output a single integer, which is 1 if the number should be routed to the directory information operator,
or 0 if the number should not be routed to the directory information operator.
"""

number = input()

if number[0:3] == "555":
    print(1)
else:
    print(0)