"""
Given a string S and a string T, count the number of distinct 
subsequences of T in S.

A subsequence of a string is a new string which is formed from 
the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
    	def dp(sStart, tStart, memo = {}):
    		if (sStart, tStart) in memo:
    			return memo[(sStart, tStart)]
    		if tStart == len(T):
    			return 1
    		num = 0
    		for i in range(sStart, len(S)- (len(T) - tStart) + 1):
    			
    			if T[tStart] == S[i]:
    				# print i, tStart
    				# print T[tStart], S[i]
    				num += dp(i+1, tStart+1, memo)
    		memo[(sStart, tStart)] = num
    		return num
    	return dp(0,0)

S, T = "a red rabbbbit", "rabbit"
s = Solution()
print s.numDistinct(S, T)

