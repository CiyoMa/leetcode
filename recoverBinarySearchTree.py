"""
Two elements of a binary search tree (BST) are 
swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight 
forward. Could you devise a constant space solution?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        