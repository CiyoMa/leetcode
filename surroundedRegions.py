class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        n = len(board)
        if n == 0:
            return 
        w = len(board[0])

        # newboard = []
        # for i in range(n):
        #     newboard.append([char for char in board[i]])
        # board = newboard[:]
        # for i in board:
        #     print i

    	# zeros = []
        notSurrended = []
        for i in range(n):
            for j in range(w):
                if board[i][j] == 'O' and (i * j == 0 or i == n-1 or j == w-1):
                    #board[i][j] = '#'
                    notSurrended.append( (i, j) )

        exploredNotSurrounded = set(notSurrended)
        #print notSurrended
        while len(notSurrended) > 0:
            i, j = notSurrended[0]
            #print i,j
            #board[i][j] = '#'
            notSurrended = notSurrended[1:]
            if i != 0 and (i-1,j) not in exploredNotSurrounded and board[i-1][j] == 'O':
                #board[i-1][j] = '#'
                notSurrended.append((i-1,j))
                exploredNotSurrounded.add( (i-1, j) )
            if i != n-1 and (i+1,j) not in exploredNotSurrounded and board[i+1][j] == 'O':
                #board[i+1][j] = '#'
                notSurrended.append((i+1,j))
                exploredNotSurrounded.add( (i+1, j) )
            if j != 0 and (i,j-1) not in exploredNotSurrounded and board[i][j-1] == 'O':
                #board[i][j-1] = '#'
                notSurrended.append((i,j-1))
                exploredNotSurrounded.add( (i, j-1) )
            if j != w-1 and (i,j+1) not in exploredNotSurrounded and board[i][j+1] == 'O':
                #board[i][j+1] = '#'
                notSurrended.append((i,j+1))
                exploredNotSurrounded.add( (i, j+1) )
        #print exploredNotSurrounded
        for i in range(n):
            temp = ''
            for j in range(w):
                # if board[i][j] == 'O':
                #   zeros.append( (i, j) )
                #print board[i][j],
                if (i,j) in exploredNotSurrounded:
                    temp += 'O'
                else:
                    temp += 'X'
            board[i] = temp
            #print
X = 'X'
O = 'O'
matrix = [
[X, X, X, X, X, X, X, X, X],\
[X, O, O, X, X, O, O, X, O],\
[X, X, O, X, X, X, O, X, O],\
[X, O, X, X, X, X, O, X, O],\
[X, O, O, X, X, O, O, X, O],\
[X, X, O, X, X, X, O, X, O],\
[X, O, X, X, X, X, O, X, O],\
[X, O, X, X, X, X, O, X, O],\
[X, X, X, X, X, X, X, X, X]\
]
matrix = [
[X, X, X, X],\
[X, O, O, X],\
[X, X, O, X],\
[X, O, X, X]\
]
matrix = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]

s = Solution()
s.solve(matrix)
for i in matrix:
    print i





