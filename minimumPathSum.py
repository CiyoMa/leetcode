class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
    	n = len(grid)
    	m = len(grid[0])
        M = [['invalid' for i in range(m)] for j in range(n)]
        temp = M[0][:]
        tempSum = 0
        for i in range(m):
        	tempSum += grid[0][i]
        	temp[i] = tempSum
        M[0] = temp

        tempSum = grid[0][0]
        for i in range(1, n):
        	tempSum += grid[i][0]
        	M[i][0] = tempSum

        for i in range(1, n):
        	for j in range(1, m):
        		M[i][j] = min(M[i-1][j], M[i][j-1]) + grid[i][j]

        return M[n-1][m-1]

matrix = [\
  [1,   3,  5,  7],\
  [10, 11, 16, 20],\
  [23, 30, 34, 50]\
]
matrix = [[1,2],[1,1]]

s = Solution()
print s.minPathSum(matrix)