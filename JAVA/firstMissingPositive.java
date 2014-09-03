public class Solution {
    public int firstMissingPositive(int[] A) {
        Boolean[] count = new Boolean[A.length];
        for (int i=0; i<A.length; i++)
            count[i] = false;
        for (int t: A)
            if (t > 0 && t-1 < A.length)
                count[t-1] = true;
        for (int i = 0; i < A.length; i++)
            if (!count[i])
                return i+1;
        return A.length + 1;
    }
}