"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there
exists one unique longest palindromic substring.
"""

#Not Subsequence!!!!!

class Solution:
    # @return a string
    def longestPalindrome(self, s):
    	

    	# def change(i,j):
    	# 	if j == i:
    	# 		return 1
    	# 	return 0
    	# 	# elif j == i + 1:
    	# 	# 	return 0
    	# 	# else: return -1 

    	# def dprog(s):
    	# 	dp = [[change(i,j) for j in range(len(s)+1)] for i in range(len(s))]
    	# 	best = [[i if i == j else 'inv' for j in range(len(s)+1)] for i in range(len(s))]
    	# 	longest = 0
    	# 	for j in range(1,len(s)):
    	# 		for i in range(j-1,-1,-1):
    	# 			if s[i] == s[j]: #and dp[j-1][i+1] >= 0:
    	# 				dp[j][i] = 1
    	# 				# dp[j][i] = dp[j-1][i+1] + 2
    	# 				# best[j][i] = (j-1, i+1)
    	# 			else:
    	# 				if dp[j][i+1] > dp[j-1][i]:
    	# 					temp = dp[j][i+1]
    	# 					best[j][i] = (j,i+1)
    	# 				else:
    	# 					temp = dp[j-1][i]
    	# 					best[j][i] = (j-1,i)

    	# 				dp[j][i] = temp
    	# 		print 'row', j+1
    	# 		for i in dp:
    	# 			print i
    	# 	print '!!'
    	# 	print dp[len(s)-1][0]
    	# 	return best

    	# dprog(s)
    	# for i in dprog(s):
    	# 	print i

s = Solution()
s.longestPalindrome("abcgggdefggg")
        