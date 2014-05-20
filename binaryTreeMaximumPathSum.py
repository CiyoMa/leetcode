# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        def marker(root):
        	if root is None:
        		return 0
        	result = root.val
        	temp1, temp2 = None, None
        	if root.left:
        		temp1 = marker(root.left)
        	if root.right:
        		temp2 = marker(root.right)
        	if temp1 is not None and temp2 is not None:
        		best = max(temp1, temp2)
        	elif temp1 is not None:
        		best = temp1
        	elif temp2 is not None:
        		best = temp2
        	else:
        		best = 0
        	if best < 0:
        		root.score = result
        	else:
        	   	root.score = result + best
        	#print root.val, root.score
        	return root.score

        def helper(root):
        	if root is None:
        		return None
        	score = root.val
        	left, right = None, None
        	if root.left:
        		if root.left.score > 0:
        			score += root.left.score
        		left = helper(root.left)
        	if root.right:
        		if root.right.score > 0:
        			score += root.right.score
        		right = helper(root.right)
        	if left and right:
        		return max(score, left, right)
        	elif left:
        		return max(score, left)
        	elif right:
        		return max(score, right)
        	else:
        		return score

        if root is None:
        	return 0
        marker(root)
        return helper(root)

t1 = TreeNode(2)
t2 = TreeNode(-1)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
# t1.right = t3
# t2.left = t4
# t2.right = t5

s = Solution()
print s.maxPathSum(t1)