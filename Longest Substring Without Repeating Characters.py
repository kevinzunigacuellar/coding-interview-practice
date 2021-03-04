""" 
Leetcode Problem 3:
Difficulty: Medium
Language: Python
Description: Given a string s, find the length of the longest substring without repeating characters.

testcase:
Input: s = "abcabcbb"
Output: 3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stored_values = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in stored_values and stored_values[s[i]] >= start:
                start = stored_values[s[i]] + 1
            else: 
                max_len = max(max_len, i - start + 1)
            stored_values[s[i]] = i
        return max_len