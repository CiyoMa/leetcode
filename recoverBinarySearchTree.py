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
    	bads = self.find(root)
    	print [i.val for i in bads]
    	bads[0].val, bads[1].val = bads[1].val, bads[0].val
    	print self.inOrder(root)
    	return root

    def find(self, root):
    	# if not root:
    	# 	return []
    	# result = []
    	# flag = False
    	# if root.right and root.right.val < root.val:
    	# 	flag = True
    	# 	result.append(root.right)
    	# if root.left and root.left.val > root.val:
    	# 	flag = True
    	# 	result.append(root.left)
    	# if flag and not root.left and root.right or not root.right and root.left:
    	# 	flag = False
    	# 	result.append(root)
    	# return self.find(root.left) + result + self.find(root.right)

    # @param root, a tree node
    # @return a tree node
    # def recoverTree(self, root):
    #     sort = self.inOrder(root)
    #     #print sort
    #     i = 0
    #     end = len(sort) - 1
    #     x = []
    #     while i <= end:
    #     	if i == 0 and sort[i] > sort[i+1] or i == end and sort[i] < sort[i-1] or i> 0  and i < end and (sort[i] < sort[i-1] or sort[i] > sort[i+1]):
    #     		x.append(sort[i])
    #     	i += 1
    #     #print x
    #     if len(x)==2:
    #     	# find the mistake swaped one
    #     	x1 = self.search(root, x[0])
    #     	x2 = self.search(root, x[1])
    #     	#print x1.val, x2.val
    #     	x1.val, x2.val = x2.val, x1.val
    #     elif len(x) == 3:
    #     	#print '!'
    #     	x1 = self.search(root, x[0])
    #     	x2 = self.search(root, x[2])
    #     	#print x1.val, x2.val
    #     	x1.val, x2.val = x2.val, x1.val

    #     #print self.inOrder(root)
    #     return root

    # def search(self, root, target):
    # 	if root is None:
    # 		return None
    # 	if root.val == target:
    # 		#print root, '!'
    # 		return root
    # 	left = self.search(root.left,target)
    # 	if left:
    # 		return left
    # 	right = self.search(root.right,target)
    # 	if right:
    # 		return right
    # 	return None


    def inOrder(self, root):
    	if root is None:
    		return []
    	left = self.inOrder(root.left)
    	right = self.inOrder(root.right)
    	return left + [root.val] + right

# t1 = TreeNode(2)
# t2 = TreeNode(3)
# t3 = TreeNode(1)
# t1.left = t2
# t1.right = t3
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
s = Solution()
print s.recoverTree(t1)