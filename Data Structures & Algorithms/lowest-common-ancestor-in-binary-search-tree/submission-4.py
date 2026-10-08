# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        while current:
            if q.val > current.val and p.val > current.val:
                #go right
                current = current.right
            elif q.val < current.val and p.val < current.val:
                #go left
                current = current.left
            else:
                # the answer is the root node itself
                return current