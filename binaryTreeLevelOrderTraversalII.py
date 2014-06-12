# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
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
                result.insert(0, [n.val for n in nextLevel])
                #print [n.val for n in nextLevel]
                currentLevel = nextLevel
        return result