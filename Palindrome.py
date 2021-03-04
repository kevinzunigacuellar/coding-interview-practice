"""
Palindrome:  returns True if a word can be spelled the same
from right-left and left-right.

testcase 1:
Input: "racecar"
Output: True

testcase 2:
Input: "apple"
Output: False
"""

def palindrome(word):
    if len(word) <= 1: return True
    if word[0] is not word[-1]: return False
    striped_word = word[1:-1]
    return palindrome(striped_word)


