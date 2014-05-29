# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
    	# @return a list of tree nodes, 
    	# which are root nodes of binary search tree
        def buildTrees(start,end):
        	if start == end:
        		return [TreeNode(start)]
        	if start > end:
        		return [None]
        	roots = []
        	for i in range(start, end+1):
        		leftCandidates = buildTrees(start, i-1)
        		rightCandidates = buildTrees(i+1, end)
        		for left in leftCandidates:
        			for right in rightCandidates:
        				root = TreeNode(i)
        				root.left = left
        				root.right = right
        				roots.append(root)
        	return roots
        return buildTrees(1,n)
