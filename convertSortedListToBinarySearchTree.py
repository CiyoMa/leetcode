"""
Given a singly linked list where elements are sorted 
in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
    	return self.helper(head)

    # @param head, a list node
    # @return a tree node which is the root of a height balanced BST
    #  converted from the given list
    def helper(self, head):
    	if head is None:
    		return None
    	if head.next is None:
    		return TreeNode(head.val)

        p = head
    	before = p
        q = head.next
        while q:
        	q = q.next
        	if not q:
        		break
        	q = q.next
        	before = p
        	p = p.next
        secondHalf = p.next
        before.next = None
        x = p.val
        root = TreeNode(x)
        if before != p:
            left = self.helper(head)
            root.left = left
        right = self.helper(secondHalf)
        root.right = right
        return root

