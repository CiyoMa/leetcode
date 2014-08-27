public class Solution {
    public int minDistance(String word1, String word2) {
        int[] lastRow = new int[word2.length()+1];
        int[] currentRow = new int[word2.length()+1], temp;
        for (int i=0;i<word2.length()+1;i++)
            currentRow[i] = i;
        int count = 1;
        while(count < word1.length()+1){
            temp = lastRow;
            lastRow = currentRow;
            currentRow = temp;
            currentRow[0] = count;
            for(int j=1;j<word2.length()+1;j++)
                currentRow[j] = Math.min(Math.min(currentRow[j-1]+1, lastRow[j]+1), lastRow[j-1]+(word1.charAt(count-1) == word2.charAt(j-1)? 0:1));
            count++;
        }
        return currentRow[word2.length()];
    }
}