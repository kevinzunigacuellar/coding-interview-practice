# Leetcode Problem 2:
# Difficulty: Medium
# Language: Python
# Description: You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Author: Kevin D. Zuniga Cuellar
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

# Definition for singly-linked list


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = ListNode()
        head = node
        while l1 or l2:
            l1_val = l1.val if l1.val else 0
            l2_val = l2.val if l2.val else 0
            sum = l1_val + l2_val + carry
            carry = 0
            if sum > 9:
                output = sum % 10
                carry = 1
            else:
                output = sum
            node.next = ListNode(output)
            node = node.next
            l1.next if l1 else None
            l2.next if l2 else None
        if carry == 1: ListNode(carry)
        return head.next
