# Leetcode Problem 1:
# Difficulty: Easy
# Language: Python
# Description: Given an array of integers nums and an integer target return indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Author: Kevin D. Zuniga Cuellar
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_values = {}
        for i in range(len(nums)):
            if nums[i] in lookup_values:
                return [lookup_values[nums[i]],i]
            else:
                lookup_values[target-nums[i]] = i 
        return []
