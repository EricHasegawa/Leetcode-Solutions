"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        curr = curr2 = head
        d = {}
        while curr is not None:
            new_node = Node(curr.val)
            d[curr] = new_node
            curr = curr.next
        curr2
        while curr2 is not None:
            node = d[curr2]
            print(node.val)
            if curr2.next is not None:
                node.next = d[curr2.next]
            else:
                node.next = None
            if curr2.random is not None:
                node.random = d[curr2.random]
            else:
                node.random = None
            curr2 = curr2.next
        return d[head]
