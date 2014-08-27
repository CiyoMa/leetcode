public class Solution {
    public int singleNumber(int[] A) {
        int j = 0;
        for (int i = 0; i<A.length; i++)
            j ^= A[i];
        return j;
    }
}