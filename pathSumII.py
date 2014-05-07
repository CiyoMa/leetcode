# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
    	if root is None:
    		return []
        return self.helper(root, [], [], sum, 0)

    def helper(self, root, path, result, target, sum):
    	if root is None:
    		return []

    	if root.left is None and root.right is None:
    		if sum + root.val == target:
    			path.append(root.val)
    			result.append(path)
    			return result

    	if root.left:
    		temp = path[:]
    		temp.append(root.val)
    		self.helper(root.left, temp, result, target, sum + root.val)
    	if root.right:
    		temp = path[:]
    		temp.append(root.val)
    		self.helper(root.right, temp, result, target, sum + root.val)
    	return result

