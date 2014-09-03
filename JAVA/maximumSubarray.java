public class Solution {
    public int maxSubArray(int[] A) {
        int[] maxEndByIndex = new int[A.length];
        maxEndByIndex[0] = A[0];
        for (int i = 1; i < A.length; i++)
            maxEndByIndex[i] = Math.max(A[i], A[i]+maxEndByIndex[i-1]);
        int best = maxEndByIndex[0];
        for (int i = 1; i < A.length; i++)
            best = best >= maxEndByIndex[i] ? best : maxEndByIndex[i];
        return best;
    }
}

// try divide & conquer!