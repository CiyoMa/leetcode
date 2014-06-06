"""
Two elements of a binary search tree (BST) are 
swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight 
forward. Could you devise a constant space solution?
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
    	order = self.inOrder(root)
    	#print [n.val for n in self.inOrder(root)]
    	i = 0
    	bigger, smaller = None, None
    	while i < len(order):
    		if i == 0 and order[0].val > order[1].val: # and len(order) > 1
    			bigger = order[0]
    		elif i == len(order) - 1 and order[i].val < order[i - 1].val:
    			smaller = order[i]
    		elif i > 0 and i < len(order) - 1:
    			if order[i].val > order[i+1].val and bigger is None:
    				bigger = order[i]
    			elif order[i].val < order[i-1].val:
    				smaller = order[i]
    		i += 1
    	#print bigger.val, smaller.val
    	#beware of the chain effect of the smaller one!!
    	bigger.val, smaller.val = smaller.val, bigger.val
    	#print [n.val for n in self.inOrder(root)]
    	return root

    def inOrder(self, root):
    	if root is None:
    		return []
    	left = self.inOrder(root.left)
    	right = self.inOrder(root.right)
    	return left + [root] + right

# t1 = TreeNode(2)
# t2 = TreeNode(3)
# t3 = TreeNode(1)
# t1.left = t2
# t1.right = t3
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(1)
t1.left = t2
t1.right = t3
s = Solution()
print s.recoverTree(t1)