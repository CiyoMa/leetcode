class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
    	m = len(obstacleGrid)
    	n = len(obstacleGrid[0])
    	if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
    		return 0

    	q = [i for i in range(n) if obstacleGrid[m-1][i] == 1]

    	if len(q)>0:
    		last = max(q)
    	else:
    		last = -1
        t = [1 for i in range(n)]
        for i in range(n):
        	if i == last:
        		t[i] = '#'
        	elif i < last:
        		t[i] = 0
        k = t[:]
        for i in range(m-2, -1, -1):
        	#print t
        	for j in range(n-1, -1, -1):
        		if obstacleGrid[i][j] == 1:
        			k[j] = '#'
        		else:
        			p = 0
        			if j+1 < n and k[j+1] != '#':
        				p = k[j+1]
        			q = t[j]
        			if t[j] == '#':
        				q = 0
        			k[j] = p + q
        	t = k[:]
        #print t
        return t[0]

board = [\
  [0,0,0],\
  [0,1,0],\
  [0,0,0]\
]
board = [[0,0]]
s = Solution()
print s.uniquePathsWithObstacles(board)