public class Solution {
    public int uniquePaths(int m, int n) {
        if (n == 1||m == 1)
            return 1;
        int[] lastLine = new int[n];
        int[] currentLine = new int[n];
        
        for (int k = 0; k < n; k++)
            currentLine[k] = 1;
            
        int count = 1;
        while (count < m){
            for (int j = 1; j < n; j++)
                lastLine[j] = currentLine[j];
            for (int i = 1; i < n; i++)
                currentLine[i] = currentLine[i-1] + lastLine[i];
            count++;
        }
        return currentLine[n-1];
    }
}