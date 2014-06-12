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
    def postorderTraversal(self, root):
        result = []
        s = stack()
        lastVisited = None
        node = root
        while not s.isEmpty() or node:
            if node:
                s.push(node)
                node=node.left
            else:
                n = s.getTop()
                if n.right and lastVisited != n.right:
                    node = n.right
                else:
                    s.pop()
                    result.append(n.val)
                    lastVisited = n
        return result
                    