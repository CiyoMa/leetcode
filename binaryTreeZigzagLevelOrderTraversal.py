# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
    	return str(self.val)

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
    	if root is None:
    		return []
        count = 0
        result = [[root.val]]
        currentLevel = [root]
        nextLevel = []
        n = 1
        i = 0
        while n - i > 0:
        	#print '@'
        	#for j in currentLevel:
        	#	print j,
        	#print '$'
        	while n - i > 0:
        		current = currentLevel[i]
        		i += 1
        		#print current, i, n
        		if count % 2 == 0:
        			if current.left:
        				nextLevel.insert(0, current.left)
        			if current.right:
        				nextLevel.insert(0, current.right)
        		else:
        			if current.right:
        				nextLevel.insert(0, current.right)
        			if current.left:
        				nextLevel.insert(0, current.left)
        		
        	count += 1

        	if len(nextLevel) != 0:
        		result.append([j.val for j in nextLevel])
        		currentLevel = nextLevel[:]
        		nextLevel = []
        		# if count <= 2:
        		# 	print result, [j.val for j in currentLevel]
        		n = len(currentLevel)
        		i = 0
        return result

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5

s = Solution()
print s.zigzagLevelOrder(t1)
