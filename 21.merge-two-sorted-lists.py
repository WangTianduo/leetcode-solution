#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        nextNode = result
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            nextNode.next = temp
            nextNode = nextNode.next

        while l1 != None:
            nextNode.next = l1
            nextNode = nextNode.next
            l1 = l1.next
        while l2 != None:
            nextNode.next = l2
            l2 = l2.next
            nextNode = nextNode.next
        return result.next

