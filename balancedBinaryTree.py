# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return root == None or \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right) and \
               abs(self.height(root.left) - self.height(root.right)) <= 1

    def height(self, root):
    	if root is None:
    		return 0
    	return max(self.height(root.left), self.height(root.right)) + 1
