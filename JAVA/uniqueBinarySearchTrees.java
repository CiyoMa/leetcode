public class Solution {
    public int numTrees(int n) {
        //if (n==0) return 1;
        int[] num = new int[n+1];
        num[0] = 1;
        num[1] = 1;
        int temp;
        for (int i=2; i<=n; i++){
            temp = 0;
            for (int j=0; j < i; j++){
                temp += num[j] * num[i-j-1];
            }
            num[i] = temp;
        }
        return num[n];
    }
}