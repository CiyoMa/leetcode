class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
    	# zeros = []
        notSurrended = []
        for i in range(9):
        	for j in range(9):
        		# if board[i][j] == 'O':
        		# 	zeros.append( (i, j) )
        		if board[i][j] == 'O' and i * j == 0:
        			notSurrended.append( (i, j) )

        for n in notSurrended:


