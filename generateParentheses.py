"""
Given n pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
    	dp = [set() for i in range(n+1)]
    	dp[0] = set(["dummy"])
    	dp[1] = set(["()"])
    	for i in range(2,n+1):
    		dp[i] |= set(['('+s+')' for s in dp[i-1]])
    		for j in range(1,i):
    			for p in dp[j]:
    				for q in dp[i-j]:
    					dp[i].add(p+q)
    	return list(dp[n])

s = Solution()
print s.generateParenthesis(8)

        