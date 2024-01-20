"""
Input:
The input consists of a single 2-digit code with only digits 1 to 9, without any space between the digits.

Output
Output a single line with the swapped 2-digit code, without any space between the digits.
"""

code = input()
print(code[1] + code[0])