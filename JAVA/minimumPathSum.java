public class Solution {
    public int minPathSum(int[][] grid) {
        int[] lastRow = new int[grid[0].length];
        int[] currentRow = new int[grid[0].length], temp;
        currentRow[0] = grid[0][0];
        for (int i = 1; i< grid[0].length; i++)
            currentRow[i] = currentRow[i-1]+grid[0][i];
        int count = 1;
        while (count < grid.length){
            temp = lastRow;
            lastRow = currentRow;
            currentRow = temp;
            currentRow[0] = lastRow[0] + grid[count][0];
            for (int j=1;j<grid[0].length;j++)
                currentRow[j] = (currentRow[j-1] > lastRow[j]? lastRow[j]:currentRow[j-1] ) + grid[count][j];
            count++;
        }
        return currentRow[grid[0].length-1];
    }
}