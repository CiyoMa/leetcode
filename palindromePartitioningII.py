"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):

        dp = [i for i in range(len(s))]
        isPalidromeTable = [[False for i in range(len(s)+1)] for j in range(len(s))]

        # store info: substring[start:end+1] is palindrome?
        for end in range(len(s)):
            isPalidromeTable[end][end] = True
            isPalidromeTable[end][end+1] = True
            for start in range(end):
                isPalidromeTable[end][start] = isPalidromeTable[end-1][start+1] and s[start] == s[end]
            # print isPalidromeTable[end]
        
        # print 
        # for line in isPalidromeTable:
        #     print line

        for end in range(1, len(s)):
            if isPalidromeTable[end][0]:
                dp[end] = 0
                continue
            tempMin = dp[end-1] + 1
            for start in range(1, end):
                if isPalidromeTable[end][start]:
                    if tempMin > dp[start-1] + 1:
                    	tempMin = dp[start-1] + 1

            dp[end] = tempMin
        # print dp
        return dp[len(s) - 1]


    # #Memory limit exceeded
    # def minCut(self, s):
    #     dp = [i for i in range(len(s))]
    #     isPalidromeTable = {}

    #     # store info: substring[i:j+1] is palindrome?
    #     for j in range(len(s)):
    #         isPalidromeTable[(j,j)] = True
    #         isPalidromeTable[(j+1,j)] = True
    #         for i in range(j):
    #             isPalidromeTable[(i, j)] = isPalidromeTable[(i+1, j-1)] and s[i] == s[j]

    #     for i in range(1, len(s)):
    #         if isPalidromeTable[(0, i)]:
    #             dp[i] = 0
    #             continue
    #         tempMin = None
    #         for j in range(i-1, -1, -1):
    #             if (tempMin is None or tempMin > dp[j] + 1) and isPalidromeTable[(j, i)]:
    #                 tempMin = dp[j] + 1
    #         if tempMin is not None:
    #             dp[i] = tempMin
    #     #print dp
    #     return dp[len(s) - 1]

string = 'coder'#"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#'abbc'
s = Solution()
print s.minCut(string)
