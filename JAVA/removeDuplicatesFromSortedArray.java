public class Solution {
    public int removeDuplicates(int[] A) {
        if (A.length <= 1)
            return A.length;
        int currentLast = 0;
        for (int j = 1; j<A.length; j++)
            if (A[j] != A[currentLast])
                A[++currentLast] = A[j];
        return currentLast + 1;
    }
}