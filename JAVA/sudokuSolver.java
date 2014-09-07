public class Solution {
    public void solveSudoku(char[][] board) {
        dfs(board, 0, 0);
    }
    
    public boolean dfs(char[][] board, int row, int col){
        if (col == 9)
            return dfs(board, row+1, 0);
        if (row == 9)
            return true;
        if (board[row][col] != '.')
            return dfs(board, row, col+1);
            
        for (int i = 0; i < 9; i++){
            board[row][col] = (char)('1' + i);
            if (isValid(board, row, col) && dfs(board, row, col+1))
                return true;
            board[row][col] = '.';
        }
        return false;
    }
    
    public boolean isValid(char[][] board, int row, int col){
        for (int i=0; i<9; i++)
            if(i!=col && board[row][i] == board[row][col])
                return false;
            else if(i!=row && board[i][col] == board[row][col])
                return false;
        for (int i=row/3*3; i<row/3*3+3; i++)
            for (int j=col/3*3; j<col/3*3+3; j++)
                if(i!=row && j!=col && board[i][j] == board[row][col])
                    return false;
        return true;
    }
}