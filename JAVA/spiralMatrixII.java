public class Solution {
    public int[][] generateMatrix(int n) {
        int row = 0, col = 0, cycle = 0, count = 1;
        int[][] result = new int[n][n];
        while (row < n - row && col < n - col){
            // move right
            while (col < n - cycle)
                result[row][col++] = count++;
            col--;
            row++;
            // move down
            while (row < n - cycle)
                result[row++][col] = count++;
            row--;
            col--;
            // move left
            while (col >= cycle)
                result[row][col--] = count++;
            col++;
            row--;
            // move up
            while (row > cycle)
                result[row--][col] = count++;
            cycle++;
            row = cycle;
            col = cycle;
        }
        return result;
    }
}