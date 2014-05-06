class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			x |= 1 << i
        			y |= 1 << j
        			#print x, y

        #print x, y
        for i in range(m):
        	for j in range(n):
        		#print x & 1<<i, y & 1<<j
        		if x & 1<<i != 0 or y & 1<<j != 0:
        			matrix[i][j] = 0

matrix = [[1,0,0],[2,1,3],[0,2,4]]
s = Solution()
s.setZeroes(matrix)
print matrix
