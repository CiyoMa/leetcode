class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        bit = 0
        n = len(A)
        if n < 1:
        	return 1
        for i in A:
        	if i <= n and i > 0:
        		bit |= 1 << i
        for i in range(1,n+1):
        	if bit & 1 << i == 0:
        		return i
        return n + 1

s = Solution()
A = []
print s.firstMissingPositive(A)

#if absoutely no extra memory: inPlaceCountSort