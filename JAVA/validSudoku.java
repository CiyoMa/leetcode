public class Solution {
    public boolean isValidSudoku(char[][] board) {
        int probe = 0, temp;
        for (int i=0; i < 9; i++){
            probe = 0;
            for (int j = 0; j < 9; j++){
                if (board[i][j] == '.')
                    continue;
                temp = probe & 1 << (board[i][j] - '1');
                if (temp != 0)
                    return false;
                probe |= 1 << (board[i][j] - '1');
            }
        }        
        for (int i=0; i < 9; i++){
            probe = 0;
            for (int j = 0; j < 9; j++){
                if (board[j][i] == '.')
                    continue;
                temp = probe & 1 << (board[j][i] - '1');
                if (temp != 0)
                    return false;
                probe |= 1 << (board[j][i] - '1');
            }
        }        
        for (int i=0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                probe = 0;
                for (int k = 0; k < 3; k++){
                    for (int q = 0; q < 3; q++){
                        if (board[3*i+k][3*j+q] == '.')
                            continue;
                        temp =  probe & 1 << (board[3*i+k][3*j+q] - '1');
                        if (temp != 0)
                            return false;
                        probe |= 1 << (board[3*i+k][3*j+q] - '1');
                    }
                }
            }
        }
        return true;
    }
}