class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        t = [1 for i in range(n)]
        k = [1 for j in range(n)]
        for i in range(m-1):
        	for j in range(n-2, -1, -1):
        		k[j] = k[j+1] + t[j]
        	t = k
        	k = [1 for j in range(n)]
        return t[0]

s = Solution()
print s.uniquePaths(2,2)