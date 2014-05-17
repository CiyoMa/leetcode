"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
      if root is None:
        return root
      stack = [root]
      #result = []
      last = None
      current = None
      while len(stack) > 0:
        last = current
        current = stack.pop()
        if last:
          last.right = current
        if current.right:
          stack.append(current.right)
        if current.left:
          stack.append(current.left)
          current.left = None
          current.right = None
      return root

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)

t1.left = t2
t1.right = t5
t2.left = t3
t2.right = t4
t5.right = t6

s = Solution()
h = s.flatten(t1)
while h:
  print h.val,
  h = h.right
