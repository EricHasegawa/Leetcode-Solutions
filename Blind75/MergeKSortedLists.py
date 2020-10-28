import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:        
        k = len(lists)
        minheap = []
        # build minheap
        for i in range(k):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, i, lists[i]))
        dummy = rtail = ListNode(0)
        
        # while minheap is not empty
        while minheap:
            # pop i and the first element of the linked list at h[0]
            i, n = heapq.heappop(minheap)[1:]
            rtail.next = n
            rtail = rtail.next
            # move linked list forward
            if n.next:
                heapq.heappush(minheap, (n.next.val, i, n.next))
                
        return dummy.next
