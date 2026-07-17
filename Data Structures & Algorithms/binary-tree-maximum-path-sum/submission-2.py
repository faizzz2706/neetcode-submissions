# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")

        def pathSum(node):
            if not node:
                return 0
            
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))

            total = left + right + node.val

            self.max_path = max(total, self.max_path)

            return node.val + max(left, right)
        
        pathSum(root)
        return self.max_path
