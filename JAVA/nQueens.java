public class Solution {
    public List<String[]> solveNQueens(int n) {
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
    
    public List<String[]> helper(int cur_row, int n, boolean[] downward_to_left, boolean[] downward_to_right, boolean[] row, boolean[] col){
        List<String[]> result = new ArrayList<String[]>(), rest;
        if (cur_row == n){
            String[] cur = new String[n];
            result.add(cur);
            return result;
        }
        
        row[cur_row] = true;
        
        String empty = "";
        for (int i=0; i<n; i++)
            empty += ".";
        
        for (int cur_col = 0; cur_col < n; cur_col++){
            if (downward_to_left[cur_col+cur_row] || downward_to_right[cur_col-cur_row+n-1] || col[cur_col])
                continue;
            downward_to_left[cur_col+cur_row] = true;
            downward_to_right[cur_col-cur_row+n-1] = true;
            col[cur_col] = true;
            
            rest = helper(cur_row+1,n,downward_to_left,downward_to_right,row,col);
            for (String[] s: rest){
                s[cur_row] = empty.substring(0,cur_col) + "Q" + empty.substring(0,n - 1 - cur_col);
            }
            result.addAll(rest);
            
            downward_to_left[cur_col+cur_row] = false;
            downward_to_right[cur_col-cur_row+n-1] = false;
            col[cur_col] = false;
        }
        row[cur_row] = false;
        return result;
    }
}