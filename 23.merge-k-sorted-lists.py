#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def heapify(ls, i):
	    # ls: list of Node
            left = i * 2 + 1
            right = i * 2 + 2
            
            smallest = left if left < len(ls) and ls[left].val < ls[i].val else i	
            smallest = right if right < len(ls) and ls[right].val < ls[smallest].val else smallest
                
            if smallest != i:
                ls[i], ls[smallest] = ls[smallest], ls[i]
                heapify(ls, smallest)

        def make_heap(ls):
            # ls: list of Node
            for i in range(int((len(ls))/2-1), -1, -1):
                heapify(ls, i)

        def heappop(ls):
            if len(ls) <= 1:
                return
            ls[0] = ls[-1]
            heapify(ls, 0)
            
        def extract_min(ls, former_node):
            former_node.next = ls[0]

            ls[0] = ls[0].next
        
            if ls[0] is None:
                heappop(ls)
            else:
                heapify(ls, 0)
                
        node_num = len(lists)
        start_node = ListNode(0)
        while node_num > 0:
            extract_min(lists, start_node)
            start_node = start_node.next
            node_num = len(lists)
        return start_node.next

