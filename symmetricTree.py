# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None or root.left is None and root.right is None:
            return True
        if root.left and not root.right or root.right and not root.left:
            return False
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if left is None and right is None:
            return True
        elif left and not right or not left and right:
            return False
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
        