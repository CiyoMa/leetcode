# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.insert(0, item)
        
    def getTop(self):
        return self.data[0]
        
    def pop(self):
        result = self.data[0]
        self.data=self.data[1:]
        return result
        
    def isEmpty(self):
        return len(self.data) == 0
        
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        s = stack()
        s.push(root)
        while root and not s.isEmpty():
            cur = s.pop()
            result.append(cur.val)
            if cur.right:
                s.push(cur.right)
            if cur.left:
                s.push(cur.left)
        return result