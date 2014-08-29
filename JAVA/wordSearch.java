public class Solution {
    public boolean exist(char[][] board, String word) {
        Boolean[][] visited = new Boolean[board.length][board[0].length];
        for (int i=0; i<board.length; i++)
            for (int j=0; j<board[0].length; j++)
                visited[i][j] = false;
        
        for (int i=0; i<board.length; i++)
            for (int j=0; j<board[0].length; j++)
                if (board[i][j] == word.charAt(0) && dfs(board, visited, word, 1, i, j))
                    return true;
        return false;
    }
    public boolean dfs(char[][] board, Boolean[][] visited, String word, int start, int row, int col){
        if (start == word.length())
            return true;
        visited[row][col] = true;
        char target = word.charAt(start);
        // up
        if (row > 0 && !visited[row-1][col] && board[row-1][col] == target && dfs(board, visited, word, start+1, row-1, col))
            return true;
        
        // right
        if (col < board[0].length-1 && !visited[row][col+1] && board[row][col+1] == target && dfs(board, visited, word, start+1, row, col+1))
            return true;
        
        // down
        if (row < board.length-1 && !visited[row+1][col] && board[row+1][col] == target && dfs(board, visited, word, start+1, row+1, col))
            return true;
            
        // left
        if (col > 0 && !visited[row][col-1] && board[row][col-1] == target && dfs(board, visited, word, start+1, row, col-1))
            return true;
        
        visited[row][col] = false;
        return false;
    }
}