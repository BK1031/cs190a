"""
Input:
The input consists of a single line with two integers 1 ≤ h ≤ 1000 and 1 ≤ b ≤ 1000,
the height and base of the triangle.

Output
Output a single number, the area of the triangle.
Your answer must be correct within an absolute or relative error of 10^-7.
"""

triangle = input().split()
height = int(triangle[0])
base = int(triangle[1])

print(height * base / 2)