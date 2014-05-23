"""
Given preorder and inorder traversal of a tree, construct the binary tree.

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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
    	def inOrder(root):
    		if root:
    			return inOrder(root.left) + [root.val] + inOrder(root.right)
    		return []

    	def preOrder(root):
    		if root:
    			return [root.val] + preOrder(root.left) + preOrder(root.right)
    		return []

    	# reference parameter ---- list
        def recursive(iStart, iEnd, lastPreIndex):
        	#print lastPreIndex,preorder[lastPreIndex]
        	if iStart > iEnd:
        		return None
        	#global lastPreIndex
        	lastPreIndex[0] = lastPreIndex[0] + 1
        	root = TreeNode(preorder[lastPreIndex[0]])
        	if iStart == iEnd:
        		return root

        	#print iStart,iEnd, preorder[lastPreIndex],lastPreIndex
        	for i in range(iStart, iEnd+1):
        		if inorder[i] == preorder[lastPreIndex[0]]:
        			inorderIndex = i
        			break
        	root.left = recursive(iStart, inorderIndex - 1, lastPreIndex)
        	root.right = recursive(inorderIndex + 1, iEnd, lastPreIndex)
        	return root

        #global lastPreIndex
        #lastPreIndex = -1
        if len(preorder) == 0:
        	return None
        #return recursive(0,len(preorder)-1,[-1])

        root = recursive(0,len(preorder)-1,[-1])
        print inOrder(root)
        print preOrder(root)
        return root

p,i = [2,1,3,4], [1,2,3,4] #[1,2,3],[3,2,1]#[1,2,3],[1,3,2]#[4,1,2,3], [1,2,3,4]
s = Solution()
s.buildTree(p,i)


