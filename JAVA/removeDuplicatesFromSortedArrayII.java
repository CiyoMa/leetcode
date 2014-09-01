public class Solution {
    public int removeDuplicates(int[] A) {
        if (A.length <= 1)
            return A.length;
        int lastPosition = 0;
        int count = 1;
        for (int j = 1; j < A.length; j++)
            if (A[j] != A[lastPosition]){
                A[++lastPosition] = A[j];
                count = 1;
            }
            else if (A[j] == A[lastPosition] && count == 1){
                A[++lastPosition] = A[j];
                count++;
            }
        return lastPosition + 1;
    }
}