# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        fast = slow = head
        # split list into two halves
        while (fast is not None and fast.next is not None): 
                fast = fast.next.next
                slow = slow.next
        head2 = slow.next
        slow.next = None
        
        # reverse second half of list
        head2 = Solution.reverseList(self, head2)
        
        # merge two lists
        head1 = head
        while head2 is not None:
            head1_next = head1.next
            head2_next = head2.next
            
            head1.next = head2
            if head1.next is None:
                break
            head2.next = head1_next
            head1 = head1_next
            head2 = head2_next
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        curr = head.next
        head.next = None
        prev = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
