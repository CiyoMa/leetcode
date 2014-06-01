class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        # @return a boolean indicating whether it is solvable 
        #  from current configuration
        def dfs(row,column):
            if column >= 9:
                return dfs(row+1,0)
            if row >= 9:
                return True
            if board[row][column] != '.':
                return dfs(row, column+1)

            # For leetcode input
            # prefix = ''.join(board[row][:column])
            # suffix = ''.join(board[row][(column+1):])
            prefix = board[row][:column]
            suffix = board[row][(column+1):]

            original = board[row]
            candidate = set(range(1,10))
            # for char in original:
            # 	if char != '.':
            # 		candidate.remove(int(char))

            # print prefix, suffix
            for value in candidate:#range(1,10):
                string = prefix + str(value) + suffix
                board[row] = string
                # print board[row]
                if isValid(row, column) and dfs(row, column+1):
                    #print board[row]
                    return True
                board[row] = original
                # print 
            return False

        def isValid(row, column):
        	for i in range(9):
        		if board[row][i] == board[row][column] and column != i:
        			return False
        		if board[i][column] == board[row][column] and row != i:
        			return False

        	for i in range(row/3*3,row/3*3+3):
        		for j in range(column/3*3,column/3*3+3):
        			if board[i][j] == board[row][column] and i != row and j != column:
        				return False
        	return True
        dfs(0, 0)
        # return dfs(0, 0)

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
#["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s = Solution()
# for i in board:
#     print i 
# print 
print s.solveSudoku(board)
for i in board:
    print i 