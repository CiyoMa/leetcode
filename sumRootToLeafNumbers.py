# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	if root is None:
    		return 0
    	result = self.helper(root, [], [])
    	return sum([int(i) for i in result])

    # @param root, a tree node
    # @param pathElements, a list of node.val on the path to root
    # @param result, a list of paths that the root node is on	
    # @return set of paths
    def helper(self, root, pathElements, result):
    	if root.left is None and root.right is None:
    		result.append(''.join(pathElements)+str(root.val))

    	if root.left is not None:
    		newPath = pathElements[:]
    		newPath.append(str(root.val))
    		self.helper(root.left, newPath, result)
    	if root.right is not None:
    		newPath = pathElements[:]
    		newPath.append(str(root.val))
    		self.helper(root.right, newPath, result)
    	return result

root = TreeNode(1)
l = TreeNode(2)
r = TreeNode(3)
root.left = l
root.right = r

s = Solution()
print s.sumNumbers(root)


