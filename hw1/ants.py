"""
Input:
The first line of input contains one integer giving the number of cases that follow, at most 100.
The data for each case start with two integer numbers: the length l of the pole (in cm) and n,
the number of ants residing on the pole. These two numbers are followed by n integers giving the
position of each ant on the pole as the distance measured from the left end of the pole,
in no particular order. All input integers are between 0 and 1000000 and they are separated by whitespace.

Output:
For each case of input, output two numbers separated by a single space.
The first number is the earliest possible time when all ants fall off the pole
(if the directions of their walks are chosen appropriately) and the second number
is the latest possible such time.
"""

cases = int(input())

for i in range(cases):
    data = input().split()
    length = int(data[0])
    ants = int(data[1])
    positions = [int(x) for x in input().split()]
    earliest = 0
    latest = 0
    for j in positions:
        earliest = max(earliest, min(j, length - j))
        latest = max(latest, max(j, length - j))
    
    print(f"{earliest} {latest}")