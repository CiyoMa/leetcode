# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
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
    def inorderTraversal(self, root):
        result = []
        s = stack()
        s.push(root)
        while root and not s.isEmpty():
            node = s.pop()
            while node:
                if node.right:
                    s.push(node.right)
                s.push(node)
                node = node.left

            cur = s.pop()
            while not s.isEmpty() and not cur.right:
                result.append(cur.val)
                cur = s.pop()

            result.append(cur.val)
            # print result
            
        return result

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

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t2.right = t3

s = Solution()
print s.preorderTraversal(t1)
print s.preorderTraversal(None)