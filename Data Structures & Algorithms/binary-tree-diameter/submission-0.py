# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = float("-inf")

        def diameter(node):
            if not node:
                return 0
            
            left = diameter(node.left)
            right = diameter(node.right)

            curr = left + right
            self.max_diameter = max(self.max_diameter, curr)

            return 1 + max(left,right)
        
        diameter(root)
        return self.max_diameter