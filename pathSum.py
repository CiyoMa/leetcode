# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param s, an integer
    # @return a boolean
    def hasPathSum(self, root, s):
        return self.helper(root, 0, s)

    def helper(self, root, s, t):
        if root is None:
            return False
        sub = s + root.val
        if root.left is None and root.right is None:
            return sub == t
        flag = False
        if root.left is not None:
            flag |= self.helper(root.left, sub, t)
        if root.right is not None:
            flag |=  self.helper(root.right, sub, t)sub
        return flag

# value parameter passing to a function will change the parameter itself! Test it!