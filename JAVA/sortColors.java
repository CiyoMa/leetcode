public class Solution {
    public void sortColors(int[] A) {
        int lastRed = -1, lastWhite = -1;
        for (int i=0; i<A.length; i++){
            if (A[i] == 0){
                A[i] = A[lastWhite+1];
                A[++lastRed] = 0;
                if (lastWhite >= lastRed)
                    A[++lastWhite] = 1;
                else
                    lastWhite = lastRed;
            }
            else if (A[i] == 1){
                A[i] = A[lastWhite+1];
                A[++lastWhite] = 1;
            }
        }
    }
}