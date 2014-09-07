public class Solution {
    public int totalNQueens(int n) {
        boolean[] downward_to_left = new boolean[2*n-1];
        boolean[] downward_to_right = new boolean[2*n-1], row = new boolean[n], col = new boolean[n];
        for (int i = 0; i<n; i++){
            row[i] = false;
            col[i] = false;
        }
        for (int i = 0; i<2*n-1; i++){
            downward_to_left[i] = false;
            downward_to_right[i] = false;
        }
        
        return helper(0,n,downward_to_left,downward_to_right,row,col);
    }
    
    public int helper(int cur_row, int n, boolean[] downward_to_left, boolean[] downward_to_right, boolean[] row, boolean[] col){
        if (cur_row == n)
            return 1;
        
        row[cur_row] = true;
        int count = 0;
        
        for (int cur_col = 0; cur_col < n; cur_col++){
            if (downward_to_left[cur_col+cur_row] || downward_to_right[cur_col-cur_row+n-1] || col[cur_col])
                continue;
            downward_to_left[cur_col+cur_row] = true;
            downward_to_right[cur_col-cur_row+n-1] = true;
            col[cur_col] = true;
            
            count += helper(cur_row+1,n,downward_to_left,downward_to_right,row,col);
            
            downward_to_left[cur_col+cur_row] = false;
            downward_to_right[cur_col-cur_row+n-1] = false;
            col[cur_col] = false;
        }
        row[cur_row] = false;
        return count;
    }
}