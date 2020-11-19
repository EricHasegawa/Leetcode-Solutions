"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        d = {}
        return self.cloneGraphHelper(node, d)
    
    def cloneGraphHelper(self, node, d):
        if node.val in d:
            return d[node.val]
        else:
            copy = Node(node.val)
            d[node.val] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(self.cloneGraphHelper(neighbor, d))
        return copy
