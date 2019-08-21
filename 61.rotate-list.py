#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if k == 0:
            return head
        elif head == None:
            return head

        prob = head
        cnt = 0
        while prob != None:
            prob = prob.next
            cnt += 1
        k = k % cnt
        fast = head
        for _ in range(k):
            if fast.next == None:
                fast = head
            else:
                fast = fast.next
        slow = head

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        if slow.next == None:
            return head
        else:
            new_head = slow.next
            fast.next = head
            slow.next = None
            return new_head


