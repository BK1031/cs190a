"""
Fergus determines that a word belongs to a category according to the following rules:
If there are more “b” than “k” in the word, then the word is a “boba” word.
If there are more “k” than “b” in the word, then the word is a “kiki” word.
If the word contains an equal number of “b” and “k”, then Fergus calls it a “boki” word.

These rules hold with one exception:
If there are no “b” and “k” in the word, the word is neither close to a “boba” word nor a “kiki” word.
In this case, Fergus refers to the word as a “none” word.

Help Fergus write a program that, given a word, can categorize the word according to Fergus’ rules.

Input:
The only line of the input contains a string consisting of characters “a”-“z”,
the word that Fergus wants to categorize.

Output:
Print a category: either “boba”, “kiki”, “boki” or “none”, according to Fergus’ rules stated above.
There is always one category that fits each word.
"""

word = input()

b = 0
k = 0

for i in word:
    if i == "b":
        b += 1
    elif i == "k":
        k += 1

if b > k:
    print("boba")
elif k > b:
    print("kiki")
elif k == b and k != 0:
    print("boki")
else:
    print("none")