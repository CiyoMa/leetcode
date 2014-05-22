"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
    	def neighbor(x,y,n,m,visited):
    		neighbors = []
    		if x > 0 and not visited[x-1][y]:
    			neighbors.append( (x-1, y) )
    		if x < n-1 and not visited[x+1][y]:
    			neighbors.append( (x+1, y) )
    		if y > 0 and not visited[x][y-1]:
    			neighbors.append( (x, y-1) )
    		if y < m-1 and not visited[x][y+1]:
    			neighbors.append( (x, y+1) )
    		return neighbors

    	def dfs(board,word,n,m,visited,start,currentXY):
    		#print word[start],start
    		x,y = currentXY
    		# if start == len(word) - 1 and word[start] == board[x][0][y]:
    		# 	return True
    		# elif start == len(word) - 1:
    		# 	return False
    		# elif start >= len(word):
    		# 	return True
    		if start >= len(word):
    			return True

    		visited[x][y] = True
    		neighbors = neighbor(x,y,n,m,visited)
    		#print neighbors,currentXY, visited
    		for nextX, nextY in neighbors:
    			if board[nextX][nextY] != word[start]:
    				continue
    			if board[nextX][nextY] == word[start] and dfs(board,word,n,m,visited,start+1,(nextX,nextY)):
    				return True
    		visited[x][y] = False
    		return False



    	n = len(board)
    	#print board[0][0]
    	m = len(board[0])
    	#print n,m
    	# if n == 1:
    	# 	m = len(board[0])
    	# 	board = [board]
    	# else:
    	#   	m = len(board[0][0])
    	#print n, m
        visited = [[False for i in range(m)] for j in range(n)]

        maps = {}
        for i in range(n):
        	for j in range(m):
        		temp = maps.get(board[i][j], [])
        		temp.append( (i,j) )
        		maps[board[i][j]] =  temp
        #print maps.get(word[0],[])
        for i in maps.get(word[0],[]):
        	x,y = i
        	visited[x][y] = True
        	if dfs(board,word,n,m,visited,1,i):
        		return True
        	visited[x][y] = False
        return False

        #print maps

word = "AF"
board = [\
  ["ABCE"],\
  ["SFCS"],\
  ["ADEE"]\
]
board , word = ["ab"], "ab"
s = Solution()
print s.exist(board, word)
