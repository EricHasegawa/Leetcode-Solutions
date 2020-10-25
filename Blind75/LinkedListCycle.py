# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        passed = []
        curr = head
        while curr is not None:
            if curr in passed:
                return True
            passed.append(curr)
            curr = curr.next
        return False
