# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        ret = []
        ret.append([root.val])
        if root.left is None and root.right is None:
            return ret
        elif root.left is None:
            return ret + Solution.levelOrder(self, root.right)
        elif root.right is None:
            return ret + Solution.levelOrder(self, root.left)
        else:
            left_tree = Solution.levelOrder(self, root.left)
            right_tree = Solution.levelOrder(self, root.right)
            len_left = len(left_tree)
            len_right = len(right_tree)
            if len_left < len_right:
                longer = right_tree
            else:
                longer = left_tree
            end = min(len(left_tree), len(right_tree))
            for i in range(end):
                ret.append(left_tree[i] + right_tree[i])
            return ret + longer[end:]
