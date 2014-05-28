"""
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

#DFS, TO-DO: Try DP bottom up
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
    	def dfs(start, memo):
    		if start in memo:
    			return memo[start]
    		if start >= len(s):
    			memo[start] = 1
    			return 1

    		if start == len(s) - 1 and s[start] != '0':
    			memo[start] = 1
    			return 1
    		elif s[start] == '0':
    			memo[start] = 0
    			return 0

    		flag = start < len(s) - 1 
    		flag &= s[start] == '1' and s[start+1] != '0' or s[start] == '2' and int(s[start+1]) <= 6
    		if flag:
    			temp = dfs(start + 1,memo) + dfs(start + 2,memo)
    		elif s[start] == '1' and s[start+1] == '0':
    			temp = dfs(start + 2, memo)
    		else:
    			temp = dfs(start + 1,memo)
    		memo[start] = temp
    		return temp

    	if len(s) == 0:
    		return 0
    	return dfs(0,{})

s = Solution()
print s.numDecodings("12")
