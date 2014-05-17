class Solution:
    # @return an integer
    def totalNQueens(self, n):
        row = 0
        leftDiagonal = 0
        RightDiagonal = 0
        column = 0
        
        count = 0
        for i in range(n):
        	row = 0
        	leftDiagonal = 0
        	RightDiagonal = 0
        	column = 0
