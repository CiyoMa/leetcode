"""
Given n, how many structurally unique BST's (binary search trees) 
that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
    	t = [1 for i in range(n+1)]
        for i in range(2,n+1):
        	temp = 0
        	for j in range(i):
        		print j+1, i-j-1
        		temp += t[j+1] * t[i-j-1]
        	print '#'
        	t[i] = temp
        return t[n]

s = Solution()
print s.numTrees(4)
