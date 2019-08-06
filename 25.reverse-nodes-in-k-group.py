#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def check_condition(pre, k):
            condition = True
            if pre is None:
                return False
            temp = pre.next
            for i in range(k):
                if temp is not None:
                    temp = temp.next
                else:
                    condition = False
                    break
            return condition
        
        def convert_k_node(pre, k):
            temp_ls = list()
            temp_node = pre.next
            for i in range(k):
                temp_ls.append(temp_node)
                temp_node = temp_node.next
            
            next_group_node = temp_ls[-1].next
            for i in range(k-1, -1, -1):
                pre.next = temp_ls[i]
                pre = pre.next
            
            pre.next = next_group_node
            return pre
            
        
        pre, pre.next = ListNode(0), head

        condition = True
        current = head
        
        temp = pre
        while check_condition(temp, k):
            temp = convert_k_node(temp, k)

        return pre.next

