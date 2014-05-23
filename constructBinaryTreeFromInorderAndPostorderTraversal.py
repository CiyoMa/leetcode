"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
    	def inOrder(root):
    		if root:
    			return inOrder(root.left) + [root.val] + inOrder(root.right)
    		return []

    	def postOrder(root):
    		if root:
    			return postOrder(root.left) + postOrder(root.right) + [root.val]
    		return []

        def recursive(iStart, iEnd, postIndex):
        	if iStart > iEnd or postIndex[0] == 0:
        		return None
        	postIndex[0] -= 1
        	#print postIndex
        	root = TreeNode(postorder[postIndex[0]])
        	if iStart == iEnd:
        		return root
        	for i in range(iStart, iEnd+1):
        		if postorder[postIndex[0]] == inorder[i]:
        			break
        	root.right = recursive(i+1,iEnd,postIndex)
        	root.left = recursive(iStart,i-1,postIndex)
        	return root
        l = len(inorder)
        if l == 0:
        	return None
        return recursive(0,l-1,[l])
        
        root = recursive(0,l-1,[l])
        print postOrder(root)
        print inOrder(root)

i,p = [3,1,2,4],[3,4,2,1] 
s = Solution()
s.buildTree(i,p)
