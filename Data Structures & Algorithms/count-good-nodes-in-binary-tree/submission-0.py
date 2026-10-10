# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxNum):
            if not node:
                return 0
            total = 1 if node.val >= maxNum else 0
            maxNum = max(maxNum, node.val)
            total += dfs(node.left, maxNum)
            total += dfs(node.right, maxNum)

            return total
        return dfs(root, root.val)