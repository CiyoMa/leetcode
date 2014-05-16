"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
      if root is None: 
        return
      currentHead = root
      #p = currentHead
      while currentHead:
        nextHead = None
        nextTail = None
        p = currentHead
        while p:
          # print p.val
          if p.left:
            if nextHead == None:
              nextHead = p.left
              nextTail = p.left
            else:
              nextTail.next = p.left
              nextTail = nextTail.next
          if p.right:
            if nextHead == None:
              nextHead = p.right
              nextTail = p.right
            else:
              nextTail.next = p.right
              nextTail = nextTail.next
          p = p.next
        currentHead = nextHead

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
root.right = n2
s = Solution()
s.connect(root)
h = n1
while h:
  print h.val
  h = h.next





        