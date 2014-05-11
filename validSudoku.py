class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
    	for i in range(9):
    		for j in range(9):
    			print board[i][j],
    		print 

        for i in range(9):
        	t = set()
        	for char in board[i]:
        		if char == '.':
        			continue
        		elif char in t:
        			return False
        		else:
        			t.add(char)

        for j in range(9):
        	t = set()
        	for i in range(9):
        		char = board[i][j]
        		if char == '.':
        			continue
        		elif char in t:
        			return False
        		else:
        			t.add(char)

        print 
        for i in range(3):
        	print '#', i
        	for j in range(3):

        		t = set()
        		for k in range(3):
        			for m in range(3):
        				print board[3*i + k][3*j + m],
        				char = board[3*i + k][3*j + m]
		        		if char == '.':
		        			continue
		        		elif char in t:
		        			return False
		        		else:
		        			t.add(char)
		        print 
		        print i,j
	return True

board = [\
"..5.....6",\
"....14...",\
".........",\
".....92..",\
"5....2...",\
".......3.",\
"...54....",\
"3.....42.",\
"...27.6.."\
]
board = ["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]
s = Solution()
print s.isValidSudoku(board)
