# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(node, subnode):
            if not node and not subnode:
                return True


            if not node or not subnode:
                return False
            
            if node.val != subnode.val:
                return False
            left = check(node.left, subnode.left)
            right = check(node.right, subnode.right)

            return left and right

        def find(node, subnode):
            if not node:
                return 
            ans = None
            if node.val == subnode.val:
                ans = check(node, subnode)
            if ans:
                return True
            
            left = find(node.left, subnode)
            right = find(node.right, subnode)

            return left or right
        
        if find(root, subRoot):
            return True
        else:
            return False
