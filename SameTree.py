# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        left_empty = p.left is None and p.right is None
        right_empty = q.left is None and q.right is None
        if left_empty and right_empty:
            return p.val == q.val
        elif left_empty or right_empty:
            return False
        else:
            return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)
