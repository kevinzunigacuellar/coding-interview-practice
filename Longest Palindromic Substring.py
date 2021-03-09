"""
Leetcode Problem 5:
Difficulty: Medium
Language: Python
Description: Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
# Comments: Due to time complexity n^3 this answer was not accepted by Leetcode.
"""
#  check if substring is palindrome - return boolean
def palindrome(word):
    if len(word) <= 1: return True
    elif word[0] is not word[-1]: return False
    else:
        strip_word = word[1:-1]
        return palindrome(strip_word)

def get_substring(s):
    # initialize vars
    longest_substring = ""
    # empty string
    if len(s) <= 0: return longest_substring
    # string only has one item
    if len(s) == 1: return s

    for i in range(len(s)-1):
        current_substring = ""
        for j in range(i,len(s)):
            current_substring += s[j]
            if palindrome(current_substring):
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
    return longest_substring

