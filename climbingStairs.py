class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
        	return 1
        if n == 2:
        	return 2
        m, l = 1, 2
        for i in range(3, n+1):
        	m, l = l, m + l
        return l

s = Solution()
print s.climbStairs(5)
