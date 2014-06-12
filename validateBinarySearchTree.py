# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def __init__(self):
        self.pre = None
        
    def isValidBST(self, root):
        return self.isBST(root)
        
    def isBST(self,node):
        if not node:
            return True
        if not self.isBST(node.left):
            return False
        if self.pre and self.pre.val >= node.val:
            return False
        self.pre = node
        return self.isBST(node.right)