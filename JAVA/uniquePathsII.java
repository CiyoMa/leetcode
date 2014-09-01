public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[] cur = new int[obstacleGrid[0].length];
        int[] last = new int[obstacleGrid[0].length], temp;
        last[0] = (obstacleGrid[0][0] == 0)? 1:0;
        for (int i=1; i<last.length; i++)
            if (obstacleGrid[0][i] == 0)
                last[i] = last[i-1];
            else
                last[i] = 0;
        int count = 2;
        while (count <= obstacleGrid.length){
            cur[0] = (obstacleGrid[count-1][0] == 1)? 0:last[0];
            for (int j = 1; j < obstacleGrid[0].length; j++)
                cur[j] = (obstacleGrid[count-1][j] == 1)? 0:last[j]+cur[j-1];
            
            temp = cur;
            cur = last;
            last = temp;
            count++;
        }
        return last[obstacleGrid[0].length-1];
    }
}