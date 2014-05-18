# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        n = len(num)
        return self.helper(num, 0, n-1)

    def helper(self, num, start, end):
    	if start > end:
    		return None
    	if start == end:
    		return TreeNode(num[start])

    	mid = (start + end)/2
    	left = self.helper(num, start, mid - 1)
    	right = self.helper(num, mid + 1, end)
    	root = TreeNode(num[mid])
    	root.left = left
    	root.right = right
    	return root
