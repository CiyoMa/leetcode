class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle) - 2
        while l >= 0:
        	for j in range(len(triangle[l])):
        		triangle[l][j] += min(triangle[l+1][j], triangle[l+1][j+1])
        	l -= 1
        return triangle[0][0]

s = Solution()
triangle = [\
     [2],\
  #   [3,4],\
  #  [6,5,7],\
  # [4,1,8,3]\
]
print s.minimumTotal(triangle)