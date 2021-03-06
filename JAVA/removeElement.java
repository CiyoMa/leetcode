public class Solution {
    public int removeElement(int[] A, int elem) {
        int currentLast = -1;
        for (int j = 0; j < A.length; j++)
            if (A[j] != elem)
                A[++currentLast] = A[j];
        return currentLast + 1;
    }
}