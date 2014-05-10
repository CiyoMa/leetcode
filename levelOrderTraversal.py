# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class queue:
# 	def __init__(self):
# 		self.data = []
# 		self.last = -1
# 		self.head = -1

# 	def enqueue(self, item):
# 		self.data.append(item)
# 		self.last += 1

# 	def dequeue(self):
# 		if self.head == -1 or self.head > self.last:
# 			raise Exception("queue underflow")
# 		self.last += 1
# 		return self.data[self.last - 1]

# 	def isEmpty(self):
# 		return self.head == -1 or self.last > self.head


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
    	if root is None:
    		return []

        currentLevel = [root]
        result = [[root.val]]

        while len(currentLevel) > 0:
            nextLevel = []
            while len(currentLevel) > 0:
            	current = currentLevel[0]
            	currentLevel = currentLevel[1:]
            	if current.left:
            		nextLevel.append(current.left)
            	if current.right:
            		nextLevel.append(current.right)

            if len(nextLevel) > 0:
                result.append([n.val for n in nextLevel])
                #print [n.val for n in nextLevel]
                currentLevel = nextLevel
        return result

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

s = Solution()
print s.levelOrder(t1)

